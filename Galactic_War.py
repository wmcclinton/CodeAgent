### Defining Game Globals ###

global resources
resources = [500,500]

global ledger
ledger = [[],[]]

global round_num
round_num = 1

global round_max
round_max = 3000

### END ###

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
        self.allowed_actions = ["Communicate","Attack"]

class Nexus(Structure_Unit):
    def __init__(self, team, source):
        super().__init__(name="Nexus", cost=None, attack=20, defense=70, attack_rng=2, sight_rng=4, team=team, is_main=True, earning=50, interaction=self.interaction)
        self.source = source

    def interaction(self, unit):
        global resources
        if unit.name == "Miner" and unit.item == "ore":
            unit.item = None
            resources[unit.team] = resources[unit.team] + 10
            print("Nexus Recieved Ore")
        elif unit.name == "Miner":
            print("Miner had no Ore")

### END ###

### Defining Game Map ###

from codeagent_utils.world_utils import *
from random import randint

class Montain_Tile(Tile):
    def __init__(self):
        super().__init__(name="Mountains", move_penalty=2, bonus=1, allowed_units=["All"], interaction=None)

    def interaction(self, unit):
        if unit.name == "Constructor":
            unit = deepcopy(self.alternator["Factory"](unit.team, self.generators[unit.team-1]["Factory"]()))
            print("Constuctor turned into factor")

class LMontain_Tile(Tile):
    def __init__(self):
        super().__init__(name="Large Mountains", move_penalty=None, bonus=1, allowed_units=None, interaction=None)

class Mineral_Tile(Tile):
    def __init__(self):
        super().__init__(name="Minerals", move_penalty=1, bonus=1, allowed_units=["All"], interaction=self.interaction)

    def interaction(self, unit):
        if unit.name == "Miner":
            unit.item = "ore"
            print("Miner Collected Ore")


from Galactic_War_Codebases.P1_Nexus_CodeBase import *
from Galactic_War_Codebases.P2_Nexus_CodeBase import *

class Game_1_World(World):
    def __init__(self):
        width = 100
        height = 100
        base_tile = Tile()
        P1NC = "Galactic_War_Codebases/P1_Nexus_CodeBase.py"
        P2NC = "Galactic_War_Codebases/P2_Nexus_CodeBase.py"

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
            "Minerals": [255, 255, 255], \
            "Unknown": [75, 75, 75], \
            "EOW": [0, 0, 0]}

        #color_map = {"Invader": [[255,102,102],[102,102,255]], "ReconBot": [[255,178,102],[102,178,255]], "Miner": [[255,255,102],[102,255,255]], "RangeBlaseter": [[178,255,102],[102,255,178]], "Constructor": [[51,102,0],[0,102,51]], "Factory": [[102,102,0],[0,102,102]], "LazerCannon": [[102,51,0],[0,51,102]], "Nexus": [[102,0,0],[0,0,102]], "Dirt": [100, 100, 100], "Mountains": [125, 125, 125], "Large Mountains": [150, 150, 150], "Unknown": [75, 75, 75], "EOW": [0, 0, 0]}

        super().__init__(width, height, base_tile, tile_comp, unit_comp, color_map)
        pass

    def verify_script(self,path):
        # TODO finish this verification <<<

        # TODO make requirements.txt <<<

        return

    def render(self):
        global resources
        global round_num
        global round_max
        
        def get_color(unit, tile):
            if unit == None:
                return self.color_map[tile.name]
            else:
                return self.color_map[unit.name][unit.team-1]

        rgb_world = np.array([[get_color(self.layout[y][x]["unit"], self.layout[y][x]["tile"]) for x in range(self.width)] for y in range(self.height)])
        #print(rgb_world)
        plt.title("[Roung {}/{}][Resources => Team {}: {} | Team {}: {}]".format(round_num,round_max,1,resources[0],2,resources[1]))
        plt.imshow(rgb_world)
        plt.draw()
        plt.pause(0.0001)
        plt.clf()


### END ###

### Defining Game Mechanics ###

# TODO finish this and GAME class in game_utils.py <<<

from codeagent_utils.game_utils import *
from copy import deepcopy

class Game_1(Game):
    def __init__(self):
        global round_num
        global round_max

        world = Game_1_World()

        self.round_counter = round_num
        self.max_rounds = round_max #3000

        self.alternator = {"Invader": Invader, \
                        "ReconBot": ReconBot, \
                        "Miner": Miner, \
                        "RangeBlaster": RangeBlaster, \
                        "Constructor": Constructor, \
                        "Factory": Factory, \
                        "LazerCannon": LazerCannon, \
                        "Nexus": Nexus}

        self.generators = [{"Invader": P1_Invader, \
                        "ReconBot": P1_ReconBot, \
                        "Miner": P1_Miner, \
                        "RangeBlaster": P1_RangeBlaster, \
                        "Constructor": P1_Constructor, \
                        "Factory": P1_Factory, \
                        "LazerCannon": P1_LazerCannon, \
                        "Nexus": P1_Nexus}, \
                        {"Invader": P2_Invader, \
                        "ReconBot": P2_ReconBot, \
                        "Miner": P2_Miner, \
                        "RangeBlaster": P2_RangeBlaster, \
                        "Constructor": P2_Constructor, \
                        "Factory": P2_Factory, \
                        "LazerCannon": P2_LazerCannon, \
                        "Nexus": P2_Nexus}]

        super().__init__(world)
        pass

    def finish_check(self):
        done = False

        is_alive = [False, False]

        for i, row in enumerate(self.world.layout):
            for j, item in enumerate(row):
                if item["unit"] != None:
                    if item["unit"].name == "Nexus":
                        if item["unit"].is_main == True:
                            if item["unit"].current_hp > 0:
                                is_alive[item["unit"].team - 1] = True

        if is_alive[0] and is_alive[1]:
            if self.round_counter >= self.max_rounds:
                print("Players Tied - Max Rounds")
                return True
            else:
                return False
        else:
            if is_alive[0]:
                print("Winner is Player 1")

            if is_alive[1]:
                print("Winner is Player 2")

            return True

    def start(self, verbose=True):
        global round_num

        done = False
        team_turn = 1
        while not done:
            self.world.render()
            if verbose:
                print()
                print("%"*100)
                print("Round {}/{}".format(self.round_counter, self.max_rounds))
                print("%"*100)
                print()
            done = self.full_turn(team_turn, verbose=verbose)

            if team_turn == 1:
                team_turn = 2
            else:
                team_turn = 1

            self.round_counter = self.round_counter + 1
            round_num = self.round_counter

    def get_resources(self,team):
        global resources
        return resources[team-1]

    def set_resources(self,team,amount):
        global resources
        resources[team-1] = amount

    def add_ledger(self,team,message):
        global ledger
        ledger[team-1].append(message)
    
    def get_ledger(self,team):
        global ledger
        return ledger[team-1]

    def producer(self,unit_name,team):
        return deepcopy(self.alternator[unit_name](team, self.generators[team-1][unit_name]()))

### END ###

game = Game_1()
game.start()


