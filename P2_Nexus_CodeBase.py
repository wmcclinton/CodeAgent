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

### End ###

class P2_Invader:
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

        action, direction, option = random_movement(move_rng, attack_rng)

        self.last_state = state

        message = "Hello World"

        ### End ###
        return (action, direction, option), message

class P2_Miner:
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
        action, direction, option = random_attack(attack_rng)

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