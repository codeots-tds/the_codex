class Basemethod:
    def __init__(self, name):
        self.name = name



    @classmethod
    def get_age(cls, name, age):
        return cls(name, age)

if __name__=="__main__":
    person1=Basemethod("Ark")
    age=Basemethod.get_age("Kara", 42)
    print(age)
    pass
