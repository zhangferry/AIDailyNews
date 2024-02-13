import path from "path";
import { promises as fs } from "fs";
import { globby } from "globby";
import grayMatter from "gray-matter";

(async function () {
  // prepare the dirs
  const srcDir = path.join(process.cwd(), "src");
  const publicDir = path.join(process.cwd(), "public");
  const contentBlogDir = path.join(srcDir, "content", "blog");
  const contentWeeklyDir = path.join(srcDir, "content", "weekly");
  // 过滤出文件后缀为md或者mdx的文件
  const mdContentFilePattern = path.join(contentBlogDir, "*.md");
  const mdxContentFilePattern = path.join(contentBlogDir, "*.mdx");

  const mdWeeklyFilePattern = path.join(contentWeeklyDir, "*.md");
  const mdxWeeklyFilePattern = path.join(contentWeeklyDir, "*.mdx");

  const indexFile = path.join(publicDir, "search-index.json");
  const getSlugFromPathname = (pathname) =>
    path.basename(pathname, path.extname(pathname));

  const contentFilePaths = await globby([
    mdContentFilePattern,
    mdxContentFilePattern,
    mdWeeklyFilePattern,
    mdxWeeklyFilePattern,
  ]);

  if (contentFilePaths.length) {
    const files = contentFilePaths.map(
      async (filePath) => await fs.readFile(filePath, "utf8")
    );
    const index = [];
    let i = 0;
    for await (let file of files) {
      const {
        data: { title, description, tags },
        content,
      } = grayMatter(file);
      index.push({
        slug: getSlugFromPathname(contentFilePaths[i]),
        category: "blog",
        title,
        description,
        tags,
        body: content,
      });
      i++;
    }
    await fs.writeFile(indexFile, JSON.stringify(index));
    console.log(
      `Indexed ${index.length} documents from ${contentBlogDir} to ${indexFile}`
    );
  }
})();
