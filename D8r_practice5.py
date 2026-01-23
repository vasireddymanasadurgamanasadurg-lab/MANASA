sentence = input("Enter a sentence: ")
letter = input("Enter a single letter: ")

count = 0
for ch in sentence:
    if ch == letter:
        count += 1

print("The letter", letter, "repeats", count, "times")
