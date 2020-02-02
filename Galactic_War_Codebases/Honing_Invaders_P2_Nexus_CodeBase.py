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

def random_movement_weighted(move_rng, attack_rng):
    action = "Move"
    direction = [random.choice(["up","up","up","down","left","left","left","right"]) for _ in range(move_rng)]
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

def produce_invader(state):
    my_i = int(len(state[0])/2)
    my_j = int(len(state[0])/2)
    if state[my_i - 1][my_j]["unit"] == None:
        return "Produce", ["up"], "Invader"
    elif state[my_i + 1][my_j]["unit"] == None:
        return "Produce", ["down"], "Invader"
    elif state[my_i][my_j - 1]["unit"] == None:
        return "Produce", ["left"], "Invader"
    elif state[my_i][my_j + 1]["unit"] == None:
        return "Produce", ["right"], "Invader"

    return "Wait", None, None

def honing_invader(state,route):
    my_i = int(len(state[0])/2)
    my_j = int(len(state[0])/2)

    directions = []
    option = None
    while len(directions) < 4:
        if route == 0:
            # if see Nexus Attack else move towards nexus
            if state[my_i - 1][my_j]["unit"] != None and str(state[my_i - 1][my_j]["unit_team"]) == "1":
                option = ("Attack", ["up"], None)
                break
            elif state[my_i + 1][my_j]["unit"] != None and str(state[my_i + 1][my_j]["unit_team"]) == "1":
                option = ("Attack", ["down"], None)
                break
            elif state[my_i][my_j - 1]["unit"] != None and str(state[my_i][my_j - 1]["unit_team"]) == "1":
                option = ("Attack", ["left"], None)
                break
            elif state[my_i][my_j + 1]["unit"] != None and str(state[my_i][my_j + 1]["unit_team"]) == "1":
                option = ("Attack", ["right"], None)
                break
            elif state[my_i - 1][my_j]["unit"] == None and (state[my_i][my_j]["location"][0] - 1 > 19):
                my_i = my_i - 1
                directions.append("up")
            elif state[my_i][my_j - 1]["unit"] == None and (state[my_i][my_j]["location"][1] - 1 > 19):
                my_j = my_j - 1
                directions.append("left")
            elif state[my_i + 1][my_j]["unit"] == None:
                directions.append(random.choice(["up","down","left","right"]))
            elif state[my_i][my_j + 1]["unit"] == None:
                directions.append(random.choice(["up","down","left","right"]))
            else:
                directions.append(random.choice(["up","down","left","right"]))

    return "Move", directions, option

