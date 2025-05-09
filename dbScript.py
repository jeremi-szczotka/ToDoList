import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dbScript import db, app  # jeśli chcesz od razu utworzyć tabele

DB_NAME = "todo_db"
DB_USER = "postgres"
DB_PASSWORD = "jerry"     # <-- Zmień na swoje hasło!
DB_HOST = "localhost"

# Połączenie z bazą główną, np. "postgres"
connection = psycopg2.connect(
    dbname="postgres",
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST
)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()

# Usuń starą bazę
cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME};")

# Utwórz nową bazę
cursor.execute(f"CREATE DATABASE {DB_NAME};")

cursor.close()
connection.close()

print("✅ Baza danych zresetowana.")

# Teraz utwórz tabele w nowej bazie
with app.app_context():
    db.create_all()
    print("✅ Tabele utworzone.")