from modules.datamodel import Animal, Result
from typing import List, Tuple


class PetManager:
    def __init__(self) -> None:
        self.zoo = []

    def _validate(self, animal: Animal) -> bool:
        """check if we can accept this animal.
        Checks:
            1. species is "dog" or "cat"
            2. id is unique
        """
        existing_ids = set(map(lambda x: x.id, self.zoo))
        if animal.id in existing_ids:
            return False
        return True

    def add_animal(self, animal: Animal) -> bool:
        if  self._validate(animal):
            self.zoo.append(animal)
            return True
        return False

    def list_animals(self, species: str = None, gender: bool = None) -> List[Animal]:
        """
        return list of animal objects, if "species"or "gender" are specified - return only
        animals with specified parameters. If none found = return an empty array.
        """
        animals=list(filter(lambda x: x.species==species or species == None, self.zoo))
        
        result=list(filter(lambda x: x.gender_male==gender or gender == None, animals))

        return result
        # result = []
        # print (self.zoo)
        # Your code here
        # return result

    def get_animal(self, id: int = None, name: str = None) -> Animal:
        if id != None:
            result=list(filter(lambda x: x.id == id, self.zoo))
            
    
        if name != None:
            result=list(filter(lambda x: x.name == name, self.zoo))

            return result

        """for i in self.zoo:   
            if i == id:
                print("YES")
            else:
                print("NO")"""
        
        """
        Return requested animal and search result.

        If id is passed - return the animal with given id
        if id and name are passed - return the animal with given id and given name, if exists
        if only name is given - return the only animal with this name. If more then 1 animals
        have this name - fail.
        The method should return object of type Animal if search was successful or None.
        """
        # return result

    def delete_animal(self, deleted: int) -> Result:
        self.zoo=list(filter(lambda x: x.id != deleted, self.zoo))
        return self.zoo
        """
        Delete from the list the animal with given id, if found.
        Return Result object with success=True if the animal deleted, else with success=False
        """


class Commands:
    add = 1
    search = 2
    list = 3
    delete = 4
    exit = 5


if __name__ == "__main__":
    print("Starting Pet Manager")
    mgr = PetManager()

    menu = """
    1) add animal
    2) search for animal
    3) lsit all animals
    4) delete an animal
    5) exit
    """

    w = """Welcome to Pet manager! Please, choose command:
    1 - add animal;
    2 - search for an animal;
    3 - list all animals;
    4 - delete an animal;
    5 - exit
    Enjoy!"""

    print(w)

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
            result = mgr.add_animal(animal)
            if result.success:
                print("OK")
            else:
                print(f"Error: {result.message}")

    if command == Commands.list:
        # al=mgr.list_animals(species != None) - Trying to insert values to method_list, but it doesn't work now.
        g=input("Gender (M/F, empty for all)")# .strip()
        # g M, F, ""
        #True = M, False = F, None = ""
        #gm= ....... 
        print(f"DEBUG: gm={gm}")
        sp=input("Species (empty for all): ")
        sp=sp if sp != "" else None
        print(f"DEBUG: sp={sp}")
        
        
        al=mgr.list_animals(gender=gm, species=sp)
        print(al)
    if command == Commands.exit:
        print("Goodbye!")
        quit()
    # Other commands here
    if command == Commands.delete:
        print ("Input ID:")
        id_to_delete=int(input())
        de=mgr.delete_animal(id_to_delete)
        print(de)

    if command == Commands.search:
        id_to_search=int(input("Inpui ID: "))
        name_to_search=str(input("Input Name: "))
        se=mgr.get_animal(id_to_search, name_to_search)
        print(se)