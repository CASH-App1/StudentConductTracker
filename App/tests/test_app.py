import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import *
from App.controllers import *
    create_user,
    get_all_users_json,
    login,
    get_user,
    get_user_by_username,
    update_user
)


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''

class ReviewUnitTests(unittest.TestCase):

    def test_new_review(self):
        #newStaff = Staff("bob", "bobpass", "bob@mail.com", "Bobby", "Smith")
        #newReview = newStaff.createReview("816011111", "1", "This student continues to show great potential", "positive")
        newReview = Review("816011111", "1", "This student continues to show great potential", "positive")
        assert (newReview.studentID, newReview.staffID, newReview.description, newReview.reviewType) == ("816011111", "1", "This student continues to show great potential", "positive")

    def test_review_toDict(self):
        newReview = Review("816011111", "1", "This student continues to show great potential", "positive")
        review_json = newReview.toDict()
        self.assertDictEqual(review_json, {"Review ID": "01", "Student ID": "816011111", "Staff ID": "1", "Description": "This student continues to show great potential", "Date": datetime.utcnow, "Upvote": "0", "Downvote": "0", "Review Type": "positive"})

    def test_upvote(self):
        newStudent = Student("816011111", "Dale", "Barbara")
        newStaff = Staff("RobertJackson", "robby123", "robertjackson@mail.com", "Robert", "Jackson")
        newReview = newStaff.createReview("816011111", "This student continues to show great potential", "positive")
        newReview.upvote()
        assert newReview.upvote == 1

    def test_upvote(self):
        newStudent = Student("816011111", "Dale", "Barbara")
        newStaff = Staff("RobertJackson", "robby123", "robertjackson@mail.com", "Robert", "Jackson")
        newReview = newStaff.createReview("816011111", "This student continues to show great potential", "positive")
        newReview.downvote()
        assert newReview.downvote == 1


class StaffUnitTests(unittest.TestCase):

    def test_new_staff(self):
        newStaff = Staff("bob", "bobpass", "bob@mail.com", "Bobby", "Smith")
        assert (newStaff.username, newStaff.email, newStaff.firstName, newStaff.lastName) == ("bob", "bob@mail.com", "Bobby", "Smith")

    # pure function no side effects or integrations called
    def test_staff_toDict(self):
        newStaff = Staff("bob", "bobpass", "bob@mail.com", "Bobby", "Smith")
        staff_json = newStaff.toDict()
        self.assertDictEqual(staff_json, {"Staff ID": "1", "First Name": "Bobby", "Last Name": "Smith", "Email": "bob@mail.com", "Username": "bob"})
    

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
