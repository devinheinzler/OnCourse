from flask import Flask
from flask_login import LoginManager
from database import db
import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import User

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(config.get_config())

# Initialize database
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Initialize Flask-Login
login_manager = LoginManager(app)

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import blueprints and register them
from routes import user_routes, category_routes, course_routes, saved_course_routes

app.register_blueprint(user_routes)
app.register_blueprint(category_routes)
app.register_blueprint(course_routes)
app.register_blueprint(saved_course_routes)

if __name__ == '__main__':
    app.run(debug=True)