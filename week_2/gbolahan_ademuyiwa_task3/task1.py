# Task1
# 1. Write a program to take a string input from the user and display it in uppercase.
name = input("Enter your name: ")
print(name.upper())

# 2. Given the string "python", print its first and last character
word = "python"
print(word[0])
print(word[1])

# 3. Ask the user for their name and print "Hello,!" where is the user's input.
user_name = input("Enter your Name: ")
print(f"Hello {user_name}!")

# 4. Write a program to count the number of characters in a string without using len()
text = "where are you".lower()
print(text.count("e"))

# 5. Given "Hello World", replace "word" with "python".
message = "Hello Word"
print(message.replace("Word", "Python"))