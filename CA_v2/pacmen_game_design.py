from abstract_game_design import GameObject, Game
import copy

# Object Definitions

# Non-Agents

class Pellet_Object(GameObject):
    def __init__(self, team=None, code=None, obj_type="pellet", loc=None, message="", color=(155,155,155), specific_attributes=None, action_set=None):
        super().__init__(obj_type, loc, message, team, color, specific_attributes, action_set, code)

class Big_Pellet_Object(GameObject):
    def __init__(self, team=None, code=None, obj_type="big-pellet", loc=None, message="", color=(255,255,255), specific_attributes=None, action_set=None):
        super().__init__(obj_type, loc, message, team, color, specific_attributes, action_set, code)

class Wall_Object(GameObject):
    def __init__(self, team=None, code=None, obj_type="wall", loc=None, message="", color=(50,50,50), specific_attributes=None, action_set=None):
        super().__init__(obj_type, loc, message, team, color, specific_attributes, action_set, code)

# Agents

class Pacman_Agent(GameObject):
    def __init__(self, team, code, obj_type="pacman", loc=None, message="", color=[(0,255,0),(255,0,0)], specific_attributes={"power-up": 0, "sight": 5}, action_set=["up","down","left","right","stay"]):
        super().__init__(obj_type, loc, message, team, color, specific_attributes, action_set, code)

class Ghost_Agent(GameObject):
    def __init__(self, team, code, obj_type="ghost", loc=None, message="", color=[(0,55,0),(55,0,0)], specific_attributes={"sight": 5}, action_set=["up","down","left","right","stay"]):
        super().__init__(obj_type, loc, message, team, color, specific_attributes, action_set, code)


# Game Definition
# Game Logic

