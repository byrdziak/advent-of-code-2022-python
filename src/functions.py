def read_file(path):
    with open(path) as f:
        file = f.read()

    return file


def list_to_chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
