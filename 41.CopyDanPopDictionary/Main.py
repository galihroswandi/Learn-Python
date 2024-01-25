
teman_teman = {
    "cup": "ucup surucup",
    "dung": "dudung surudung",
    "tong": "otong surotong"
}


# copy dictionary
friends = teman_teman.copy()
teman_teman["cup"] = "Ucup si kasyep"
print(f"teman_teman = {teman_teman}")
print(f"friends = {friends}")


# pop dictionary
ucup = teman_teman.pop("cup")
print(f"ucup = {ucup}")
print(f"teman_teman = {teman_teman}")


# popitem dictionary
otong = teman_teman.popitem()
print(f"otong = {otong}")
print(f"teman_teman = {teman_teman}")