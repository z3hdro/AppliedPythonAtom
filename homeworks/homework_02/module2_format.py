import json
import csv


def file_tsv(file_name, encode):
    with open(file_name, encoding=encode) as f:
        inside_data = csv.reader(f, delimiter='\t')
        a = list()
        for i in list(inside_data):
            a.append(len(i))
        if a.count(a[0]) == len(a):
            return True
        else:
            return False


def file_json(file_name, encode):
    try:
        with open(file_name, encoding=encode) as f:
            inside_data = json.load(f)
    except json.JSONDecodeError:
        return False
    return True


def file_format(file_type, charset):
    if file_tsv(file_type, charset):
        return 'tsv'
    elif file_json(file_type, charset):
        return 'json'
    else:
        raise SystemExit("Формат не валиден")
