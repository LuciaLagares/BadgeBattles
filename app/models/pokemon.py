class Pokemon:

    def __init__(self, id, name, height, weight, stats, sprites, moves, types):
        self.id = id
        self.name = name
        self.weight = weight
        self.height = height
        self.stats = stats
        self.sprites = sprites
        self.moves = moves
        self.types = types

    def __str__(self):
        return f'{self.name.capitalize()}'

    def to_dict(self):
        pokemon = {
            "id": self.id,
            "name": self.name,
            "weight": self.weight,
            "height": self.height,
            "stats": self.stats,
            "sprites": self.sprites,
            "moves": self.moves,
            "types": self.types,

        }
        return pokemon

    def asing_moves(self,moves):
        self.moves=moves
        
        
    @staticmethod
    def from_dict(dict):
        
        return Pokemon(**dict)
