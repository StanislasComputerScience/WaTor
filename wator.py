class Fish:
        def __init__(self, pregnancy, age, x_coordinate, y_coordinate):
            self.pregnancy = pregnancy
            self.age = age
            self.x_coordinate = x_coordinate
            self.y_coordinate = y_coordinate

        def move():
            pass
        def reproduce():
            pass

class Shark:
        def __init__(self, pregnancy, age, x_coordinate, y_coordinate, energy):
            super().__init__(pregnancy, age, x_coordinate, y_coordinate)
            self.energy = energy
        def eat():
            pass

#from models.fish import Fish
#from models.shark import Shark

class Sea:
    def __init__(self, width=50, length=30):
        self.sea = [[None for _ in range(width)] for _ in range(length)]
        self.width = width
        self.length = length

    def add_fish(self,fish_obj):
        """_summary_
            ajout d'un poisson (requin ou autre)
        Args:
            fish_obj (_type_): objet de type poisson
        """
        x = fish_obj.x_coordinate
        y = fish_obj.y_coordinate
        if 0 <= x < len(self.sea) and 0 <= y < len(self.sea[0]):
            if self.sea[x][y] is None:
                self.sea[x][y] = fish_obj
            else:
                print(f"Case ({x},{y}) déjà occupée.")
        else:
            print(f"Coordonnées ({x},{y}) hors limites.")

    def print_sea(self):
        """fonction pour imprimer la mer, avec une variable en fonction de si la case est vide ou occupée.
        """
        for row in self.sea:
            for cell in row:
                if cell is None:
                    print('\033[44m🌊\033[0m', end='')  # océan bleu
                elif isinstance(cell, Fish):
                    print('\033[43m🐟\033[0m', end='')  # poisson jaune
                elif isinstance(cell, Shark):
                    print('\033[41m🦈\033[0m', end='')  # requin rouge
                else:
                    print(f'{cell} ', end='')  # debug
            print()


#from models.sea import Sea
#my_sea = Sea()
#my_sea.print_sea()

f = Fish(5, 0, 1, 1)
s = Shark(5, 0, 3, 3, 10)
