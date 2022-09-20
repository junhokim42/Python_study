class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    # def __eq__(self, other):
    #     return self.age == other.age and self.name == other.name

kim = Human(29, 'Kim Sanghyeong')
sang = Human(29, 'Kim Sanghyeong')
moon = Human(44, 'Moon Jongmin')

print(kim == sang)
print(kim == moon)