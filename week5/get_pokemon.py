import requests

from pprint import pprint

# pokemon_number = input("What is the Pokémon's ID? ")
pokemon_number = 1

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
print(response)
pokemon = response.json()
# pprint(pokemon)
# Get the height and weight of a specific Pokemon and print the output
# Extension: Print the names of all of a specific Pokemon's moves
pprint(pokemon['sprites']['other']['official-artwork']['front_default'])
# print('Pokemon\'s height is {}'.format(pokemon['height']))
# print('Pokemon\'s weight is {}'.format(pokemon['weight']))
# print('Pokemon\'s moves are \n{}'.format(pokemon['moves']))

# moves = pokemon['moves']
# for move in moves:
#     print(move['move']['name'])
# Get the height and weight of a specific Pokemon and print the output
# Extension: Print the names of all of a specific Pokemon's moves
