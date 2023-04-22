from petmanager import PetManager
from modules.datamodel import Animal




class Commands:
    add = 1
    search = 2
    list = 3
    delete = 4
    exit = 5

mgr=PetManager()

while True:
    c = input("Enter command: ")
    try:
        command = int(c)
    except ValueError:
        print("Invalid command")
        command = 0
    if command == Commands.add:
        try:
            id = int(input("ID: "))
        except ValueError as e:
            print("non-integer id")
        else:
        
            name = input("NAME: ")
            g = input("Gender (M/F): ")
            gender_male = g == "M"
            species = input("Species: ")
            animal = Animal(id, gender_male, name, species)
            print(animal)
            try:
                result = mgr.add_animal(animal)
            except Exception as e:
                print(f"Error: {e}")