### Defining Game Units ###

from codeagent_utils.unit_utils import *

class Invader(Ground_Unit):
    def __init__(self, team, source):
        super().__init__(name="Invader",cost=100, attack=60, defense=20, attack_rng=1, sight_rng=4, move_rng=4, team=team)
        self.source = source

class ReconBot(Ground_Unit):
    def __init__(self, team, source):
        super().__init__(name="ReconBot",cost=120, attack=20, defense=10, attack_rng=1, sight_rng=6, move_rng=5, team=team)
        self.source = source

class Miner(Ground_Unit):
    def __init__(self, team, source):
        super().__init__(name="Miner",cost=150, attack=0, defense=0, attack_rng=0, sight_rng=4, move_rng=3, team=team)
        self.source = source

class RangeBlaster(Ground_Unit):
    def __init__(self, team, source):
        super().__init__(name="RangeBlaseter", cost=200, attack=50, defense=10, attack_rng=3, sight_rng=5, move_rng=3, team=team)
        self.source = source

class Constructor(Ground_Unit):
    def __init__(self, team, source):
        super().__init__(name="Constructor", cost=350, attack=0, defense=30, attack_rng=0, sight_rng=4, move_rng=3, team=team)
        self.source = source

class Factory(Structure_Unit):
    def __init__(self, team, source):
        super().__init__(name="Factory", cost=None, attack=20, defense=70, attack_rng=2, sight_rng=4, team=team, is_main=False, earning=0)
        self.source = source

class LazerCannon(Structure_Unit):
    def __init__(self, team, source):
        super().__init__(name="LazerCannon", cost=500, attack=60, defense=70, attack_rng=3, sight_rng=4, team=team, is_main=False, earning=0)
        self.source = source

class Nexus(Structure_Unit):
    def __init__(self, team, source):
        super().__init__(name="Nexus", cost=None, attack=20, defense=70, attack_rng=2, sight_rng=4, team=team, is_main=True, earning=50)
        self.source = source

### END ###

### Defining Game Map ###

from codeagent_utils.world_utils import *
from random import randint

class Montain_Tile(Tile):
    def __init__(self):
        super().__init__(name="Mountains", move_penalty=2, bonus=1, allowed_units=["All"], interaction=None)

class LMontain_Tile(Tile):
    def __init__(self):
        super().__init__(name="Large Mountains", move_penalty=None, bonus=1, allowed_units=None, interaction=None)

class Mineral_Tile(Tile):
    def __init__(self):
        super().__init__(name="Minerals", move_penalty=1, bonus=1, allowed_units=["All"], interaction=None)

from P1_Nexus_CodeBase import *
from P2_Nexus_CodeBase import *

class Game_1_World(World):
    def __init__(self):
        width = 100
        height = 100
        base_tile = Tile()
        P1NC = "P1_Nexus_CodeBase.py"
        P2NC = "P2_Nexus_CodeBase.py"

        self.verify_script(P1NC)
        self.verify_script(P2NC)

        tile_comp = [(randint(24,75),randint(24,75),Montain_Tile()) for i in range(500)] \
            + [(randint(24,75),randint(24,75),LMontain_Tile()) for i in range(250)] \
            + [(randint(0,70),randint(29,99),Montain_Tile()) for i in range(250)] \
            + [(randint(29,99),randint(0,70),Montain_Tile()) for i in range(250)] \
            + [(randint(5,13),randint(5,13),Mineral_Tile()) for i in range(5)] \
            + [(randint(86,94),randint(86,94),Mineral_Tile()) for i in range(5)] \
            + [(randint(39,59),randint(39,59),Mineral_Tile()) for i in range(10)]

        unit_comp = [(19,19,Nexus(1,P1_Nexus())), (20,19,ReconBot(1,P1_ReconBot())), (19,20,Miner(1,P1_Miner())), (19,18,Miner(1,P1_Miner())), (18,19,Miner(1,P1_Miner()))] \
            + [(80,79,ReconBot(2,P2_ReconBot())), (79,80,Miner(2,P2_Miner())), (80,81,Miner(2,P2_Miner())), (81,80,Miner(2,P2_Miner())), (80,80,Nexus(2,P2_Nexus()))]

        color_map = {"Invader": [[255,102,102],[178,102,255]], \
            "ReconBot": [[255,178,102],[102,102,255]], \
            "Miner": [[255,255,102],[102,178,255]], \
            "RangeBlaseter": [[178,255,102],[102,255,255]], \
            "Constructor": [[51,102,0],[0,102,102]], \
            "Factory": [[102,102,0],[0,51,102]], \
            "LazerCannon": [[102,51,0],[0,0,102]], \
            "Nexus": [[102,0,0],[51,0,102]], \
            "Dirt": [100, 100, 100], \
            "Mountains": [125, 125, 125], \
            "Large Mountains": [150, 150, 150], \
            "Minerals": [255, 255, 255] }

        #color_map = {"Invader": [[255,102,102],[102,102,255]], "ReconBot": [[255,178,102],[102,178,255]], "Miner": [[255,255,102],[102,255,255]], "RangeBlaseter": [[178,255,102],[102,255,178]], "Constructor": [[51,102,0],[0,102,51]], "Factory": [[102,102,0],[0,102,102]], "LazerCannon": [[102,51,0],[0,51,102]], "Nexus": [[102,0,0],[0,0,102]], "Dirt": [100, 100, 100], "Mountains": [125, 125, 125], "Large Mountains": [150, 150, 150]}

        super().__init__(width, height, base_tile, tile_comp, unit_comp, color_map)
        pass

    def verify_script(self,path):
        # TODO finish this verification <<<
        return

### END ###

### Defining Game Mechanics ###

# TODO finish this and GAME class in game_utils.py <<<

from codeagent_utils.game_utils import *

class Game_1(Game):
    def __init__(self):
        world = Game_1_World()
        super().__init__(world)
        pass

    def finish_check(self):
        return True

    def start(self):
        done = False
        team_turn = 1
        while not done:
            #self.world.render()
            done = self.full_turn(team_turn)

            if team_turn == 1:
                team_turn = 2
            else:
                team_turn = 1

### END ###


#unit_list = [Invader(1), ReconBot(1), Miner(1), RangeBlaster(1), Constructor(1), Factory(1), LazerCannon(1), Nexus(1)]

#for bot in unit_list:
    #print(type(bot))
    #bot.display()
    #print()

game = Game_1()
game.start()


