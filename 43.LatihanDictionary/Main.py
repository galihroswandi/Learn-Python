import datetime
import os
import string
import random

mahasiswa_template = {
    "nama": "Ucup Setiawan",
    "nim": "A11.2020.12345",
    "sks_lulus": 100,
    "lahir": datetime.datetime(2000, 1, 1)
}

data_mahasiswa = {}

while True : 
    os.system("clear")
    print(f"{'SELAMAT DATANG':^30}")
    print(f"{'DATA MAHASISWA':^30}")
    print("-" * 30)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys(), "Undefined")

    mahasiswa["nama"] = input("Nama mahasiswa: ")
    mahasiswa["nim"] = input("NIM mahasiswa: ")
    mahasiswa["sks_lulus"] = int(input("SKS Lulus: "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
    BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    
    KEY = ''.join((random.choice(string.ascii_uppercase + string.digits) for _ in range(6)))
    data_mahasiswa.update({KEY: mahasiswa})

    print(f"{'KEY':<6} {'Nama':<17} {'nim':<15} {'SKS':<5} {'lahir':<10}")
    print("-"*60)

    for mhs in data_mahasiswa:
        KEY = mhs
        print(f"{KEY:<6} {data_mahasiswa[KEY]['nama']:<17} {data_mahasiswa[KEY]['nim']:<15} {data_mahasiswa[KEY]['sks_lulus']:<5} {data_mahasiswa[KEY]['lahir'].strftime('%d-%m-%Y'):<10}")
    
    is_done = input('\nApakah anda ingin melanjutkan (y/n)?')
    if is_done == 'n': 
        break



