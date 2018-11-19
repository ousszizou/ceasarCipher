#!usr/bin/python3
# Caesar Cipher 
# Encryption => C = E(k,p) = (p + k) mod 26

MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('Do you want to encrypt or decrypt or brute force a message?')
        mode = input().lower()
        if mode in "e encrypt d decrypt b brute":
            return mode[0]
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b".')

def getMessage():
    print('Enter you message text: ')
    return input()

def getKey():
    key = 0
    print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
    key = int(input())
    if (key >= 1 and key <= MAX_KEY_SIZE):
        return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == "d":
        key = -key
    translated = ""

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            if symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()

message = getMessage()

if mode[0] != 'b':
    key = getKey()
    print('Your translated text is:')
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('decrypt', message, key))