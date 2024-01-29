import string

def sepuluhPangkat (pangkat: int) -> int:
    return 10 ** pangkat

HASIL = sepuluhPangkat(4)
print(HASIL)


def display(name: string):
    print(f"Hello {name}")

display("Otong")