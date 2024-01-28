'''Fungsi dengan argument / parameter'''

def hello_world(nama):
    print(f"Hello dunia {nama}")

hello_world("Ucup surucup")
hello_world("Otong surotong")


def tambah(angka_1, angka_2):
    print(f"{angka_1} + {angka_2} = {angka_1 + angka_2}")

tambah(10, 5)
tambah(20, 5)

def listFunction(lists):
    dataLists = lists.copy()
    
    for list in dataLists:
        print(f"Hello selamat datang {list}")

listFunction(["Ucup", "Otong", "Dudung"])