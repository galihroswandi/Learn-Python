
data_dict = {
    "cup": "ucup surucup",
    "tg": "otong surotong",
    "key": "value"
}


# Panjang dari sebuah dictionary
dic_length = len(data_dict)
print(f"Data {data_dict} dengan panjang = {dic_length}")

# mengambil data dari sebuah dictionary atau object
dic_get = data_dict["cup"]
print(f"data {dic_get}")
dict_getMethod = data_dict.get("cup")
print(f"Data dictionary dengan get = {dict_getMethod}")

# mengubah data dictionary
data_dict.update({"key": "galihroswandi"})
print(data_dict)

# menghapus data dictionary
del data_dict["key"]
print(data_dict)