from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from my_parse.spiders.Avito import AvitoSpider


if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule("my_parse.settings")
    crawler_process = CrawlerProcess(settings=crawler_settings)
    crawler_process.crawl(AvitoSpider)
    crawler_process.start()
