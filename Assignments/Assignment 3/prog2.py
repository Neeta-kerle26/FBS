
ch = input("Enter an alphabet: ")

if ch.lower() in "aeiou" and len(ch) == 1 and ch.isalpha():
    print("Vowel")
elif len(ch) == 1 and ch.isalpha():
    print("Consonant")
else:
    print("Invalid input")