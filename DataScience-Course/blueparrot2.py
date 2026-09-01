class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

blue = Parrot("Blue", 10)

print(blue.sing("'Happy'"))
print(blue.dance())