country = input().split(", ")
capital = input().split(", ")

dict_countries = dict(zip(country, capital))
for x, y in dict_countries.items():
    print(f"{x} -> {y}")