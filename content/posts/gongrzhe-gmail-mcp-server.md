---
title: "GongRzhe/Gmail-MCP-Server"
date: 2025-05-11T01:36:23.012431+00:00
tags: ["MCP"]
draft: false
---

<p>```json
{
  "title": "使用 GongRzhe/Gmail-MCP-Server 集成 Gmail 到 Claude Desktop",
  "tutorial_html": "<p>在当今的数字时代，自动化和人工智能技术日益流行。GongRzhe/Gmail-MCP-Server 是一个开源工具，它通过 Model Context Protocol (MCP) 服务器将 Gmail 集成到 Claude Desktop 中，使 AI 助手能够通过自然语言交互管理 Gmail。本文将详细介绍如何使用此工具实现 Gmail 集成。</p><h2>前提条件</h2><p>在开始之前，请确保满足以下条件：</p><ul><li>安装了 Claude Desktop。</li><li>安装了 Node.js 和 npm。</li><li>拥有一个 Gmail 账户。</li></ul><h2>步骤一：克隆仓库</h2><p>首先，您需要将 GongRzhe/Gmail-MCP-Server 仓库克隆到本地计算机。打开终端并输入以下命令：</p><pre><code>git clone https://github.com/GongRzhe/Gmail-MCP-Server.git</code></pre><p>克隆完成后，进入项目目录：</p><pre><code>cd Gmail-MCP-Server</code></pre><h2>步骤二：安装依赖</h2><p>在项目目录中，运行以下命令来安装所有必要的依赖：</p><pre><code>npm install</code></pre><p>这将根据 package.json 文件安装所有的项目依赖。</p><h2>步骤三：配置 Gmail 认证</h2><p>GongRzhe/Gmail-MCP-Server 提供自动认证支持。您需要设置 Gmail API 凭据以允许服务器访问您的 Gmail 账户。请按照以下步骤进行设置：</p><ol><li>访问 <a href=\"https://console.developers.google.com/\">Google Developer Console</a>。</li><li>创建一个新项目。</li><li>启用 Gmail API。</li><li>创建 OAuth 2.0 凭据，并下载 JSON 格式的凭据文件。</li></ol><p>将下载的凭据文件保存到项目目录，并重命名为 <code>credentials.json</code>。</p><h2>步骤四：启动 MCP 服务器</h2><p>完成配置后，您可以启动 MCP 服务器。运行以下命令：</p><pre><code>node server.js</code></pre><p>服务器启动后，它将自动进行 Gmail 认证，并准备好接受来自 Claude Desktop 的请求。</p><h2>步骤五：在 Claude Desktop 中使用集成</h2><p>打开 Claude Desktop，并确保它连接到运行中的 MCP 服务器。您现在可以通过自然语言与 AI 助手交互，管理您的 Gmail，包括收发邮件、设置过滤器等。</p><h2>总结</h2><p>通过 GongRzhe/Gmail-MCP-Server，您可以轻松地将 Gmail 集成到 Claude Desktop 中，实现邮件管理的自动化。此工具不仅简化了日常任务，还展示了 AI 技术在实际应用中的潜力。希望这篇教程能帮助您顺利完成集成，并提高工作效率。</p>",
  "tags": ["Gmail","MCP","Claude Desktop","AI Integration","Automation"]
}
```</p><p>本教程由 <a href="https://www.lumjf.com/" target="_blank">@https://www.lumjf.com/ 全模型中转api可免费试用</a> 自动生成。</p>