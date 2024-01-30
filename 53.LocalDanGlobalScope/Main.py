
# Access global scope from function

name = "Otong Surotong"

def printHello():
	print(f"Hello my name is {name}")
	nama = "Ucup Surucup"

printHello()

# print(f"Hello my name is {nama}") <-- tidak bisa mengakses variabel yang ada di dalam function


# Update nilai global variabel from function
angka = 0

def updateAngka(inputAngka:int)->int:
	global angka
	angka = inputAngka

updateAngka(6)
print(angka)


# tidak berpengaruh untuk operator if dll.
