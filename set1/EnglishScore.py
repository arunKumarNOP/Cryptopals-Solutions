import binascii
from collections import *
from Xor import xor
import string

#WORDLIST = open('dictionary.txt').readlines()
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ENGLETTERS = string.printable

def getFreqCount(msg):
    letterCount = Counter()
    msg2 = msg.upper()

    for letter in LETTERS:
        count = msg2.count(letter)
        if count in letterCount:
            letterCount[count].append(letter)
        else:
            letterCount[count] = [letter]

    for freq in letterCount:
        letterCount[freq].sort(key=ETAOIN.find)
        letterCount[freq] = ''.join(letterCount[freq])

    s = ''
    for i in letterCount:
        s = letterCount[i] + s
    return s

def getScore(msg):
    freqCount = getFreqCount(msg)

    score = 0

    for c in ETAOIN[:6]:
        if c in freqCount[:6]:
            score += 1

    for c in ETAOIN[-6:]:
        if c in freqCount[-6:]:
            score += 1
    return score


def getEnglishLetterPercent(msg):
    count = 0
    msg = msg.upper()
    for letter in ENGLETTERS:
        if letter in msg:
            count += msg.count(letter)

    return (count*100.0)//len(msg)


def solve_single_xor(msg, engPerc=50, minScore=2):
    for i in range(0, 256):
        decry = xor(msg.strip(), hex(i)[2:], False)
        englishScore = getEnglishLetterPercent(decry)
        if englishScore >= engPerc:
            score = getScore(decry)
            if score >= minScore:
                yield i, decry

if __name__=='__main__':
    for line in open('4.txt').readlines():
        for ans in solve_single_xor(line):
            print ans