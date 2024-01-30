
import sains.matematika
from sains import matematika
from sains.fisika import gaya as force

HasilTambah = sains.matematika.tambah(4,5,6,7)
print(f"Hasil tambah = {HasilTambah}")

HasilPangkat = matematika.pangkat(5)(4)
print(f"Hasil pangkat = {HasilPangkat}")

HasilGaya = force(10,20)
print(f"Hasil gaya = {HasilGaya}")