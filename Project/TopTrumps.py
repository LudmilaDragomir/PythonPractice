import random
from typing import Any

import requests

from Project.Dictionary import Dictionary
from Project.PlayerMultiple import PlayerMultiple

# players = [Player(1, dict), Player(2, dict)]
players2 = [PlayerMultiple(1, [], 3, ''), PlayerMultiple(2, [], 3, '')]

print(f''.center(60, '-'))
print(f" Welcome to Pokemon Top Trumps game!: {len(players2)} players ".center(60, "-"))
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


def getPokemons():
    multiple_pokemon = []
    ids = []
    while len(multiple_pokemon) < 3:
        pokemon = getPokemon().__dict__
        # if ids.__contains__(pokemon['id']):
        if pokemon['id'] not in ids:
            multiple_pokemon.append(pokemon)
            ids.append(pokemon['id'])
    return multiple_pokemon


def getStats(pokemon):
    stats = []
    for key in pokemon:
        if [str, int].__contains__(type(pokemon[key])):
            stats.append(key)
    return stats
    # return list(pokemon.keys())


def play():
    for player in players2:
        player.pokemons = getPokemons()

    has_lives: bool | Any = players2[0].lives > 0 and players2[1].lives > 0
    while has_lives:
        player1_use = input("Player {}, which pokemon do you want to use {}?\n".
                            format(players2[0].id, [dic['name'] for dic in players2[0].pokemons]))
        players2[0].selected = next((item for item in players2[0].pokemons if item["name"] == player1_use), None)
        players2[1].selected = random.choice(list(players2[1].pokemons))
        print("Player {}, uses {} from {}?\n".
              format(players2[1].id, players2[1].selected['name'].upper(),
                     [dic['name'] for dic in players2[1].pokemons]))

        stats2 = getStats(players2[0].pokemons[0])
        # print(*stats2, sep="\n")
        stat = input("Which stat they want to use {}?\n".format(stats2))
        print('')
        if stat in stats2:
            print(stat, players2[0].selected[stat])
            print(stat, players2[1].selected[stat])

            if players2[0].selected[stat] > players2[1].selected[stat]:
                print("Player {} wins!".format(players2[0].id))
                players2[0].pokemons = remove_selected(players2[0].pokemons, player1_use)
                players2[1].lives -= 1
            elif players2[0].selected[stat] < players2[1].selected[stat]:
                print("Player {} wins!".format(players2[1].id))
                players2[1].pokemons = remove_selected(players2[1].pokemons, players2[1].selected['name'])
                players2[0].lives -= 1
            else:
                print('Draw')

            has_lives = players2[0].lives > 0 and players2[1].lives > 0
            print(f" {has_lives} ".center(60, "-"))
            for player in players2:
                print("Player {} has {} lives ".format(player.id, player.lives))
                # print("Pokemon's name : \"{}\"".format(player.selected['name'].upper()))
                # print("Pokemon's id {}".format(player.selected['id']))
                # print("Pokemon's weight {}".format(player.selected['weight']))
                # print("Pokemon's height {}".format(player.selected['height']))
                print(f"".center(60, "-"))
                if players2[len(players2) - 1].id != player.id:
                    print("VS")
                    print(f"".center(60, "-"))

            # players2[0].pokemons = remove_selected(players2[0].pokemons, player1_use)
            # players2[1].pokemons = remove_selected(players2[1].pokemons, player2_use)


def remove_selected(pokemon_list, selected):
    for i in range(len(pokemon_list)):
        if pokemon_list[i]['name'] == selected:
            del pokemon_list[i]
            break
    return pokemon_list


play()
