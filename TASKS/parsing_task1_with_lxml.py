from datetime import datetime

import pandas as pd
import re
from lxml import html


def main():
    item = {}
    html_page_link = 'Data_Engineer_test/candidateEvalData/webpage.html'
    html_etree = html.parse(html_page_link)

    name_xpath = '//h1[@class="lotName"]//text()'
    title_xpath = '//h2[@class="itemName"]/i//text()'
    usd_xpath = '//div[@class="price grey"]//text()'
    gbp_xpath = "//span[contains(text(),'Price realised')]/following-sibling::span/text()"
    est_gbp_xpath = "//span[contains(text(),'Estimate')]/following-sibling::span/text()"
    est_usd_xpath = "//div[contains(@class,'PriceEstimatedSecondary')]//span/text()"
    image_xpath = '//img[@id="imgLotImage"]/@src'
    date_xpath = "//span[contains(@id,'SaleDate')]/text()"

    # parse artist name
    if name := html_etree.xpath(name_xpath):
        name = re.sub(r"\(.*", "", name[0]).strip()
        item['artist'] = name

    # parse painting name
    if title := html_etree.xpath(title_xpath):
        item['title'] = title[0]

    # parse price GBP
    if gbp_price := html_etree.xpath(gbp_xpath):
        item['price_gpb'] = gbp_price[0].strip('GBP').replace(',', ' ')

    # parse price US
    if usd_price := html_etree.xpath(usd_xpath):
        item['price_usd'] = usd_price[0].strip('USD').replace(',', ' ')

    # parse price GBP est
    if price_est_gpb := html_etree.xpath(est_gbp_xpath):
        if price_est_gpb := re.findall(r"[\d|,]+", price_est_gpb[0]):
            item['price_est_gpb'] = ", ".join([re.sub(",", " ", ss) for ss in price_est_gpb])

    # parse price US est
    if price_est_usd := html_etree.xpath(est_usd_xpath):
        if price_est_usd := re.findall(r"[\d|,]+", price_est_usd[0]):
            item['price_est_usd'] = ", ".join([re.sub(",", " ", ss) for ss in price_est_usd])

    # image link
    if image := html_etree.xpath(image_xpath):
        item['image'] = image[0]

    # sale date
    if sel_date := html_etree.xpath(date_xpath):
        sel_date = sel_date[0].replace(',', '').strip()
        item['sel_date'] = str(datetime.strptime(sel_date, "%d %B %Y").date())

    df = pd.DataFrame({
        'artist_name': [item.get('artist', '')],
        'painting_name': [item.get('title', '')],
        'price_gbp': [item.get('price_gpb', '')],
        'price_usd': [item.get('price_usd', '')],
        'estimate_gbp': [item.get('price_est_gpb', '')],
        'estimate_usd': [item.get('price_est_usd', '')],
        'image_url': [item.get('image', '')],
        'sale_date': [item.get('sel_date', '')],
    })
    print(df.head(10))


if __name__ == "__main__":
    main()
