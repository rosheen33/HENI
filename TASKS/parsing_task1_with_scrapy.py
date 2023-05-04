from scrapy.selector import Selector

# Extra Effort to show how this task can be concisely done with scrapy

# OUTPUT
# '''
#     The name of the artist (Peter Doig )
#     The name of the painting (The Architect's Home in the Ravine )
#     Price realised in GBP ( 11,282,500)
#     Price realised in USD ( 16,370,908)
#     Estimates in GBP ( 10,000,000 -  15,000,000)
#     Estimate in USD ( 14,509,999 -  21,764,999)
#     The url of the image of the painting
#     Saledate of the painting (11 February 2016 )
# '''


def main():
    input_file = open('../Data_Engineer_test/candidateEvalData/webpage.html', 'r')
    sel = Selector(text=input_file.read())
    input_file.close()

    item = {}
    item['artist'] = ' '.join(sel.css('.lotName ::text').getall()).strip().replace('(b. 1959)', '')
    item['title'] = sel.css('.itemName ::text').get()
    item['price_gpb'] = sel.css('#main_center_0_lblPriceRealizedPrimary::text').get().strip('GBP')
    item['price_usd'] = sel.css('#main_center_0_lblPriceRealizedSecondary::text').get().strip('USD')
    item['price_est_gpb'] = sel.css('#main_center_0_lblPriceEstimatedPrimary::text').get().replace('GBP', '')
    item['price_est_usd'] = sel.css('#main_center_0_lblPriceEstimatedSecondary::text').get().replace('USD', '')
    item['image'] = sel.css('#imgLotImage::attr(src)').get()
    item['sel_date'] = sel.css('#main_center_0_lblSaleDate ::text').get().replace(',', '')

    result = '''
    The name of the artist ({})
    The name of the painting ({})
    Price realised in GBP ({})
    Price realised in USD ({})
    Estimates in GBP ({})
    Estimate in USD ({})
    The url of the image of the painting: ({})
    Saledate of the painting ({})
    '''

    print(
        result.format(
            item['artist'], item['title'], item['price_gpb'],
            item['price_usd'], item['price_est_gpb'],
            item['price_est_usd'], item['image'], item['sel_date']
        )
    )

    return item


if __name__ == "__main__":
    main()

