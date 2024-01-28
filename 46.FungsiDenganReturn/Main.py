'''Fungsi dengan return'''

# Kuadrat
def kuadrat(value):
    return value**2

x = kuadrat(5)
print(x)

tambah = 67 + kuadrat(3)
print(tambah)

# Tambah
def tambah(angka_1, angka_2):
    return angka_1 + angka_2

hasil = tambah(10, 5)
print(hasil)


# opersi kabataku
def operasi_matematika(angka_1, angka2):
    tambah = angka_1 + angka2
    kurang = angka_1 - angka2
    kali = angka_1 * angka2
    bagi = angka_1 / angka2

    return tambah,kurang,kali,bagi

k,l,m,n = operasi_matematika(9,8)

print(f"Hasil dari tambah = {k}")
print(f"Hasil dari kurang = {l}")
print(f"Hasil dari kali = {m}")
print(f"Hasil dari bagi = {n}")