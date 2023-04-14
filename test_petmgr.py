import pytest

from exercise1 import PetManager 

def test_init():
    t=PetManager()
    assert type(t) == PetManager
