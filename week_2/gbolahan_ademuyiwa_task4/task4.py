# Name Organizer
names = input("Enter five names \"seprated with space\" : ")
name = names.lower()
name_list = name.split(" ")
name_list.sort()
print(name_list)
for name in range(len(name_list)):
    print(name_list[name])