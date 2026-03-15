# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

DailyNewsReport 是一个自动化新闻聚合系统，通过 RSS 订阅源采集内容,使用 AI(GPT/Gemini/GLM)进行分析总结，生成每日新闻报告并发布到网站。

**技术栈:**
- **数据采集**: Python (feedparser, httpx, BeautifulSoup)
- **AI 集成**: OpenAI API / Google Gemini API / 智谱 GLM
- **前端渲染**: Astro (SSR) + Svelte + TailwindCSS
- **部署**: GitHub Actions (定时任务) + Vercel

**工作流程:**
```
RSS 订阅源 → Python 采集 → AI 分析评分 → Markdown 生成 → Astro 渲染 → Vercel 部署
```

## 项目结构

```
DailyNewsReport/
├── main.py                     # Python 入口，触发数据采集
├── workflow/                   # Python 数据处理逻辑
│   ├── mainflow.py            # 主流程编排
│   ├── article/               # 文章处理
│   │   ├── rss.py            # RSS 解析和文章提取
│   │   └── blog.py           # Markdown 文件生成
│   ├── gpt/                   # AI 集成
│   │   ├── request.py        # AI 请求封装 (OpenAI/Gemini)
│   │   ├── summary.py        # 文章评分和总结
│   │   └── prompt.py         # AI 提示词
│   ├── resources/            # 配置文件
│   │   └── rss.json          # RSS 订阅源配置
│   └── test_mainflow.py      # 单元测试入口
├── src/                       # Astro 前端代码
│   ├── config.ts             # 站点配置
│   ├── content/blog/         # 生成的 Markdown 文章存放于此
│   ├── pages/                # Astro 页面路由
│   └── components/           # Svelte/React 组件
└── .github/workflows/main.yml # GitHub Actions 定时任务
```

## 常用命令

### Python 数据采集开发

```bash
# 安装 Python 依赖
pip3 install -r ./requirements.txt

# 本地运行数据采集 (需要先配置 .env 文件)
python3 main.py

# 运行单元测试 (需要配置 workflow/test_resources/rss.json)
cd workflow && python -m pytest test_mainflow.py -s
# 或使用 unittest
cd workflow && python test_mainflow.py
```

### 前端开发

```bash
# 安装依赖
yarn install

# 启动开发服务器
yarn dev

# 构建生产版本
yarn build

# 类型检查
yarn check:type

# 代码检查
yarn lint

# 代码格式化
yarn format
```

## 核心配置

### 环境变量 (.env)

必需的环境变量:

```bash
# AI 提供商配置
AI_PROVIDER=openai              # 可选: openai, gemini
GPT_API_KEY=your_api_key       # API Key
GPT_MODEL_NAME=glm-4           # 模型名称
GPT_BASE_URL=https://open.bigmodel.cn/api/paas/v4  # API 地址

# 智谱 GLM 推荐:
# AI_PROVIDER=openai
# GPT_BASE_URL=https://open.bigmodel.cn/api/paas/v4
# GPT_MODEL_NAME=glm-4 或 glm-4-flash

# GitHub Actions 使用
GIT_NAME=your_name
GIT_EMAIL=your_email
ACCESS_TOKEN=github_token       # 需要 repo 权限

# 可选配置
MAX_ARTICLE_NUMS=12            # 每日最大文章数
RSS_CACHE_ENABLE=true          # 启用 RSS 缓存 (开发时)
```

### RSS 订阅配置 (workflow/resources/rss.json)

配置 RSS 订阅源和分类:

```json
{
  "configuration": {
    "rsshub_domain": "https://rsshub.zhangferry.com/"
  },
  "categories": [
    {
      "category": "分类名称",
      "items": [
        {
          "title": "订阅源标题",
          "url": "https://example.com/rss.xml",
          "rsshub_path": "github/trending/daily/swift",  // RSSHub 路径
          "type": "link",                                // link/code/原始RSS
          "output_count": 2,                             // 最大输出文章数
          "input_count": 5,                              // 最大输入文章数
          "image_enable": true                           // 是否提取图片
        }
      ]
    }
  ]
}
```

