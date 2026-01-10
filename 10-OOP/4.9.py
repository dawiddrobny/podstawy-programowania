class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        s = f"{self.surname}{self.name[0]}{self.seniority}"
        if self.age >= 18:
            return s.upper()
        else:
            return s.lower()

print(C("Anna","May",17,7))
print(C("George","Brown",21,4))
