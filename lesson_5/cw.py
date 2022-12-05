from pprint import pprint

import requests


url = 'https://dummyjson.com/products'

response = requests.get(url)
# print(response.content)
# pprint(response.text)

data = response.json()
products = data['products']
# pprint(products)


total_amount = 0

for product in products:
    if product['brand'].capitalize() == 'Apple'.capitalize():
        total_amount += product['price'] * product['stock']

print(total_amount)

# print(len(set(products[0]['description'].lower().split())))

first_product = products[0]
first_product_images = first_product['images']
pprint(first_product_images)

response2 = requests.get(first_product_images[0])

print(response2.content)


with open('pic.jpg', mode='wb') as future_file:
    future_file.write(response2.content)


with open('pic.jpg', mode='rb') as actual_file:
    print(actual_file.read())

