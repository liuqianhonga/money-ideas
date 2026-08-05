module.exports = function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy("src/favicon.svg");
  eleventyConfig.addPassthroughCopy("src/styles.css");
  eleventyConfig.addPassthroughCopy("src/robots.txt");

  eleventyConfig.setTemplateFormats(["md", "njk", "html"]);

  // 项目 collection：按日期倒序
  eleventyConfig.addCollection("projects", function (collectionApi) {
    return collectionApi
      .getFilteredByGlob("src/projects/*.md")
      .sort((a, b) => (a.data.date < b.data.date ? 1 : -1));
  });

  // 按日期分组（倒序）
  eleventyConfig.addFilter("groupByDate", function (collection) {
    const groups = new Map();
    for (const item of collection) {
      const d = new Date(item.data.date);
      const key = d.toISOString().slice(0, 10);
      if (!groups.has(key)) groups.set(key, []);
      groups.get(key).push(item);
    }
    return Array.from(groups, ([date, items]) => ({ date, items }));
  });

  // 日期显示格式 YYYY-MM-DD
  eleventyConfig.addFilter("dateDisplay", function (date) {
    if (!date) return "";
    const d = new Date(date);
    return d.toISOString().slice(0, 10);
  });

  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      data: "_data",
    },
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk",
  };
};
