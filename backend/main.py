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
    usersDb.insert_one({username, email, password})
    return {username, email, password}

@app.post("/auth/login")
def user_login(username:str, email:str, password:str):
    user = usersDb.find_one({username, email, password})
    if user:
        return {"Login successful!"}
    else:
        return {"User does not exist!"}

@app.get("/auth/user/{user_id}")
def get_user_profile(user_id:str):
    user = usersDb.find_one({user_id})
    if user:
        return user
    else:
        return {"User does not exist!"}

# WORKOUT MANAGEMENT

workoutsDb = db["workouts"]

@app.get("/workouts")
def get_workouts():
    workouts = workoutsDb.find({})
    return workouts

@app.post("/workouts")
def create_workout(plan_name:str, difficulty_level:str, duration:str, target_muscle_groups:str, exercises_list:str):
    workoutsDb.insert_one({plan_name, difficulty_level, duration, target_muscle_groups, exercises_list})
    return {plan_name, difficulty_level, duration, target_muscle_groups, exercises_list}

@app.put("/workouts/{id}")
def update_workoutid(id:str, plan_name:str, difficulty_level:str, duration:str, target_muscle_groups:str, exercises_list:str):
    workoutsDb.replace_one({plan_name: plan_name},{plan_name, difficulty_level, duration, target_muscle_groups, exercises_list})
    return

@app.delete("/workouts/{id}")
def update_workoutid(id:str):
    workoutsDb.delete_one({id: id})
    return

# EXERCISES DATABASE

exercisesDb = db["exercises"]

@app.get("/exercises")
def get_exercises():
    exercises = exercisesDb.find({})
    return exercises

@app.post("/exercises")
def create_workout(exercise_name:str, category:str, equipment_needed:str, difficulty:str, instructions:str, target_muscles:str):
    exercisesDb.insert_one({exercise_name, category, equipment_needed, difficulty, instructions, target_muscles})
    return {exercise_name, category, equipment_needed, difficulty, instructions, target_muscles}

@app.put("/exercises/{id}")
def update_workoutid(id:str, exercise_name:str, category:str, equipment_needed:str, difficulty:str, instructions:str, target_muscles:str):
    exercisesDb.replace_one({exercise_name: exercise_name},{exercise_name, category, equipment_needed, difficulty, instructions, target_muscles})
    return

@app.delete("/exercises/{id}")
def update_workoutid(id:str):
    exercisesDb.delete_one({id: id})
    return

# PROGRESS TRACKING

progressDb = db["progress"]

@app.get("/progress/{user_id}")
def get_progress(user_id:str):
    progress = progressDb.find({user_id})
    return progress

@app.post("/progress/{user_id}")
def create_workout(user_id:str, workout_id:str, date:str, exercises_completed:str, sets:str, reps:str, weights:str, duration:str, calories_burned:str):
    progressDb.insert_one({user_id, workout_id, date, exercises_completed, sets, reps, weights, duration, calories_burned})
    return {user_id, workout_id, date, exercises_completed, sets, reps, weights, duration, calories_burned}

@app.put("/progress/{id}")
def update_workoutid(id:str, user_id:str, workout_id:str, date:str, exercises_completed:str, sets:str, reps:str, weights:str, duration:str, calories_burned:str):
    progressDb.replace_one({id: id},{user_id, workout_id, date, exercises_completed, sets, reps, weights, duration, calories_burned})
    return

@app.delete("/progress/{id}")
def update_workoutid(id:str):
    progressDb.delete_one({id: id})
    return

# NUTRITION LOGGING

nutritionDb = db["nutrition"]

@app.get("/nutrition/{user_id}")
def get_nutrition(user_id:str):
    nutrition = nutritionDb.find({user_id})
    return nutrition

@app.post("/nutrition/{user_id}")
def create_workout(user_id:str, date:str, meals:str, calories:str, macronutrients:str):
    nutritionDb.insert_one({user_id, date, meals, calories, macronutrients})
    return {user_id, date, meals, calories, macronutrients}

@app.put("/nutrition/{id}")
def update_workoutid(id:str, user_id:str, date:str, meals:str, calories:str, macronutrients:str):
    nutritionDb.replace_one({id: id},{user_id, date, meals, calories, macronutrients})
    return

@app.delete("/nutrition/{id}")
def update_workoutid(id:str):
    nutritionDb.delete_one({id: id})
    return

client.close()