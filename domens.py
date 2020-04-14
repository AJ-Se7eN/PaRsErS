import time

from selenium import webdriver


def save():
    with open("parser.txt", "a") as file:
        file.write(
            f"{new_title[0]} ---- {new_title[1]} --- {new_title[2]} --- {new_title[3]}\n"
        )


def parser():
    for i in range(1, 7):
        driver = webdriver.Chrome()
        driver.get(
            "https://prod.etim-international.com/Unit/SearchPartial?page=" + str(i)
        )
        time.sleep(3)
        titles = driver.find_elements_by_class_name("selectableRef  ")
        for title in titles:
            global new_title
            new_title = title.text.split(" ")
            print(new_title[0], new_title[1], new_title[2], new_title[3])
            save()


parser()
