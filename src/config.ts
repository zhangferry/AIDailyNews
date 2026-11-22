import type { NavItems } from "./types";
import config from "./config/config.json"

export const NAV_ITEMS: NavItems = {
	home: {
		path: "/",
		title: "最新日报",
	},
	blog: {
		path: "/blog",
		title: "往期归档",
	},
	tags: {
		path: "/tags",
		title: "主题",
	},
	about: {
		path: "/about",
		title: "关于",
	},
};

export const SITE = {
	// Your site's detail?
	name: config.name,
	title: "Daily News · 每日科技简报",
	description: `Made with ${config.aiprovider_model}`,
	url: "https://daily.zhangferry.com",
	githubUrl: "https://github.com/zhangferry/AIDailyNews",
	listDrafts: true,
	image:
		"https://cdn.zhangferry.com/Images/moyuzai_alpha.png",
	// YT video channel Id (used in media.astro)
	ytChannelId: "",
	// Optional, user/author settings (example)
	// Author: name
	author: "zhangferry", // Example: Fred K. Schott
	// Author: Twitter handler
	authorTwitter: "", // Example: FredKSchott
	// Author: Image external source
	authorImage: "https://cdn.zhangferry.com/Images/moyuzai_alpha.png", // Example: https://pbs.twimg.com/profile_images/1272979356529221632/sxvncugt_400x400.jpg, https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png
	// Author: Bio
	authorBio:
		"gemini pro",
};

// Ink - Theme configuration
export const PAGE_SIZE = 8;
export const USE_POST_IMG_OVERLAY = false;
export const USE_MEDIA_THUMBNAIL = false;

export const USE_AUTHOR_CARD = true;
export const USE_SUBSCRIPTION = false; /* works only when USE_AUTHOR_CARD is true */

export const USE_VIEW_STATS = false;

// Google AdSense —— 手动广告位
// AD_SLOT_* 值在 AdSense 后台「广告 → 按广告单元 → 展示广告」创建后填入 data-ad-slot；
// 留空字符串则对应位置不渲染任何广告元素
export const ADSENSE_CLIENT = "ca-pub-1404623154743926";
export const AD_SLOT_ARTICLE_BOTTOM = "8364484754"; // daily-news-bottom（新单元）；旧备用 4581227313
