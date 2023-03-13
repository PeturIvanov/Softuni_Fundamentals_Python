# countries = input().split(", ")
# cities = input().split(", ")
#
# countries_cities = list(zip(countries, cities))
#
# for i, el in countries_cities:
#     print(f"{i} -> {el}")
#

countries = input().split(", ")
cities = input().split(", ")

data = dict(zip(countries, cities))


for country, city in data.items():
    print(f"{country} -> {city}")
