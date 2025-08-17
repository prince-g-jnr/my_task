# Shopping List Manager
shopping_list = []
item1 = input("Enter you first shopping item: ")
item2 = input("Enter you second shopping item: ")
item3 = input("Enter you third shopping item: ")
shopping_list.append(item1)
shopping_list.append(item2)
shopping_list.append(item3)
print(shopping_list)
print(f"shopping list: {", ".join(shopping_list)}")