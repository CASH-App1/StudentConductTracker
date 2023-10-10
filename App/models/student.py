from App.database import db

class Student(db.Model):
  studentID: db.Column(db.String(5), primary_key= True)
  fname: db.Column(db.String(30), nullable=False)
  lname: db.Column(db.String(40), nullable=False)
  karmaScore: db.Column(db.Integer, nullable=False)
  reviews: db.relationship('Listing',backref=db.student('user', lazy='joined'))

def updateKarmaScore( self, karmaScore):
     self.karmaScore += karmaScore
