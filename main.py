from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from my_parse.spiders.auto_youla import AutoyoulaSpider


if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule("my_parse.settings")
    crawler_process = CrawlerProcess(settings=crawler_settings)
    crawler_process.crawl(AutoyoulaSpider)
    crawler_process.start()
