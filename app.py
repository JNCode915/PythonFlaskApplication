from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#from flask_sqlalchemy import SQLAlchemy

from config.config import Config
from routes.Student_Routes import student_bp
from models.Student import db



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
       
    # Initialize database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(student_bp)

  

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug = True)