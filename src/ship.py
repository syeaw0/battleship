

##########################################
# CLASS Ship
# ----------------------------------------
# This class will represent a single ship.
##########################################
class Ship:

    # ATTRIBUTES
    hitList = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.orientation = ""

    # def got_hit(self, location):


##########################################
# CLASS ShipSet
# ----------------------------------------
# This class will represent a set of ships
##########################################
class ShipSet:
    # ATTRIBUTES

    def __init__(self, is_full):
        self.ships = []
        if is_full:
            self.fill_set()

    def fill_set(self):
        self.ships = [
            Ship("Carrier", 5),
            Ship("Battleship", 4),
            Ship("Destroyer", 3),
            Ship("Submarine", 3),
            Ship("Patrol Boat", 2)
        ]

    # def get_ships(self):

