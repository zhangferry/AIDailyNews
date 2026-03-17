/**
 * 动态封面生成器
 * 为文章生成独特的 SVG 封面
 */

export interface CoverConfig {
  title: string;
  tags?: string[];
  date?: string;
  category?: string;
}

// 预定义的配色方案
const colorSchemes = {
  light: [
    { primary: '#5b7c99', secondary: '#6bb8b8', accent: '#d4a5a5', bg: '#f8f9fa' },
    { primary: '#7C93C3', secondary: '#7da87b', accent: '#d8b8a0', bg: '#e9ecef' },
    { primary: '#6bb8b8', secondary: '#d4a5a5', accent: '#5b7c99', bg: '#f0f4f8' },
    { primary: '#d4a5a5', secondary: '#d8b8a0', accent: '#6bb8b8', bg: '#faf5f5' },
    { primary: '#7da87b', secondary: '#5b7c99', accent: '#d4a5a5', bg: '#f0f8f0' },
  ],
  dark: [
    { primary: '#6bb8b8', secondary: '#d4a5a5', accent: '#d8b8a0', bg: '#1a1a2e' },
    { primary: '#d4a5a5', secondary: '#6bb8b8', accent: '#7da87b', bg: '#252540' },
    { primary: '#d8b8a0', secondary: '#d4a5a5', accent: '#6bb8b8', bg: '#2f2f4f' },
    { primary: '#7da87b', secondary: '#d8b8a0', accent: '#d4a5a5', bg: '#1a2a2a' },
    { primary: '#5b7c99', secondary: '#6bb8b8', accent: '#d4a5a5', bg: '#1e2a3e' },
  ],
};

// 几何图案类型
type PatternType = 'gradient' | 'geometric' | 'waves' | 'dots' | 'lines' | 'abstract';

/**
 * 根据文章标题生成随机数（保持一致性）
 */
function seededRandom(seed: string): () => number {
  let hash = 0;
  for (let i = 0; i < seed.length; i++) {
    hash = ((hash << 5) - hash) + seed.charCodeAt(i);
    hash = hash & hash;
  }
  return () => {
    const x = Math.sin(hash++) * 10000;
    return x - Math.floor(x);
  };
}

/**
 * 生成随机颜色方案
 */
function getColorScheme(title: string, isDark: boolean = false) {
  const random = seededRandom(title);
  const schemes = isDark ? colorSchemes.dark : colorSchemes.light;
  return schemes[Math.floor(random() * schemes.length)];
}

/**
 * 生成图案类型
 */
function getPatternType(title: string): PatternType {
  const random = seededRandom(title);
  const patterns: PatternType[] = ['gradient', 'geometric', 'waves', 'dots', 'lines', 'abstract'];
  return patterns[Math.floor(random() * patterns.length)];
}

/**
 * 生成渐变背景 SVG
 */
function generateGradient(colors: typeof colorSchemes.light[0], width: number, height: number): string {
  const angle = Math.floor(Math.random() * 360);
  return `
    <defs>
      <linearGradient id="grad" gradientTransform="rotate(${angle})">
        <stop offset="0%" stop-color="${colors.primary}" stop-opacity="0.3"/>
        <stop offset="50%" stop-color="${colors.secondary}" stop-opacity="0.2"/>
        <stop offset="100%" stop-color="${colors.accent}" stop-opacity="0.3"/>
      </linearGradient>
    </defs>
    <rect width="100%" height="100%" fill="${colors.bg}"/>
    <rect width="100%" height="100%" fill="url(#grad)"/>
  `;
}

/**
 * 生成几何图案 SVG
 */
