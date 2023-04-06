import operator
import random
import requests

from Project.Dictionary import Dictionary
from Project.Player import Player

players = [Player(1, dict), Player(2, dict)]

print(f"".center(60, "-"))
print(f" Welcome to Pokemon Top Trumps game!: {len(players)} ".center(60, "-"))
print(f"".center(60, "-"))


def getRandomNumber():
    return random.randint(1, 151)


def getPokemon():
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(getRandomNumber())
    response = requests.get(url)
    if int(response.status_code) == 200:
        return Dictionary(response.json())
    else:
        return "Error getting the pokemon!"


def getStats(dict):
    return list(dict.keys())


def play():
    for player in players:
        player.pokemon = getPokemon().__dict__
        print("Player {}: ".format(player.id))
        print("Pokemon's name : \"{}\"".format(player.pokemon['name'].upper()))
        print("Pokemon's id {}".format(player.pokemon['id']))
        print("Pokemon's weight {}".format(player.pokemon['weight']))
        print("Pokemon's height {}".format(player.pokemon['height']))
        print(f"".center(60, "-"))
        if players[len(players) - 1].id != player.id:
            print("VS")
            print(f"".center(60, "-"))

    stats2 = getStats(players[0].pokemon)
    print(*stats2, sep="\n")
    stat = input("Which stat they want to use {}?\n".format(stats2))
    if stat in stats2 and [str, int].__contains__(type(players[0].pokemon[stat])):
        print(players[0].pokemon[stat])
        print(players[1].pokemon[stat])
        if players[0].pokemon[stat] > players[1].pokemon[stat]:
            print("Player {} wins!".format(players[0].id))
        else:
            print("Player {} wins!".format(players[1].id))
    else:
        print("Incorrect stat! {}".format(type(players[0].pokemon[stat])))


play()

