import os

class Config:
    SECRET_KEY = 'temporary_test_key'
    
    # This tells your app to use a simple local file for the database
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False