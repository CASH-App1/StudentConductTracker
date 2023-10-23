import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User
from App.controllers import (
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
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = User("bob", "bobpass")
        assert user.username == "bob"

    # pure function no side effects or integrations called
    def test_get_json(self):
        user = User("bob", "bobpass")
        user_json = user.get_json()
        self.assertDictEqual(user_json, {"id":None, "username":"bob"})
    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob", password)
        assert user.password != password

    def test_check_password(self):
        password = "mypass"
        user = User("bob", password)
        assert user.check_password(password)

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


    def test_authenticate(self):
        created_staff = create_staff("bob", "bobpass", "bob@mail.com", "Bobby", "Smith")
        access_token = jwt_authenticate("bob", "bobpass")
        assert access_token != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_staff(self):
        created_staff = create_staff("rick", "rickypass123", "rick1@mail.com", "Ricky", "Martin")
        retrieved_staff = get_staff(created_staff.staffID)
        assert retrieved_staff.username == "rick"
        assert retrieved_staff.email == "rick1@mail.com"
        assert retrieved_staff.firstName == "Ricky"
        assert retrieved_staff.lastName == "Martin"

    def test_get_all_staff_json(self):
        staff1 = create_staff("sid", "sidpass", "sid@mail.com", "Sidique", "Brenson")
        staff2 = create_staff("ross", "rosspass", "ross@mail.com", "Ross", "Sanchez")
        
        staff_json = get_all_staff_json()

        expected_json = [
            {
                "Staff ID": staff1.staffID,
                "First Name": "Bobby",
                "Last Name": "Smith",
                "Email": "bob@mail.com",
                "Username": "bob"
            },
            {
                "Staff ID": staff2.staffID,
                "First Name": "Rick",
                "Last Name": "Sanchez",
                "Email": "rick@mail.com",
                "Username": "rick"
            }
        ]
        assert staff_json == expected_json

    def test_password_reset(self):
        staff = create_staff("bob", "bobpass", "bob@mail.com", "Bobby", "Smith")
        new_password = "bob1234pass"
        update_password(1, new_password)
        updated_staff = get_staff(1)
        assert updated_staff.password == new_password

    def test_log_review(self):
        staff = create_staff("dev", "evolve123", "dev1@mail.com", "Devon", "Jones")
        student = add_student("816011112", "Jess", "Smith")
        review = "This student continues to show great potential"
        review_type = "positive"
        new_review = log_review(staff.staffID, student.studentID, review, review_type)
        logged_review = get_review(new_review.reviewID)

        assert logged_review.staffID == staff.staffID
        assert logged_review.studentID == student.studentID
        assert logged_review.description == review
        assert logged_review.reviewType == review_type

    def test_view_student(self):
        staff = create_staff("bob", "bobpass", "bob@mail.com", "Bobby", "Smith")
        new_student = add_student("816012122", "Alice", "Smith")
        student = get_student("816012122")

        assert student.studentID == "816012122"
        assert student.firstName == "Alice"
        assert student.lastName == "Smith"
    
    def test_view_student_review(self):
        staff = create_staff("Dean", "deanpass", "dean@example.com", "Dean", "Doe")
        new_review = log_review(staff.staffID, "816011112", "This student is doing well", "positive")
        review = get_review(new_review.reviewID)
        
        assert review.staffID == staff.staffID
        assert review.studentID == "816011112"
        assert review.review == "This student is doing well"
        assert review.reviewType == "positive"
        
    def test_update_student(self):
        update_student("816011112", "Jessica", "Colten")
        updated_student = get_user(816011112)
        assert updated_student.firstName == "Jessica"
        assert updated_student.lastName == "Colten"

