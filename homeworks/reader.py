def read_data(filename):
    for coding in ('utf8', 'cp1251', 'utf16le', 'utf-16be'):
        try:
            with open(filename, encoding=coding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    raise ValueError
