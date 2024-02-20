## DailyNewsReport

基于 AI 进行信息采集，设置定时任务，每天早上 9 点总结前一天的内容，汇总内容生成一份 markdown 文档，将文档内容展示到网页中，就形成了一份每日总结。

![](https://cdn.zhangferry.com/Images/202402210023524.png)

## 数据采集

### 环境配置

信息采集部分使用 Python 完成，需要安装 python 依赖：

```bash
pip3 install -r ./requirements.txt
```

创建 `.env`

```bash
mv .env.example .env
```

添加这几个环境变量，`AI_PROVIDER` 可选 `gemini` 和 `openai`，`GPT_API_KEY` 根据设置的引擎填充对应的 Key，
如果使用代理地址，还需要设置 `GPT_BASE_HOST`。

开启采集：

```bash
python3 main.py
```

### 数据源

通过 RSS 链接生成数据源，建议每个分类创建一个 json 文件，格式如下：

```json
[
  {
    "category": "Daily Code", // 用于标记一类rss，它会在博客里渲染为二级标题
    "items": [
      {
        "title": "The Keyword",
        "url": "https://blog.google/rss/", // rss 源地址
        "type": "link" // 表示获取rss信息的方式，不填会从rss返回信息获取，link：会从原始链接获取，code：会通过github api 获取readme信息
      }
    ]
  }
]
```

有些网站没有提供 RSS 信息，如果仍想收集该网站信息的话，有两种方式，一种是在一些三方制作的 RSS 源进行查找，类似 [RSSHub](https://docs.rsshub.app)，看是否已经收录；另一种方式是自己制作，类似 [python-feedgen](https://github.com/lkiesow/python-feedgen)，这种库。

## 页面渲染

页面渲染是基于 [astro-ink](https://github.com/one-aalam/astro-ink) 主题修改的，你可以换成基于该主题定制，也可以换成其他前端主题。

```bash
# 安装依赖
yarn install --ignore-engines
# 开启调试
yarn dev
```
