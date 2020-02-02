import random

### Space for defining functions ###
### No global variables ###
### Edit Code Below Line ###

def random_attack(attack_rng):
    if attack_rng == 0:
        return None
    else:
        return ("Attack", [random.choice(["up","down","left","right"]) for _ in range(attack_rng)], None)

def random_movement(move_rng, attack_rng):
    action = "Move"
    direction = [random.choice(["up","down","left","right"]) for _ in range(move_rng)]
    option = random_attack(attack_rng)

    return action, direction, option

def produce_recon_bot(state):
    my_i = int(len(state[0])/2)
    my_j = int(len(state[0])/2)
    if state[my_i - 1][my_j]["unit"] == None:
        return "Produce", ["up"], "ReconBot"
    elif state[my_i + 1][my_j]["unit"] == None:
        return "Produce", ["down"], "ReconBot"
    elif state[my_i][my_j - 1]["unit"] == None:
        return "Produce", ["left"], "ReconBot"
    elif state[my_i][my_j + 1]["unit"] == None:
        return "Produce", ["right"], "ReconBot"

    return "Wait", None, None

def produce_lazer_cannon(state):
    my_i = int(len(state[0])/2)
    my_j = int(len(state[0])/2)
    if state[my_i][my_j + 1]["unit"] == None:
        return "Produce", ["right"], "LazerCannon"
    elif state[my_i - 1][my_j]["unit"] == None:
        return "Produce", ["up"], "LazerCannon"
    elif state[my_i + 1][my_j]["unit"] == None:
        return "Produce", ["down"], "LazerCannon"
    elif state[my_i][my_j - 1]["unit"] == None:
        return "Produce", ["left"], "LazerCannon"

    return "Wait", None, None


def random_miner(state,move_rng,attack_rng):
    my_i = int(len(state[0])/2)
    my_j = int(len(state[0])/2)
    if state[my_i - 1][my_j]["unit"] == "Nexus" or state[my_i - 1][my_j]["tile"] == "Minerals":
        return "Interact", ["up"], None
    elif state[my_i + 1][my_j]["unit"] == "Nexus" or state[my_i + 1][my_j]["tile"] == "Minerals":
        return "Interact", ["down"], None
    elif state[my_i][my_j - 1]["unit"] == "Nexus" or state[my_i][my_j - 1]["tile"] == "Minerals":
        return "Interact", ["left"], None
    elif state[my_i][my_j + 1]["unit"] == "Nexus" or state[my_i][my_j + 1]["tile"] == "Minerals":
        return "Interact", ["right"], None

    return random_movement(move_rng,attack_rng)

def lazer_cannon_destroy_enemy(state,attack_rng=3):
    my_i = int(len(state[0])/2)
    my_j = int(len(state[0])/2)

    directions = []

    for i, row in enumerate(state):
        for j, item in enumerate(row):
            if item["unit"] != None and str(item["unit_team"]) == "2":
                if (abs(item["location"][0] - state[my_i][my_j]["location"][0]) + abs(item["location"][1] - state[my_i][my_j]["location"][1])) <= attack_rng:
                    i_distance = item["location"][0] - state[my_i][my_j]["location"][0]
                    j_distance = item["location"][1] - state[my_i][my_j]["location"][1]
                    
                    for i_diff in range(abs(i_distance)):
                        if i_distance > 0:
                            directions.append("up")
                        else:
                            directions.append("down")

                    for j_diff in range(abs(j_distance)):
                        if j_distance > 0:
                            directions.append("left")
                        else:
                            directions.append("right")

                    return ("Attack", directions, None)

    return "Wait", None, None
          

### End ###

class P1_Invader:
    def __init__(self):
        ### Edit Code Below Line ###
        
        self.internal_ledger = None
        self.last_state = None

        ### End ###
        return

    def code(self, state, ledger):
        ### Edit Code Below Line ###

        self.internal_ledger = ledger

        move_rng = 4
        attack_rng = 1

        action, direction, option = random_movement(move_rng, attack_rng)

        self.last_state = state

        message = "Hello World"

        ### End ###
        return (action, direction, option), message

