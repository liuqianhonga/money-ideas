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

  // 全部标签聚合（去重，用于首页筛选栏）
  eleventyConfig.addCollection("allTags", function (collectionApi) {
    const tags = new Set();
    collectionApi.getFilteredByGlob("src/projects/*.md").forEach((item) => {
      (item.data.tags || []).forEach((t) => tags.add(t));
    });
    return Array.from(tags).sort();
  });

  // 信心指数计算（0-100）
  // confidence = 100 × (0.4×变现 + 0.3×(1-难度) + 0.3×(1-门槛))
  eleventyConfig.addFilter("confidence", function (data) {
    const ease = (n) => Math.max(1, Math.min(5, n || 3));
    const monetizationEase = ease(data.monetizationEase);
    const effortScore = ease(data.effortScore);
    const barrierScore = ease(data.barrierScore);
    const score =
      0.4 * (monetizationEase / 5) +
      0.3 * (1 - (effortScore - 1) / 4) +
      0.3 * (1 - (barrierScore - 1) / 4);
    return Math.round(score * 100);
  });

  // 信心指数评级文字
  eleventyConfig.addFilter("confidenceLabel", function (n) {
    if (n >= 80) return "极佳";
    if (n >= 60) return "良好";
    if (n >= 40) return "一般";
    return "谨慎";
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
