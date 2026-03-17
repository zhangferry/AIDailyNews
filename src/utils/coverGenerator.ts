/**
 * 动态封面生成器
 * 为文章生成独特的 SVG 封面
 */

export interface CoverConfig {
  title: string;
  tags?: string[];
  date?: string;
  category?: string;
  headings?: string[];
}

declare const Deno:
  | {
    writeTextFile: (outputPath: string, svg: string) => Promise<void>;
  }
  | undefined;

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
type ColorScheme = (typeof colorSchemes.light)[number];

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

function hashString(value: string): number {
  let hash = 0;
  for (let i = 0; i < value.length; i++) {
    hash = (hash << 5) - hash + value.charCodeAt(i);
    hash |= 0;
  }
  return Math.abs(hash);
}

/**
 * 生成随机颜色方案
 */
function getColorScheme(title: string, isDark = false) {
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
function generateGradient(colors: ColorScheme, width: number, height: number): string {
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
function generateGeometric(colors: ColorScheme, width: number, height: number): string {
  const shapes: string[] = [];
  const numShapes = 5 + Math.floor(Math.random() * 5);

  for (let i = 0; i < numShapes; i++) {
    const x = Math.random() * width;
    const y = Math.random() * height;
    const size = 50 + Math.random() * 150;
    const type = Math.random() > 0.5 ? 'circle' : 'rect';
    const color = [colors.primary, colors.secondary, colors.accent][Math.floor(Math.random() * 3)];
    const opacity = 0.1 + Math.random() * 0.2;

    if (type === 'circle') {
      shapes.push(`<circle cx="${x}" cy="${y}" r="${size / 2}" fill="${color}" fill-opacity="${opacity}"/>`);
    } else {
      shapes.push(`<rect x="${x - size / 2}" y="${y - size / 2}" width="${size}" height="${size}" fill="${color}" fill-opacity="${opacity}" transform="rotate(${Math.random() * 45} ${x} ${y})"/>`);
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
function generateWaves(colors: ColorScheme, width: number, height: number): string {
  const waves: string[] = [];
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
function generateDots(colors: ColorScheme, width: number, height: number): string {
  const dots: string[] = [];
  const spacing = 30 + Math.floor(Math.random() * 20);
  const radius = 3 + Math.random() * 5;

  for (let x = spacing / 2; x < width; x += spacing) {
    for (let y = spacing / 2; y < height; y += spacing) {
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
function generateLines(colors: ColorScheme, width: number, height: number): string {
  const lines: string[] = [];
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
function generateAbstract(colors: ColorScheme, width: number, height: number): string {
  const elements: string[] = [];
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
      elements.push(`<circle cx="${x}" cy="${y}" r="${size / 2}" fill="${color}" fill-opacity="${opacity}"/>`);
    } else if (type < 0.66) {
      // 三角形
      const points = [
        `${x},${y - size / 2}`,
        `${x - size / 2},${y + size / 2}`,
        `${x + size / 2},${y + size / 2}`
      ].join(' ');
      elements.push(`<polygon points="${points}" fill="${color}" fill-opacity="${opacity}"/>`);
    } else {
      // 椭圆
      elements.push(`<ellipse cx="${x}" cy="${y}" rx="${size / 2}" ry="${size / 3}" fill="${color}" fill-opacity="${opacity}" transform="rotate(${Math.random() * 360} ${x} ${y})"/>`);
    }
  }

  return `
    <rect width="100%" height="100%" fill="${colors.bg}"/>
    ${elements.join('\n    ')}
  `;
}

function collectMotionSnippets(config: CoverConfig): string[] {
  const snippets = [config.title, ...(config.headings || []), ...(config.tags || [])]
    .map((item) => item.trim())
    .filter((item) => item.length > 0);

  return Array.from(new Set(snippets)).slice(0, 5);
}

type PixelIcon = {
  id: string;
  aliases: string[];
  pattern: string[];
};

const PIXEL_ICONS: PixelIcon[] = [
  {
    id: 'robot',
    aliases: ['agent', '智能体', '机器人', 'bot', 'assistant', 'ai agent'],
    pattern: ['000111111000', '001111111100', '011010010110', '111111111111', '110110110011', '111111111111', '101111111101', '101001001101', '111111111111', '001100001100', '011000000110', '110000000011']
  },
  {
    id: 'mouse',
    aliases: ['mouse', '鼠标', 'pointing device', 'trackpad'],
    pattern: ['001100001100', '011110011110', '111111111111', '111111111111', '111001100111', '111001100111', '111111111111', '011111111110', '001111111100', '000111111000', '000011110000', '000001100000']
  },
  {
    id: 'chip',
    aliases: ['ai', 'llm', '模型', '芯片', 'chip', 'gpu', 'compute'],
    pattern: ['000010000100', '001111111110', '011111111111', '111000000111', '111011110111', '111011110111', '111011110111', '111000000111', '111111111111', '011111111110', '001111111100', '000010000100']
  },
  {
    id: 'code',
    aliases: ['code', 'coding', '开发', '编程', 'repo', 'github'],
    pattern: ['000110000000', '001111000000', '011011100000', '110001110000', '000001110000', '000011100000', '000111000000', '001110000110', '011100001100', '111000011000', '011100001100', '001110000110']
  },
  {
    id: 'browser',
    aliases: ['browser', 'web', '页面', '前端', 'chrome', 'firefox'],
    pattern: ['111111111111', '100000000001', '101111111101', '101000001101', '101011101101', '101010101101', '101011101101', '101000001101', '101111111101', '100000000001', '111111111111', '000000000000']
  },
  {
    id: 'cloud',
    aliases: ['cloud', '云', 'server', 'infra', 'k8s', '部署'],
    pattern: ['000001110000', '000111111000', '001111111100', '011110011110', '111100001111', '111111111111', '111111111111', '011111111110', '001111111100', '000111111000', '000011110000', '000001100000']
  },
  {
    id: 'security',
    aliases: ['security', 'safe', '加密', '安全', 'auth', 'token'],
    pattern: ['000011110000', '000111111000', '001111111100', '001111111100', '001111111100', '000111111000', '000111111000', '001111111100', '011110011110', '111100001111', '011000000110', '001000000100']
  }
];

function detectPixelIcons(snippets: string[]): PixelIcon[] {
  const normalized = snippets.map((item) => item.toLowerCase());
  const matched = PIXEL_ICONS.filter((icon) =>
    icon.aliases.some((alias) =>
      normalized.some((text) => text.includes(alias.toLowerCase()))
    )
  );

  if (matched.length) {
    return matched.slice(0, 5);
  }

  return [PIXEL_ICONS[hashString(snippets.join('|')) % PIXEL_ICONS.length]];
}

function expandIconSet(baseIcons: PixelIcon[], targetCount: number, seedSource: string): PixelIcon[] {
  const expanded: PixelIcon[] = [];
  const base = baseIcons.length > 0
    ? baseIcons
    : [PIXEL_ICONS[hashString(seedSource) % PIXEL_ICONS.length]];
  const seed = hashString(seedSource);
  for (let i = 0; i < targetCount; i++) {
    if (i < base.length) {
      expanded.push(base[i]);
    } else {
      const fallback = PIXEL_ICONS[(seed + i) % PIXEL_ICONS.length];
      expanded.push(base[i % base.length] ?? fallback);
    }
  }
  return expanded;
}

function renderPixelPattern(
  pattern: string[],
  pixelSize: number,
  fill: string,
  secondary: string
): string {
  const rows = pattern.length;
  const cols = pattern[0]?.length || 0;
  const pixels: string[] = [];
  const shadows: string[] = [];
  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < cols; x++) {
      if (pattern[y][x] === '1') {
        shadows.push(
          `<rect x="${x * pixelSize + 1}" y="${y * pixelSize + 1}" width="${pixelSize}" height="${pixelSize}" fill="#000000" fill-opacity="0.18"/>`
        );
        const color = (x + y) % 3 === 0 ? secondary : fill;
        pixels.push(
          `<rect x="${x * pixelSize}" y="${y * pixelSize}" width="${pixelSize}" height="${pixelSize}" fill="${color}"/>`
        );
      }
    }
  }
  return `${shadows.join('\n          ')}\n          ${pixels.join('\n          ')}`;
}

function generatePixelMotion(
  config: CoverConfig,
  colors: ColorScheme,
  width: number,
  height: number
): string {
  void config;
  void colors;
  void width;
  void height;
  return '';
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

  const content = generatePixelMotion(config, colors, width, height);

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
