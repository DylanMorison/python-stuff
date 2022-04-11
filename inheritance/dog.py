import animal


class Dog(animal.Animal):
    def __init__(self, age):
        self.age = age
        print("called init on Dog class that inherits Animal class!")


