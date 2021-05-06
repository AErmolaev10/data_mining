# -*- coding: utf-8 -*-
import pymongo
import scrapy




class AutoyoulaSpider(scrapy.Spider):
    name = 'auto.youla'
    allowed_domains = ['auto.youla.ru']
    start_urls = ['https://auto.youla.ru/']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_client = pymongo.MongoClient()


    def _get_follow(self, response, selector_str, callback):
        for itm in response.css(selector_str):
            url = itm.attrib["href"]
            yield response.follow(url, callback=callback)

    def parse(self, response, *args, **kwargs):
        yield from self._get_follow(
            response,
            ".TransportMainFilters_brandsList__2tIkv .ColumnItemList_column__5gjdt a.blackLink", #бренды
            self.brand_parse
        )

    def brand_parse(self, response):
        yield from self._get_follow(
            response,
            ".Paginator_block__2XAPy a.Paginator_button__u1e7D",
            self.brand_parse
        )
        yield from self._get_follow(
            response,
            "article.SerpSnippet_snippet__3O1t2 a.SerpSnippet_name__3F7Yu.blackLink",
            self.car_parse
        )


    def car_parse(self, response):
        data = {
            "url": response.url,
            "title": response.css(".AdvertCard_advertTitle__1S1Ak::text").extract_first(),
            "img": [img.attrib["src"] for img in response.css("img.PhotoGallery_photoImage__2mHGn")],
            "description": response.css(".AdvertCard_descriptionInner__KnuRi::text").extract_first(),
        }

        self.db_client["scrapy_HW4"][self.name].insert_one(data)