class Pacmen(Game):
    def __init__(self, codebase1, codebase2, h=30, w=30, background_color=(0,0,0)):

        self.codebase1 = codebase1
        self.codebase2 = codebase2

        filename = "pacmen_env_1.txt"

        #filename = input("Init Env Filename: ")
        f = open(filename, "r")
        init_frame = self.txt2init_frame(f.readlines()) # Dictionary of Objects and tile tyoe they are on
        f.close()

        super().__init__(h, w, background_color, init_frame)

        self.p1_score = 0
        self.p2_score = 0

        self.p1_pacman_alive = True
        self.p2_pacman_alive = True


    def txt2init_frame(self, source):
        source = [line.replace("\n","") for line in source]
        frame = {}

        char2obj = {"#" : Wall_Object, " ": None, ".": Pellet_Object, "*": Big_Pellet_Object, "1": Pacman_Agent, "2": Ghost_Agent, "3": Pacman_Agent, "4": Ghost_Agent}
        char2agent = ["1","2","3","4"]

        for i in range(len(source)):
            for j in range(len(source[0])):

                if source[i][j] in char2agent:
                    if source[i][j] == "1":
                        frame[(i,j)] = {"obj": char2obj[source[i][j]](1, self.codebase1.source_code["Pacman_Agent"]),"tile": 0}
                    if source[i][j] == "2":
                        frame[(i,j)] = {"obj": char2obj[source[i][j]](1, self.codebase1.source_code["Ghost_Agent"]),"tile": 0}
                    if source[i][j] == "3":
                        frame[(i,j)] = {"obj": char2obj[source[i][j]](2, self.codebase2.source_code["Pacman_Agent"]),"tile": 0}
                    if source[i][j] == "4":
                        frame[(i,j)] = {"obj": char2obj[source[i][j]](2, self.codebase2.source_code["Ghost_Agent"]),"tile": 0}
                else:
                    if char2obj[source[i][j]] != None:
                        frame[(i,j)] = {"obj": char2obj[source[i][j]](),"tile": 0}
                    else:
                        frame[(i,j)] = {"obj": None,"tile": 0}
        
        return frame

    def get_obs(self,frame, obj, loc):
        obs = [[{} for _ in range(2*obj.specific_attributes["sight"] + 1)] for _ in range(2*obj.specific_attributes["sight"] + 1)]

        for i in range(2*obj.specific_attributes["sight"] + 1):
            for j in range(2*obj.specific_attributes["sight"] + 1):
                actual_i = loc[0] -  obj.specific_attributes["sight"] + i
                actual_j = loc[1] -  obj.specific_attributes["sight"] + j
                try:
                    if abs(actual_i - loc[0]) + abs(actual_j - loc[1]) <= obj.specific_attributes["sight"]:
                        obs[i][j] = frame[(i, j)]
                    else:
                        obs[i][j] = "Unknown"
                except IndexError:
                    obs[i][j] = "EOW"

        return obs

    def get_next_location(self, d_step, loc):
        if d_step == "up":
            return loc[0] - 1, loc[1]
        elif d_step == "down":
            return loc[0] + 1, loc[1]
        elif d_step == "left":
            return loc[0], loc[1] - 1
        elif d_step == "right":
            return loc[0], loc[1] + 1
        else:
            return loc[0], loc[1]

    def step(self):

        # Set agents to have not moved
        for key, val in self.current_frame.items():
            if val["obj"] != None:
                if val["obj"].obj_type in ["pacman","ghost"]:
                    val["obj"].has_moved = False


        # TODO need turn ordering function

        # Get obs for every agent
        # Get message for every agent
        # Get memory for every agent

        next_frame = {}

        for key, val in self.current_frame.items():
            if val["obj"] != None:
                if val["obj"].obj_type in ["pacman","ghost"]:
                    if not val["obj"].has_moved:
                        val["obj"].has_moved = True

                        #print(key)
                        #print(val)

                        this_loc = key
                        this_obj_type = val["obj"].obj_type
                        this_obj = copy.deepcopy(val["obj"])

                        obs = self.get_obs(self.current_frame, val["obj"], this_loc)
                        message = None
                        memory = val["obj"].memory

                        #self.render_agent(obs)

                        #print(obs, message, memory)
                        #input()
                        info = str(val["obj"].obj_type) + str(val["obj"].team)
                        action, action_args, message = val["obj"].code(obs, message, memory, info)

                        # Step
                        val["obj"].memory.append(message)

                        if action in val["obj"].action_set:
                            # Move
                            # Check Collision
                            next_loc = self.get_next_location(action, this_loc)
                            next_loc_info = self.current_frame[next_loc]

                            #print(next_loc_info)

                            if next_loc_info["obj"] == None:
                                self.current_frame[next_loc]["obj"] = this_obj
                                self.current_frame[this_loc]["obj"] = None

                            else:
                                if next_loc_info["obj"].obj_type == "big-pellet":
                                    if this_obj_type == "pacman":
                                        val["obj"].specific_attributes["power-up"] = 10
                                        if val["obj"].team == 1:
                                            self.p1_score += 10
                                        elif val["obj"].team == 2:
                                            self.p2_score += 10

                                    self.current_frame[next_loc]["obj"] = this_obj
                                    self.current_frame[this_loc]["obj"] = None
                                
                                elif next_loc_info["obj"].obj_type == "pellet":
                                    if this_obj_type == "pacman":
                                        if val["obj"].team == 1:
                                            self.p1_score += 1
                                        elif val["obj"].team == 2:
                                            self.p2_score += 1

                                    self.current_frame[next_loc]["obj"] = this_obj
                                    self.current_frame[this_loc]["obj"] = None
                                
                                elif next_loc_info["obj"].obj_type == "wall":
                                    pass

                                elif next_loc_info["obj"].obj_type == "pacman":
                                    if this_obj_type == "ghost" and val["obj"].team != next_loc_info["obj"].team:
                                        if next_loc_info["obj"].team == 1:
                                            self.p1_pacman_alive = False
                                        elif next_loc_info["obj"].team == 2:
                                            self.p2_pacman_alive = False

                                        self.current_frame[next_loc]["obj"] = this_obj
                                        self.current_frame[this_loc]["obj"] = None

                                    else:
                                        pass

                                elif next_loc_info["obj"].obj_type == "ghost":
                                    pass
                            
                                if this_obj_type == "pacman" and this_obj.specific_attributes["power-up"] != 0:
                                    this_obj.specific_attributes["power-up"] -= 1
                        #print()


        # Pass those in and get (action, action arg, and message) for every agent

        # Use those to step frame to next frame

        #

        # Check if done

        return self.current_frame

    def done_check(self):
        print("P1 Score:", self.p1_score)
        print("P2 Score:", self.p2_score)

        if self.p1_score >= 100 or self.p2_score >= 100 or (not self.p1_pacman_alive and not self.p2_pacman_alive) or self.internal_timer >= 1000:
            self.done = True
        
        self.internal_timer += 1

        return self.done