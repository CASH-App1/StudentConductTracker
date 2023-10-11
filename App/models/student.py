from App.database import db
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

class Student(db.Model):
  studentID= db.Column(db.Integer, primary_key= True)
  fname= db.Column(db.String(30), nullable=False)
  lname= db.Column(db.String(40), nullable=False)
  karmaScore= db.Column(db.Integer, nullable=False, default = "0")
  reviews= db.relationship('Review',backref=db.backref('student', lazy='joined'))

  def __init__(self, studentID, fname, lname):
    self.studentID = studentID
    self.fname = fname
    self.lname = lname
 
  def updateKarmaScore( self):
     #self.karmaScore += karmaScore
    for r in self.reviews:
      upvotes = upvotes + r.upvote 
      downvotes = downvotes + r.downvote
      total = upvotes + downvotes

      #calculating the KarmaScore by adding the upvotes and subtracting downvotes
      karmaScore = karmaScore + (upvotes/total * 1.0) 
      karmaScore = karmaScore - (downvotes/total * 1.0)
      self.karmaScore = karmaScore

  def toDict(self):
        return{
            'Student ID': self.studentID,
            'First Name': self.fName,
            'Last Name': self.lName,
            'Karma Score': self.karmaScore    
        }
