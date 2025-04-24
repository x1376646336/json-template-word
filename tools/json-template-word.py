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
        # Get parameters
        template_path = tool_parameters.get("template_path", "")
        data = tool_parameters.get("json_value", {})
        data = json.loads(data)

        if not template_path:
            yield self.create_text_message("Template path not provided")
            return

        try:
            # Generate DOCX file
            docx_bytes = self._process_template(template_path, data)

            # Construct file metadata
            filename = data.get("filename", "output.docx")
            mime_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

            # Return file Blob
            yield self.create_blob_message(
                blob=docx_bytes,
                meta={
                    "mime_type": mime_type,
                    "file_name": filename
                }
            )

        except Exception as e:
            yield self.create_text_message(f"Document generation failed: {str(e)}")


    def _process_template(self, template_path: str, data: Dict[str, Any]) -> bytes:
        # Determine whether it is a remote URL
        if self.is_remote_url(template_path):
            # Download remote template
            local_template = self.download_template(template_path)
        else:
            # Process local paths (ensuring that the paths are legal)
            local_template = Path(template_path)
            if not local_template.exists():
                raise FileNotFoundError(f"The local template file does not exist: {template_path}")

        # Load and render templates
        doc = DocxTemplate(local_template)
        doc.render(data)

        # Clean up temporary files (if downloaded)
        if isinstance(local_template, Path) and local_template.exists():
            local_template.unlink()

        # Return byte stream
        output_stream = BytesIO()
        doc.save(output_stream)
        return output_stream.getvalue()

    def is_remote_url(self,url: str) -> bool:
        """Determine whether it is remote URL（http/https协议）"""
        parsed = urlparse(url)
        return parsed.scheme in ('http', 'https')

    def download_template(self,url: str) -> Path:
        """Download remote template to temporary file"""
        response = requests.get(url)
        response.raise_for_status()
        temp_file = NamedTemporaryFile(delete=False, suffix=".docx")
        temp_file.write(response.content)
        temp_file.close()
        return Path(temp_file.name)

