---
title: "modelcontextprotocol/typescript-sdk"
date: 2025-05-11T01:26:37.965954+00:00
tags: ["MCP"]
draft: false
---

<p>```json
{
  "title": "使用 Model Context Protocol 的官方 TypeScript SDK 构建你的第一个应用",
  "tutorial_html": "<p>在本教程中，我们将探讨如何使用 Model Context Protocol 的官方 TypeScript SDK 来构建一个简单的应用程序。Model Context Protocol（MCP）是一种用于服务器和客户端之间通信的协议，而这个 SDK 提供了一种简便的方式来与 MCP 服务器进行交互。</p><h2>前提条件</h2><p>在开始之前，请确保你已经具备以下条件：</p><ul><li>Node.js 和 npm 已安装在你的系统中。</li><li>基本的 TypeScript 知识。</li><li>访问 MCP 服务器的权限。</li></ul><h2>步骤 1：设置项目</h2><p>首先，我们需要创建一个新的项目目录，并初始化一个新的 Node.js 项目：</p><pre><code>mkdir mcp-app\ncd mcp-app\nnpm init -y</code></pre><p>接下来，我们需要安装 Model Context Protocol 的 TypeScript SDK：</p><pre><code>npm install modelcontextprotocol/typescript-sdk</code></pre><h2>步骤 2：配置 TypeScript</h2><p>在项目中创建一个 <code>tsconfig.json</code> 文件，以配置 TypeScript 编译选项：</p><pre><code>{\n  \"compilerOptions\": {\n    \"target\": \"ES6\",\n    \"module\": \"commonjs\",\n    \"strict\": true,\n    \"esModuleInterop\": true,\n    \"skipLibCheck\": true,\n    \"forceConsistentCasingInFileNames\": true\n  }\n}</code></pre><h2>步骤 3：编写代码</h2><p>在项目目录中创建一个 <code>src</code> 文件夹，并在其中创建一个 <code>index.ts</code> 文件。我们将在这个文件中编写与 MCP 服务器交互的代码。</p><p>首先，我们需要导入 SDK 并创建一个客户端实例：</p><pre><code>import { MCPClient } from 'modelcontextprotocol/typescript-sdk';\n\nconst client = new MCPClient({\n  serverUrl: 'https://your-mcp-server.com', // 替换为你的 MCP 服务器 URL\n  apiKey: 'your-api-key' // 如果需要，替换为你的 API 密钥\n});</code></pre><p>接下来，我们将实现一个简单的功能来从服务器获取一些数据：</p><pre><code>async function fetchData() {\n  try {\n    const data = await client.getData('/your-endpoint'); // 替换为你的 API 端点\n    console.log('Data received:', data);\n  } catch (error) {\n    console.error('Error fetching data:', error);\n  }\n}\n\nfetchData();</code></pre><h2>步骤 4：编译和运行代码</h2><p>现在，我们需要编译 TypeScript 代码并运行它。首先，编译代码：</p><pre><code>npx tsc</code></pre><p>接下来，运行生成的 JavaScript 文件：</p><pre><code>node dist/index.js</code></pre><p>如果一切正常，你应该会在控制台中看到从 MCP 服务器接收到的数据。</p><h2>总结</h2><p>在本教程中，我们学习了如何使用 Model Context Protocol 的官方 TypeScript SDK 来构建一个简单的应用程序。通过这个 SDK，你可以轻松地与 MCP 服务器进行交互，为你的应用程序提供强大的数据支持。</p><p>接下来，你可以尝试扩展这个示例，增加更多的功能，比如处理不同的 API 端点、添加错误处理机制或者集成到更大的应用程序中。</p>",
  "tags": ["TypeScript", "SDK", "Model Context Protocol", "MCP", "编程教程"]
}
```</p><p>本教程由 <a href="https://www.lumjf.com/" target="_blank">@https://www.lumjf.com/ 全模型中转api可免费试用</a> 自动生成。</p>