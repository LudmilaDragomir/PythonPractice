from Project.Pokemon import Pokemon


class PlayerMultiple:
    pokemons: []
    selected: Pokemon

    def __init__(self, __id, pokemons, lives, selected):
        self.id = __id
        self.pokemons = pokemons
        self.lives = lives
        self.selected = selected
