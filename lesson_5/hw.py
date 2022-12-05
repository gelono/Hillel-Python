# https://www.dictionary.com/e/vowels/
# The vowels in English are a, e, i, o, u, and sometimes y.
# we accept only English with y

vowels = set('euoiay')

user_text = input('Please, enter your text to analyse. Only    English is >>> ').lower().split()

word_counter = 0

for word in user_text:
    vowel_counter = 0
    for letter in word:
        if letter in vowels:
            vowel_counter += 1
        else:
            vowel_counter = 0

        if vowel_counter == 2:
            word_counter += 1
            break


n = None

try:
    n = int('00065.')
    m = n * 'kjtfg'
    print(m)


except ValueError:
    pass

if n:
    print('I am in')
else:
    print('fire!!!!!!!!')

