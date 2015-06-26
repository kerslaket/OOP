from wheat_class import *
from potato_class import *
from cow_class import *
from sheep_class import *

def display_menu():
    print()
    print("What would you like to create")
    print()
    print("1. Potato")
    print("2. Wheat")
    print("3. Cow")
    print("4. Sheep")
    print()
    print("Please select an option from the above menu")

def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option Selected: "))
            if choice in (1,2,3,4):
                valid_option = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def create_crop():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_crop = Potato()
    if choice == 2:
        new_crop = Wheat()
    if choice == 3:
        new_crop = Cow("Bleep")
    if choice == 4:
        new_crop = Sheep("Shaun")
    return new_crop

def main():
    new_crop = create_crop()
    manage_crop(new_crop)

if __name__ == "__main__":
    main()
