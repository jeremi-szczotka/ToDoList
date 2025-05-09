import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# DATABASE AND MODELS
db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    is_done = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# UNIT TEST CLASS
class TaskAppUnitTests(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        db.init_app(self.app)
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_user_and_task(self):
        with self.app.app_context():
            user = User(username="sample_user", password="123")
            db.session.add(user)
            db.session.commit()

            task = Task(content="Sample task", user_id=user.id)
            db.session.add(task)
            db.session.commit()

            self.assertEqual(User.query.count(), 1)
            self.assertEqual(Task.query.first().content, "Sample task")

    def test_duplicate_username_fails(self):
        with self.app.app_context():
            user1 = User(username="duplicate", password="123")
            db.session.add(user1)
            db.session.commit()

            user2 = User(username="duplicate", password="abc")
            db.session.add(user2)
            with self.assertRaises(Exception):
                db.session.commit()

    def test_delete_task(self):
        with self.app.app_context():
            user = User(username="delete_user", password="abc")
            db.session.add(user)
            db.session.commit()

            task = Task(content="Task to delete", user_id=user.id)
            db.session.add(task)
            db.session.commit()

            db.session.delete(task)
            db.session.commit()

            self.assertEqual(Task.query.count(), 0)

    def test_toggle_task_status(self):
        with self.app.app_context():
            user = User(username="status_user", password="pass")
            db.session.add(user)
            db.session.commit()

            task = Task(content="Toggle status task", user_id=user.id)
            db.session.add(task)
            db.session.commit()

            task.is_done = True
            db.session.commit()
            self.assertTrue(Task.query.first().is_done)

            task.is_done = False
            db.session.commit()
            self.assertFalse(Task.query.first().is_done)

    def test_task_without_user_fails(self):
        with self.app.app_context():
            task = Task(content="No user assigned", user_id=None)
            db.session.add(task)
            with self.assertRaises(Exception):
                db.session.commit()

if __name__ == "__main__":
    unittest.main()
