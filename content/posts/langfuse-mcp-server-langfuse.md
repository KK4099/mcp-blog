---
title: "langfuse/mcp-server-langfuse"
date: 2025-05-11T01:39:13.321596+00:00
tags: ["MCP"]
draft: false
---

<p>```json
{
  "title": "使用 Langfuse MCP 服务器管理提示语",
  "tutorial_html": "<p>在现代应用程序开发中，提示语管理是一个关键环节，尤其是在处理复杂的模型和上下文时。Langfuse 提供了一种强大的解决方案，通过其 MCP 服务器来管理提示语。本文将介绍如何使用 langfuse/mcp-server-langfuse 工具来有效地管理您的提示语。</p>\n<p><strong>工具简介</strong></p>\n<p>langfuse/mcp-server-langfuse 是一个基于 Model Context Protocol (MCP) 的服务器，专为 Langfuse 提示语管理设计。它允许开发者方便地访问和管理与 Langfuse 相关的提示语，使得在不同应用和模型之间共享和复用提示语变得简单高效。</p>\n<p><strong>安装与配置</strong></p>\n<p>首先，我们需要从 GitHub 仓库克隆 langfuse/mcp-server-langfuse 项目：</p>\n<pre><code>git clone https://github.com/langfuse/mcp-server-langfuse.git</code></pre>\n<p>接下来，进入项目目录并安装必要的依赖：</p>\n<pre><code>cd mcp-server-langfuse\nnpm install</code></pre>\n<p>在安装完依赖后，我们可以通过以下命令启动 MCP 服务器：</p>\n<pre><code>npm start</code></pre>\n<p>服务器启动后，默认会监听在本地的某个端口，通常是 3000。您可以通过浏览器访问 <code>http://localhost:3000</code> 来确认服务器是否正常运行。</p>\n<p><strong>使用 MCP 服务器管理提示语</strong></p>\n<p>启动服务器后，您可以通过 MCP API 来管理提示语。以下是一些常用的 API 操作示例：</p>\n<p><strong>1. 创建新的提示语</strong></p>\n<p>您可以使用 POST 请求来创建新的提示语。请求的主体应包含提示语的详细信息，例如内容和关联的模型。</p>\n<pre><code>POST /prompts\n{\n  \"model\": \"your-model-name\",\n  \"content\": \"your-prompt-content\"\n}</code></pre>\n<p><strong>2. 获取提示语列表</strong></p>\n<p>通过 GET 请求，您可以获取所有已创建的提示语的列表：</p>\n<pre><code>GET /prompts</code></pre>\n<p><strong>3. 更新现有的提示语</strong></p>\n<p>使用 PUT 请求更新某个提示语的内容或模型：</p>\n<pre><code>PUT /prompts/{prompt_id}\n{\n  \"model\": \"updated-model-name\",\n  \"content\": \"updated-prompt-content\"\n}</code></pre>\n<p><strong>4. 删除提示语</strong></p>\n<p>通过 DELETE 请求删除某个提示语：</p>\n<pre><code>DELETE /prompts/{prompt_id}</code></pre>\n<p><strong>总结</strong></p>\n<p>langfuse/mcp-server-langfuse 提供了一种简便且高效的方式来管理提示语，使得在多个应用和模型之间共享信息变得更为简单。通过本文的介绍，您应该能够安装、配置并使用 MCP 服务器来管理您的提示语。若您有进一步的需求或问题，建议参考项目的 GitHub 仓库获取更多信息和支持。</p>",
  "tags": ["Langfuse", "提示语管理", "MCP服务器", "模型上下文协议"]
}
```</p><p>本教程由 <a href="https://www.lumjf.com/" target="_blank">@https://www.lumjf.com/ 全模型中转api可免费试用</a> 自动生成。</p>