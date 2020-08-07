class Agent:
    def __init__(self):
        self.memory = None

    def act(self,obs):
        return "action"


class Env:
    def __init__(self):
        self.memory = None
        self.current_frame = None

    def transition(self, actions):
        next_frame = None
        self.current_frame = next_frame
        return self.current_frame

    def get_obs(self):
        return None

env = Env()
A1 = Agent()

action = A1.act(env.get_obs())
print(action)

env.transition([action])

print(env.current_frame)


