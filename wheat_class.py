from crop_class import *

class Wheat(Crop):
    """A Wheat Crop"""

    def __init__(self):
        super().__init__(1,3,6)
        self._type = "Wheat"

    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling":
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young":
                self._growth += self._growth_rate * 1.25
            elif self._status == "Old":
                self._growth += self._growth_rate / 2
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()

def main():
    new_wheat = Wheat()
    print(new_wheat.report())
    manual_grow(new_wheat)
    print(new_wheat.report())
    manual_grow(new_wheat)
    print(new_wheat.report())

if __name__ == "__main__":
    main()
