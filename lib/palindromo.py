# -*- coding: utf-8 -*-

def palindrome(word):
    reversedLetters = []
    for letter in word:
        reversedLetters.insert(0, letter)
    reversedWord = ''.join(reversedLetters)
    if reversedWord == word:
        return True
    else:
        return False

def palindrome2(word):
    reversedWord = word[::-1]

    if reversedWord == word:
        return True
    return False


if __name__ == '__main__':
    word = str(raw_input('Escribe una palabra: '))
    
    result = palindrome2(word)

    if result is True:
        print('{} La palabra es un palindromo'.format(word))
    else:
        print('{} La palabra No es un palindromo'.format(word))
