from animal_class import*

class Cow(Animal):
    """A Cow"""

    def __init__(self):
        super().__init__(1,3,6)
        self.type = "Cow"

    def grow(self,food,water):
        if 


def main():
    new_cow = Cow()
    print(new_cow.report())
    manual_grow(new_cow)
    print(new_cow.report())
    manual_grow(new_cow)
    print(new_cow.report())

if __name__ == "__main__":
    main()
    
