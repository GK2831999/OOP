class PokemonBasic:
    def __init__(self, name = 'Default', hp = 0,weakness = 'None', type = 'Unknown'):
        self.name = name
        self.hit_point = hp
        self.weakness = weakness
        self.type = type
    def get_type(self):
        return 'Main type: ' + self.type
    def get_move(self):
        return 'Basic move: ' + 'Quick Attack'
    def __str__(self):
        return "Name: " + self.name + ", HP: " +str(self.hit_point) + ", Weakness: " + self.weakness



class PokemonExtra:
    def __init__(self, name = 'Default', hp = 0,weakness = 'None', type = 'Unknown',s_type = "",o_move = ()):
        self.name = name
        self.hit_point = hp
        self.weakness = weakness
        self.type = type
        self.s_type= s_type
        self.o_move = o_move

    def get_type(self):
        if len(self.s_type) == 0 :return 'Main type: ' + self.type
        else: return 'Main type: ' + self.type +" ,Secondary Type = " + self.s_type
    def get_move(self):
        if len(self.o_move)== 0 :return 'Basic move: ' + 'Quick Attack'
        else: 
            s = 'Basic move: ' + 'Quick Attack' + '\n'+'Other Move: '
            k = 0
            for i in self.o_move:
                
                s+= i
                if k<1:s+=','
                k+=1
            return s
    def __str__(self):
        return "Name: " + self.name + ", HP: " +str(self.hit_point) + ", Weakness: " + self.weakness
        
print('\n------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())
print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water','Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())
print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water',  'Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())
