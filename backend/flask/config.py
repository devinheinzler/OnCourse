from flask import Flask
from database import db
from routes import user_routes, category_routes, course_routes, saved_course_routes
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(user_routes)
app.register_blueprint(category_routes)
app.register_blueprint(course_routes)
app.register_blueprint(saved_course_routes)

if __name__ == '__main__':
    app.run(debug=True)

class Config:
    DEBUG = True  # Set this to False for production
    SECRET_KEY = 'your_secret_key_here'  # Replace with a strong secret key

    # Database configuration for SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///courses.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False






