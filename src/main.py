###########
# IMPORTS #
###########
from ship import *

########
# MAIN #
########
ships = ShipSet(True)
for ship in ships.ships:
	print(ship.name + ": " + str(ship.length))