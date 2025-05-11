---
title: "modelcontextprotocol/create-typescript-server"
date: 2025-05-11T01:40:40.578259+00:00
tags: ["MCP"]
draft: false
---

<p>```json
{
  "title": "使用 MCP CLI 工具创建一个新的 TypeScript 服务器",
  "tutorial_html": "<p>在现代 Web 开发中，TypeScript 已成为构建可靠且可维护的服务器端应用程序的首选语言之一。而 Model Context Protocol（MCP）为开发者提供了一种标准化的方式来构建和管理这些应用程序。本文将带您一步步使用 <code>modelcontextprotocol/create-typescript-server</code> CLI 工具来创建一个新的 TypeScript MCP 服务器。</p><h2>准备工作</h2><p>在开始之前，请确保您的开发环境中已经安装了 Node.js 和 npm。您可以通过在终端中运行 <code>node -v</code> 和 <code>npm -v</code> 来检查它们是否已经安装并获取版本信息。</p><h2>安装 CLI 工具</h2><p>首先，我们需要全局安装 <code>create-typescript-server</code> CLI 工具。打开终端并运行以下命令：</p><pre><code>npm install -g create-typescript-server</code></pre><p>此命令将会在您的计算机上全局安装该工具，使您可以在任何目录中使用它来创建新的服务器项目。</p><h2>创建新的 TypeScript MCP 服务器</h2><p>一旦安装完成，您可以通过运行以下命令来创建一个新的 TypeScript MCP 服务器：</p><pre><code>create-typescript-server my-new-server</code></pre><p>在上述命令中，<code>my-new-server</code> 是您将要创建的项目的名称。您可以根据需要更改此名称。</p><p>命令执行后，CLI 工具将会在当前目录下创建一个名为 <code>my-new-server</code> 的新文件夹，并在其中初始化一个基本的 TypeScript MCP 服务器项目结构。</p><h2>项目结构</h2><p>让我们来看一下生成的项目结构：</p><pre><code>my-new-server/\n├── src/\n│   ├── index.ts\n├── package.json\n├── tsconfig.json\n└── README.md</code></pre><p>在这个结构中，<code>src/index.ts</code> 是您的服务器入口文件，<code>package.json</code> 包含项目的元数据和依赖项，<code>tsconfig.json</code> 是 TypeScript 的配置文件。</p><h2>运行服务器</h2><p>在进入项目目录后，您可以通过运行以下命令来启动服务器：</p><pre><code>cd my-new-server\nnpm install\nnpm start</code></pre><p>首先，<code>npm install</code> 将会安装所有必要的依赖项。然后，<code>npm start</code> 将会编译 TypeScript 代码并启动服务器。</p><p>启动成功后，您将在终端中看到服务器正在监听的端口信息。您可以通过浏览器或其他 HTTP 客户端工具访问该端口，验证服务器是否正常运行。</p><h2>自定义和扩展</h2><p>现在，您已经成功创建并运行了一个基本的 TypeScript MCP 服务器。接下来，您可以根据项目需求修改 <code>src/index.ts</code> 文件，添加更多功能和路由。</p><p>此外，您还可以通过修改 <code>tsconfig.json</code> 来调整 TypeScript 的编译选项，以满足特定的项目要求。</p><h2>结语</h2><p>通过 <code>create-typescript-server</code> CLI 工具，您可以快速搭建一个基础的 TypeScript MCP 服务器，节省了大量的初始配置时间。希望本教程能帮助您顺利开始使用 TypeScript 和 MCP 构建高效的服务器应用程序。</p>",
  "tags": ["TypeScript", "MCP", "CLI", "服务器开发", "Web开发"]
}
```</p><p>本教程由 <a href="https://www.lumjf.com/" target="_blank">@https://www.lumjf.com/ 全模型中转api可免费试用</a> 自动生成。</p>