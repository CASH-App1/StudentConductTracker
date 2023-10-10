from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin, login_user
from App.database import db
import random

class StaffMember(db.Model) :
    staffID = db.Column(db.String(5), primary_key=True)
    fName = db.Column(db.String(30), nullable=False)
    lName = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    reviews = db.relatoinship('Review', backref= db.backref('staff', lazzy='joined'))

    def __init__(self, username, password) :
        self.username = username;
        self.set_password(password)

    def  __repr__(self):
        return f'<StaffMember {self.staffID} - {self.username} - {self.fName} - {self.lName} - {self.email>'
        
    def toDict(self):
        return{
            'Staff ID': self.staffID,
            'First Name': self.fName,
            'Last Name': self.lName,
            'Email': self.email,
            'Username': self.username      
        }

    def set_password(self, password):
            self.password =generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def createReview(student, description, type, upvote, downvote):
        review = 
        

    def upvoteReview(reviewID):
        for review in reviews:
            if reviewID == review.reviewID:
                if review.student.karmaScore != 10
                    review.student.karmaScore += 1

    def downvoteReview(reviewID):
        for review in reviews:
            if reviewID == review.reviewID:
                if review.student.karmaScore != 0
                    review.student.karmaScore -= 1

    def generate_id(length=5):
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        random_id = ''.join(random.choice(characters) for _ in range(length))
    
        return random_id


    


    
    

