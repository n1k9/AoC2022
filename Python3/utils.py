def read_file(filename: str) -> str:
    with open(filename) as f:
        s = f.read()
    return s


def aggregate(s: str) -> list[list]:
    split = s.split()
    print(split)
    return split
