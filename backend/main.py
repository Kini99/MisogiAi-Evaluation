from typing import Union
from pymongo import MongoClient
from fastapi import FastAPI

app = FastAPI()
uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

db=client["fitness_coach"]
usersDb = db["users"]

# AUTHENTICATION

@app.post("/auth/register")
def user_registration(username:str, email:str, password:str):
    usersDb.insert({username, email, password})
    return {username, email, password}

@app.post("/auth/login")
def user_login(item_id: int, q: Union[str, None] = None):
    # usersDb.insertOne({username, email, password})
    return {"item_id": item_id, "q": q}

@app.post("/auth/user/{user_id}")
def get_user_profile(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# GET/POST/PUT/DELETE /workouts - Workout management
# GET/POST/PUT/DELETE /exercises - Exercise database
# GET/POST/PUT/DELETE /nutrition - Nutrition logging
# GET/POST/PUT/DELETE /progress - Progress tracking

# WORKOUT MANAGEMENT

