

def tambah(*angka)->int:
    total = 0
    for i in angka:
        total += i
    return total

HASIL = tambah(1,2,3,4,5,6,7,8,9)
print(HASIL)