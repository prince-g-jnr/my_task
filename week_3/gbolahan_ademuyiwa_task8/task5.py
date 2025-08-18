# Creating a dictionary
store = {"Bag": 5, "Eraser": 10, "crayon": 15, "Book": 20, "Pen": 25}
print(store)
buy = input("What do you want to buy from the above items: ").title()
quantity = int(input(f"How many {buy} do you want to buy: "))
print(f"Before Purchase: {store}")
# Using assignment operator to update
store[buy] -= quantity
print(f"After Purchase: {store}")