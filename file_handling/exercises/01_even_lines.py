punctuations = ["-", ",", ".", "!", "?"]

with open("exercises/text.txt", "r") as even_lines_file:
    text = even_lines_file.readlines()
for r in range(0, len(text), 2):
    for symbol in punctuations:
        text[r] = text[r].replace(symbol, "@")
    print(*text[r].split()[::-1], sep=" ")