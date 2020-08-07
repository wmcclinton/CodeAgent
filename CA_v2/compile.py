
# Change Depending on Game
from pacmen_game_design import Pacmen as Game_Code
# 

# Change Depending on Player 1 Codebase
from codebase import Code as codebase1
# 

# Change Depending on Player 2 Codebase
from codebase import Code as codebase2
# 

game = Game_Code(codebase1(), codebase2())
game.run(render=True)