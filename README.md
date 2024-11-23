## DailyNewsReport

My Daily News：一键部署独属于你的每日新闻总览,支持 GPT3，Gemini Pro 模型。

![](https://cdn.zhangferry.com/Images/202411041740985.png)

基于 RSS 地址，每天早上 9 点采集一次前一天的内容，通过 GPT 进行分析总结，形成一份每日报告。

## Get Started

Fork 该仓库，删除 [src/content/blog](https://github.com/zhangferry/AIDailyNews/tree/main/src/content/blog) 里的文件，然后做如下修改：

1、修改 [rss.json](https://github.com/zhangferry/AIDailyNews/blob/main/workflow/resources/rss.json)，这里是你要订阅的 RSS 内容，以下是各参数说明：
   ```json5
{
    "configuration": {
      // rsshub domain，当使用自定义 rsshub_path 时会自动拼接这个值
      "rsshub_domain": "https://rsshub.zhangferry.com/"
    },
    "categories": [
      {
        // rss分组，同时对应网页二级标题
        "category": "Daily News",
        // rss内容
        "items": [
          {
            // rss 标题，仅用做备注
            "title": "OpenAI Blog",
            // rss 地址
            "url": "https://openai.com/blog/rss.xml",
            // rss 内容获取方式。link：会从关联原始链接获取，code：会通过github api 获取对应仓库readme文件。不带该字段提取 rss 原始信息
            "type": "link",
            // 该链接最大输出内容数量，默认为 2
            "output_count": 3,
            // 会跟 `configuration.rsshub_domain` 进行拼接
            "rsshub_path": "github/trending/daily/swift",
             // 是否提取 rss 中的图片，仅从原始 rss 信息获取
             "image_enable": true
          },
        ],
      },
    ]
}
   ```
2、配置数据采集的环境变量，为 Github Action 定时任务所需。

  环境变量配置到 [main.yml](https://github.com/zhangferry/AIDailyNews/blob/main/.github/workflows/main.yml)中，隐私信息通过 Action 的 secret 管理。
   ![](https://cdn.zhangferry.com/Images/202403161224264.png)

   GPT 能力所需：

   - `AI_PROVIDER`: 可选 `gemini` 和 `openai`。默认 `gemini`
   - `GPT_API_KEY`: 根据设置的 AI 能力填写对应的 Key
   - `GPT_MODEL_NAME`: gemimi 默认 `gemini-pro`，openai 默认 `gpt-3.5-turbo`
   - `GPT_BASE_HOST`: 默认官方地址，可选

   更新仓库所需：

   - `GIT_NAME`：git 提交用户名
   - `GIT_EMAIL`: git email 地址
   - `ACCESS_TOKEN`: github token 权限。token 的生成需要到这里：个人头像 -> Settings -> Developer settings -> Personal access tokens，点击 Generate new token。

3、部署到 Vercel：[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fzhangferry%2FAIDailyNews)

🎉恭喜，你将会每天收到所订阅内容的总结啦！

## Build & Custom

用于本地调试和项目自定义。项目工作流程如下：

![](https://cdn.zhangferry.com/Images/whiteboard_exported_image.png)

数据采集部分使用 Python 实现，前端渲染使用 Astro 框架。

### 环境准备安装

创建本地环境变量

```bash
# copy 一个 env 模版
mv .env.example .env
```

在 .env 中填入`AI_PROVIDER` 和 `GPT_API_KEY`的值。

```bash
# python 依赖：
pip3 install -r ./requirements.txt

# js 依赖
yarn install --ignore-engines
```

### workflow 调试

workflow 的调试可以借助于 `workflow/test_mainflow` 里的 `test_mainflow_flow` 这个单测方法。 测试文件放在 `test_resources` 里， `.env` 和 `rss.json` 两个文件，分别用于指定本地的环境变量和需要观测的 rss 链接。

其他函数的调试对应 `test_` 开头的 python 文件。

### 启动数据采集

```bash
python3 main.py
```

### 页面渲染

页面样式基于 [astro-ink](https://github.com/one-aalam/astro-ink) 主题修改的，你可以换成基于该主题定制。

```bash
# 开启调试
yarn dev
```

首页样式配置对应 [src/config.ts](https://github.com/zhangferry/AIDailyNews/blob/main/src/config.ts) 中。
