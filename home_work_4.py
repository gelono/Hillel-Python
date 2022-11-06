# 1. Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів,
# які містять дві голосні літери підряд.

some_string = 'Start enjoying custom English lessons with a teacher we guarantee will bring out your best. ' \
              'Learn any language systematically with different monthly subscriptions anywhere you want. ' \
              '30, 45, 60 min lessons. 30+ Languages to learn. Native speakers.'

pool_of_letters = 'aeiouy'

some_string = some_string.lower().split()
num_of_words = []
for word in some_string:
    temp_value = ' '
    for letter in word:
        if letter in pool_of_letters and temp_value in pool_of_letters:
            num_of_words.append(word)
            break
        temp_value = letter

print(num_of_words)
print(f'The number of words with the two vowels in a row is: {len(num_of_words)}')

# 2. Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами: { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245,
# "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між
# мінімальною і максимальною ціною.

stores_and_prices = { "cito": 47.999,
                      "BB_studio": 42.999,
                      "momo": 49.999,
                      "main-service": 37.245,
                      "buy.now": 38.324,
                      "x-store": 37.166,
                      "the_partner": 38.988,
                      "store": 37.720,
                      "rozetka": 38.003}

lower_limit = 35.9
upper_limit = 37.339

for store in stores_and_prices:
    if lower_limit <= stores_and_prices[store] <= upper_limit:
        print(store)
