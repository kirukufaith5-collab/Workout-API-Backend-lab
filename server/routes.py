from flask import Blueprint, request, jsonify, make_response
from marshmallow import ValidationError
from models import db, Exercise, Workout, WorkoutExercise
from schemas import (
    exercise_schema,
    exercises_schema,
    exercise_detail_schema,
    workout_schema,
    workouts_schema,
    workout_exercise_schema,
)

# Create a Blueprint for API routes
api_bp = Blueprint('api', __name__)

# WORKOUT ROUTES
@api_bp.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return make_response(workouts_schema.dump(workouts), 200)

@api_bp.route('/workouts/<int:id>', methods=['GET'])
def get_workout_by_id(id):
    workout = db.session.get(Workout, id)
    if not workout:
        return make_response(jsonify({'error': 'Workout not found'}), 404)
    return make_response(workout_schema.dump(workout), 200)

@api_bp.route('/workouts', methods=['POST'])
def create_workout():
    json_data = request.get_json()
    try:
        data = workout_schema.load(json_data)
    except ValidationError as err:
        return make_response(jsonify({'errors': err.messages}), 400)

    try:
        new_workout = Workout(
            date=data['date'],
            duration_minutes=data['duration_minutes'],
            notes=data.get('notes')
        )
        db.session.add(new_workout)
        db.session.commit()
        return make_response(workout_schema.dump(new_workout), 201)
    except ValueError as err:
        db.session.rollback()
        return make_response(jsonify({'error': str(err)}), 400)

@api_bp.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = db.session.get(Workout, id)
    if not workout:
        return make_response(jsonify({'error': 'Workout not found'}), 404)
    
    db.session.delete(workout)
    db.session.commit()
    return make_response(jsonify({'message': f'Workout {id} deleted successfully.'}), 200)


# EXERCISE ROUTES
@api_bp.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    return make_response(exercises_schema.dump(exercises), 200)

@api_bp.route('/exercises/<int:id>', methods=['GET'])
def get_exercise_by_id(id):
    exercise = db.session.get(Exercise, id)
    if not exercise:
        return make_response(jsonify({'error': 'Exercise not found'}), 404)
    return make_response(exercise_detail_schema.dump(exercise), 200)

@api_bp.route('/exercises', methods=['POST'])
def create_exercise():
    json_data = request.get_json()
    try:
        data = exercise_schema.load(json_data)
    except ValidationError as err:
        return make_response(jsonify({'errors': err.messages}), 400)

    try:
        new_exercise = Exercise(
            name=data['name'],
            category=data['category'],
            equipment_needed=data['equipment_needed']
        )
        db.session.add(new_exercise)
        db.session.commit()
        return make_response(exercise_schema.dump(new_exercise), 201)
    except Exception as err:
        db.session.rollback()
        return make_response(jsonify({'error': str(err)}), 400)

@api_bp.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = db.session.get(Exercise, id)
    if not exercise:
        return make_response(jsonify({'error': 'Exercise not found'}), 404)
    
    db.session.delete(exercise)
    db.session.commit()
    return make_response(jsonify({'message': f'Exercise {id} deleted successfully.'}), 200)


# JOIN TABLE ROUTE
@api_bp.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    workout = db.session.get(Workout, workout_id)
    if not workout:
        return make_response(jsonify({'error': 'Workout not found'}), 404)
    
    exercise = db.session.get(Exercise, exercise_id)
    if not exercise:
        return make_response(jsonify({'error': 'Exercise not found'}), 404)

    json_data = request.get_json() or {}
    try:
        data = workout_exercise_schema.load(json_data)
    except ValidationError as err:
        return make_response(jsonify({'errors': err.messages}), 400)

    try:
        workout_exercise = WorkoutExercise(
            workout_id=workout.id,
            exercise_id=exercise.id,
            reps=data.get('reps'),
            sets=data.get('sets'),
            duration_seconds=data.get('duration_seconds')
        )
        db.session.add(workout_exercise)
        db.session.commit()
        return make_response(workout_exercise_schema.dump(workout_exercise), 201)
    except Exception as err:
        db.session.rollback()
        return make_response(jsonify({'error': str(err)}), 400)