import json

def parsing(data):
    try:
        return read_json(data)
    except ValueError:
        return read_tsv(data)
    except IOError:
        pass
    raise ValueError


def read_tsv(data):
    try:
        return [row.split('\t') for row in data.split('\n') if row]
    except Exception:
        raise ValueError


def read_json(data):
    try:
        data = json.loads(data)
    except json.decoder.JSONDecodeError:
        raise ValueError

    result = [list(data[0].keys())]
    for item in data:
        try:
            result.append([
                str(item[column_name])
                for column_name in result[0]
            ])
        except (KeyError, IndexError):
            raise IOError
    return result
