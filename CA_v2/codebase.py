import random

class Code:
    def __init__(self):
        self.source_code = {"Pacman_Agent": self.Pacman_Agent_Code, "Ghost_Agent": self.Ghost_Agent_Code}

    def Pacman_Agent_Code(self, obs, message, memory):
        return random.choice(["up","down","left","right","stay"]), 0, "Hello world!"

    def Ghost_Agent_Code(self, obs, message, memory):
        return random.choice(["up","down","left","right","stay"]), 0, "Hello world!"