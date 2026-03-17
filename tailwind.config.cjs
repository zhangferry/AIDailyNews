const { fontFamily } = require("tailwindcss/defaultTheme");
const config = require("./tailwind.theme.config.cjs");

/**
 * Find the applicable theme color palette, or use the default one
 * Using neon-magazine theme for modern digital magazine style
 */
const themeConfig =
  process.env.THEME_KEY && config[process.env.THEME_KEY]
    ? config[process.env.THEME_KEY]
    : config.neonmagazine;

const { colors } = themeConfig;

module.exports = {
  darkMode: "class",
  content: ["./public/**/*.html", "./src/**/*.{astro,js,ts}"],
  safelist: ["dark"],
  theme: {
    fontFamily: {
      display: ["Syne", "sans-serif"],
      sans: ["Plus Jakarta Sans", "sans-serif"],
      mono: ["Fira Code", ...fontFamily.mono],
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
