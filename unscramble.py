import string, random

def unscramble(word):
    wordlist = open('wordlist.txt')
    wordlist = wordlist.read()
    wordlist = wordlist.split()

    word = [char for char in word]
    word = sorted(word)
    
    for i in range(len(wordlist)):
        other = wordlist[i]
        other = [char for char in other]
        other = sorted(other)

        if (word == other):
            print('Result : ' + wordlist[i])
            break
         
unscramble('kekak')