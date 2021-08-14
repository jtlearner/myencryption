import random

width = 16
min_length = 512

mystring = "fuck transposition is cool"
casestring = ""
listgen = []

def gencase(char):
    randnum = random.random() * 25
    char = str(char)
    if randnum < 2: return char.capitalize()
    else: return char.lower()

def genchar():
    randnum = random.random()*25
    if randnum < 2: return chr(int(randnum+65)) # produce uppercase
    else: return chr(int(randnum+97)) # produce lowercase

for chars in mystring:
    casestring += gencase(chars)

def calclength(mystring, width):
    length = len(mystring) % width
    if length == 0: return (len(mystring) // width)
    else: return (len(mystring) // width)

mystring = casestring

#Calculate filler text
length = calclength(mystring, width)
min_filler = length * width
min_filler = min_filler + min_length
rangeinterval = min(width, length)

for nums in range(min_filler, (min_filler * 1000), rangeinterval):
    if (min_filler + nums) % length == 0:
        if (min_filler + nums) % width == 0:
            min_filler = (min_filler + nums)
            break

for chars in range(min_filler):
    mystring += genchar()

length = calclength(mystring, width)

# generate lists within list for that length
for chars in range(length):
    listgen.append([])

#workout what list the character belongs in, and place it in that list
for charnum, char in enumerate(mystring):
    position = (charnum % length)
    if char == " ": char = genchar()
    listgen[position].append(char)

placeholder = []
[placeholder.append(chars) for each in listgen for chars in each]

mystring = ""

for chars in placeholder:
    mystring += chars

print(mystring)