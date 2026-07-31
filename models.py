from sqlalchemy import CheckConstraint
from sqlalchemy.orm import validates
from datetime import date

db =SQLAlchemy()

class Exercise(db.Model):
    __tablename__='exercises'

    id = db.Column(db.Integer ,primary_key=True)
    name =db.Column(db.String ,nullable = False)
    category= db.column(db.String ,nullable=False)
    equipment_needed =db.Column(db.Boolean,default=False,nullable=False)

    workout_exerices =db.relationship('WorkoutExercise',back_populates='exercise')
