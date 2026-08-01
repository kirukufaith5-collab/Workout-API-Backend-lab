from sqlalchemy import CheckConstraint
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint ,UniqueConstraint
from datetime import date

db =SQLAlchemy()
#Exercise model
class Exercise(db.Model):
    __tablename__='exercises'

    id = db.Column(db.Integer ,primary_key=True)
    name =db.Column(db.String ,nullable = False)
    category= db.column(db.String ,nullable=False)
    equipment_needed =db.Column(db.Boolean,default=False,nullable=False)

   # Relationships
workout_exerices =db.relationship('WorkoutExercise',back_populates='exercise')
workouts=db.relationship('Workout', secondary='workout_exercises'back_populates='exercises',viewonly =True)
#Database level Table Constraints (>1Validation)
 UniqueConstraint('name',name ='uq_exercise')

