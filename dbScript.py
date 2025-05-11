import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from app import db, app 

DB_NAME = "todo_db"
DB_USER = "postgres"
DB_PASSWORD = "jerry"     
DB_HOST = "localhost"

# Connect with postgres
connection = psycopg2.connect(
    dbname="postgres",
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST
)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()

# Delete the database if it exists
cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME};")


cursor.execute(f"CREATE DATABASE {DB_NAME};")

cursor.close()
connection.close()

print("Database running")

#old dbScript.py
with app.app_context():
    db.create_all()
    print("Tables has been made.")