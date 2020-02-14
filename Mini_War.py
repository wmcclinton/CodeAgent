### Defining Game Globals ###

global resources
resources = [500,500]

global ledger
ledger = [[],[]]

global round_num
round_num = 1

global round_max
round_max = 1000 #3000

global render_time
render_time = 0.0001 #0.01 #0.0001

### END ###

### Defining Game Units ###

from codeagent_utils.unit_utils import *

class Warrior(Ground_Unit):
    def __init__(self, team, source):
        super().__init__(name="Warrior",cost=100, attack=60, defense=20, attack_rng=1, sight_rng=4, move_rng=4, team=team)
        self.source = source

class Archer(Ground_Unit):
    def __init__(self, team, source):
        super().__init__(name="Archer",cost=120, attack=50, defense=10, attack_rng=4, sight_rng=6, move_rng=3, team=team)
        self.source = source

class Worker(Ground_Unit):
    def __init__(self, team, source):
        super().__init__(name="Worker",cost=150, attack=0, defense=0, attack_rng=0, sight_rng=4, move_rng=3, team=team)
        self.source = source

class City(Structure_Unit):
    def __init__(self, team, source):
        super().__init__(name="City", cost=None, attack=20, defense=70, attack_rng=2, sight_rng=4, team=team, is_main=False, earning=0)
        self.source = source

    def interaction(self, unit):
        global resources
        if unit.name == "Worker" and unit.item == "ore":
            unit.item = None
            resources[unit.team - 1] = resources[unit.team - 1] + 10
            print("Capital Recieved Ore")
        elif unit.name == "Worker":
            print("Worker had no Ore")

class Capital(Structure_Unit):
    def __init__(self, team, source):
        super().__init__(name="Capital", cost=None, attack=20, defense=70, attack_rng=2, sight_rng=4, team=team, is_main=True, earning=50, interaction=self.interaction)
        self.source = source

    def interaction(self, unit):
        global resources
        if unit.name == "Worker" and unit.item == "ore":
            unit.item = None
            resources[unit.team - 1] = resources[unit.team - 1] + 10
            print("Capital Recieved Ore")
        elif unit.name == "Worker":
            print("Worker had no Ore")

### END ###

### Defining Game Map ###

from codeagent_utils.world_utils import *
from random import randint

class Montain_Tile(Tile):
    def __init__(self):
        super().__init__(name="Mountains", move_penalty=2, bonus=1, allowed_units=["All"], interaction=None)

    def interaction(self, unit):
        if unit.name == "Worker":
            unit = deepcopy(self.alternator["City"](unit.team, self.generators[unit.team-1]["City"]()))
            print("Workers turned into City")

class LMontain_Tile(Tile):
    def __init__(self):
        super().__init__(name="Large Mountains", move_penalty=None, bonus=1, allowed_units=None, interaction=None)

class Mineral_Tile(Tile):
    def __init__(self):
        super().__init__(name="Minerals", move_penalty=1, bonus=1, allowed_units=["All"], interaction=self.interaction)

    def interaction(self, unit):
        if unit.name == "Worker":
            unit.item = "ore"
            print("Worker Collected Ore")

import sys
import importlib

if len(sys.argv) < 3:
    print("Invalid Arguments:")
    print("python3 Mini_War.py p1_code.py p2_code.py")
    quit()

P1CC = sys.argv[1]
P2CC = sys.argv[2]

p1_lib = __import__(P1CC)
p2_lib = __import__(P2CC)

class Game_1_World(World):
    def __init__(self):
        width = 25
        height = 25
        base_tile = Tile()

        self.verify_script(P1CC)
        self.verify_script(P2CC)

        tile_comp = [(i,24-i,Montain_Tile()) for i in range(25)] \
            + [(0,i,LMontain_Tile()) for i in range(25)] \
            + [(i,0,LMontain_Tile()) for i in range(25)] \
            + [(24,i,LMontain_Tile()) for i in range(25)] \
            + [(i,24,LMontain_Tile()) for i in range(25)] \
            + [(7,7,Mineral_Tile()),(17,17,Mineral_Tile()),(3,21,Mineral_Tile()),(21,3,Mineral_Tile())]

        unit_comp = [(3,3,Capital(1,p1_lib.P1_Capital()))] \
            + [(21,21,Capital(2,p2_lib.P2_Capital()))]

        color_map = {"Warrior": [[255,102,102],[178,102,255]], \
            "Archer": [[255,178,102],[102,102,255]], \
            "Worker": [[255,255,102],[102,178,255]], \
            "City": [[102,102,0],[0,51,102]], \
            "Capital": [[102,0,0],[51,0,102]], \
            "Dirt": [100, 100, 100], \
            "Mountains": [125, 125, 125], \
            "Large Mountains": [150, 150, 150], \
            "Minerals": [255, 255, 255], \
            "Unknown": [75, 75, 75], \
            "EOW": [0, 0, 0]}

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
        global render_time
        
        def get_color(unit, tile):
            if unit == None:
                return self.color_map[tile.name]
            else:
                return self.color_map[unit.name][unit.team-1]

        rgb_world = np.array([[get_color(self.layout[y][x]["unit"], self.layout[y][x]["tile"]) for x in range(self.width)] for y in range(self.height)])
        #print(rgb_world)
        plt.title("[Round {}/{}][Resources => Team {}: {} | Team {}: {}]".format(round_num,round_max,1,resources[0],2,resources[1]))
        plt.imshow(rgb_world)
        plt.draw()
        plt.pause(render_time) #0.0001
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

        self.alternator = {"Warrior": Warrior, \
                            "Archer": Archer, \
                            "Worker": Worker, \
                            "City": City, \
                            "Capital": Capital}

        self.generators = [{"Warrior": p1_lib.P1_Warrior, \
                            "Archer": p1_lib.P1_Archer, \
                            "Worker": p1_lib.P1_Worker, \
                            "City": p1_lib.P1_City, \
                            "Capital": p1_lib.P1_Capital}, \
                            {"Warrior": p2_lib.P2_Warrior, \
                            "Archer": p2_lib.P2_Archer, \
                            "Worker": p2_lib.P2_Worker, \
                            "City": p2_lib.P2_City, \
                            "Capital": p2_lib.P2_Capital}]

        super().__init__(world)
        pass

    def finish_check(self):
        done = False

        is_alive = [False, False]

        for i, row in enumerate(self.world.layout):
            for j, item in enumerate(row):
                if item["unit"] != None:
                    if item["unit"].name == "Capital":
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

            # Second/Ending Render
            self.world.render()

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


