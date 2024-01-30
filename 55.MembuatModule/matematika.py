# module

TAMBAH = lambda *args: sum(args)

def kali(*args)->float:
    output = 1
    for i in args:
        output *= i
    return output

def pangkat(n):
    return lambda i: i**n