function generateGeometric(colors: typeof colorSchemes.light[0], width: number, height: number): string {
  const shapes = [];
  const numShapes = 5 + Math.floor(Math.random() * 5);

  for (let i = 0; i < numShapes; i++) {
    const x = Math.random() * width;
    const y = Math.random() * height;
    const size = 50 + Math.random() * 150;
    const type = Math.random() > 0.5 ? 'circle' : 'rect';
    const color = [colors.primary, colors.secondary, colors.accent][Math.floor(Math.random() * 3)];
    const opacity = 0.1 + Math.random() * 0.2;

    if (type === 'circle') {
      shapes.push(`<circle cx="${x}" cy="${y}" r="${size/2}" fill="${color}" fill-opacity="${opacity}"/>`);
    } else {
      shapes.push(`<rect x="${x - size/2}" y="${y - size/2}" width="${size}" height="${size}" fill="${color}" fill-opacity="${opacity}" transform="rotate(${Math.random() * 45} ${x} ${y})"/>`);
    }
  }

  return `
    <rect width="100%" height="100%" fill="${colors.bg}"/>
    ${shapes.join('\n    ')}
  `;
}

/**
 * 生成波浪图案 SVG
 */
function generateWaves(colors: typeof colorSchemes.light[0], width: number, height: number): string {
  const waves = [];
  const numWaves = 3 + Math.floor(Math.random() * 3);

  for (let i = 0; i < numWaves; i++) {
    const amplitude = 20 + Math.random() * 40;
    const y = (height / (numWaves + 1)) * (i + 1);
    const color = [colors.primary, colors.secondary, colors.accent][i % 3];
    const opacity = 0.15 + Math.random() * 0.1;

    let path = `M 0 ${y}`;
    for (let x = 0; x <= width; x += 50) {
      const yOffset = Math.sin((x / width) * Math.PI * 2 + i) * amplitude;
      path += ` L ${x} ${y + yOffset}`;
    }
    path += ` L ${width} ${height} L 0 ${height} Z`;

    waves.push(`<path d="${path}" fill="${color}" fill-opacity="${opacity}"/>`);
  }

  return `
    <rect width="100%" height="100%" fill="${colors.bg}"/>
    ${waves.join('\n    ')}
  `;
}

/**
 * 生成点阵图案 SVG
 */
function generateDots(colors: typeof colorSchemes.light[0], width: number, height: number): string {
  const dots = [];
  const spacing = 30 + Math.floor(Math.random() * 20);
  const radius = 3 + Math.random() * 5;

  for (let x = spacing/2; x < width; x += spacing) {
    for (let y = spacing/2; y < height; y += spacing) {
      const color = [colors.primary, colors.secondary, colors.accent][Math.floor(Math.random() * 3)];
      const opacity = 0.1 + Math.random() * 0.2;
      dots.push(`<circle cx="${x}" cy="${y}" r="${radius}" fill="${color}" fill-opacity="${opacity}"/>`);
    }
  }

  return `
    <rect width="100%" height="100%" fill="${colors.bg}"/>
    ${dots.join('\n    ')}
  `;
}

/**
 * 生成线条图案 SVG
 */
function generateLines(colors: typeof colorSchemes.light[0], width: number, height: number): string {
  const lines = [];
  const numLines = 8 + Math.floor(Math.random() * 8);

  for (let i = 0; i < numLines; i++) {
    const x1 = Math.random() * width;
    const y1 = Math.random() * height;
    const x2 = Math.random() * width;
    const y2 = Math.random() * height;
    const color = [colors.primary, colors.secondary, colors.accent][Math.floor(Math.random() * 3)];
    const opacity = 0.15 + Math.random() * 0.15;
    const strokeWidth = 1 + Math.random() * 3;

    lines.push(`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="${strokeWidth}" stroke-opacity="${opacity}" stroke-linecap="round"/>`);
  }

  return `
    <rect width="100%" height="100%" fill="${colors.bg}"/>
    ${lines.join('\n    ')}
  `;
}

/**
 * 生成抽象图案 SVG
 */
