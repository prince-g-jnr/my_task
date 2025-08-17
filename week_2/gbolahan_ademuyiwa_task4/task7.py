# List manipulation
# creating a list of five cities
cities = ["Sango", "Oshodi", "Epe", "Lekki", "Yaba"]
print(cities)
# Replacing the third city with a new one (entered by the user).
cities[2] = input("Enter a new cities: ")
# Removing the last city
cities.pop()
# Adding a new city to the beginning of the list
cities.insert(0, "Ikeja")
# Updated List
print(cities)