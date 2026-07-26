import os

class Config:
    SECRET_KEY = 'temporary_test_key'
    
    # Using the new dedicated user and password
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flix_user:Flix12345@127.0.0.1:3306/flixrec_db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False