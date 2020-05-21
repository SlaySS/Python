class IceCream:
    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles

def sweetest_icecream(lst):
    flavor_values = {
        "Plain": 0,
        "Vanilla": 5,
        "ChokolateChip": 5,
        "Strawberry": 10,
        "Chokolate": 10
    }