from crop_class import *

class Potato(Crop):
    """A potato crop"""

    def __init__(self):
        super().__init__(1,3,6)
        self._type = "Potato"

    def grow(self,light,water): #override
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status == "young" and warer > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()

def main():
    new_potato = Potato()
    print(new_potato.report())
    manual_grow(new_potato)
    print(new_potato.report())
    manual_grow(new_potato)
    print(new_potato.report())
if __name__ == "__main__":
    main()

    
