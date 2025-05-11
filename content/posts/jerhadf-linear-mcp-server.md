---
title: "jerhadf/linear-mcp-server"
date: 2025-05-11T01:35:38.632821+00:00
tags: ["MCP"]
draft: false
---

<p>```json
{
  "title": "使用 Jerhadf 的 Linear MCP Server 将 LLMs 与 Linear 项目管理系统集成",
  "tutorial_html": "<p>在现代软件开发中，项目管理工具如 Linear 扮演着至关重要的角色。它们帮助团队组织任务、跟踪进度并确保项目按时交付。随着人工智能技术的发展，尤其是大语言模型（LLMs）的兴起，我们有机会让这些智能体与项目管理工具进行交互，从而提高生产效率。今天，我们将介绍如何使用 Jerhadf 的 <code>linear-mcp-server</code> 工具来实现这一目标。</p><h2>什么是 Linear MCP Server？</h2><p><code>linear-mcp-server</code> 是一个服务器端应用程序，它将 Linear 的项目管理系统与 Model Context Protocol (MCP) 集成。这种集成使得 LLMs 能够与 Linear 进行交互，获取项目管理数据并执行相关操作。</p><h2>准备工作</h2><p>在开始之前，请确保您已经安装了以下工具和库：</p><ul><li>Node.js：<a href=\"https://nodejs.org/\">下载链接</a></li><li>Git：<a href=\"https://git-scm.com/\">下载链接</a></li></ul><p>此外，您需要在 Linear 上拥有一个账户，并获取 API 访问权限。</p><h2>安装步骤</h2><ol><li>克隆仓库：<pre><code>git clone https://github.com/jerhadf/linear-mcp-server.git</code></pre></li><li>进入项目目录：<pre><code>cd linear-mcp-server</code></pre></li><li>安装依赖项：<pre><code>npm install</code></pre></li><li>配置环境变量：创建一个 <code>.env</code> 文件，并填入以下内容：<pre><code>LINEAR_API_KEY=your_linear_api_key\nMCP_SERVER_PORT=3000</code></pre><p>请将 <code>your_linear_api_key</code> 替换为您的 Linear API 密钥。</p></li><li>启动服务器：<pre><code>npm start</code></pre></li></ol><h2>使用教程</h2><p>服务器启动后，您可以通过 MCP 与 Linear 进行交互。以下是一些基本操作示例：</p><h3>获取项目列表</h3><p>发送一个 MCP 请求到服务器端点，您将获得当前项目的列表。</p><h3>创建新任务</h3><p>通过 MCP，您可以发送请求来创建新的任务，并指定任务的详细信息，如标题、描述和分配人。</p><h3>更新任务状态</h3><p>LLMs 可以通过 MCP 更新任务状态，例如将任务标记为完成或更改优先级。</p><h2>总结</h2><p>通过 <code>linear-mcp-server</code>，您可以将 LLMs 的强大能力与 Linear 项目管理系统结合起来，从而提高团队的协作效率。这个工具为自动化项目管理操作提供了便利，并使得智能体能够更好地理解和参与项目管理流程。</p>",
  "tags": ["项目管理", "人工智能", "MCP", "Linear", "LLMs"]
}
```</p><p>本教程由 <a href="https://www.lumjf.com/" target="_blank">@https://www.lumjf.com/ 全模型中转api可免费试用</a> 自动生成。</p>