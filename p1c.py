from Mini_War_Codebases.Capital_CodeBase import *

# WARNING DO NOT REMOVE ANY COMMENTS #

# All units: (state, ledger, self.internal_state, self.last_state) -> ((action, direction, option), message) #

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


# Warrior: #

### Edit Code Below Line ###

class P1_Warrior(Base_Warrior):
    def code(self, state, ledger):
        self.internal_ledger = ledger
        move_rng = 4
        attack_rng = 1
        action, direction, option = random_movement(move_rng, attack_rng)
        message = "Hello World"

        return (action, direction, option), message

### End ###


# Archer: #

### Edit Code Below Line ###

class P1_Archer(Base_Archer):
    def code(self, state, ledger):
        self.internal_ledger = ledger
        move_rng = 3
        attack_rng = 3
        action, direction, option = random_movement(move_rng, attack_rng)
        message = "Hello World"

        return (action, direction, option), message

### End ###


# Worker: #

### Edit Code Below Line ###

class P1_Worker(Base_Worker):
    def code(self, state, ledger):
        self.internal_ledger = ledger
        move_rng = 3
        attack_rng = 0
        action, direction, option = random_movement(move_rng, attack_rng)
        message = "Hello World"

        return (action, direction, option), message

### End ###


# City: #

### Edit Code Below Line ###

class P1_City(Base_City):
    def code(self, state, ledger):
        self.internal_ledger = ledger
        attack_rng = 2
        action, direction, option = random_attack(attack_rng)
        message = "Hello World"

        return (action, direction, option), message

### End ###


# Capital: #

### Edit Code Below Line ###
        
class P1_Capital(Base_Capital):
    def code(self, state, ledger):
        self.internal_ledger = ledger
        attack_rng = 2
        action, direction, option = random_attack(attack_rng) #("Wait", None, None)
        message = "Hello World"

        return (action, direction, option), message

### End ###
### TOTAL END ###