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

