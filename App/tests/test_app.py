import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import *
from App.controllers import *


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class StudentUnitTests(unittest.TestCase):

    def test_new_student(self):
        newStudent = Student("816011111", "Dale", "Barbara")
        assert (newStudent.username, newStudent.fname, newStudent.lname) == ("816011111", "Dale", "Barbara")

    def test_student_toDict(self):
        newStudent = Student("816011111", "Dale", "Barbara")
        student_json = newStudent.toDict()
        self.assertDictEqual(student_json, {"Student ID":"816011111", "First Name":"Dale", "Last Name":"Barbara", "Karma Score":"0"})
    
    def updateKarmaScore(self):
        newStudent = Student("816011111", "Dale", "Barbara")
        newStaff = Staff("RobertJackson", "robby123", "robertjackson@mail.com", "Robert", "Jackson")
        newReview = newStaff.createReview("816011111", "This student continues to show great potential", "positive")
        newReview.upvote()
        newStudent.updateKarmaScore()
        assert(newStudent.karmaScore == 1)

class StaffUnitTests(unittest.TestCase):

    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        newStaff = Staff("bob", "bobpass", "bob@mail.com", "Bobby", "Smith")
        assert newStaff.password != password

    def test_check_password(self):
        password = "mypass"
        newStaff = Staff("bob", password, "bob@mail.com", "Bobby", "Smith")
        assert newStaff.check_password(password) 

    def test_create_review(self):
        newStaff = Staff("bob", password, "bob@mail.com", "Bobby", "Smith")
        newReview = newStaff.createReview("816011111", "This student continues to show great potential", "positive")
        assert (newReview.studentID, newReview.description, newReview.reviewType) == ("816011111", "This student continues to show great potential", "positive")

'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()


def test_authenticate():
    user = create_user("bob", "bobpass")
    assert login("bob", "bobpass") != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "bobpass")
        assert user.username == "rick"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"id":1, "username":"bob"}, {"id":2, "username":"rick"}], users_json)

    # Tests data changes in the database
    def test_update_user(self):
        update_user(1, "ronnie")
        user = get_user(1)
        assert user.username == "ronnie"
