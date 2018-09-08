##########################################
# CLASS Ship
# ----------------------------------------
# This class will represent a single ship.
##########################################
class Ship():

	def __init__(self, name, length):
		
		self.name = name
		self.length = length
		self.orientation = ""

##########################################
# CLASS ShipSet
# ----------------------------------------
# This class will represent a set of ships
##########################################
class ShipSet():
	
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
		



