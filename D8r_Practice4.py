#Python task ============
#Write a Python program to take a string and replace every character with its previous ASCII value character, then print the new string. Example: Input: Hello Output: Gdkkn

s = input("Enter a string: ")
result = ""

for ch in s:
    result += chr(ord(ch) - 1)

print("Output:", result)
