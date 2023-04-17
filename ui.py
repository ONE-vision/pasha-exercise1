from petmanager import PetManager
from modules.datamodel import Animal, Result
class Commands:
    add = 1
    search = 2
    list = 3
    delete = 4
    exit = 5
while True:
    c = input("Enter command: ")
    try:
        command = int(c)
    except ValueError:
        print("Invalid command")
        command = 0
    if command == Commands.add:
        id = int(input("ID: "))
        name = input("NAME: ")
        g = input("Gender (M/F): ")
        gender_male = g == "M"
        species = input("Species: ")
        animal = Animal(id, gender_male, name, species)
        print(animal)
        result = PetManager.add_animal(animal)
        if result.success:
            print("OK")
        else:
            print(f"Error: {result.message}")