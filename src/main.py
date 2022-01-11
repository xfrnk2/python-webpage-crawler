from dataclasses import dataclass
from urllib.request import urlopen

from bs4 import BeautifulSoup

CSV_PATH = "..\\resources\\Site1.csv"
URL_INDEX = 1


@dataclass
class Course:
    href: str
    title: str
    instructor: str


def read_urls_from_csv(path):
    url_list = []
    f = open(path, 'r')
    for _ in f:
        line = f.readline()
        url = line.split(",")[URL_INDEX]
        url_list.append(url)
    return url_list


def scrap_category(url_list):
    result = []
    for url in url_list:
        url_without_new_line = url[:-1]
        u = urlopen(url)
        soup = BeautifulSoup(u.read(), 'html.parser')
        raw_result = soup.find_all("div", {"class": "course_card_item"})
        result.append(scrap_course(url_without_new_line, raw_result))
    return result


def scrap_course(url, raw_category_data):
    result = []
    for data in raw_category_data:
        href = url + data.find("a")["href"]
        info = data.find("div", {"class": "card-content"})
        title = info.find("div", {"class": "course_title"}).get_text()
        instructor = info.find("div", {"class": "instructor"}).get_text()
        result.append(Course(href, title, instructor))
    return result


def print_result(category_data):
    for course_data in category_data:
        for course in course_data:
            print(f"title: {course.title}\n"
                  f"instructor: {course.instructor}\n"
                  f"href: {course.href}\n")


if __name__ == "__main__":
    urls = read_urls_from_csv(CSV_PATH)
    result = scrap_category(urls)
    print_result(result)
