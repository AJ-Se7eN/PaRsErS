import time

from bs4 import BeautifulSoup as BS
from selenium import webdriver


def save():
    with open("parser.xls", "a") as file:
        file.write(f'{telephon["title"]} ----- {telephon["photo"]}\n')


def parser():
    driver = webdriver.Chrome()
    driver.get(
        "https://www.ebay.pl/sch/Telefony-komorkowe-i-smartfony/9355/i.html?LH_PrefLoc=2&rt=nc&_dmd=2&LH_BIN=1"
    )
    time.sleep(3)
    pageSource = driver.page_source

    soup = BS(pageSource, "html.parser")
    items = soup.findAll("div", class_="mimg itmcd img")

    telephons = []
    try:
        for item in items:
            telephons.append(
                {
                    "title": item.find("a", class_="vip").get_text(strip=True),
                    "photo": item.find("img", class_="img").get("src"),
                }
            )
            global telephon
            for telephon in telephons:
                print(telephon["title"], telephon["photo"])
                save()
    except:
        print("Успешно выполнено!")
    driver.quit()


parser()
