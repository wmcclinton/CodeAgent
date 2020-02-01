class Unit:
    def __init__(self, name, cost, attack, defense, attack_rng, sight_rng, team=None, current_hp=100):
        self.name = name
        self.team = team
        self.cost = cost
        self.current_hp = current_hp
        self.attack = attack
        self.defense = defense
        self.attack_rng = attack_rng
        self.sight_rng = sight_rng

    def showUnitAttributes(self):
        print("Name:",self.name)
        print("Team:",self.team)
        print("Cost:",self.cost)
        print("Current_HP:",self.current_hp)
        print("Attack:",self.attack)
        print("Defense:",self.defense)
        print("Attack_RNG:",self.attack_rng)
        print("Sight_RNG:",self.sight_rng)


class Ground_Unit(Unit):
    def __init__(self, name, cost, attack, defense, attack_rng, sight_rng, move_rng, team=None, critical_pos=None, type_effect=None, item=None, current_hp=100):
        super().__init__(name, cost, attack, defense, attack_rng, sight_rng, team, current_hp)
        self.move_rng = move_rng
        self.critical_pos = None
        self.type_effect = None
        self.item = None
    
    def display(self):
        self.showUnitAttributes()
        print("### Specific Attributes ###")
        print("Move_RNG:",self.move_rng)
        print("Critical_POS:",self.critical_pos)
        print("Type_EFFECT:",self.type_effect)
        print("Item:",self.item)
        
class Structure_Unit(Unit):
    def __init__(self, name, cost, attack, defense, attack_rng, sight_rng, team=None, is_main=False, earning=None, tile_restriction=None, producible_units=["All"], interaction=None, current_hp=100):
        super().__init__(name, cost, attack, defense, attack_rng, sight_rng, team, current_hp)
        self.is_main = is_main
        self.earning = earning
        self.tile_restriction = tile_restriction
        self.producible_units = producible_units
        self.interaction = interaction

    def display(self):
        self.showUnitAttributes()
        print("Is_MAIN:",self.is_main)
        print("Earning:",self.earning)
        print("Tile_RESTRICT:",self.tile_restriction)
        print("Production:",self.producible_units)
        print("Interaction:",self.interaction)
