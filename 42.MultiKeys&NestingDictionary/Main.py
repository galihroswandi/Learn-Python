import datetime

mahasiswa1 = {
    "Nama":"Ucup surucup",
    "nim": "2645378463",
    "sks_lulus": 100,
    "beasiswa": False,
    "lahir": datetime.datetime(2000, 1, 1)
}

mahasiswa2 = {
    "Nama":"Otong surotong",
    "nim": "6374628347",
    "sks_lulus": 200,
    "beasiswa": True,
    "lahir": datetime.datetime(2005, 8, 30)
}

mahasiswa3 = {
    "Nama":"Asep si kasyep",
    "nim": "7453637289",
    "sks_lulus": 130,
    "beasiswa": False,
    "lahir": datetime.datetime(2004, 3, 10)
}

data_mahasiswa = {
    "MHSA001": mahasiswa1,
    "MHSA002": mahasiswa2,
    "MHSA003": mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<17} {'nim':<15} {'SKS':<5} {'beasiswa':<9} {'lahir':<10}")
print("-"*70)

for  mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    
    NAMA = data_mahasiswa[KEY]["Nama"]
    NIM = data_mahasiswa[KEY]["nim"]
    SKS = data_mahasiswa[KEY]["sks_lulus"]
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%d-%m-%Y")

    print(f"{KEY:<6} {NAMA:<17} {NIM:<15} {SKS:^5} {BEASISWA:<9} {LAHIR:<10}")