function generateAbstract(colors: typeof colorSchemes.light[0], width: number, height: number): string {
  const elements = [];
  const numElements = 6 + Math.floor(Math.random() * 6);

  for (let i = 0; i < numElements; i++) {
    const type = Math.random();
    const x = Math.random() * width;
    const y = Math.random() * height;
    const size = 30 + Math.random() * 100;
    const color = [colors.primary, colors.secondary, colors.accent][Math.floor(Math.random() * 3)];
    const opacity = 0.1 + Math.random() * 0.25;

    if (type < 0.33) {
      // 圆形
      elements.push(`<circle cx="${x}" cy="${y}" r="${size/2}" fill="${color}" fill-opacity="${opacity}"/>`);
    } else if (type < 0.66) {
      // 三角形
      const points = [
        `${x},${y - size/2}`,
        `${x - size/2},${y + size/2}`,
        `${x + size/2},${y + size/2}`
      ].join(' ');
      elements.push(`<polygon points="${points}" fill="${color}" fill-opacity="${opacity}"/>`);
    } else {
      // 椭圆
      elements.push(`<ellipse cx="${x}" cy="${y}" rx="${size/2}" ry="${size/3}" fill="${color}" fill-opacity="${opacity}" transform="rotate(${Math.random() * 360} ${x} ${y})"/>`);
    }
  }

  return `
    <rect width="100%" height="100%" fill="${colors.bg}"/>
    ${elements.join('\n    ')}
  `;
}

/**
 * 生成 SVG 封面
 */
export function generateSVGCover(
  config: CoverConfig,
  options: {
    width?: number;
    height?: number;
    isDark?: boolean;
    showTitle?: boolean;
    showDate?: boolean;
  } = {}
): string {
  const {
    width = 800,
    height = 500,
    isDark = false,
    showTitle = true,
    showDate = false,
  } = options;

  const colors = getColorScheme(config.title, isDark);
  const patternType = getPatternType(config.title);

  // 生成背景图案
  let background: string;
  switch (patternType) {
    case 'gradient':
      background = generateGradient(colors, width, height);
      break;
    case 'geometric':
      background = generateGeometric(colors, width, height);
      break;
    case 'waves':
      background = generateWaves(colors, width, height);
      break;
    case 'dots':
      background = generateDots(colors, width, height);
      break;
    case 'lines':
      background = generateLines(colors, width, height);
      break;
    case 'abstract':
      background = generateAbstract(colors, width, height);
      break;
    default:
      background = generateGradient(colors, width, height);
  }

  // 不生成文字内容，只保留背景图案
  let content = '';

  // 组合完整 SVG
  const svg = `
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" width="${width}" height="${height}">
      ${background}
      ${content}
    </svg>
  `;

  return svg;
}

/**
 * 将 SVG 转换为 Data URL
 */
export function svgToDataUrl(svg: string): string {
  const encoded = svg
    .replace(/"/g, "'")
    .replace(/</g, '%3C')
    .replace(/>/g, '%3E')
    .replace(/#/g, '%23');

  return `data:image/svg+xml,${encoded}`;
}

/**
 * 为文章生成封面图片 URL
 */
export function generateCoverImageUrl(
  config: CoverConfig,
  options: {
    width?: number;
    height?: number;
    isDark?: boolean;
    showTitle?: boolean;
    showDate?: boolean;
  } = {}
): string {
  const svg = generateSVGCover(config, options);
  return svgToDataUrl(svg);
}

/**
 * 保存 SVG 为文件（用于构建时生成）
 */
export async function saveSVGAsFile(
  svg: string,
  outputPath: string
): Promise<void> {
  // 这个函数在 Node.js 环境中使用
  // 在 Astro 构建时调用
  if (typeof Deno !== 'undefined') {
    await Deno.writeTextFile(outputPath, svg);
  } else if (typeof require !== 'undefined') {
    const fs = require('fs');
    fs.writeFileSync(outputPath, svg, 'utf8');
  } else {
    throw new Error('Cannot save file: no file system API available');
  }
}
