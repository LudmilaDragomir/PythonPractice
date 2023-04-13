import random
import requests

print(f''.center(60, '-'))
print(f" Welcome to Pokemon Top Trumps game! ".center(60, "-"))
print(f"".center(60, "-"))


def random_pokemon(identifier):
    if identifier == 'me':
        pokemon_number = input('Please choose a number \n')  # random.randint(1, 151)
    else:
        pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']
    }


def get_species(poke_id):
    species_url = 'https://pokeapi.co/api/v2/pokemon-species/{}/'.format(poke_id)
    response = requests.get(species_url)
    pokemon_sp = response.json()
    return {
        'name': pokemon_sp['name'],
        'base_happiness': pokemon_sp['base_happiness'],
        'is_baby': pokemon_sp['is_baby'],
        'is_legendary': pokemon_sp['is_legendary'],
        'color': pokemon_sp['color']
    }


def run():
    my_pokemon = random_pokemon('me')
    poke_sp = get_species(my_pokemon['id'])
    species_url = 'https://pokeapi.co/api/v2/pokemon-species/{}/'.format(my_pokemon['id'])
    response = requests.get(species_url)
    pokemon = response.json()
    print('You choose {}'.format(my_pokemon['name']))
    stat_choice = input('Which stat do you want to use? (id, height, weight) ')
    opponent_pokemon = random_pokemon('')
    # print('The opponent chose {}'.format(opponent_pokemon['name']))
    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]
    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')
    print('----------------')
    print("My pokemon info:")
    print('Name {}'.format(my_pokemon['name']))
    print('Color {}'.format(poke_sp['color']['name']))
    print('Base happiness {}'.format(poke_sp['base_happiness']))
    print('Is baby {}'.format(poke_sp['is_baby']))
    print(my_pokemon['id'])
    print(my_pokemon['height'])
    print(my_pokemon['weight'])
    print('----------------')
    print('Opponent\'s pokemon info:')
    print(opponent_pokemon['name'])
    print(opponent_pokemon['id'])
    print(opponent_pokemon['height'])
    print(opponent_pokemon['weight'])


run()
