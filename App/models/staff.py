from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin, login_user
from App.database import db

class StaffMember(db.Model) :
    staffID = db.Column(db.String(5), primary_key=True)
    fName = db.Column(db.String(30), nullable=False)
    lName = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def __init__(self, username, password) :
        self.username = username;
        self.set_password(password)

    def  __repr__(self):
        return f'<StaffMember {self.staffID} - {self.username}>'
        
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

    def createReview(student, descripotion, type):

    def upvoteConductReview(Review):

    def downvoteConductReview(Review);

    def resolveConductReview(Review):

    def logOut():

    def logIn(username,password):
        staff_member = StaffMember.query.filter_by(username=username).first()
        if staff_member and staff_member.check_password(password):
            login_user(staff_member)
            return True
        else:
            return False
            
    def load_user(user_id):
        return StaffMember.query.get(int(user_id))
        
    def addStudent():
    


    
    

