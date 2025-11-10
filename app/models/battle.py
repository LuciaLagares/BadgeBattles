class Battle:
    
    def __init__(self,turno, data_pokemon_player, data_pokemon_rival, log, health_player,health_rival, moves_player,moves_rival):
        
        self.turno=turno,
        self.data_pokemon_player = data_pokemon_player,
        self.data_pokemon_rival = data_pokemon_rival,
        self.log = log,
        self.health_player = health_player,
        self.health_rival = health_rival,
        self.moves_player = moves_player,
        self.moves_rival = moves_rival
        
    def __str__(self):
        pass