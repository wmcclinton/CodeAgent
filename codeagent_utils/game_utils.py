from random import randint

class Game:
    def __init__(self, world):
        self.world = world

    def get_aim_location(self, direction, location):
        aim_location = list(location)
        for d_step in direction:
            if d_step == "up":
                aim_location[0] = aim_location[0] - 1
            elif d_step == "down":
                aim_location[0] =  aim_location[0] + 1
            elif d_step == "left":
                aim_location[1] =  aim_location[1] - 1
            elif d_step == "right":
                aim_location[1] =  aim_location[1] + 1

        return aim_location

    def get_new_location(self, d_step, location):
        if d_step == "up":
            return location[0] - 1, location[1]
        elif d_step == "down":
            return location[0] + 1, location[1]
        elif d_step == "left":
            return location[0], location[1] - 1
        elif d_step == "right":
            return location[0], location[1] + 1

    def calc_attack(self, unit_A, unit_D, location):
        A = unit_A.attack
        A_chp = unit_A.current_hp
        D = unit_D.attack
        D_chp = unit_D.current_hp
        A_Bonus = self.world.layout[location[0]][location[1]]["tile"].bonus
        if A_Bonus == None:
            A_Bonus = 1
        
        dmg = (A * (A_chp/100.))*(1 - ((D * (D_chp/100.)/100.)))*(A_Bonus) + randint(0,5)

        # TODO Add verbose option here print this function
        return int(dmg)

    def get_state(self, unit, location):

        state = [[{} for _ in range(2*unit.sight_rng + 1)] for _ in range(2*unit.sight_rng + 1)]

        for i in range(2*unit.sight_rng + 1):
            for j in range(2*unit.sight_rng + 1):
                actual_i = location[0] -  unit.sight_rng + i
                actual_j = location[1] -  unit.sight_rng + j
                if abs(actual_i - location[0]) + abs(actual_j - location[1]) <= unit.sight_rng:
                    if self.world.layout[actual_i][actual_j]["unit"] == None:
                        state[i][j]["unit"] = None
                        state[i][j]["unit_current_hp"] = None
                    else:
                        state[i][j]["unit"] = self.world.layout[actual_i][actual_j]["unit"].name
                        state[i][j]["unit_current_hp"] = self.world.layout[actual_i][actual_j]["unit"].current_hp

                    state[i][j]["tile"] = self.world.layout[actual_i][actual_j]["tile"].name
                else:
                    state[i][j]["unit"] = "Unknown"
                    state[i][j]["unit_current_hp"] = "Unknown"
                    state[i][j]["tile"] = "Unknown"

        return state

    def full_turn(self, team, verbose=True):
        if verbose:
            print("#"*100)
            print("BEGINNING [TEAM " + str(team) + "] TURN:")
            print("-"*100)

        for i, row in enumerate(self.world.layout):
            for j, item in enumerate(row):
                if item["unit"] != None:
                    if item["unit"].team == team:
                        item["unit"].has_moved = False

        for i, row in enumerate(self.world.layout):
            for j, item in enumerate(row):
                if item["unit"] != None:
                    if item["unit"].team == team:
                        if item["unit"].has_moved == False:
                            state = self.get_state(item["unit"], (i,j))
                            #print(state)
                            #self.world.render_state(state,team)
                            team = item["unit"].team
                            ledger = self.get_ledger(team)
                            #print(ledger)
                            name = item["unit"].name
                            action_tuple = item["unit"].source.code(state, ledger)
                            item["unit"].has_moved = True

                            if verbose:
                                print("({},{}) [Team {}]".format(i,j,team),name,"=>",action_tuple)
                                print(self.turn(item["unit"], action_tuple, (i,j)))
                                print("-"*100)
                        
        done = self.finish_check() # Must be defined in Game.py
        return done

    def turn(self, unit, action_tuple, location):
        #print(unit,action_tuple,location)
        action_type = action_tuple[0]
        direction = action_tuple[1]
        option = action_tuple[2]
        i, j = location

        if action_type not in unit.allowed_actions:
            return "\"" + str(action_type)  + "\" is an invalid Action Type"

        if action_type == "Move":
            moves_left = unit.move_rng

            for d_step in direction:
                # Check if unit in that location
                new_i, new_j = self.get_new_location(d_step, location)

                if self.world.layout[new_i][new_j]["unit"] != None or self.world.layout[new_i][new_j]["tile"].move_penalty == None or moves_left <= 0:
                    break
                else:
                    your_unit = self.world.layout[i][j]["unit"]
                    self.world.layout[i][j]["unit"] = None
                    self.world.layout[new_i][new_j]["unit"] = your_unit
                    i = new_i
                    j = new_j
                    location = (new_i, new_j)
                    moves_left = moves_left - self.world.layout[new_i][new_j]["tile"].move_penalty

            self.world.render()
            if option == None:
                return "Unit moved"
            else:
                action_type = option[0]
                direction = option[1]
                option = option[2]

        if action_type == "Attack":
            aim_i, aim_j = self.get_aim_location(direction, location)
            defense_unit = self.world.layout[aim_i][aim_j]["unit"]

            if defense_unit!= None:
                dmg = self.calc_attack(unit, defense_unit, location)
                # Update defense unit current_hp
                defense_unit.current_hp = defense_unit.current_hp - dmg

                # Check if dead then remove
                if defense_unit.current_hp <= 0:
                    self.world.layout[aim_i][aim_j]["unit"] = None

                    return "Attack Landed - Opposing Unit Died"
                else:
                    # Check if alive then counterattack
                    counter_dmg = self.calc_attack(defense_unit, unit, (aim_i,aim_j))

                    # Update unit current_hp
                    unit.current_hp = unit.current_hp - counter_dmg

                    if unit.current_hp <= 0:
                        self.world.layout[i][j]["unit"] = None
                        return "Attack Landed - Your Unit Died"

                return "Attack Landed"
            else:

                return "Attack Missed"

        elif action_type == "Reinforce":
            aim_i, aim_j = self.get_aim_location(direction, location)
            reinforcing_unit = self.world.layout[aim_i][aim_j]["unit"]

            if reinforcing_unit != None:
                if reinforcing_unit.team == unit.team:
                    if self.get_resources(unit.team) >= (100 - unit.current_hp) and reinforcing_unit.current_hp > (100 - unit.current_hp):
                        reinforcing_unit.current_hp = reinforcing_unit.current_hp - (100 - unit.current_hp)
                        unit.current_hp = 100
                        self.set_resources(unit.team, self.get_resources(unit.team) - (100 - unit.current_hp)) # Must Define Get and Set Resources
                        return "Successfully Reinforced"

            return "Reinforcement Failed"

        elif action_type == "Interact":
            aim_i, aim_j = self.get_aim_location(direction, location)
            interacting_unit = self.world.layout[aim_i][aim_j]["unit"]
            interacting_tile = self.world.layout[aim_i][aim_j]["tile"]

            if interacting_unit != None:
                if interacting_unit.interaction != None:
                    interacting_unit.interaction(unit)
                    return "Successfully Interacted with Unit"

            if interacting_tile != None:
                if interacting_tile.interaction != None:
                    interacting_tile.interaction(unit)
                    return "Successfully Interacted with Tile"

            return "Interaction Failed"

        elif action_type == "Communicate":
            if option == None:
                return "Failed to send Message"

            message = str(option)
            if len(message) > 25:
                return "Failed to send Message Too Long"
            else:
                self.add_ledger(unit.team,message)
                return "Message Successfully Uploaded"

        elif action_type == "Produce":
            aim_i, aim_j = self.get_aim_location(direction, location)
            produce_unit = self.world.layout[aim_i][aim_j]["unit"]
            produce_tile = self.world.layout[aim_i][aim_j]["tile"]

            if produce_unit == None:
                if produce_tile.move_penalty != None and ("All" in produce_tile.allowed_units or unit.name in produce_tile.allowed_units):
                    if option == None:
                        return "Failed to Define Unit for Production"

                    try:
                        self.world.layout[aim_i][aim_j]["unit"] = self.producer(option, unit.team) # Define producer
                    except KeyError:
                        self.world.layout[aim_i][aim_j]["unit"] = None
                        return "Failed to produce " + str(option)

        return "\"" + str(action_type)  + "\" was invalid"