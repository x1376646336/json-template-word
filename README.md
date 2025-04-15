## json-template-word

**Author:** xuyefang
**Version:** 0.0.1
**Type:** tool

### Description
本插件支持将您在dify平台将生成的json转换为word模板导出

# JSON Template Word 插件

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Dify Compatibility](https://img.shields.io/badge/Dify-%3E%3D0.6.0-blue)

将大语言模型输出的JSON数据智能填充到预定义的Word模板中，自动生成标准化文档并支持下载。

## 功能特性

✅ &zwnj;**模板引擎**&zwnj;  
支持使用Microsoft Word (.docx) 作为模板文件，通过{{ mustache }}语法实现智能字段替换

✅ &zwnj;**动态渲染**&zwnj;  
支持复杂JSON结构解析，包括：  
- 嵌套对象处理  
- 数组循环渲染  
- 条件判断语句

✅ &zwnj;**格式保留**&zwnj;  
完美保留原始模板的：  
- 文字样式（字体/颜色/大小）  
- 段落格式  
- 表格结构  
- 页眉页脚



## 应用场景

🏢 &zwnj;**企业场景**&zwnj;  
- 合同/协议生成  
- 项目报告自动化  
- 客户信函处理

🎓 &zwnj;**教育场景**&zwnj;  
- 成绩单生成  
- 录取通知书制作  
- 实验报告格式化

⚖️ &zwnj;**法律场景**&zwnj;  
- 法律文书生成  
- 委托书模板化  
- 合规文件制作

## 安装指南

### 通过Dify应用市场安装
1. 进入您的Dify工作区
2. 打开「插件市场」
3. 搜索 "JSON Template Word"
4. 点击安装并授权所需权限

### 手动安装（私有部署）
```bash
git clone https://github.com/x1376646336/json-template-word.git
cd json-template-word-plugin
pip install -r requirements.txt






