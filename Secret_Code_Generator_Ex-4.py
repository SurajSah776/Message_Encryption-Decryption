# Secret Code Generator
''' Write a python program to translate a message into secret code language.
to translate normal English into secret code language

    Coding:
Use the rules below
if the word contains at least 3 characters,
    remove the first letter and append it at the end
    now append three random characters at the starting and the end
else:
    simply reverse the string

    Decoding:
if the word contains less than 3 characters,
    reverse it
else:
    remove 3 random characters from start and end. Now remove the last letter and add it to the beginning
    
#Your program should ask whether you want to code or decode
'''

# Program
import random
import string

# Function to generate 'n' random letters


def randomLetters(n):
    randomLetters = ""
    for x in range(n):
        randomLetters += random.choice(string.ascii_letters)
    return randomLetters


# Taking message Input
message = input("Enter Your Message : ")

choice = input("Enter 1 for Coding and 2 for Decoding : ")
coding = True if (choice == "1") else False

msgWords = message.split(" ")  # Gives the list of all the words
# print("Splitted Words : ", msgWords)


# Coding the Message
if (coding):

    # Asking User for Encrypting/Encoding Key
    key = int(input("Enter Encrypting Key (3, 4, 5) : "))

    codeWords = []
    for word in msgWords:
        if (len(word) >= 3):
            word = word[1:]+word[0]
            first = randomLetters(key)
            last = randomLetters(key)
            newWord = first+word+last
            # OR  newWord = first + word[1:] + word[0] + last
            codeWords.append(newWord)  # Putting the code words in list
        else:
            newWord = word[::-1]
            codeWords.append(newWord)
    print("Coded Word : ", " ".join(codeWords))

# Decoding the Message
else:

    # Asking User for Decrypting/Decoding Key
    key = int(input("Enter Decrypting Key (3, 4, 5) : "))

    decodeWords = []
    for word in msgWords:
        if (len(word) >= 3):
            word = word[key:-key]
            newWord = word[-1]+word[:-1]
            decodeWords.append(newWord)
        else:
            newWord = word[::-1]
            decodeWords.append(newWord)
    print("Decoded Word : ", " ".join(decodeWords))
