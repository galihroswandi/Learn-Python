'''Matematika'''

def tambah(*args):
    output = 0
    for i in args:
        output += i
    return output

def pangkat(n):
    return lambda angka:angka**n
