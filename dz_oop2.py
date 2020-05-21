class Calculator:

    def add(self, a, b):
        self.a = a
        self.b = b
        return self.a + self.b

    def subtract(self, a, b):
        self.a = a
        self.b = b
        return self.a - self.b

    def multiply(self, a, b):
        self.a = a
        self.b = b
        return self.a * self.b

    def divide(self, a, b):
        self.a = a
        self.b = b
        return self.a / self.b

c = Calculator()
print(c.devide(5,6))
