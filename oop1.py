class Character():
    MAX_SPEED = 100        # заглавными буквами записываются константы

    def __init__(self, race, health):
        self.__race = race  # два подчеркивания приватный аттрибут, не может наследоваться
        self._health = health  # одно подчеркивание защищенный аттрибут

    def hit(self, damage):
        self._health -= damage


unit1 = Character('orc', 100)
unit1.hit(50)
print(unit1._health)
