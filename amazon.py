from bs4 import BeautifulSoup as BS
from selenium import webdriver
import time


def save():
    with open("parser.xls", "a") as file:
        file.write(f'{camera["title"]} ----- {camera["photo"]}\n')


def parser():
    driver = webdriver.Chrome()
    driver.get(
        "https://www.amazon.com/gp/browse.html?node=16713337011&ref_=nav_em_0_2_8_5_sbdshd_cameras"
    )
    time.sleep(3)
    pageSource = driver.page_source

    soup = BS(pageSource, "html.parser")
    items = soup.findAll("div", class_="s-item-container")

    cameras = []
    try:
        for item in items:
            cameras.append(
                {
                    "title": item.find(
                        "a",
                        class_="a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal",
                    ).get_text(strip=True),
                    "photo": item.find("img", class_="s-access-image cfMarker").get(
                        "src"
                    ),
                }
            )
            global camera
            for camera in cameras:
                print(camera["title"], camera["photo"])
                save()
    except:
        print("Данные не обнаружены!")
    driver.quit()


parser()
