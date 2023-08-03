# models.py
from .database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .helpers import hash_password


#User model
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


#Category model
class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(100), nullable=False)


#Course model
class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructor = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)
    price = db.Column(db.Float)
    rating = db.Column(db.Float)


#Saved Course model
class SavedCourse(db.Model):
    saved_course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)
    saved_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
