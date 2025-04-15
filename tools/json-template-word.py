import json
from collections.abc import Generator
from io import BytesIO
from typing import Dict, Any
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

    def _process_template(self, template_path: str, data: Dict[str, Any]) -> bytes:
        # 加载模板并渲染数据
        doc = DocxTemplate(template_path)
        doc.render(data)

        # 将渲染结果保存到字节流
        output_stream = BytesIO()
        doc.save(output_stream)
        return output_stream.getvalue()