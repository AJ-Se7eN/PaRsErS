from bs4 import BeautifulSoup as BS
import requests

def save():
    with open('parser.xls','a') as file:
        file.write(f'{comp["title"]}---- {comp["price"]} ---- {comp["photo"]}\n')
def parse():
    URL= "https://www.olx.kz/elektronika/kompyutery-i-komplektuyuschie/"
    user_agent=input()
    HEADERS = {
        "User-Agent": user_agent
    }
    response = requests.get(URL, headers = HEADERS)
    soup = BS(response.content, "html.parser")
    items = soup.findAll('div', class_="offer-wrapper")
    comps = []
    try:
        for item in items:
            comps.append({
                "title":item.find('a', class_="marginright5 link linkWithHash detailsLink"),
                "price":item.find('p', class_='price').get_text(strip=True),
                "photo":item.find("img", class_="fleft").get('src')
            })
            global comp
            for comp in comps:
                print(comp["title"], comp["price"], comp["photo"])
                save()
    except:
        print("Данные не обнаружены!")
    
parse()