## 开发工作流

### 调试数据采集流程

1. **使用 RSS 缓存** (推荐用于调试 AI 部分)
   ```bash
   # 在 .env 中设置
   RSS_CACHE_ENABLE=true
   ```
   这会加载 `workflow/draft/article_cache_*.json` 而不重新抓取 RSS

2. **运行完整流程**
   ```bash
   python3 main.py
   ```

3. **查看生成的文章**
   生成的 Markdown 文件位于 `src/content/blog/dailyNews_*.md`

### 调试单个模块

- **RSS 解析**: `workflow/article/test_rss.py`
- **Markdown 生成**: `workflow/article/test_blog.py`
- **AI 评分**: `workflow/gpt/test_summary.py`

### 修改前端样式

- 站点配置: `src/config.ts`
- 主题基于 astro-ink 修改
- 页面布局: `src/layouts/`, `src/pages/`
- 组件: `src/components/`

## 重要说明

### AI 提供商配置

项目支持三种 AI 服务:

1. **智谱 GLM** (推荐，性价比高)
   - `AI_PROVIDER=openai`
   - `GPT_BASE_URL=https://open.bigmodel.cn/api/paas/v4`
   - `GPT_MODEL_NAME=glm-4`

2. **OpenAI**
   - `AI_PROVIDER=openai`
   - `GPT_BASE_URL=https://api.openai.com`

3. **Google Gemini**
   - `AI_PROVIDER=gemini`
   - `GPT_MODEL_NAME=gemini-2.5-flash`

### GitHub Actions 定时任务

- 定时任务: 每天 23:59 (UTC+8) 运行
- 配置文件: `.github/workflows/main.yml`
- 使用智谱 Coding 专用 API (`https://open.bigmodel.cn/api/coding/paas/v4`)
- 自动提交并推送到 main 分支

### RSS 文章类型处理

- **type: "link"**: 从原始链接提取内容
- **type: "code"**: 通过 GitHub API 获取仓库 README
- **无 type 字段**: 使用 RSS 原始内容

### 文章评分机制

- AI 根据文章内容评分 (0-10分)
- 按评分降序排列
- 每个订阅源根据 `output_count` 输出最多 N 篇文章
- 满分文章(10分)可以超过 `output_count` 限制

### 时区处理

- 所有时间统一使用 `Asia/Shanghai` 时区
- 文章发布时间会转换为中国时区
- 生成的 Markdown 文件名使用 `YYYY-MM-DD` 格式

## 测试

### 单元测试位置

- `workflow/test_mainflow.py`: 主流程测试
- `workflow/article/test_rss.py`: RSS 解析测试
- `workflow/article/test_blog.py`: Markdown 生成测试
- `workflow/gpt/test_summary.py`: AI 评分测试

### 测试资源

测试时需要配置 `workflow/test_resources/` 目录:
- `.env`: 环境变量
- `rss.json`: 测试用 RSS 配置

## 常见问题

1. **RSS 解析失败**: 检查 RSS URL 是否可访问,某些源需要代理
2. **AI 请求失败**: 检查 API Key 和网络连接, Gemini 在国内可能需要代理
3. **文章内容为空**: 检查 RSS 源格式,某些源需要设置 `type: "link"`
4. **GitHub Actions 失败**: 检查 Secrets 配置,确保 ACCESS_TOKEN 有 repo 权限

## 架构关键点

1. **Article 类** (`workflow/article/rss.py:16`): 文章数据模型,包含标题、摘要、链接、评分等
2. **AIProvider 类** (`workflow/gpt/request.py:8`): AI 请求封装,支持 OpenAI 和 Gemini 两种接口
3. **mainflow.execute()** (`workflow/mainflow.py:12`): 主流程入口,协调整个数据采集和生成过程
4. **RSS 配置加载** (`workflow/article/rss.py:39`): 支持单文件或目录方式加载 RSS 配置
5. **缓存机制** (`workflow/mainflow.py:93`): 可选启用 JSON 缓存避免重复抓取 RSS
