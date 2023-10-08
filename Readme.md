This is A scalable rest API project 

## Installation
1. Clone the repository
2. Install the requirements to install the requirements run the following command
```bash
pip install -r requirements.txt
```
3. do alembic migration
```bash
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
```
4. run the server
```bash
python main.py
```

```
## Testing
1. you can go to the swagger documentation by going to the following url
```bash
http://localhost:8000/docs
```
 Features of the auction management system
1. User can register and login
2. After a login user will recieve a uuid as a token which will help in Authorization of the user 
3. after authentication user can get it's details and also change thier use name 
4. after each successive login user will get a uuid which will also help in getting data from redis db 
