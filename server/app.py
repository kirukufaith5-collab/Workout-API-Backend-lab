from flask import Flask
from flask_migrate import Migrate

from models import db
from routes import api_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

# Register Blueprint
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(port=5555, debug=True)