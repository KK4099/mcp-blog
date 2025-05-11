---
title: "benborla/mcp-server-mysql"
date: 2025-05-11T01:37:33.867860+00:00
tags: ["MCP"]
draft: false
---

<p>```json
{
  "title": "使用 MCP Server MySQL 实现 LLM 数据库只读查询",
  "tutorial_html": "<p>在现代应用程序中，使用大型语言模型（LLM）来处理和分析数据变得越来越普遍。然而，直接连接到数据库并执行查询可能会带来安全和性能问题。<code>benborla/mcp-server-mysql</code> 是一个 Model Context Protocol（MCP）服务器，专门用于提供对 MySQL 数据库的只读访问，允许 LLM 检查数据库模式并执行只读查询。本文将指导您如何使用该工具来实现安全的数据库访问。</p><h2>准备工作</h2><p>在开始之前，确保您已经安装了以下软件：</p><ul><li>Node.js</li><li>MySQL 数据库</li></ul><p>此外，您需要拥有一个 MySQL 数据库的只读用户帐户，以便安全地连接和查询。</p><h2>步骤 1: 克隆仓库</h2><p>首先，克隆 <code>benborla/mcp-server-mysql</code> 仓库到您的本地机器：</p><pre><code>git clone https://github.com/benborla/mcp-server-mysql.git</code></pre><p>进入项目目录：</p><pre><code>cd mcp-server-mysql</code></pre><h2>步骤 2: 安装依赖</h2><p>在项目目录中，运行以下命令安装所有必要的依赖：</p><pre><code>npm install</code></pre><h2>步骤 3: 配置服务器</h2><p>在项目目录中创建一个配置文件，例如 <code>config.json</code>，并添加数据库连接信息：</p><pre><code>{\n  \"database\": {\n    \"host\": \"localhost\",\n    \"user\": \"readonly_user\",\n    \"password\": \"your_password\",\n    \"database\": \"your_database_name\"\n  }\n}</code></pre><p>确保使用只读用户的凭证，以限制对数据库的写入访问。</p><h2>步骤 4: 启动 MCP Server</h2><p>使用以下命令启动服务器：</p><pre><code>node index.js</code></pre><p>服务器启动后，您将能够通过 MCP 协议连接到 MySQL 数据库并执行只读查询。</p><h2>步骤 5: 使用 LLM 执行查询</h2><p>现在，您可以将您的 LLM 配置为通过 MCP Server 连接到数据库。LLM 将能够读取数据库模式并执行查询，所有操作均为只读，确保数据的完整性和安全性。</p><p>以下是一个示例查询，LLM 可以通过 MCP Server 执行：</p><pre><code>SELECT * FROM table_name WHERE condition;</code></pre><h2>总结</h2><p>通过使用 <code>benborla/mcp-server-mysql</code>，您可以安全地为 LLM 提供对 MySQL 数据库的只读访问，这不仅提高了数据安全性，还简化了访问控制。该工具为现代数据驱动的应用程序提供了一种高效且安全的解决方案。</p>",
  "tags": ["MCP", "MySQL", "LLM", "只读访问", "数据库安全"]
}
```</p><p>本教程由 <a href="https://www.lumjf.com/" target="_blank">@https://www.lumjf.com/ 全模型中转api可免费试用</a> 自动生成。</p>