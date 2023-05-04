# -*- coding: utf-8 -*-

# Define here the models for your scraped items

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Compose


class ArtWorkItem(scrapy.Item):
    url = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field(output_processor=TakeFirst())
    media = scrapy.Field(output_processor=TakeFirst())

    price_gbp = scrapy.Field(
        input_processor=MapCompose(lambda p: p.strip(u'£')),
        output_processor=TakeFirst()
    )
    height_cm = scrapy.Field(
        input_processor=MapCompose(lambda h: h.split('x')[0]),
        output_processor=TakeFirst(),
    )
    width_cm = scrapy.Field(
        input_processor=MapCompose(lambda w: w.split('x')[-1].strip('cm')),
        output_processor=TakeFirst()
    )
