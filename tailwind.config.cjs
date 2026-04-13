const { fontFamily } = require("tailwindcss/defaultTheme");
const config = require("./tailwind.theme.config.cjs");

/**
 * Editorial Magazine theme - warm, elegant, content-first design
 */
const themeConfig =
  process.env.THEME_KEY && config[process.env.THEME_KEY]
    ? config[process.env.THEME_KEY]
    : config.editorial;

const { colors } = themeConfig;

module.exports = {
  darkMode: "class",
  content: ["./public/**/*.html", "./src/**/*.{astro,js,ts}"],
  safelist: ["dark"],
  theme: {
    fontFamily: {
      display: [
        '"Playfair Display"',
        '"Noto Serif SC"',
        '"Songti SC"',
        '"SimSun"',
        "serif",
      ],
      sans: [
        '"Plus Jakarta Sans"',
        '"PingFang SC"',
        '"Microsoft YaHei"',
        "sans-serif",
      ],
      mono: ["'Fira Code'", ...fontFamily.mono],
      serif: [
        '"Playfair Display"',
        '"Noto Serif SC"',
        '"Songti SC"',
        "Georgia",
        "serif",
      ],
    },
    extend: {
      colors: {
        theme: {
          ...colors,
        },
      },
    },
  },
  plugins: [
    require("@tailwindcss/typography"),
    require("@tailwindcss/forms"),
    require("@tailwindcss/aspect-ratio"),
  ],
};
