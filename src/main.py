CSV_PATH = "..\\resources\\Site1.csv"


def main():
    pass

def read_csv_file(path):
    f = open(path, 'r')
    for line in f:
        print(f.readline())

if __name__ == "__main__":
    print("hi")
    read_csv_file(CSV_PATH)