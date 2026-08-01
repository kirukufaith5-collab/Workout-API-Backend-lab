#!/usr/bin/env python3

from datetime import date
from app import app
from models import db, Exercise, Workout, WorkoutExercise

with app.app_context():
    print("Clearing database...")
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    print("Creating exercises...")
    ex1 = Exercise(name="Push-ups", category="Calisthenics", equipment_needed=False)
    ex2 = Exercise(name="Barbell Back Squat", category="Strength", equipment_needed=True)
    ex3 = Exercise(name="Plank", category="Core", equipment_needed=False)

    db.session.add_all([ex1, ex2, ex3])
    db.session.commit()

    print("Creating workouts...")
    w1 = Workout(date=date(2026, 8, 1), duration_minutes=45, notes="Leg day and core")
    w2 = Workout(date=date(2026, 8, 2), duration_minutes=30, notes="Bodyweight express workout")

    db.session.add_all([w1, w2])
    db.session.commit()

    print("Associating exercises with workouts...")
    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=ex2.id, reps=8, sets=4)
    we2 = WorkoutExercise(workout_id=w1.id, exercise_id=ex3.id, duration_seconds=60, sets=3)
    we3 = WorkoutExercise(workout_id=w2.id, exercise_id=ex1.id, reps=20, sets=3)

    db.session.add_all([we1, we2, we3])
    db.session.commit()

    print("Seeding completed successfully!")