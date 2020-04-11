import requests
import csv
from bs4 import BeautifulSoup
def get_html(url):
    r = requests.get(url)
    return r.text
def get_all_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='table').find_all("a")
    a_tags = list(set(table))
    links = []
    for a_tag in a_tags:
        a = a_tag.get('href')
        link = 'http://kenesh.kg' + a
        links.append(link)
    return links
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        full_name = soup.find('h3', class_='deputy-name').text.strip()
        avatar = soup.find('div', class_='deputy-img').find('img').get('src')
        phone_number = soup.find('p',class_='mb-10').find('a').text.strip()
        bio = soup.find('div', id='biography').text.strip()
    except AttributeError:
        full_name =""
        avatar = ""
        phone_number = ""
        bio = ""
    deputys_data = {
        'full_name': full_name, 'avatar': avatar,
        'phone_number':phone_number, "bio":bio,
    }
    return deputys_data
def write_data_to_csv(data):
    with open('deputys-data.csv','a') as file_:
            writer = csv.writer(file_)
            writer.writerow(
                (data['full_name'], data['phone_number'],
                data['bio'], data['avatar'])
                )
def main():
    url = "http://www.kenesh.kg/ru/deputy/list/35"
    all_links = get_all_links(get_html(url))
    for link in all_links:
        data = get_content(get_html(link))
        write_data_to_csv(data)
    # print(all_links)
if __name__ == '__main__':
    main()
    
