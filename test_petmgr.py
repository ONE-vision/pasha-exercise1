import pytest

from petmanager import PetManager
from modules.datamodel import Animal



@pytest.fixture()
def populated_petmanager():
    t=PetManager()
    for a in [ 
                    (1,True, "Name1", "dog"),
                    (2,False, "Name2", "dog"),
                    (3,True, "Name3", "cat"),
                    (4,False, "Name4", "cat"),
                    ]:
        t.add_animal(Animal(*a))
    return t

## General
def test_init():
    t=PetManager()
    assert type(t) == PetManager
    
### list_animals
    
def test_list_no_filters(populated_petmanager):
    l=populated_petmanager.list_animals()
    assert len(l)==4
    ids=[x.id for x in l]
    assert set(ids) == set([1,2,3,4])
    for a in l:
        assert type(a) == Animal
        
def test_list_empty():
    mgr=PetManager()
    l=mgr.list_animals()
    assert l==[]
    
### add_animal
    
def test_add_good_animal(populated_petmanager):
    a=Animal(10,True,"a10", "dog")
    populated_petmanager.add_animal(a) 
    l=populated_petmanager.list_animals() 
    assert len(l)==5
    assert l[4].name=="a10"
    assert sum([x.id==10 for x in l]) == 1
    
def test_add_dup_id(populated_petmanager):
    a=Animal(1,True, "asdf", "dog")
    with pytest.raises(Exception):
        assert populated_petmanager.add_animal(a) 
    
def test_add_bad_species(populated_petmanager):
    a=Animal(66,False,"asdf", "gyraffe")
    with pytest.raises(AssertionError):
        populated_petmanager.add_animal(a)
    
    
### get_animal

def test_get_existing_animal(populated_petmanager):
    id: int = 1
    name: str = "Name1"
    a1=populated_petmanager.get_animal(id, None)
    assert type(a1) == Animal 
    assert a1.id==id and a1.name == name
    a2=populated_petmanager.get_animal(None, name)
    assert a2==a1
    a3=populated_petmanager.get_animal(id, name)
    assert a3==a1
    assert populated_petmanager.get_animal(id,"BadName") == False
    assert populated_petmanager.get_animal(999,name) == False
    assert populated_petmanager.get_animal(999,"Badname") == False


### delete_animal    

def test_delete_animal(populated_petmanager):
    d: int = 1
    assert populated_petmanager.delete_animal(d) == True
    l=populated_petmanager.list_animals()
    assert len(l)==3
    ids=[x.id for x in l]
    assert set(ids) == set([2,3,4])