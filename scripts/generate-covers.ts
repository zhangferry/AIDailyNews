/**
 * 构建时生成文章封面
 * 为所有没有图片的文章生成独特的 SVG 封面
 */

import { getCollection } from 'astro:content';
import { generateSVGCover } from '../src/utils/coverGenerator';
import { writeFileSync, mkdirSync } from 'fs';
import { join } from 'path';

const OUTPUT_DIR = 'public/generated-covers';

/**
 * 为单篇文章生成封面并保存
 */
async function generateCoverForPost(post: any, outputDir: string) {
  const { data, slug } = post;

  // 如果文章已有图片，跳过
  if (data.image) {
    console.log(`✓ Skipping ${slug} (已有图片)`);
    return;
  }

  // 生成浅色和深色版本的 SVG
  const lightSVG = generateSVGCover({
    title: data.title,
    tags: data.tags,
    date: data.date,
  }, {
    width: 1200,
    height: 630,
    isDark: false,
    showTitle: true,
    showDate: true,
  });

  const darkSVG = generateSVGCover({
    title: data.title,
    tags: data.tags,
    date: data.date,
  }, {
    width: 1200,
    height: 630,
    isDark: true,
    showTitle: true,
    showDate: true,
  });

  // 保存文件
  const lightPath = join(outputDir, `${slug}-light.svg`);
  const darkPath = join(outputDir, `${slug}-dark.svg`);

  writeFileSync(lightPath, lightSVG, 'utf-8');
  writeFileSync(darkPath, darkSVG, 'utf-8');

  console.log(`✓ Generated cover for ${slug}`);
}

/**
 * 主函数
 */
export default async function generateCovers() {
  console.log('🎨 开始生成文章封面...\n');

  // 获取所有文章
  const posts = await getCollection('blog');

  // 创建输出目录
  mkdirSync(OUTPUT_DIR, { recursive: true });

  // 为每篇文章生成封面
  let generatedCount = 0;
  for (const post of posts) {
    if (!post.data.image) {
      await generateCoverForPost(post, OUTPUT_DIR);
      generatedCount++;
    }
  }

  console.log(`\n✨ 完成！共生成 ${generatedCount} 个封面\n`);
  console.log(`📁 封面保存在: ${OUTPUT_DIR}/`);
}
