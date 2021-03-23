vowel = ['a', 'e', 'i', 'o', 'u', 'y']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
             'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

word = input()
for letter in word:
    if letter not in vowel and letter not in consonant:
        break
    elif letter in vowel:
        print('vowel')
    elif letter in consonant:
        print('consonant')
