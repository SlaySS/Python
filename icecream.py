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
        return max([icecream.sprinkles + flavor_values[icecream.flavor] for icecream in lst])


ice1 = IceCream("ChokolateChip", 10)
ice2 = IceCream("Vanilla", 5)
print(IceCream.sweetest_icecream([ice1, ice2]))

