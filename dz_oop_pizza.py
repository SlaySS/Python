class Pizza:
    order = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.order += 1
        self.order_number = Pizza.order

    @classmethod   #медод класса, получает в качестве аргумента сам класс через cls
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])  # по сути Pizza(['ham', 'pineapple'])

    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'olives', 'mushroom'])

    @classmethod
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])


p1 = Pizza(['spinach', 'olives', 'mushroom'])
p2 = Pizza.hawaiian()

# print(pizza2.ingredients)
print(Pizza.order)
print(p1.order_number)
print(p2.order_number)
print(p1.ingredients)
