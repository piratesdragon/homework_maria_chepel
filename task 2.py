postcards = {
    "Maria":"London",
    "Lorenzo":"Milan",
    "Oleg":"Canberra",
    "Hans":"Calgary",
    "Mark":"Milan",
    "Alex":"Krakow",
    "Julia":"Murmansk"

}

postcards["Petra"] = "Paris"
postcards["Ivan"] = "Moscow"
postcards["Oleg"] = "Sydney"
unique_cities = set()
for i in postcards.values():
    unique_cities.add(i)
print('Уникальные города в коллекции: ', end = '')
print(*unique_cities, sep = ', ')
print('Количество уникальных городов:', len(unique_cities))
