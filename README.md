# Workout-API-Backend-lab

A RESTful backend API built for personal trainers to create, manage, and track workouts and exercises. Built using Python, Flask, Flask-SQLAlchemy, Flask-Migrate, and Marshmallow.

---

## Features

- **Workouts Management**: Create, delete, and list workouts.
- **Exercises Management**: Create, delete, and list reusable exercises.
- **Workout Exercises**: Assign exercises to specific workouts with sets, reps, and duration metrics.
- **Multi-Level Validation**:
  - **Database Constraints**: Table-level check and unique constraints.
  - **Model Validations**: `@validates` hooks in SQLAlchemy models.
  - **Schema Validations**: Strict input payload validation using Marshmallow.

---

## Data Models & Relationships

- **Workout**: Has many `WorkoutExercises`. Has many `Exercises` through `WorkoutExercises`.
- **Exercise**: Has many `WorkoutExercises`. Has many `Workouts` through `WorkoutExercises`.
- **WorkoutExercise**: Belongs to a `Workout` and an `Exercise` (Join Table).

---

## Project Structure

```text
workout-tracker-api/
├── Pipfile
├── Pipfile.lock
├── README.md
├── .gitignore
└── server/
    ├── app.py
    ├── models.py
    └── seed.py