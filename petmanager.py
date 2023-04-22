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

        existing_ids =list(map(lambda x: x.id, self.zoo))
        assert type(animal.id) == int, "ID not int" 
        assert type(animal.name) == str , "Name not string"
        assert "fuck" not in animal.name.lower() , "fucking animals not allowed"
        assert type(animal.gender_male) == bool ,"Gender not bool"
        if animal.id in existing_ids: 
            raise ValueError("Duplicate id")
        assert animal.species in ['cat', 'dog'], "only cats or dogs"


    def add_animal(self, animal: Animal):
        self._validate(animal)
        self.zoo.append(animal)

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
        Return True if success, false if not
        """
