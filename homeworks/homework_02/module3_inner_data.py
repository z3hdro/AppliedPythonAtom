import json
import csv


def take_data_file(file_type, filename, encode):
    if file_type == 'json':
        with open(filename, encoding=encode) as f:
            data = json.load(f)
            try:
                arr = [list(data[0].keys())]
                for i in data:
                    arr.append(list(i.values()))
            except (KeyError, IndexError):
                raise SystemExit("Формат не валиден")
            print_file(arr)
    elif file_type == 'tsv':
        with open(filename, encoding=encode) as f:
            data = csv.reader(f, delimiter='\t', quotechar="'")
            data = [i for i in data]
            if len(data) < 1:
                raise SystemExit("Формат не валиден")
            print_file(data)


def print_file(inside):
    arr = list()
    for i in range(len(inside[0])):
        maximum = 0
        for j in inside:
            if type(j[i]) is str and len(str(j[i])) >= maximum:
                maximum = len(str(j[i]))
        arr.append(maximum)
    print("-" * (sum(arr) + (len(inside[0])-1) * 5 + 6))
    for i in inside:
        g = 0
        for j in i:
            if inside.index(i) == 0:
                print("|  " + " " * ((arr[g] - len(str(j)))//2) +
                      str(j) + " " * ((arr[g] - len(str(j)))//2), end="  ")
            else:
                if str(j).isdigit():
                    print("|  " + " " * (arr[g] - len(str(j))) +
                          str(j), end="  ")
                else:
                    print("|  " + str(j) + " " * (arr[g] - len(str(j))),
                          end="  ")
            g += 1
        print("|")
    print("-" * (sum(arr) + (len(inside[0])-1) * 5 + 6))
