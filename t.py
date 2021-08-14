import random

lst = []
maxlength = 15
mystring = "123456789"

stringlength = len(mystring)

#generates random filler characters
def genchar():
    randnum = random.random()*25
    if randnum < 2: return chr(int(randnum+65)) # produce uppercase
    else: return chr(int(randnum+97)) # produce lowercase

# calculates the number of lines required in order to generate
# appropriate number of list items
def lines(stringlength):
    charsremaining = stringlength
    x = stringlength
    line1_datum = 1
    while charsremaining <= x:
        if charsremaining <= 0:
            break
        charsremaining -= line1_datum
        line1_datum += 1
        # print(charsremaining)
    return (line1_datum) - 1

def charposition(charnum):
    #somtehing in here will determine the position the char fills
    pass
# generate filler text using genchar and inputs into string
neededchars = maxlength - stringlength
for char in range (neededchars):
    mystring += genchar()

stringlength = len(mystring)
print(lines(stringlength))

print(mystring)

lst.append([])
current = 0

for charnum, char in enumerate(mystring):
    current = len(lst)-1
    # if len(lst[current]) > 1:

    if len(lst[current]) == 1:
        lst.append([])
        current += 1
    lst[current].append(char)

print(lst)