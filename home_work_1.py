# 1. Задача: Створіть дві змінні first=10, second=30. Виведіть на екран результат математичної
# взаємодії (+, -, *, / и тд.) для цих чисел.

first, second = 10, 30
print(first + second)
print(first - second)
print(first * second)
print(first / second)
print(first // second)
print(first ** second)
print(first % second)

# 2. Задача: Створіть змінну і почергово запишіть в неї результат порівняння (<, > , ==, !=)
# чисел з завдання 1. Виведіть на екран результат кожного порівняння.

i = first < second
print(i)
i = first > second
print(i)
i = first == second
print(i)
i = first != second
print(i)

# 3. Задача: Створіть змінну - результат конкатенації (складання) строк str1="Hello " и str2="world". Виведіть на екран.

str1, str2 = 'Hello ', 'world'
result = str1 + str2
print(result)