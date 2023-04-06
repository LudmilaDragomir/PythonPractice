from Project.Pokemon import Pokemon


class Player:
    pokemon: Pokemon

    def __init__(self, id, pokemon):
        self.id = id
        self.pokemon = pokemon
