FROM python:3.9

ADD requirements.txt
RUN pip -r requirements.txt 
ADD *.py modules
CMD ['uvicorn','server-fastapi:app']