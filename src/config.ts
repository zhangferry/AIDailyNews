import type { NavItems } from "./types";
import config from "./config/config.json"

export const NAV_ITEMS: NavItems = {
	home: {
		path: "/",
		title: "today",
	},
	blog: {
		path: "/blog",
		title: "blog",
	},
	tags: {
		path: "/tags",
		title: "tags",
	},
	about: {
		path: "/about",
		title: "about",
	},
};

export const SITE = {
	// Your site's detail?
	name: config.name,
	title: "zhangferry",
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
