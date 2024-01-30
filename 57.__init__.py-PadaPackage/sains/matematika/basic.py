
def tambah(*args):
    output = 0

    for i in args:
        output += i
    return output

def kali(*args):
    output = 1

    for i in args:
        output *= i

    return output
