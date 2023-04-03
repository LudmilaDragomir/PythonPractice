import random
import requests

from Project.Dictionary import Dictionary
from Project.Player import Player

print("************************************")
print("Welcome to Pokemon Top Trumps game!")


def getRandomNumber():
    return random.randint(1, 151)


def getPokemon():
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(getRandomNumber())
    response = requests.get(url)
    if int(response.status_code) == 200:
        return Dictionary(response.json())
    else:
        return "Error getting the pokemon!"


def play():
    player1 = Player(1, getPokemon().__dict__)
    print("************************************")
    print("Player's {} pokemon:".format(player1.id))
    print("Pokemon's name \"{}\":".format(player1.pokemon['name'].upper()))
    print("Pokemon's id {}:".format(player1.pokemon['id']))
    print("Pokemon's weight {}:".format(player1.pokemon['weight']))
    print("Pokemon's height {}:".format(player1.pokemon['height']))
    print("************************************")
    print("VS")
    player2 = Player(2, getPokemon().__dict__)
    print("************************************")
    print("Player's {} pokemon:".format(player2.id))
    print("Pokemon's name \"{}\":".format(player2.pokemon['name'].upper()))
    print("Pokemon's id {}:".format(player2.pokemon['id']))
    print("Pokemon's weight {}:".format(player2.pokemon['weight']))
    print("Pokemon's height {}:".format(player2.pokemon['height']))
    print("************************************")
    # Ask the user which stat they want to use (id, height or weight)
    stats = ['id', 'height', 'weight']
    stat = input("Which stat they want to use (id, height or weight)?")
    if stat in stats:
        if player1.pokemon[stat] > player2.pokemon[stat]:
            print("Player {} wins!".format(player1.id))
        else:
            print("Player {} wins!".format(player2.id))
    else:
        print("Incorrect stat!")


play()

# print(getPokemon().name)
# print(getPokemon().id)
# print(getPokemon().weight)
# print(getPokemon().height)
# pprint(getPokemon().__dict__)
