# Secret Message Code Generator
# Both Encryption and Decryption

# Program Code:
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
