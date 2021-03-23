word = input()
word_list = []
word_res = ''
for letter in word:
    word_list.append(letter)
word_list.reverse()
for letter_res in word_list:
    word_res += letter_res
if word_res == word:
    print('Palindrome')
else:
    print('Not palindrome')
