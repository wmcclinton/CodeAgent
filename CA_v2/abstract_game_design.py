import numpy as np
import matplotlib.pyplot as plt

class GameObject():
    def __init__(self, obj_type, loc, message, team, color, specific_attributes, action_set, code):
        self.obj_type = obj_type
        self.loc = loc
        self.message = message
        self.team = team
        self.memory = []
        self.color = color
        self.specific_attributes = specific_attributes # Dictionary of other attributes
        self.action_set = action_set
        self.code = code # Function turns obs, memory into action, action arg, and message
        self.has_moved = False

class Game():
    def __init__(self, h, w, background_color, init_frame):
        self.h = h
        self.w = w
        self.background_color = background_color
        self.init_frame = init_frame
        self.current_frame = init_frame
        self.internal_timer = 0
        self.render_speed = 0.0001

        self.done = 0

    def render(self):
        def get_color(info):
            if info["obj"] != None:
                if info["obj"].team == None:
                    return info["obj"].color
                else:
                    return info["obj"].color[info["obj"].team - 1]
            else:
                return self.background_color

        rgb_frame = np.array([[get_color(self.current_frame[(y,x)]) for x in range(self.w)] for y in range(self.h)])
        #print(rgb_world)
        plt.title("World")
        plt.imshow(rgb_frame)
        plt.draw()
        plt.pause(self.render_speed)
        plt.clf()

        return

    def render_agent(self, obs):
        def get_color(info):
            if type(info) == type("string"):
                return (0,255,255)
            else:
                if info["obj"] != None:
                    if info["obj"].team == None:
                        return info["obj"].color
                    else:
                        return info["obj"].color[info["obj"].team - 1]
                else:
                    return self.background_color

        rgb_frame = np.array([[get_color(obs[x][y]) for x in range(len(obs))] for y in range(len(obs[0]))])
        #print(rgb_world)
        plt.title("World")
        plt.imshow(rgb_frame)
        plt.draw()
        plt.pause(10)
        plt.clf()

        return

    def run(self, render=False):
        print("Running")

        while(self.done == 0):
            if render:
                self.render()

            self.step()

    # Need at step function defined
        

