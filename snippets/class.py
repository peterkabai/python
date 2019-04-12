class integer():

    def __init__(self, initial):
        self.value = initial

    def __add__(self, other):
        return self.value + other

    def __str__(self):
        return str(self.value)

i = integer(5)
print(i)
print(i + 5)