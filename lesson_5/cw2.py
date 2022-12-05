# from pprint import pprint

import requests
from tabulate import tabulate

import random

m = 5 + random.choice([5, 10])


url = 'https://dummyjson.com/todos'

response = requests.get(url)


data = response.json()
# pprint(data)

data_list = []

for id_todo in range(1, 20 + 1):
    tmp_url = f'{url}/{id_todo}'
    response = requests.get(tmp_url)
    data = response.json()
    if data.get('completed'):
        data_list.append(data)


print(tabulate(data_list, headers='keys', tablefmt='grid'))
print()
print(tabulate(data_list, headers='keys', tablefmt='pipe'))
print()
print(tabulate(data_list, headers='keys', tablefmt='html'))
print()
print(tabulate(data_list, headers='keys', tablefmt='grid', stralign='center'))

list1 = ['kjdfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff']