def miner_search(state, has_ore):
    my_i = int(len(state[0])/2)
    my_j = int(len(state[0])/2)

    directions = []
    option = None
    while len(directions) < 4:
        if not has_ore:
            if state[my_i - 1][my_j]["tile"] == "Minerals":
                option = ("Interact", ["up"], None)
                break
            elif state[my_i + 1][my_j]["tile"] == "Minerals":
                option = ("Interact", ["down"], None)
                break
            elif state[my_i][my_j - 1]["tile"] == "Minerals":
                option = ("Interact", ["left"], None)
                break
            elif state[my_i][my_j + 1]["tile"] == "Minerals":
                option = ("Interact", ["right"], None)
                break
            elif state[my_i + 1][my_j]["unit"] == None and (state[my_i][my_j]["location"][0] + 1 < 90):
                my_i = my_i + 1
                directions.append("down")
            elif state[my_i][my_j + 1]["unit"] == None and (state[my_i][my_j]["location"][1] + 1 < 90):
                my_j = my_j + 1
                directions.append("right")
            elif state[my_i - 1][my_j]["unit"] == None:
                directions.append(random.choice(["up","down","left","right"]))
            elif state[my_i][my_j - 1]["unit"] == None:
                directions.append(random.choice(["up","down","left","right"]))
            else:
                directions.append(random.choice(["up","down","left","right"]))
        else:
            if state[my_i - 1][my_j]["unit"] == "Nexus" and str(state[my_i - 1][my_j]["unit_team"]) == "2":
                option = ("Interact", ["up"], None)
                break
            elif state[my_i + 1][my_j]["unit"] == "Nexus" and str(state[my_i + 1][my_j]["unit_team"]) == "2":
                option = ("Interact", ["down"], None)
                break
            elif state[my_i][my_j - 1]["unit"] == "Nexus" and str(state[my_i][my_j - 1]["unit_team"]) == "2":
                option = ("Interact", ["left"], None)
                break
            elif state[my_i][my_j + 1]["unit"] == "Nexus" and str(state[my_i][my_j + 1]["unit_team"]) == "2":
                option = ("Interact", ["right"], None)
                break
            elif state[my_i - 1][my_j]["unit"] == None and (state[my_i][my_j]["location"][0] - 1 > 80):
                my_i = my_i - 1
                directions.append("up")
            elif state[my_i][my_j - 1]["unit"] == None and (state[my_i][my_j]["location"][1] - 1 > 80):
                my_j = my_j - 1
                directions.append("left")
            elif state[my_i + 1][my_j]["unit"] == None:
                directions.append(random.choice(["up","down","left","right"]))
            elif state[my_i][my_j + 1]["unit"] == None:
                directions.append(random.choice(["up","down","left","right"]))
            else:
                directions.append(random.choice(["up","down","left","right"]))

    return "Move", directions, option

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

### End ###

class P2_Invader:
    def __init__(self):
        ### Edit Code Below Line ###
        
        self.internal_ledger = None
        self.last_state = None

        self.route = 0

        ### End ###
        return

    def code(self, state, ledger):
        ### Edit Code Below Line ###

        self.internal_ledger = ledger

        move_rng = 4
        attack_rng = 1

        #action, direction, option = random_movement(move_rng, attack_rng)
        action, direction, option = honing_invader(state, self.route)

        self.last_state = state

        message = "Hello World"

        ### End ###
        return (action, direction, option), message

class P2_ReconBot:
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

        action, direction, option = random_movement_weighted(move_rng, attack_rng)

        self.last_state = state

        message = "Hello World"

        ### End ###
        return (action, direction, option), message

class P2_Miner:
    def __init__(self):
        ### Edit Code Below Line ###
        
        self.internal_ledger = None
        self.last_state = None

        self.has_ore = False

        ### End ###
        return

    def code(self, state, ledger):
        ### Edit Code Below Line ###

        self.internal_ledger = ledger

        move_rng = 3
        attack_rng = 0

        #action, direction, option = random_movement(move_rng, attack_rng)
        action, direction, option = miner_search(state,self.has_ore)

        if option != None:
            if option[0] == "Interact":
                if self.has_ore == False:
                    self.has_ore = True
                else:
                    self.has_ore = False

        self.last_state = state

        message = "Hello World"

        ### End ###
        return (action, direction, option), message

class P2_RangeBlaster:
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

class P2_Constructor:
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

class P2_Factory:
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

class P2_LazerCannon:
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
        action, direction, option = random_attack(attack_rng)
        
        self.last_state = state

        message = "Hello World"

        ### End ###
        return (action, direction, option), message

class P2_Nexus:
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
        #action, direction, option = random_attack(attack_rng)
        action, direction, option = produce_invader(state)

        self.last_state = state

        message = "Hello World"

        ### End ###
        return (action, direction, option), message

### WARNING ###
### Code won't be used in game ###
### For testing purposes only ###
### Edit Code Below Line ###


#unit_list = [P2_Invader(), P2_ReconBot(), P2_Miner(), P2_RangeBlaster(), P2_Constructor(), P2_Factory(), P2_LazerCannon(), P2_Nexus()]

#for bot in unit_list:
    #print(type(bot))
    #state = None
    #ledger = None
    #print(bot.code(state, ledger))

    #print()

### End ###