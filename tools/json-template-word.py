import json
from collections.abc import Generator
from io import BytesIO
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Dict, Any
from urllib.parse import urlparse

import requests
from docxtpl import DocxTemplate
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class DocxTemplateTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        # 获取参数
        template_path = tool_parameters.get("template_path", "")
        data = tool_parameters.get("json_value", {})
        data = json.loads(data)

        if not template_path:
            yield self.create_text_message("未提供模板路径")
            return

        try:
            # 生成 DOCX 文件
            docx_bytes = self._process_template(template_path, data)

            # 构造文件元数据
            filename = data.get("filename", "output.docx")
            mime_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

            # 返回文件 Blob
            yield self.create_blob_message(
                blob=docx_bytes,
                meta={
                    "mime_type": mime_type,
                    "filename": filename
                }
            )

        except Exception as e:
            yield self.create_text_message(f"文档生成失败: {str(e)}")

    # def _process_template(self, template_path: str, data: Dict[str, Any]) -> bytes:
    #     # 加载模板并渲染数据
    #     doc = DocxTemplate(template_path)
    #     doc.render(data)
    #
    #     # 将渲染结果保存到字节流
    #     output_stream = BytesIO()
    #     doc.save(output_stream)
    #     return output_stream.getvalue()

    def _process_template(self, template_path: str, data: Dict[str, Any]) -> bytes:
        # 判断是否为远程URL
        if self.is_remote_url(template_path):
            # 下载远程模板
            local_template = self.download_template(template_path)
        else:
            # 处理本地路径（需确保路径合法）
            local_template = Path(template_path)
            if not local_template.exists():
                raise FileNotFoundError(f"本地模板文件不存在: {template_path}")

        # 加载并渲染模板
        doc = DocxTemplate(local_template)
        doc.render(data)

        # 清理临时文件（如果是下载的）
        if isinstance(local_template, Path) and local_template.exists():
            local_template.unlink()

        # 返回字节流
        output_stream = BytesIO()
        doc.save(output_stream)
        return output_stream.getvalue()

    def is_remote_url(self,url: str) -> bool:
        """判断是否为远程URL（http/https协议）"""
        parsed = urlparse(url)
        return parsed.scheme in ('http', 'https')

    def download_template(self,url: str) -> Path:
        """下载远程模板到临时文件"""
        response = requests.get(url)
        response.raise_for_status()
        temp_file = NamedTemporaryFile(delete=False, suffix=".docx")
        temp_file.write(response.content)
        temp_file.close()
        return Path(temp_file.name)

