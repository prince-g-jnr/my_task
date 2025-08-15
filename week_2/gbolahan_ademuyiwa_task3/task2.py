# Task2
# 6. Check if a given string contains the substring "python" (case-insensitive)
text = "python"
print("python" in text)

# 7. Write a program to reverse a string without using slicing([::-1])
text = "python"
print("".join(reversed(text)))

# 8. Given a string with extra spaces, remove the leading and trailing spaces
text = "  python  "
print(text.strip())

# 9. Ask the user to enter a sentence and print the number of vowels in it
user = input("Write a sentence: ").lower()
count  = user.count("a") + user.count("e") + user.count("i") + user.count("o") + user.count("u")
print(f"Total vowel: {count}")

# 10. convert a string "1234" to an integer and multiply it by 2.
text = int("1234")
print(text * 2)