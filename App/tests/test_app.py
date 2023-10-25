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
    
    def test_updateKarmaScore(self):
        newStudent = Student(816011111, "Dale", "Barbara")
        newStaff = StaffMember("RobertJackson", "robby123", "robertjackson@mail.com", "Robert", "Jackson")
        newReview = newStaff.createReview(816011111, "This student continues to show great potential", "positive")
        print(newReview)
        newReview.upvote()
        newStudent.updateKarmaScore()
        assert(newStudent.karmaScore == 1)

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

    def test_create_review(self):
        newStaff = StaffMember("bob", "bobpass", "bob@mail.com", "Bobby", "Smith")
        newStudent = Student(816011111 , "Dale", "Barbara")
        newReview = newStaff.createReview(newStudent.studentID, "This student continues to show great potential", "positive")
        print(newReview)
        #newReview = Review(newStudent.studentID, newStaff.staffID, "This student continues to show great potential", "positive")
        assert (newReview.studentID, newReview.staffID, newReview.description, newReview.reviewType) == (newStudent.studentID, newStaff.staffID, "This student continues to show great potential"
        , "positive")
