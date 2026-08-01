from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint, UniqueConstraint

db = SQLAlchemy()

class Exercise(db.Model):
    __tablename__ = 'exercises'

    # Table Constraints
    __table_args__ = (
        UniqueConstraint('name', name='uq_exercise_name'),
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False, nullable=False)

    # Relationships
    workout_exercises = db.relationship(
        'WorkoutExercise',
        back_populates='exercise',
        cascade='all, delete-orphan'
    )

    # Model Validations
    @validates('name')
    def validate_name(self, key, value):
        if not value or not str(value).strip():
            raise ValueError("Exercise name cannot be empty.")
        return str(value).strip()


class Workout(db.Model):
    __tablename__ = 'workouts'

    # Table Constraints
    __table_args__ = (
        CheckConstraint('duration_minutes > 0', name='check_positive_workout_duration'),
    )

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    # Relationships
    workout_exercises = db.relationship(
        'WorkoutExercise',
        back_populates='workout',
        cascade='all, delete-orphan'
    )

    # Model Validations
    @validates('duration_minutes')
    def validate_duration(self, key, value):
        if value is None or value <= 0:
            raise ValueError("Workout duration must be greater than 0 minutes.")
        return value


class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'

    # Table Constraints
    __table_args__ = (
        CheckConstraint('reps IS NULL OR reps > 0', name='check_positive_reps'),
        CheckConstraint('sets IS NULL OR sets > 0', name='check_positive_sets'),
        CheckConstraint('duration_seconds IS NULL OR duration_seconds >= 0', name='check_non_negative_duration_seconds'),
    )

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    # Relationships
    workout = db.relationship('Workout', back_populates='workout_exercises')
    exercise = db.relationship('Exercise', back_populates='workout_exercises')
