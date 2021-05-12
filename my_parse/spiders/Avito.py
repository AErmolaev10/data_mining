import scrapy
from ..loaders import AvitoLoader
from ..xpaths import Avito_xpath, Avito_xpath_data


class AvitoSpider(scrapy.Spider):
    name = "avito"
    allowed_domains = ["www.avito.ru"]
    start_urls = ["https://www.avito.ru/moskva/kvartiry/prodam"]

    def _get_follow(self, response, selector_str, callback):
        for itm in response.xpath(selector_str):
            yield response.follow(itm, callback=callback)

    def parse(self, response, *args, **kwargs):
        yield from self._get_follow(
            response, Avito_xpath["pagination"], self.parse
        )
        yield from self._get_follow(
            response, Avito_xpath["flat_url"], self.flat_parse
        )

    def flat_parse(self, response):
        flat_loader = AvitoLoader(response=response)
        flat_loader.add_value("url", response.url)
        for key, xpath in Avito_xpath_data.items():
            flat_loader.add_xpath(key, xpath)
        yield flat_loader.load_item()
