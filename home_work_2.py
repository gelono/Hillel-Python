"""
Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне:
Попросіть користувача ввести свсвій вік (можно використати константу або input()).
- якщо користувачу менше 7 - вивести повідомлення "Де твої батьки?"
- якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
- якщо користувачу більше 65 - вивести повідомлення "Покажіть пенсійне посвідчення!"
- якщо вік користувача з двох однакових цифр - вивести повідомлення "Як цікаво!"
- у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"

P.S. На екран має бути виведено лише одне повідомлення, якщо вік користувача з двох однакових цифр
то має бути виведено тільки відповідне повідомлення! Також подумайте над варіантами,
коли введені невірні або неадекватні дані.
"""

age = input('Enter your age, please: ')

if age.isdigit():
    if int(age) < 1 or int(age) > 120:
        print('It is impossible')
    else:
        if len(age) == 2:
            if int(age[0]) == int(age[1]):
                print('It is very interesting...')
            else:
                if int(age) < 16:
                    print('This movie for the adults')
                elif int(age) > 65:
                    print("Please, show your pensioner's ID")
                else:
                    print('Sorry, all tickets were sold')
        elif len(age) == 1:
            if int(age) < 7:
                print('Where are your parents?')
            else:
                print('This movie for the adults')
        else:
            print("Please, show your pensioner's ID")
else:
    print('You entered an invalid value')