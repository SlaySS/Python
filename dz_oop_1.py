class Name:

    def __init__(self, first, last):
        self.first_name = first.lower().capitalize()
        self.last_name = last.title()
        self.full_name = self.first_name + ' ' + self.last_name
        self.initials = self.first_name[0] + '.' + self.last_name[0]


user = Name('john', 'SMITH')
print(user.first_name)
print(user.full_name)
print(user.initials)