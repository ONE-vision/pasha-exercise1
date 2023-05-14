from fastapi import FastAPI

from modules.datamodel import Animal
from petmanager import PetManager

app = FastAPI()
app.mgr=PetManager()

@app.get("/api/v1/list")
async def list():
    return app.mgr.list_animals()

@app.post('/api/v1/add')
async def create(animal: Animal):
    return app.mgr.add_animal(animal)

# To run:
#pip install uvicorn
#uvicorn server-fastapi:app

# http://localhost:8000/docs 
# https://fastapi.tiangolo.com/