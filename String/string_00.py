string = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
whitespace = 0

for char in string:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        whitespace += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of digits:", digits)
print("Number of whitespace characters:", whitespace)