class P1_ReconBot:
    def __init__(self):
        ### Edit Code Below Line ###
        
        self.internal_ledger = None
        self.last_state = None

        ### End ###
        return

    def code(self, state, ledger):
        ### Edit Code Below Line ###

        self.internal_ledger = ledger

        move_rng = 5
        attack_rng = 1

        action, direction, option = random_movement(move_rng, attack_rng)

        self.last_state = state

        message = "Hello World"

        ### End ###
        return (action, direction, option), message

class P1_Miner:
    def __init__(self):
        ### Edit Code Below Line ###

        self.internal_ledger = None
        self.last_state = None

        ### End ###
        return

    def code(self, state, ledger):
        ### Edit Code Below Line ###

        self.internal_ledger = ledger

        move_rng = 3
        attack_rng = 0

        #action, direction, option = random_movement(move_rng, attack_rng)
        action, direction, option = random.choice([(random_movement(move_rng, attack_rng)), (random_miner(state,move_rng,attack_rng))])

        self.last_state = state

        message = "Hello World"

        ### End ###
        return (action, direction, option), message

class P1_RangeBlaster:
    def __init__(self):
        ### Edit Code Below Line ###
        
        self.internal_ledger = None
        self.last_state = None

        ### End ###
        return

    def code(self, state, ledger):
        ### Edit Code Below Line ###

        self.internal_ledger = ledger

        move_rng = 3
        attack_rng = 3

        action, direction, option = random_movement(move_rng, attack_rng)

        self.last_state = state

        message = "Hello World"

        ### End ###
        return (action, direction, option), message

class P1_Constructor:
    def __init__(self):
        ### Edit Code Below Line ###
        
        self.internal_ledger = None
        self.last_state = None

        ### End ###
        return

    def code(self, state, ledger):
        ### Edit Code Below Line ###

        self.internal_ledger = ledger

        move_rng = 3
        attack_rng = 0

        action, direction, option = random_movement(move_rng, attack_rng)

        self.last_state = state

        message = "Hello World"

        ### End ###
        return (action, direction, option), message

class P1_Factory:
    def __init__(self):
        ### Edit Code Below Line ###
        
        self.internal_ledger = None
        self.last_state = None

        ### End ###
        return

    def code(self, state, ledger):
        ### Edit Code Below Line ###

        self.internal_ledger = ledger

        attack_rng = 2
        action, direction, option = random_attack(attack_rng)

        self.last_state = state

        message = "Hello World"

        ### End ###
        return (action, direction, option), message

class P1_LazerCannon:
    def __init__(self):
        ### Edit Code Below Line ###
        
        self.internal_ledger = None
        self.last_state = None

        ### End ###
        return

    def code(self, state, ledger):
        ### Edit Code Below Line ###

        self.internal_ledger = ledger

        attack_rng = 3
        #action, direction, option = random_attack(attack_rng)
        action, direction, option = lazer_cannon_destroy_enemy(state)
        
        self.last_state = state

        message = "Hello World"

        ### End ###
        return (action, direction, option), message

class P1_Nexus:
    def __init__(self):
        ### Edit Code Below Line ###
        
        self.internal_ledger = None
        self.last_state = None
        self.num_lazer_cannons = 0

        ### End ###
        return

    def code(self, state, ledger):
        ### Edit Code Below Line ###

        self.internal_ledger = ledger

        attack_rng = 2
        #action, direction, option = random_attack(attack_rng)

        if self.num_lazer_cannons < 3:
            action, direction, option = produce_lazer_cannon(state)
        else:
            return "Wait", None, None

        if option == "LazerCannon":
            self.num_lazer_cannons += 1

        self.last_state = state

        message = "Hello World"

        ### End ###
        return (action, direction, option), message

### WARNING ###
### Code won't be used in game ###
### For testing purposes only ###
### Edit Code Below Line ###


#unit_list = [P1_Invader(), P1_ReconBot(), P1_Miner(), P1_RangeBlaster(), P1_Constructor(), P1_Factory(), P1_LazerCannon(), P1_Nexus()]

#for bot in unit_list:
    #print(type(bot))
    #state = None
    #ledger = None
    #print(bot.code(state, ledger))

    #print()

### End ###