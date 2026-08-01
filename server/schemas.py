from marshmallow import Schema, fields, validate

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, error="Name cannot be empty."))
    category = fields.Str(required=True, validate=validate.Length(min=1, error="Category cannot be empty."))
    equipment_needed = fields.Bool(required=True)

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(dump_only=True)
    exercise_id = fields.Int(dump_only=True)
    reps = fields.Int(allow_none=True, validate=validate.Range(min=1, error="Reps must be at least 1."))
    sets = fields.Int(allow_none=True, validate=validate.Range(min=1, error="Sets must be at least 1."))
    duration_seconds = fields.Int(allow_none=True, validate=validate.Range(min=0, error="Duration in seconds must be >= 0."))
    exercise = fields.Nested(ExerciseSchema, dump_only=True)

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True, validate=validate.Range(min=1, error="Duration must be at least 1 minute."))
    notes = fields.Str(allow_none=True)
    workout_exercises = fields.Nested(WorkoutExerciseSchema, many=True, dump_only=True)

class ExerciseDetailSchema(ExerciseSchema):
    workout_exercises = fields.Nested(WorkoutExerciseSchema, many=True, dump_only=True)

# Schema instances
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
exercise_detail_schema = ExerciseDetailSchema()

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()