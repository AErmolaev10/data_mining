Avito_xpath = {
    "pagination": '//div[contains(@class, "pagination-hidden")]//a[@class="pagination-page"]/@href',
    "flat_url": '//div[@data-marker="item"]'
                '//div[contains(@class, "iva-item-body")]'
                '//a[@data-marker="item-title"]/@href',
}

Avito_xpath_data = {
    "title": "//h1/span/text()",
    "price": "//div[@class='item-view-content-right']//span[@itemprop='price']/text()",
    "address": "//span[@class='item-address__string']/text()",
    "parameters": "//div[@class='item-params']//li//text()",
    "author": "//div[@data-marker='seller-info/name']/a/@href",
}