# 文章封面自动生成功能

## 🎨 功能概述

这个功能为没有图片的文章自动生成独特的 SVG 封面。每篇文章都会根据其标题、标签和日期生成独一无二的几何图案封面。

## ✨ 特性

- **自动生成**：无需手动设计，根据文章内容自动生成
- **独特性**：每篇文章都有独特的图案和配色
- **响应式**：支持浅色和深色主题
- **高性能**：使用 SVG，文件小且清晰
- **无需额外 API**：使用现有的 LLM 接口（可选）或纯算法生成
- **纯图案设计**：不包含文字，更简洁美观
- **全宽展示**：横向拉伸撑满屏幕，视觉效果更好

## 🚀 使用方法

### 1. 在文章卡片中使用

组件会自动检测文章是否有图片，如果没有则使用生成的封面：

```astro
---
import GeneratedCover from "$/components/GeneratedCover.astro";
---

{post.data.image ? (
  <img src={post.data.image} alt={post.data.title} />
) : (
  <GeneratedCover
    title={post.data.title}
    tags={post.data.tags}
    date={post.data.date}
    width={800}
    height={500}
    class="w-full h-full object-cover"
  />
)}
```

### 2. 自定义封面样式

#### 修改配色方案

在 `src/utils/coverGenerator.ts` 中修改：

```typescript
const colorSchemes = {
  light: [
    { primary: '#5b7c99', secondary: '#6bb8b8', accent: '#d4a5a5', bg: '#f8f9fa' },
    // 添加更多配色方案
  ],
  dark: [
    { primary: '#6bb8b8', secondary: '#d4a5a5', accent: '#d8b8a0', bg: '#1a1a2e' },
    // 添加更多配色方案
  ],
};
```

#### 修改封面比例

在各个页面组件中修改 `aspect-ratio`：

```css
/* 超宽比例（文章详情页） */
aspect-[21/9]

/* 标准比例（首页卡片） */
aspect-[16/10]

/* 方形比例 */
aspect-[1/1]
```

支持以下图案类型：
- `gradient` - 渐变背景
- `geometric` - 几何图形
- `waves` - 波浪图案
- `dots` - 点阵图案
- `lines` - 线条图案
- `abstract` - 抽象图案

### 3. 编程式使用

```typescript
import { generateCoverImageUrl } from '$/utils/coverGenerator';

const coverUrl = generateCoverImageUrl({
  title: '你的文章标题',
  tags: ['技术', 'AI'],
  date: '2024-03-17',
}, {
  width: 1200,
  height: 630,
  isDark: false,
  showTitle: true,
  showDate: true,
});
```

## 🔧 高级配置

### 选项说明

```typescript
interface CoverOptions {
  width?: number;        // 宽度，默认 800
  height?: number;       // 高度，默认 500
  isDark?: boolean;      // 是否深色模式，默认 false
  showTitle?: boolean;   // 是否显示标题（已禁用，纯图案设计）
  showDate?: boolean;    // 是否显示日期（已禁用，纯图案设计）
}
```

**注意**：当前版本默认不显示文字，只显示纯几何图案。如需显示文字，请修改 `src/components/GeneratedCover.astro` 中的参数。

### 预生成静态文件（可选）

如果你想在构建时预生成所有封面，可以使用提供的脚本：

```bash
# 构建时生成所有封面
node scripts/generate-covers.js
```

**注意**：这需要将 TypeScript 脚本编译为 JavaScript，或者在 `package.json` 中配置。

## 🎯 工作原理

1. **基于标题的一致性**：使用文章标题作为随机数种子，确保同一文章每次生成相同的封面
2. **图案选择**：根据标题哈希值选择图案类型
3. **配色方案**：随机选择预设的配色方案
4. **SVG 生成**：动态生成 SVG 代码并转换为 Data URL

## 📝 注意事项

1. **性能**：SVG Data URL 适合中小尺寸图片，对于大尺寸图片建议预生成静态文件
2. **SEO**：Data URL 不会被搜索引擎索引，如果 SEO 重要，考虑预生成静态文件
3. **缓存**：当前实现每次都会生成新的 Data URL，浏览器无法缓存。如果需要缓存，使用预生成方案

## 🔄 与 LLM 集成（可选）

如果你想使用 LLM 生成更智能的封面，可以扩展 `coverGenerator.ts`：

```typescript
// 示例：使用 LLM 生成 SVG 提示词
async function generateLLMCover(title: string, tags: string[]) {
  const prompt = `根据文章标题"${title}"和标签${tags.join(', ')}，生成一个SVG封面的描述...`;

  // 调用你的 LLM API
  const response = await callYourLLMAPI(prompt);

  // 根据 LLM 响应生成 SVG
  return generateSVGFromResponse(response);
}
```

## 🎨 示例效果

不同类型的封面示例（纯图案设计）：

1. **渐变风格**：柔和的渐变背景，无需文字干扰
2. **几何风格**：随机分布的圆形、矩形等几何图形
3. **波浪风格**：多层波浪图案，营造流动感
4. **点阵风格**：规律排列的圆点矩阵，简约现代
5. **线条风格**：随机角度的线条，动感十足
6. **抽象风格**：混合几何图形，艺术感强

所有封面都采用全宽展示，横向拉伸撑满屏幕，视觉效果更加震撼。

## 📚 相关文件

- `src/utils/coverGenerator.ts` - 核心生成逻辑
- `src/components/GeneratedCover.astro` - Astro 组件
- `scripts/generate-covers.ts` - 构建时生成脚本（可选）

## 🐛 故障排除

### 封面不显示

1. 检查浏览器控制台是否有错误
2. 确认 `title` 参数已正确传递
3. 检查 Data URL 是否过长（某些浏览器有限制）

### 封面样式不对

1. 检查 CSS 类名是否正确应用
2. 确认 `width` 和 `height` 参数
3. 检查深色模式是否正确检测

### 性能问题

1. 减少 `width` 和 `height` 参数
2. 考虑使用预生成静态文件方案
3. 减少页面上的封面数量

## 🚀 未来改进

- [ ] 支持更多图案类型
- [ ] LLM 智能生成封面描述
- [ ] 预生成并缓存封面
- [ ] 支持自定义字体
- [ ] 支持更多语言
- [ ] 添加动画效果
