###########
# IMPORTS #
###########
import ship

####################################################
# CLASS Player
# --------------------------------------------------
# This class represents a player, either the user or
# the AI. It contains the player's battlefield, the
# enemy's battlefield, and the ships at his or her
# disposal
####################################################
class Player:

    # CONSTRUCTOR
    def __init__(self):
        # ATTRIBUTES
        self.__ships = ship.ShipSet(True)  # Initializes a full collection of ships (as opposed to an empty on
        self.__my_field = Field(True)  # Initializes the player's field, with fog of war off
        self.__opponent_field = Field(False)  # Initializes the enemy's field, with fog of war on

    # PUBLIC METHODS
    # place_ship - Adds a ship to the player's field
    def place_ship(self, ship_name, coordinate, orientation):
        # Check if ship is in ship set
        if not self.__ships.ship_exists(ship_name):
            raise Exception("*** " + ship_name + " does not exist in ship placement pool")
    
        # Get the ship
        ship = self.__ships.get(ship_name)
    
        # Place it into the field at the right coordinate
        self.__my_field.place(ship, coordinate, orientation)
        
        # Pop that ship from self.__ships
        self.__ships.pop(ship_name)

    # attack - Attacks the enemy's field
    def attack(self, x_coordinate, y_coordinate):
        # TODO
        pass

    # OVERRIDEN METHODS
    # __str__ - convert player object into a string
    def __str__(self):
        output = "ENEMY FIELD\n"
        output = output + str(self.__opponent_field) + "\n\n"
        output = output + "MY FIELD\n"
        output = output + str(self.__my_field) + "\n"
        output = output + "SHIPS TO PLACE\n"
        output = output + str(self.__ships)
        return output


####################################################
# CLASS Field
# --------------------------------------------------
# This class represents a field. It can be
# initialized with or without the fog of war
####################################################
class Field:

    # CONSTRUCTOR
    def __init__(self, fog_of_war):
        # ATTRIBUTES
        self.__fog_of_war = fog_of_war  # Sets the fog of war to on or off
        self.__matrix = self.__init_matrix()  # Initializes the matrix

    # PUBLIC METHODS
    # place a ship into field
    # convert coordinate to matrix format and place ship according to orientation
    def place(self, a_ship, coordinate, orientation):

        # prints all placement info
        print("Placing ship at " + coordinate + " with orientation of " + orientation)

        # convert Column from letter to number
        matrixCol = ord(coordinate[0].upper())-65
        print(matrixCol)
        matrixRow = int(coordinate[1:]) - 1
        print(matrixRow)

        # Check orientation to determine placement algorithm
        if orientation.lower() == "horizontal":
            end_point = len(a_ship) + int(matrixCol)
            if end_point > 10:
                raise Exception("*** ship goes out of bounds")
        elif orientation.lower() == "vertical":
            end_point = len(a_ship) + int(matrixRow)
            if end_point > 10:
                raise Exception("*** ship goes out of bounds")
        else:
            raise Exception("*** invalid orientation")
                
        # Check to see if it conflicts with a previously placed ship
        if orientation.lower() == "horizontal":
            for index in range(matrixCol, matrixCol + len(a_ship)):
                if self.__matrix[matrixRow][index] == 1:
                    raise Exception("*** placement conflicts with previously placed ship")
        elif orientation.lower() == "vertical":
            for index in range(matrixRow, matrixRow + len(a_ship)):
                print(str(self.__matrix[index][matrixCol]))
                if self.__matrix[index][matrixCol] == 1:
                    raise Exception("*** placement conflicts with previously placed ship")

        # Places all of ship points based on length in a specific orientation VERT / HORIZ
        if orientation.lower() == "horizontal":
            for index in range(0, len(a_ship)):
                self.__matrix[matrixRow][matrixCol] = 1
                matrixCol = matrixCol + 1
        else:
            for index in range(0, len(a_ship)):
                self.__matrix[matrixRow][matrixCol] = 1
                matrixRow = matrixRow + 1
        
    # PRIVATE METHODS
    # init_matrix - returns an initialized matrix. For internal class use only
    def __init_matrix(self):
        return [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # converting to string variable
    def __str__(self):
        output = "  A, B, C, D, E, F, G, H, I, J \n"
        output = output + "------------------------------" + "\n"
        for x in self.__matrix:
            output = output + "|" + str(x) + "\n"
            output = output + "------------------------------" + "\n"
        return output

    # MAIN
    if __name__ == "__main__":
        player1 = Player()
        print(str(player1))
