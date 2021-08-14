string = ""
newstring = ""

string = input("What needs spongebobbing?\n")

for charnum, char in enumerate(string):
    if string.find(char,charnum) % 2 == 0: char = char.lower()
    else: char = char.capitalize()
    newstring += char

print(newstring)