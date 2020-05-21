class Employee():

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def from_string(cls, string_all):
        string_to_list = string_all.split('-')
        return cls(string_to_list[0], string_to_list[1], int(string_to_list[2]))

emp1 = Employee('Mary', 'Sue', 60000)
emp2 = Employee.from_string('ff-ff-55')


print(emp1.first_name)
print(emp1.salary)

print(emp2.first_name)
