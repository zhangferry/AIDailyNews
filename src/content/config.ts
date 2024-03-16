import { z, defineCollection } from "astro:content";

const blogCollection = defineCollection({
	schema: z.object({
		title: z
			.string()
			.max(100, "The title length must be less than or equal to 100 chars"),
		description: z.string().optional(),
		tags: z.array(z.string()),
		date: z.string(),
		image: z.string().optional(),
	}),
});

export const collections = {
	blog: blogCollection,
};
