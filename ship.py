
"""init ships using shipBuilder"""
class ShipBuilder:
    def __init__(self, name, length):
        self.name = name
        self.length = length


#init ships here
ship1 = ShipBuilder("Destroyer", 5)


#place ships on GUI


#test print ships to console
print(ship1.name, ship1.length, sep=" ")



