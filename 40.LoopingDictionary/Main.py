
teman_teman = {
    "cup": "ucup surucup",
    "tong": "otong surotong",
    "sep": "asep si kasyep",
    "dung": "dudung surudung"
}

# looping dictionary
for teman in teman_teman:
    print(teman)

# get spesifik for key
keys = teman_teman.keys()
print(keys)
for key in teman_teman.keys():
    print(key)

# get spesifik for values
values = teman_teman.values()
print(values)
for value in teman_teman.values():
    print(value)

# get all key and value
items = teman_teman.items()
print(items)
for item in teman_teman.items():
    print(item)

for key,value in teman_teman.items():
    print(f"{key} = {value}")