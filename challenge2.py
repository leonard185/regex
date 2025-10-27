import re

sentence = input("Enter a sentence containing one email: ")

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
match = re.search(pattern, sentence)

if match:
    email = match.group(0)
    print("Extracted email:", email)
