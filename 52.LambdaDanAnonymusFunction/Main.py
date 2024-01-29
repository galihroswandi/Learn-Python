
def sayHello (name):
    return f"Hello my name is {name}"
print(sayHello("Otong surotong"))


# Use lambda function
sayHello = lambda name: f"Hello my name is {name}"

print(sayHello("Galih Roswandi"))

listAngka = [1,2,3,4,5,6,7]
filtersName = list(filter(lambda name: name < 3, listAngka))
print(filtersName) 


# anonymous function
def pangkat(n):
    return lambda x: x**n

pangkat2 = pangkat(2)
print(f"Hasil dari pangkat 2 = {pangkat2(20)}")
pangkatBebas = pangkat(5)(45)
print(f"Hasil dari pangkat bebas = {pangkatBebas}")