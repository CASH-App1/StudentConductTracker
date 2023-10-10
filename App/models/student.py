from App.database import db

class Student(db.Model):
  studentID: db.Column(db.String(5), primary_key= True)
  fname: db.Column(db.String(30), nullable=False)
  lname: db.Column(db.String(40), nullable=False)
  karmaScore: db.Column(db.Integer, nullable=False, default = "0")
  reviews: db.relationship('Review',backref=db.backref('student', lazy='joined'))

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

      karmaScore = karmaScore + (upvotes/total * 1.0)
      karmaScore = karmaScore - (downvotes/total * 1.0)
      self.karmaScore = karmaScore

