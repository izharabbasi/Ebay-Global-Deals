import requests
from lxml import html
from urllib.parse import urljoin
import csv

def get(element_lists):
    try:
        return element_lists.pop(0)
    except:
        return ''

def write_to_csv(data):
    headers = ['title' , 'price' , 'discont' , 'shipping']
    with open('deals.csv' , 'w' , encoding='utf-8') as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerows(data)


global_deal = []

resp = requests.get(url= 'https://www.ebay.com/globaldeals', headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
})

tree = html.fromstring(html=resp.content)

global_deals = tree.xpath("//div[@class='ebayui-dne-item-featured-card']/div/div")

for deals in global_deals:
    d = {
        'title': get(deals.xpath(".//h3/span/span[contains(@class,'ebayui-ellipsis-2')][1]/text()")),
        'price': get(deals.xpath(".//div[@class='dne-itemtile-price']/span[1]/text()")),
        'discont': get(deals.xpath(".//span[@class='itemtile-price-bold']/text()")),
        'shipping': get(deals.xpath(".//span[@class='dne-itemtile-delivery']/text()"))

    }
    global_deal.append(d)

print(len(global_deal))
write_to_csv(global_deal)

