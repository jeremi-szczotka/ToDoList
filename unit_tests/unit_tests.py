import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db, User, Task
from flask import url_for


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # testowa baza
        app.config['TESTING'] = True
        self.app = app.test_client()
        
    def tearDown(self):
       pass

    def test_create_user(self):
        with app.app_context():
            user = User(username='test', password='hashedpw')
            db.session.add(user)
            db.session.commit()
            self.assertEqual(User.query.count(), 1)

    def test_add_task(self):
        with app.app_context():
            user = User(username='test', password='pw')
            db.session.add(user)
            db.session.commit()
            task = Task(content='Zrób coś', user_id=user.id)
            db.session.add(task)
            db.session.commit()
            self.assertEqual(Task.query.first().content, 'Zrób coś')

if __name__ == '__main__':
    unittest.main()
