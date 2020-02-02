# CodeAgent

## How to write agent script:

There are 5 different actions :
Left is the "Name" and Right is how to output ("Name", Direction_List, Option)
- "Move" - Reposition in the World => (“Move”, [“up”, “up”,“right”,“up”], None)
- "Attack" - Damage unit => (“Attack”, [“up”], None)
- "Reinforce" - Heal HP around structure => (“Reinforce”, [“up”], None)
- "Interact" - Do something with environment => (“Interact”, [“left”], None)
- "Produce" - Make units => (“Produce”, [“down”], “Miner”)

Every agent type has a class and in the class an init and code function. The code funtion gets in a 'state' and 'ledger' then outputs a 'action_tuple' and 'message'. The init function holds varibles throughout the game.
(Example Agent Type):

'''
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
        return (action, direction, option), message # The output is of the form (“Move”, [“up”, “up”,“right”,“up”], option), "Hello World"

'''

## How agent state and ledger look:

(State Example): 
'''
[[{'unit': 'Unknown', 'unit_current_hp': 'Unknown', 'tile': 'Unknown'}, {'unit': 'Unknown', 'unit_current_hp': 'Unknown', 'tile': 'Unknown'}, {'unit': 'Unknown', 'unit_current_hp': 'Unknown', 'tile': 'Unknown'}, ...]]
'''

The 'state' is an NxN array where each element is a dictionary containing: 'unit' (the unit's name at that position), 'unit_current_hp' (the unit's current health %), and 'tile' (the tile at that position). This can be used to inform agents decisions via the code function.

(Ledger Example):
'''
["Hello World","Hello World","Hello World",...]
'''

The 'ledger' is an array where each element is a string that an agent has appended to the general ledger during their turn. This can be also be used to inform agents decisions via the code function. The entire history is passed in each time

## How agent class works:

For each game you write code in two places for every agent type. Inside each agent type's class there is an init function and a code function. During the game every time it is an agents turn to take and action the code function will be called with your agents current state and the global ledger passed in as arguments. The outpus of your code funtion will be used to take actions in the world. The init function can be used to store variables throughout your agents lifetime will playing the game, this can me thought of as internal memory.

The goal of the game is to write all of your agent classes to perfom in orchestra to acomplish tasks that lead to the demise of your opponent or atleast allow you to outlast them.

## Game 1: Galactic War

Units:

...

## Defining a game

To be continued...

