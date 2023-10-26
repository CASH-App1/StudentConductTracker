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
        newStudent = Student(816011111, "Dale", "Barbara")
        assert (newStudent.studentID, newStudent.fname, newStudent.lname) == (816011111, "Dale", "Barbara")

    def test_student_toDict(self):
        newStudent = Student(816011111, "Dale", "Barbara")
        #student_json = newStudent.toDict()
        self.assertDictEqual(newStudent.toDict(), {"Student ID":816011111, "First Name":"Dale", "Last Name":"Barbara", "Karma Score":0})
    

class StaffUnitTests(unittest.TestCase):

    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        newStaff = StaffMember("bob", "bobpass", "bob@mail.com", "Bobby", "Smith")
        assert newStaff.password != password

    def test_check_password(self):
        password = "mypass"

        newStaff = StaffMember("bob", password, "bob@mail.com", "Bobby", "Smith")
        assert newStaff.check_password(password) 

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
        staff = create_staff("rick", "rickypass123", "rick1@mail.com", "Ricky", "Martin")
        retrieved_staff = get_staff(staff.staffID)
        self.assertEqual(retrieved_staff.username, "rick")
        self.assertEqual(retrieved_staff.email, "rick1@mail.com")
        self.assertEqual(retrieved_staff.firstName, "Ricky")
        self.assertEqual(retrieved_staff.lastName, "Martin")


    def test_get_all_staff_json(self):
        staff1 = create_staff("oli", "olipass", "oli.brenson@mail.com", "Oliver", "Brenson")
        staff2 = create_staff("ross", "rosspass", "ross12@mail.com", "Ross", "Sanchez")
        
        staff_json = get_all_staff_json()

        expected_json = [
            {
                "Staff ID": staff1.staffID,
                "First Name": "Oliver",
                "Last Name": "Brenson",
                "Email": "oli.brenson@mail.com",
                "Username": "oli"
            },
            {
                "Staff ID": staff2.staffID,
                "First Name": "Ross",
                "Last Name": "Sanchez",
                "Email": "ross12@mail.com",
                "Username": "ross"
            }
        ]
        assert staff_json == expected_json

    def test_password_reset(self):
        staff = create_staff("bob", "bobpass", "bob@mail.com", "Bobby", "Smith")
        new_password = "bob1234pass"
        update_password(staff.staffID, new_password)
        updated_staff = get_staff(staff.staffID)
        assert updated_staff.password == new_password

    def test_log_review(self):
        staff = create_staff("dev", "evolve123", "dev1@mail.com", "Devon", "Jones")
        student = add_student("816011112", "Jess", "Smith")
        description = "This student continues to show great potential"
        review_type = "positive"
        new_review = log_review(staff.staffID, student.studentID, description, review_type)
        logged_review = get_review(new_review.reviewID)

        self.assertEqual(logged_review.staffID, staff.staffID)
        self.assertEqual(logged_review.studentID, student.studentID)
        self.assertEqual(logged_review.description, description)
        self.assertEqual(logged_review.reviewType, review_type)

    def test_view_student(self):
        staff = create_staff("Murphy", "sun$et@5", "e.murphy@mail.com", "Eric", "Murphy")
        new_student = add_student("816012122", "Alice", "Denver")
        student = get_student(new_student.studentID)

        self.assertEqual(student.studentID, "816012122")
        self.assertEqual(student.firstName, "Alice")
        self.assertEqual(student.lastName, "Denver")

    def test_view_student_review(self):
        staff = create_staff("Dean", "deanPizza", "dean@mail.com", "Dean", "Doe")
        student = add_student("816011113", "Sean", "Mendez")
        new_review = log_review(staff.staffID, student.studentID, "This student is doing well", "positive")
        review = get_review(new_review.reviewID)
        retrieved_student = get_student(student.studentID) 

        self.assertEqual(review.staffID, staff.staffID)
        self.assertEqual(review.studentID, student.studentID)
        self.assertEqual(review.review, "This student is doing well")
        self.assertEqual(review.reviewType, "positive")

        self.assertEqual(retrieved_student.studentID, "816011113")
        self.assertEqual(retrieved_student.firstName, "Sean")
        self.assertEqual(retrieved_student.lastName, "Mendez")
  
    def test_update_student(self):
        updated_student = update_student("816011112", "Jessica", "Colten")
        retrieved_student = get_student(updated_student.studentID)

        self.assertEqual(retrieved_student.firstName, "Jessica")
        self.assertEqual(retrieved_student.lastName, "Colten")

    def test_upvote(self):
        staff = create_staff("harry", "wolfawoo*&*","harry.persad@yahoo.com", "Harry", "Persad")
        student= add_student("816030888", "Pablo", "Esco")
        description = "This student is an excellent student and shows leadership skills"
        review_type = "positive"
        new_review = log_review(staff.staffID, student.studentID, description, review_type)
        upvoted_review = upvote_review(new_review.reviewID);
        logged_review = get_review(new_review.reviewID)

        self.assertEqual(upvoted_review, "True")
        self.assertEqual(logged_review.upvote, 1)
        
    def test_downvote(self):
        staff = create_staff("Paul", "paullita","paulDeDan@yahoo.com", "Paul", "Smith")
        student= add_student("816030988", "Susie", "Green")
        description = "This student needs to show more interest in his studies or else he will not pass his courses"
        review_type = "negative"
        new_review = log_review(staff.staffID, student.studentID, description, review_type)
        downvoted_review = downvote_review(new_review.reviewID);
        logged_review = get_review(new_review.reviewID)

        self.assertEqual(downvoted_review, "True")
        self.assertEqual(logged_review.downvote, 1)
        
    def test_search():
        student1 = add_student("816031948", "Chris", "Brown")
        student2 = add_student("816029858", "Nathalia","Andrews")
        

        student_json = get_students_by_name("Chris", "Brown")

        expected_json = [
            {"studentID": student1.studentID, "firstName": student1.firstName ,"lastName":  student1.lastName }
        ]

        assert student_json == expected_json
            
    def test_view_student_reviews():
        staff= create_staff("Everly", "pumkinpi3", "everly@gamil.com", "Everly", "Reed")
        student = add_student("816099789", "Troy" , "Bolten")
        review1 = log_review(staff.staffID, student.studentID,"Excellent work", "positive")
        review2 = log_review(staff.staffID, student.studentID, "Very hardworker which is seen in results","postitive")
        review3 = log_review(staff.staffID, student.studentID, "Student has failed the course exam and needs 100 in final to not repeat course", "negative")
        retrieved_student = get_student(student.studentID)

        self.assertEqual(retrieved_student.reviews[0], review1)
        self.assertEqaul(retrieved_student.reviews[1], review2)
        self.assertEqual(retrieved_student.reviews[2], review3)
        
    def test_add_student():
        new_student = add_student("816056789", "Lala", "Singhrambatan")
        student_added = get_student(new_student.studentID)

        self.assertEqual(student_added.firstName, "Lala")
        self.assertEqual(student_added.lastName, "Singhrambatan")
        