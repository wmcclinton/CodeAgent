import matplotlib.pyplot as plt
import numpy as np

class Tile():
    def __init__(self, name="Dirt", move_penalty=1, bonus=None, allowed_units=["All"], interaction=None):
        self.name = name
        self.move_penalty = move_penalty
        self.bonus = bonus
        self.allowed_units = allowed_units
        self.interaction = interaction


class World:
    def __init__(self, width, height, base_tile, tile_comp, unit_comp, color_map=None):
        self.__delay_time__ = 0.001

        self.width = width
        self.height = height
        self.color_map = color_map
        self.layout = [[{"tile": base_tile, "unit": None} for _ in range(width)] for _ in range(height)]
        plt.ion()

        for tile_tuple in tile_comp:
            self.layout[tile_tuple[0]][tile_tuple[1]]["tile"] = tile_tuple[2]

        for unit_tuple in unit_comp:
            self.layout[unit_tuple[0]][unit_tuple[1]]["unit"]  = unit_tuple[2]

    def render(self):
        def get_color(unit, tile):
            if unit == None:
                return self.color_map[tile.name]
            else:
                return self.color_map[unit.name][unit.team-1]

        rgb_world = np.array([[get_color(self.layout[y][x]["unit"], self.layout[y][x]["tile"]) for x in range(self.width)] for y in range(self.height)])
        #print(rgb_world)
        plt.title("World")
        plt.imshow(rgb_world)
        plt.draw()
        plt.pause(0.0001)
        plt.clf()

        return

    def render_state(self, state, team):
        def get_color(unit, tile):
            if unit == None or unit == "Unknown":
                return self.color_map[tile]
            else:
                return self.color_map[unit][team-1]

        rgb_world = np.array([[get_color(state[y][x]["unit"], state[y][x]["tile"]) for x in range(len(state))] for y in range(len(state))])
        #print(rgb_world)
        plt.title("World")
        plt.imshow(rgb_world)
        plt.draw()
        plt.pause(self.__delay_time__)
        plt.clf()

        return

    def renderP3D(self):
        # Panda3D Rendering
        return

    
    def display(self):
        for i, row in enumerate(self.layout):
            for j, item in enumerate(row):
                print(item)