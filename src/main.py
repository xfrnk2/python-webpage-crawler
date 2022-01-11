import csv
from urllib import urlopen

CSV_PATH = "..\\resources\\Site1.csv"
URL_INDEX = 1

def main():
    pass

def read_urls_from_csv(path):
    url_list = []
    f = open(path, 'r')
    for _ in f:
        line = f.readline()
        url = line.split(",")[URL_INDEX]
        url_list.append(url)
        print(url)
    return url_list

if __name__ == "__main__":
    url_list = read_urls_from_csv(CSV_PATH)
