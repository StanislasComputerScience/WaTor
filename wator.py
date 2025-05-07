class Sea:
    pass

class Fish:
    def __init__(self, pregnancy, age, x_coordinate, y_coordinate):
        self.pregnancy = pregnancy
        self.age = age
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.sea = None

    def get_neighbors(self):
        directions = [(-1, 0), (1, 0), (0,-1), (0, 1),(-1,-1),(-1, 1),(1, 1),(1, -1)]
        neighbors_coord = []
        for dx, dy in directions:
            nx, ny = (self.x_coordinate + dx) % self.sea.width, (self.y_coordinate + dy) % self.sea.length
            neighbors_coord.append((nx, ny))
        return list(map(lambda t: self.sea.sea[t[0]][t[1]],neighbors_coord))


    def move(self):
        # Implémentez la logique de déplacement ici
        pass

    def reproduce(self):
        # Implémentez la logique de reproduction ici
        pass

class Shark(Fish):
    def __init__(self, pregnancy, age, x_coordinate, y_coordinate, energy):
        super().__init__(pregnancy, age, x_coordinate, y_coordinate)
        self.energy = energy

    def eat(self):
        # Implémentez la logique d'alimentation ici
        pass

class Sea:
    def __init__(self, width=50, length=30):
        self.sea = [[None for _ in range(width)] for _ in range(length)]
        self.width = width
        self.length = length

    def add_fish(self, fish_obj):
        x = fish_obj.x_coordinate
        y = fish_obj.y_coordinate
        fish_obj.sea = self

        if 0 <= x < len(self.sea) and 0 <= y < len(self.sea[0]):
            if self.sea[x][y] is None:
                self.sea[x][y] = fish_obj
            else:
                print(f"Case ({x},{y}) déjà occupée.")
        else:
            print(f"Coordonnées ({x},{y}) hors limites.")



    def print_sea(self):
        for row in self.sea:
            for cell in row:
                if cell is None:
                    print('\033[44m🌊\033[0m', end='') # océan bleu
                elif isinstance(cell, Shark):
                    print('\033[41m🦈\033[0m', end='') # requin rouge
                elif isinstance(cell, Fish):
                    #print('\033[43m🐟\033[0m', end='') # poisson jaune
                    print('\033[42m🐟\033[0m', end='') # poisson vert

                else:
                    print(f'{cell} ', end='') # debug
            print()

    def __str__(self):
        output = ""
        for row in self.sea:
            for cell in row:
                if cell is None:
                    output += '\033[44m🌊\033[0m'
                elif isinstance(cell, Shark):
                    output += '\033[41m🦈\033[0m'
                elif isinstance(cell, Fish):
                    output += '\033[43m🐟\033[0m'
            output += "\n"
        return output

    def __repr__(self):
        return str(self)


# Test
my_sea = Sea()

d_fish={'pregnancy' : 3, 'age' : 0, 'x_coordinate' : 1, 'y_coordinate' : 1}
d_shark={'pregnancy' : 5, 'age' : 0, 'x_coordinate' : 2, 'y_coordinate' : 2, 'energy' : 3}

f = Fish(**d_fish) 
s = Shark(**d_shark)
my_sea.add_fish(f)
my_sea.add_fish(s)
print(my_sea)
print(f.get_neighbors())
