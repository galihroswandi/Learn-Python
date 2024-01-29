

def opersi(*args, **kwargs)->int:
    output = 0

    if(kwargs["option"] == "tambah"):
        for i in args:
            output += i
    elif(kwargs['option'] == "kali"):
        output = 1
        for i in args:
            output *= i
    else: 
        return "Tidak ada opersi yang dikerjakan"
    return output

HASIL = opersi(1,2,3,4, option="tambah")
print(f"Hasil tambah = {HASIL}")
HASIL = opersi(34,452,23, option="kali")
print(f"Hasil kali = {HASIL}")
