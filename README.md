## DailyNewsReport

My Daily News：一键部署独属于你的每日新闻总览,支持 GPT3，Gemini Pro 模型。

![](https://cdn.zhangferry.com/Images/202402212338780.png)

基于 RSS 地址，每天早上 9 点采集一次前一天的内容，通过 GPT 进行分析总结，形成一份每日报告。

## Get Started

Fork 该仓库，删除 [src/content/blog](https://github.com/zhangferry/AIDailyNews/tree/main/src/content/blog) 里的文件，然后做如下修改：

1、修改 [rss.json](https://github.com/zhangferry/AIDailyNews/blob/main/workflow/resources/rss.json)，这里是你要订阅的 RSS 内容，以下是各参数说明：
   ```json5
   [
     {
       category: "Daily News", // 用于标记一类rss，它会在网页里被渲染为二级标题
       items: [
         {
           title: "The Keyword", // rss 标题
           url: "https://blog.google/rss/", // rss 源地址
           type: "link", // 表示获取rss信息的方式，不填会从rss返回信息获取，link：会从原始链接获取，code：会通过github api 获取对应仓库readme文件
         },
       ],
     },
   ]
   ```
2、配置数据采集的环境变量，为 Github 定时任务所需。

   ![](https://cdn.zhangferry.com/Images/202403161224264.png)

   GPT 能力所需：

   - `AI_PROVIDER`: 可选 `gemini` 和 `openai`。默认 `gemini`
   - `GPT_API_KEY`: 根据设置的 AI 能力填写对应的 Key
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
