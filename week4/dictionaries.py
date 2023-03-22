# Dictionary: Stores a collection of labelled items. Each item has a key and a value

person = {
    'name': 'Jessica',
    'age': 23,
    'height': 172,
    'address': {
        'street': 'john street',
        'post code': 'LL3 4LS',
        'house number': 34
    }
}

people = [
    {'name': 'Jessica', 'age': 23},
    {'name': 'Trisha', 'age': 24},
]


print(person['name'])
print(person['age'])
print(person['address'])

print(person.values())

# for data in person:
