#Program to count the number of vowels in a given string
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)


# Program to reverse a given string
s = input("Enter a string: ")
rev = s[::-1]
print("Reversed string:", rev)


# Program to count the number of words in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))


# Program to check whether a given string is a palindrome
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# Program to convert all characters of a string to uppercase
s = input("Enter a string: ")
print("Uppercase string:", s.upper())


# Program to find the sum of all elements in a given list
lst = [1, 2, 3, 4, 5]
total = sum(lst)
print("Sum of elements:", total)


# Program to find the largest element in a list
lst = [10, 25, 7, 89, 34]
largest = max(lst)
print("Largest element:", largest)


# Program to count the number of even numbers in a list
lst = [1, 2, 3, 4, 5, 6]
count = 0

for num in lst:
    if num % 2 == 0:
        count += 1

print("Number of even elements:", count)


# Program to reverse a list
lst = [1, 2, 3, 4, 5]
lst.reverse()
print("Reversed list:", lst)


# Program to check whether a given element exists in a list
lst = [10, 20, 30, 40]
element = int(input("Enter element to search: "))

if element in lst:
    print("Element found")
else:
    print("Element not found")

