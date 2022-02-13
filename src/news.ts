import * as rssParser from "rss-parser";

async function getNews() {
  const parser = new rssParser();

  const xml = "https://news.google.com/rss?gl=KR&hl=ko&ceid=KR:ko";
  const feed = await parser.parseURL(xml);

  let message = "";
  feed.items!.forEach((item) => {
    const { title } = item;
    if (title && item.title.length > 20) {
      message = `${message}<br># ${title}`;
    }
  });

  return message;
}

export { getNews };
