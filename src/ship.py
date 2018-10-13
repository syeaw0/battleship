# IMPORTS
import enum

##########################################
# CLASS Ship
# ----------------------------------------
# This class will represent a single ship.
##########################################
class Ship:

    # ATTRIBUTES
    hitList = []

    def __init__(self, name, length):
        self.__name = name
        self.__length = length
        self.__orientation = Orientation.VERTICAL

    def set_orientation(self, orientation):
        self.__orientation = orientation

    def get_name(self):
        return self.__name
        
    def get_length(self):
        return self.__length
        
    # OVERRIDEN METHODS
    def __len__(self):
        return self.__length


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

    # PUBLIC METHODS
    def fill_set(self):
        self.ships = [
            Ship("Carrier", 5),
            Ship("Battleship", 4),
            Ship("Destroyer", 3),
            Ship("Submarine", 3),
            Ship("Patrol Boat", 2)
        ]

    def ship_exists(self, ship_name):
        exists = False
        for ship in self.ships:
            if ship.get_name() == ship_name:
                exists = True
        return exists
    
    def pop(self, ship_name):
        result = None
        for ship in self.ships:
            if ship.get_name() == ship_name:
                index = self.ships.index(ship)
                result = self.ships.pop(index)
                break
        print("ShipSet:pop:result = " + str(result))
        return result
        
    def get(self, ship_name):
        result = None
        for ship in self.ships:
            if ship.get_name() == ship_name:
                index = self.ships.index(ship)
                result = self.ships[index]
                break
        print("ShipSet:get:result = " + str(result))
        return result
        
    # def get_ships(self):

    # OVERRIDEN METHODS
    def __str__(self):
        output = ""
        for ship in self.ships:
            output = output + ship.get_name() + "\n"
        return output

class Orientation(enum.Enum):
    VERTICAL = 1
    HORIZONTAL = 2

