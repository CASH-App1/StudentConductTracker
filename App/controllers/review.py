
from App.models import *
from App.database import db 

# Controller of staff to log review for student
def log_review(staffID, studentID, review, reviewType):
    staff = StaffMember.query.get(staffID)
    if staff:
        newReview = staff.createReview(studentID, review, reviewType)
        if newReview:
            db.session.add(newReview)
            db.session.commit()
            return newReview
        return None
    return None

# Retrieving reviews done by staff
def get_all_reviews():
    return Review.query.all()

#Upvote review
def upvote_review(reviewID):
    review = Review.query.get(reviewID)
    
    if review:
        review.upvoteReview()
        student = Student.query.get(review.studentID)
        if student:
            student.updateKarmaScore()

        db.session.add(review)
        db.session.commit()
        return True
    return False

#Downvote review
def downvote_review(reviewID):
    review = Review.query.get(reviewID)
    
    if review:
        review.downvoteReview()
        student = Student.query.get(review.studentID)
        if student:
            student.updateKarmaScore()

        db.session.add(review)
        db.session.commit()
        return True
    return False

#Controller to get a review by reviewID
def get_review(reviewID):
    return Review.query.filter_by(reviewID=reviewID).first()
