---
title: "tadata-org/fastapi_mcp"
date: 2025-05-11T01:42:27.062119+00:00
tags: ["MCP"]
draft: false
---

<p>```json
{
  "title": "使用 fastapi_mcp 将 FastAPI 端点暴露为 MCP 工具",
  "tutorial_html": "<p>在现代应用开发中，API 的安全性和可扩展性是至关重要的。<code>fastapi_mcp</code> 是一个强大的工具，允许开发者将 FastAPI 端点暴露为 Model Context Protocol (MCP) 工具，并提供认证支持。本文将指导您如何使用该工具来创建安全、可扩展的 API。</p><h2>什么是 fastapi_mcp？</h2><p><code>fastapi_mcp</code> 是一个 Python 库，它将 FastAPI 端点转换为 MCP 工具。MCP 是一种协议，用于标准化模型和应用之间的通信。通过使用 MCP，开发者可以确保模型在不同环境中的可用性和安全性。</p><h2>安装 fastapi_mcp</h2><p>在开始之前，您需要确保已经安装了 Python 和 FastAPI。然后，您可以使用 pip 安装 <code>fastapi_mcp</code>：</p><pre><code>pip install fastapi_mcp</code></pre><h2>基本使用方法</h2><p>安装完成后，您可以开始将 FastAPI 端点转换为 MCP 工具。以下是一个简单的示例，展示了如何使用 <code>fastapi_mcp</code>：</p><pre><code>from fastapi import FastAPI\nfrom fastapi_mcp import MCPTool, Auth\n\napp = FastAPI()\n\n@app.get(\"/items/{item_id}\")\ndef read_item(item_id: int):\n    return {\"item_id\": item_id}\n\n# 使用 MCPTool 将端点暴露为 MCP 工具\nmcp_tool = MCPTool(app, auth=Auth(\"your_auth_token\"))\n\nif __name__ == \"__main__\":\n    import uvicorn\n    uvicorn.run(app, host=\"0.0.0.0\", port=8000)</code></pre><p>在这个示例中，我们创建了一个简单的 FastAPI 应用，并定义了一个端点 <code>/items/{item_id}</code>。然后，我们使用 <code>MCPTool</code> 类将这个应用暴露为一个 MCP 工具，并通过 <code>Auth</code> 提供认证支持。</p><h2>认证支持</h2><p>认证是确保 API 安全的关键。<code>fastapi_mcp</code> 提供了简单的认证支持，您可以通过设置认证令牌来保护您的端点。上面的示例展示了如何使用 <code>Auth</code> 类来实现这一点。</p><p>您可以根据自己的需求定制认证逻辑，例如集成 OAuth 或 JWT 认证。</p><h2>高级特性</h2><p>除了基本的端点暴露和认证支持，<code>fastapi_mcp</code> 还提供了一些高级特性：</p><ul><li><strong>请求和响应的验证：</strong>您可以定义验证逻辑来确保请求和响应的正确性。</li><li><strong>日志记录和监控：</strong>集成日志记录和监控工具，以便实时跟踪端点使用情况。</li><li><strong>多环境支持：</strong>轻松配置不同环境的设置，以支持开发、测试和生产环境。</li></ul><h2>总结</h2><p><code>fastapi_mcp</code> 是一个强大的工具，可以帮助开发者轻松地将 FastAPI 端点暴露为 MCP 工具，并提供认证支持。通过本文的教程，您可以快速入门并开始使用这个工具来构建安全、可扩展的 API。无论是简单的应用还是复杂的系统，<code>fastapi_mcp</code> 都可以为您提供可靠的支持。</p><p>要了解更多信息和详细文档，请访问 <a href=\"https://github.com/tadata-org/fastapi_mcp\">fastapi_mcp GitHub 仓库</a>。</p>",
  "tags": ["FastAPI", "MCP", "API", "认证", "Python"]
}
```</p><p>本教程由 <a href="https://www.lumjf.com/" target="_blank">@https://www.lumjf.com/ 全模型中转api可免费试用</a> 自动生成。</p>