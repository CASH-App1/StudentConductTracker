
from App.models import *
from App.database import db 

#Controller of staff to log review for student
def log_review(staffID, studentID, review, type):
    student = Student.query.filter_by(studentID=studentID).first()
    if not student:
        return None
    
    newReview = Review(staffID=staffID, studentID=studentID, review=review, type=type)
    if newReview:
        student.reviews.append(newReview)
        db.session.add(newReview)
        db.session.commit()
        return newReview
    return None
    

#Retrieving reviews done by staff
def get_all_reviews():
    return Review.query.all()

#Upvote review
def upvote_review(reviewID):
    review = Review.query.get(reviewID)
    
    if review:
        review.upvoteReview(reviewID)
        db.session.add(upvote)
        db.session.commit()
        return True
    return False

#Downvote review
def downVote_review(reviewID):
    review = Review.query.get(reviewID)
    
    if review:
        review.downvoteReview(reviewID)
        db.session.add(downvote)
        db.session.commit()
        return True
    return False

#Controller to get a review by reviewID
def get_review(reviewID):
    return Review.query.filter_by(reviewID=reviewID).first()
