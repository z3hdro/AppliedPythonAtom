import sys


# Ваши импорты
from module1_encoding import file_encoding
from module2_format import file_format
from module3_inner_data import take_data_file


if __name__ == '__main__':
    filename = sys.argv[1]
    try:
        f = open(filename)
        f.close()
    except FileNotFoundError:
        raise SystemExit("Файл не валиден")
    code = str(file_encoding(filename))
    extension = file_format(filename, code)
    take_data_file(extension,filename, code)