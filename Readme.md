## This is A Scalable rest API project 

## Installation
1. Clone the repository
2. create a virtual environment
```bash
python -m venv venv
```
3. Install the requirements to install the requirements run the following command
```bash
pip install -r requirements.txt
```
4. do alembic migration for the postgres db 
```bash
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
```
IMP:- don't forget to change the postgres db url in the alembic.ini file
5. run the server
```bash
python main.py
```


## Testing
1. you can go to the swagger documentation by going to the following url
```bash
http://localhost:8000/docs
```
1. you can also test the api by using the postman collection by using the file by the name of Scalable.postman_collection.json


## Features of the Scalable rest API structure
1. User can register and login
2. After a login user will recieve a uuid as a token which will help in Authorization of the user 
3. after authentication user can get it's details and also change thier use name 
4. after each successive login user will get a uuid which will also help in getting data from redis db 
5. users can also get the data from the redis db 