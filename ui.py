import logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('urllib3').setLevel(logging.WARNING)
import requests 

URL='http://localhost:8888/api/v1'


from modules.datamodel import Animal 

a=Animal(1,True,"asdf","asdf")

p=requests.post(URL+"/add",json=a.__dict__)
logging.info(p.text)

l=requests.get(URL+"/list")
res=l.json()
logging.debug(f"get: {res}")

"""d=requests.delete(URL+"/delete",json=id_to_delete)
logging.debug(f"delete: {res}")

s=requests.search(URL+"/search",json=id_to_search)
logging.debug(f"search: {res}")"""