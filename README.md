# Message_Encryption-Decryption
''' Write a python program to translate a message into secret code language.

Rules to translate normal English message into secret code language
------- Coding: -----------
-> Use the rules below
If the word contains at least 3 characters,
    * remove the first letter and append it at the end
    * now append three random characters at the starting and the end
else:
    * simply reverse the string

------- Decoding: -------
    * if the word contains less than 3 characters, reverse it
else:
    * remove 3 random characters from start and end. Now remove the last letter and add it to the beginning
    
#Your program should ask whether you want to code or decode and you can enter the encryption / decryption key 
'''
