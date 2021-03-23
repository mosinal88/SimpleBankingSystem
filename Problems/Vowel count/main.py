string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
i = 0
for vowel in string:
    if vowel in vowels:
        i += 1
print(i)
