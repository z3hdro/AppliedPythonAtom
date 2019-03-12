def file_encoding(file_check: str):
    encode = ['utf-8', 'utf-16', 'cp1251']
    for i in encode:
        try:
            with open(file_check, encoding=i) as f:
                f.read()
            return i
        except UnicodeError:
            pass
    raise UnicodeError("Не определена кодировка")
