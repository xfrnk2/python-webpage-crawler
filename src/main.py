import json
from dataclasses import dataclass
from urllib.request import urlopen

from bs4 import BeautifulSoup

CSV_PATH = "..\\resources\\Site1.csv"
CATEGORY_NAME_INDEX = 0
CATEGORY_URL_INDEX = 1


@dataclass
class Course:
    href: str
    title: str
    instructor: str


def read_info_from_csv(path):
    data = {}
    f = open(path, 'r')
    for _ in f:
        line = f.readline()
        row = line.split(",")
        name = row[CATEGORY_NAME_INDEX]
        url = row[CATEGORY_URL_INDEX]

        data[name] = url
    return data


def scrap_category(info):
    result = {}
    for name, url in info.items():
        url_without_new_line = url[:-1]
        u = urlopen(url)
        soup = BeautifulSoup(u.read(), 'html.parser')
        raw_result = soup.find_all("div", {"class": "course_card_item"})
        result[name] = scrap_course(url_without_new_line, raw_result)
    return result


def scrap_course(url, raw_category_data):
    result = []
    for data in raw_category_data:
        href = url + data.find("a")["href"]
        info = data.find("div", {"class": "card-content"})
        title = info.find("div", {"class": "course_title"}).get_text()
        instructor = info.find("div", {"class": "instructor"}).get_text()
        result.append({
            "href": href,
            "title": title,
            "instructor": instructor,
        })
    return result


def save_as_json_file(result):
    file_path = "./sample_result.json"
    print(result)
    with open(file_path, 'w', encoding='UTF-8') as outfile:
        json.dump(result, outfile, ensure_ascii=False, indent=4)


def print_result(category_data):
    for course_data in category_data.values():
        for course in course_data:
            print(f"title: {course['title']}\n"
                  f"instructor: {course['instructor']}\n"
                  f"href: {course['href']}\n")


if __name__ == "__main__":
    info = read_info_from_csv(CSV_PATH)
    result = scrap_category(info)
    print_result(result)
    save_as_json_file(result)
