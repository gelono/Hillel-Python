"""
1. Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові.
Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'".
Слово та номер символу отримайте за допомогою input() або скористайтеся константою.
Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".
"""

my_string = input("Enter your string, please: ")
symbol = input("Enter number of the symbol, please: ")

print(f"The {symbol} symbol in {my_string} is '{my_string[int(symbol) - 1]}'")

"""
2. Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою). 
Напишіть код, який визначить кількість слів, в цих даних.
"""

my_string = input("Enter your string, please: ")
my_string = my_string.split()

print(f"Your string consists {len(my_string)} words")

"""
3. Існує ліст з різними даними, наприклад 
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. 
Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1. 
Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.
"""

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

for element in lst1:
    if type(element) in (int, float):
        lst2.append(element)

print(lst2)