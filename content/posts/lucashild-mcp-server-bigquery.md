---
title: "LucasHild/mcp-server-bigquery"
date: 2025-05-11T01:38:53.151121+00:00
tags: ["MCP"]
draft: false
---

<p>```json
{
  "title": "使用 LucasHild/mcp-server-bigquery 访问 BigQuery 的教程",
  "tutorial_html": "<p>随着数据分析需求的不断增加，越来越多的企业开始转向云端解决方案以满足其大规模数据处理需求。Google BigQuery 是其中一个备受欢迎的选项，它提供了强大的分析能力和可扩展性。然而，为了更方便地与 BigQuery 进行交互，您可能需要使用一些工具来简化流程。LucasHild/mcp-server-bigquery 就是这样一个工具，它通过 Model Context Protocol (MCP) 提供对 BigQuery 的访问。</p><p>本文将指导您如何使用 LucasHild/mcp-server-bigquery 来访问和查询 BigQuery 数据。</p><h2>准备工作</h2><p>在开始使用 mcp-server-bigquery 之前，您需要确保以下准备工作已经完成：</p><ul><li><strong>Google Cloud 账户：</strong>您需要一个有效的 Google Cloud 账户，并且已创建一个项目来使用 BigQuery。</li><li><strong>BigQuery 数据集：</strong>确保您的项目中已经存在一个 BigQuery 数据集。</li><li><strong>服务账户密钥：</strong>您需要创建一个服务账户，并下载其 JSON 格式的密钥文件，以便 mcp-server-bigquery 能够进行身份验证。</li></ul><h2>安装和配置</h2><p>首先，您需要克隆 mcp-server-bigquery 仓库并安装相关依赖项：</p><pre><code>git clone https://github.com/LucasHild/mcp-server-bigquery.git<br>cd mcp-server-bigquery<br>npm install</code></pre><p>接下来，配置您的服务账户密钥。将下载的 JSON 密钥文件放置在项目根目录，然后在项目中创建一个 <code>.env</code> 文件来存储环境变量：</p><pre><code>GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account-key.json</code></pre><h2>启动 MCP 服务器</h2><p>配置完成后，您可以启动 MCP 服务器：</p><pre><code>npm start</code></pre><p>服务器启动后，您将可以通过 MCP 协议与 BigQuery 交互。</p><h2>使用 MCP 进行查询</h2><p>启动服务器后，您可以使用 MCP 来执行查询。以下是一个简单的查询示例：</p><pre><code>const mcp = require('mcp-client');<br>const client = new mcp.Client('http://localhost:3000');<br><br>async function queryBigQuery() {<br>  const query = `SELECT name, age FROM \`your_project.your_dataset.your_table\``;<br>  const result = await client.query(query);<br>  console.log(result);<br>}<br><br>queryBigQuery();</code></pre><p>上述代码段展示了如何使用 <code>mcp-client</code> 库来连接到本地运行的 MCP 服务器并执行查询。在查询结果返回后，您可以根据具体需求进行处理。</p><h2>总结</h2><p>通过本文的教程，您已经了解了如何使用 LucasHild/mcp-server-bigquery 来与 Google BigQuery 进行交互。该工具通过 MCP 提供了一个简单的接口，使您能够轻松处理和查询大规模数据。希望这篇教程能够帮助您更好地利用 BigQuery 进行数据分析。</p>",
  "tags": ["BigQuery", "MCP", "数据分析", "教程"]
}
```</p><p>本教程由 <a href="https://www.lumjf.com/" target="_blank">@https://www.lumjf.com/ 全模型中转api可免费试用</a> 自动生成。</p>