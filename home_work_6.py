# 1. Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0.

argument = input('Enter an argument: ')


def type_convert(arg):
    """
    This function converts type of argument to float
    :param arg: any type
    :return: float or 0
    """
    try:
        arg = float(arg)
    except Exception:
        arg = 0
    return arg


result = type_convert(argument)
print(type(result))
print(result)

# 2. Напишіть функцію, що приймає два аргументи. Функція повинна
# якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
# у будь-якому іншому випадку повернути кортеж з цих аргументів

def action_with_arguments(arg_1, arg_2):
    """
    This function make an action with arguments depending on the type of arguments
    :param arg_1: any type
    :param arg_2: any type
    :return: int, float, str or tuple
    """
    if isinstance(arg_1, (int, float)) and isinstance(arg_2, (int, float)):
        return arg_1 * arg_2
    elif isinstance(arg_1, str) and isinstance(arg_2, str):
        return arg_1 + arg_2
    else:
        return arg_1, arg_2


value_1 = 1
value_2 = "string"
res = action_with_arguments(value_1, value_2)
print(res)

# 3. Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
# Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік.
# Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача
# (1 - рік, 22 - роки, 35 - років і тд...).

age = input('Вкажiть ваш вiк: ')


def box_office(age):
    """
    This function notes the user about the available tickets
    :param age: str
    :return: str
    """

    def get_years(age):
        """
        This inner function picks up correct word for user age
        :param age: str
        :return: str
        """
        if 11 <= int(age) <= 19:
            return 'років'
        elif int(age[-1]) == 1:
            return 'рік'
        elif int(age[-1]) in (2, 3, 4):
            return 'роки'
        else:
            return 'років'

    if age.isdigit():
        if int(age) < 1 or int(age) > 120:
            return f'Вам {age} {get_years(age)}? Це неможливо'
        else:
            if '7' in age:
                return f'Вам {age} {get_years(age)}, вам пощастить'
            elif len(age) == 2:
                if int(age) < 16:
                    return f'Тобі лише {age} {get_years(age)}, а це е фільм для дорослих!'
                elif int(age) > 65:
                    return f'Вам {age} {get_years(age)}? Покажіть пенсійне посвідчення!'
                else:
                    return f'Незважаючи на те, що вам {age} {get_years(age)}, білетів всеодно нема!'
            elif len(age) == 1:
                if int(age) < 7:
                    return f'Тобі ж {age} {get_years(age)}! Де твої батьки?'
                else:
                    return f'Тобі лише {age} {get_years(age)}, а це е фільм для дорослих!'
            else:
                return f'Вам {age} {get_years(age)}? Покажіть пенсійне посвідчення!'
    else:
        return 'Ви вказали некоректне значення'


res = box_office(age)
print(res)