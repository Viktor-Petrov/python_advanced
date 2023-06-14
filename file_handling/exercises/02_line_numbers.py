from string import punctuation

with open("exercises/text.txt", "r") as text_file:
    text = text_file.readlines()

new_file = open("exercises/new_text.txt", "w")

for i in range(len(text)):
    row = text[i]
    letters = 0
    marks = 0
    for symbol in row:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    new_file.write(f"Line {i + 1}: {''.join(row[:-1])} ({letters})({marks})\n")
new_file.close()