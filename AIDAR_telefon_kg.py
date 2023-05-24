import requests
import csv
from bs4 import BeautifulSoup

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    'User-Agen :Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'
}


def get_html_page(url, params):
    response = requests.get(url=url, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.text
    else:
        return False

def get_all_block(html, tag, tag_class):
    return html.findAll(tag, class_=tag_class)


def get_content():
    url = 'https://telefon.kg/smartphone'
    result_list = list()
    for i in range(1):
        html = get_html_page(url, {'page': i})
        if html:
            soup_html = BeautifulSoup(html, 'html.parser')
            products = get_all_block(soup_html, 'div', 'product-layout product-list col-xs-12')
            for item in products:
                temp_list = list()
                temp_list.append(item.find('div', class_="caption").get_text(strip=True))
                temp_list.append(item.find('p', class_='price').get_text(strip=True))    
                temp_list.append(item.find('p', class_='description').get_text(strip=True))
                temp_list.append(item.find('a', href=True)['href'])
                temp_list.append(item.find('img', src=True)['src'])
                result_list.append(temp_list)
                with open('telefon_kg.csv', 'w') as csv_file:
                    file = csv.writer(csv_file, delimiter=',')
                    file.writerow(['Название', 'Цена', 'Описание', 'Ссылка на телефон', 'Ссылка на картинку'])
                    file.writerows(result_list)
    return result_list



res = get_content()

for i in res:
    print(res)


