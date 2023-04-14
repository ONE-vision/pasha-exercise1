import pytest

from exercise1 import PetManager
from modules.datamodel import Animal

def test_init():
    t=PetManager()
    assert type(t) == PetManager

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

def test_list_no_filters(populated_petmanager):
    l=populated_petmanager.list_animals()
    assert len(l)==4
    ids=[x.id for x in l]
    assert set(ids) == set([1,2,3,4])
    for a in l:
        assert type(a) == Animal