---
title: "jasonsum/gmail-mcp-server"
date: 2025-05-11T01:38:43.107074+00:00
tags: ["MCP"]
draft: false
---

<p>```json
{
  "title": "使用 jasonsum/gmail-mcp-server 搭建 Gmail MCP 服务器教程",
  "tutorial_html": "<p>在现代应用开发中，处理电子邮件的能力是一个重要的功能。<code>jasonsum/gmail-mcp-server</code> 是一个专为 Gmail 设计的 Model Context Protocol (MCP) 服务器，旨在简化与 Gmail 的集成。本教程将指导您如何设置和使用这个工具。</p>\n\n<h2>前提条件</h2>\n<p>在开始之前，请确保您具备以下条件：</p>\n<ul>\n<li>基本的编程知识和对命令行的熟悉。</li>\n<li>已安装的 Node.js 环境（建议使用最新的 LTS 版本）。</li>\n<li>一个可用的 Gmail 帐户。</li>\n<li>访问 <a href=\"https://github.com/jasonsum/gmail-mcp-server\">GitHub 仓库</a>的权限。</li>\n</ul>\n\n<h2>步骤 1：克隆仓库</h2>\n<p>首先，您需要将 <code>gmail-mcp-server</code> 仓库克隆到您的本地机器。打开终端并运行以下命令：</p>\n<pre><code>git clone https://github.com/jasonsum/gmail-mcp-server.git</code></pre>\n<p>进入项目目录：</p>\n<pre><code>cd gmail-mcp-server</code></pre>\n\n<h2>步骤 2：安装依赖</h2>\n<p>在项目目录中，运行以下命令以安装必要的依赖包：</p>\n<pre><code>npm install</code></pre>\n<p>这将下载并安装项目所需的所有模块。</p>\n\n<h2>步骤 3：配置 Gmail API</h2>\n<p>要使 <code>gmail-mcp-server</code> 正常工作，您需要设置 Gmail API 凭据：</p>\n<ol>\n<li>访问 <a href=\"https://console.developers.google.com/\">Google Developers Console</a>。</li>\n<li>创建一个新的项目。</li>\n<li>启用 Gmail API。</li>\n<li>创建 OAuth 2.0 凭据。</li>\n<li>下载凭据 JSON 文件，并将其命名为 <code>credentials.json</code>，然后将其放置在项目根目录下。</li>\n</ol>\n\n<h2>步骤 4：启动服务器</h2>\n<p>一旦配置完成，您可以启动服务器。运行以下命令：</p>\n<pre><code>npm start</code></pre>\n<p>首次运行时，系统会提示您进行 OAuth 验证。按照终端中的说明进行操作以完成验证。</p>\n\n<h2>步骤 5：使用 MCP 接口</h2>\n<p>服务器启动后，您可以通过 MCP 接口与 Gmail 交互。以下是一个简单的示例，显示如何通过 MCP 发送电子邮件：</p>\n<pre><code>curl -X POST http://localhost:3000/mcp/send \\\n  -H 'Content-Type: application/json' \\\n  -d '{\n    \"to\": \"recipient@example.com\",\n    \"subject\": \"Hello from MCP\",\n    \"body\": \"This is a test email sent from MCP server.\"\n  }'</code></pre>\n<p>确保将 <code>recipient@example.com</code> 替换为实际的电子邮件地址。</p>\n\n<h2>总结</h2>\n<p>通过本教程，您学习了如何设置和使用 <code>jasonsum/gmail-mcp-server</code> 来集成 Gmail 功能。这个工具为开发者提供了一种简化的方式来处理电子邮件操作。如果您遇到任何问题，请参考 <a href=\"https://github.com/jasonsum/gmail-mcp-server\">官方文档</a>获取更多信息。</p>",
  "tags": ["Gmail", "MCP", "Node.js", "API", "邮件处理"]
}
```</p><p>本教程由 <a href="https://www.lumjf.com/" target="_blank">@https://www.lumjf.com/ 全模型中转api可免费试用</a> 自动生成。</p>