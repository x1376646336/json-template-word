## json-template-word

**Author:**  xuyefang
**Version:**  0.0.1
**Type:**  tool

### Description
This plugin supports converting the generated JSON on the dify platform into a Word template for export

#JSON Template Word Plugin

[![License: MIT]( https://img.shields.io/badge/License-MIT-yellow.svg )]( https://opensource.org/licenses/MIT )
![Dify Compatibility]( https://img.shields.io/badge/Dify-%3E%3D0.6.0-blue)

Intelligently fill the JSON data output by the big language model into predefined Word templates, automatically generate standardized documents, and support downloads.
## Setup
Installation
Install the plugin from Dify Marketplace
Navigate to Plugins section in your Dify workspace
Find the "JSON Template Word" plugin and click "Install"
Once installed, you can use the plugin in your applications
Adding to Applications
Create or edit a Chatflow or Workflow application
In the tool selection panel, select "JSON Template Word" tool
Configure the tool in your application flow as needed
Save and publish your application
Usage
You can use this tool to convert json content to DOCX format with two parameters:

json_value (required): The json content you want to convert

template_path (required): The template_path for the word template path 

![image-20250416091001332](https://xuxuweizhi.oss-cn-beijing.aliyuncs.com/typora/image-20250416091001332.png)
##Functional characteristics

✅ **Template Engine**
Support the use of Microsoft Word (. docx) as a template file, and implement intelligent field replacement through {mustache} syntax

✅ **Dynamic rendering**
Support complex JSON structure parsing, including:
-Nested object handling
-Array Loop Rendering
-Conditional judgment statement

✅**Format retention**
Perfectly preserving the original template:
-Text style (font/color/size)
-Paragraph format
-Table Structure
-Header and Footer



## Application scenarios

🏢**Enterprise scenario**
-Contract/Agreement Generation
-Project report automation
-Customer letter processing

🎓**Educational scene**
-Transcript generation
-Production of admission letter
-Experimental report formatting

⚖️**Legal Scene**
-Legal document generation
-Template based power of attorney
-Production of compliance documents


###Manual installation (private deployment)
```bash
git clone  https://github.com/x1376646336/json-template-word.git
cd json-template-word-plugin
pip install -r requirements.txt






