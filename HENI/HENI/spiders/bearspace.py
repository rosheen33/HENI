import re
from HENI.items import ArtWorkItem
from scrapy.loader import ItemLoader
from scrapy.spiders import SitemapSpider


class BearspaceSpider(SitemapSpider):
    name = 'bearspace'
    allowed_domains = ['bearspace.co.uk']

    sitemap_urls = ['https://www.bearspace.co.uk/sitemap.xml']
    sitemap_rules = [('/product', 'parse_item')]

    start_regex = r'(\d+\.?\d*)[cm|cms|W|w]'
    mid_regex = r'*\s*[x|×|X]\s*[\D]*\s*'
    last_regex = r'(\d+\.?\d*)\s*[cm|cms]*'
    dims_regex = rf"{start_regex}{mid_regex}{last_regex}"

    def parse_item(self, response):
        item_loader = ItemLoader(
            item=ArtWorkItem(), response=response
        )
        item_loader.add_value('url', response.url)
        item_loader.add_css('title', 'h1[data-hook=product-title]::text')
        item_loader.add_css('price_gbp', '[property="product:price:amount"]::attr(content)')
        self.extract_height_width_media(response, item_loader)
        yield item_loader.load_item()

    def extract_height_width_media(self, response, item_loader):
        description = response.css('[data-hook=description] ::text').getall()

        for desc in description:
            raw_dims = re.search(self.dims_regex, desc)
            if raw_dims:
                item_loader.add_value('height_cm', raw_dims.group(1))
                item_loader.add_value('width_cm', raw_dims.group(2))
            else:
                item_loader.add_value('media', desc)
