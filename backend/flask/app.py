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

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)