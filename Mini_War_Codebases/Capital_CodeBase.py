import random

### Space for defining functions ###
### No global variables ###

class Base_Warrior:
    def __init__(self):
        self.internal_ledger = None
        self.last_state = None

    def code(self, state, ledger):

        self.last_state = state

        return ("Wait", None, None), "Hello World"

class Base_Worker:
    def __init__(self):
        self.internal_ledger = None
        self.last_state = None

    def code(self, state, ledger):

        self.last_state = state

        return ("Wait", None, None), "Hello World"

class Base_Archer:
    def __init__(self):
        self.internal_ledger = None
        self.last_state = None

    def code(self, state, ledger):

        self.last_state = state

        return ("Wait", None, None), "Hello World"

class Base_City:
    def __init__(self):
        self.internal_ledger = None
        self.last_state = None

    def code(self, state, ledger):

        self.last_state = state

        return ("Wait", None, None), "Hello World"

class Base_Capital:
    def __init__(self):
        self.internal_ledger = None
        self.last_state = None

    def code(self, state, ledger):

        self.last_state = state

        return ("Wait", None, None), "Hello World"

### WARNING ###
### Code won't be used in game ###
### For testing purposes only ###
### Edit Code Below Line ###

### End ###