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

class ReviewUnitTests(unittest.TestCase):

    def test_new_review(self):
        #newStaff = Staff("bob", "bobpass", "bob@mail.com", "Bobby", "Smith")
        #newReview = newStaff.createReview("816011111", "1", "This student continues to show great potential", "positive")
        newReview = Review("816011111", "1", "This student continues to show great potential", "positive")
        assert (newReview.studentID, newReview.staffID, newReview.description, newReview.reviewType) == ("816011111", "1", "This student continues to show great potential", "positive")

    def test_review_toDict(self):
        newReview = Review(816011111, 1, "This student continues to show great potential", "positive")
        #review_json = newReview.toDict()
        self.assertDictEqual(newReview.toDict(), {"Review ID":None, "Student ID":816011111, "Staff ID":1, "Description":"This student continues to show great potential", "Date":datetime.utcnow ,"Upvote":0, "Downvote":0, "Review Type":"positive"})

    

class StaffUnitTests(unittest.TestCase):

    def test_new_staff(self):
        newStaff = StaffMember("bob", "bobpass", "bob@mail.com", "Bobby", "Smith")
        assert (newStaff.username, newStaff.email, newStaff.firstName, newStaff.lastName) == ("bob", "bob@mail.com", "Bobby", "Smith")

    # pure function no side effects or integrations called
    def test_staff_toDict(self):
        newStaff = StaffMember("bob", "bobpass", "bob@mail.com", "Bobby", "Smith")
        #staff_json = newStaff.toDict()
        self.assertDictEqual(newStaff.toDict(), {"Staff ID":None, "First Name":"Bobby", "Last Name":"Smith", "Email":"bob@mail.com", "Username":"bob"})
    
    