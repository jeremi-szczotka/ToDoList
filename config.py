import os

class Config:
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:jerry@localhost/todo_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
