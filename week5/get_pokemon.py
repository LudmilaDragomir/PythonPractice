import requests

from pprint import pprint

pokemon_number = input("What is the Pokemon's ID? ")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
print(response)
pokemon = response.json()
pprint(pokemon)
# Get the height and weight of a specific Pokemon and print the output
# Extension: Print the names of all of a specific Pokemon's moves
print('Pokemon\'s name is {}'.format(pokemon['name']))
print('Pokemon\'s height is {}'.format(pokemon['height']))
print('Pokemon\'s weight is {}'.format(pokemon['weight']))
# print('Pokemon\'s moves are \n{}'.format(pokemon['moves']))

moves = pokemon['moves']
for move in moves:
    print(move['move']['name'])
# Get the height and weight of a specific Pokemon and print the output
# Extension: Print the names of all of a specific Pokemon's moves
