sentence = input("Enter a sentence containing one email: ")

# Split by spaces
words = sentence.split()

for word in words:
    if "@" in word and "." in word:
        email = word.strip(",.")
        break

print("Extracted email:", email)
