###########
# IMPORTS #
###########
import player as player_module
import cmd

#########
# CLASS #
#########
class Console(cmd.Cmd):

    # ATTRIBUTES
    player = player_module.Player()
    ai = player_module.Player()

    def do_new(self, args):
        """new - Starts a new game and initializes the player and ai"""
        print("...Starting a new game\n")
        self.prompt = "<player_info>\n" + "> "

    def do_exit(self, args):
        """exit - Exits the program"""
        raise SystemExit

    # OVERRIDEN METHODS
    def emptyline(self):
        pass

########
# MAIN #
########
if __name__ == "__main__":

    console = Console()
    console.prompt = "> "
    console.cmdloop("BATTLESHIP")
