#!/bin/bash/env python3
"""
This python script extracts a passphrase from a matrix of encrypted text
- You will need to convert vertical text back to horizontal.
- Clue: Treat the string of text like a matrix and transpose it. The keyword here is TRANSPOSE.
- Clue: there is fixed width/row:55 and hight/column:36.
- Clue: Write a regex to replace the symbols with a single space to get the password.
"""

def main():
    # Copy the text at the bottom into a file called matrix
    rawfile = open('C:\\Users\\James\\Desktop\\sandbox\\encrypt\\matrix.txt', 'r')
    rawmatrix = []
    for line in rawfile.readlines():
        row = []
        [row.append(char) if char.isalpha() == True else row.append(" ") for char in line]
        rawmatrix.append(row)
    
    newrow = []
    [newrow.append( rawmatrix[j][i]) for i in range (55) for j in range (36)]
    
    key = ""
    for char in newrow: key += char
    key = " ".join(key.split())
    print(key)

if __name__ == "__main__":
    main()