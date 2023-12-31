from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

from App.controllers import *

review_views = Blueprint('review_views', __name__, template_folder='../templates')

@review_views.route('/view/student/review', methods=['PUT'])
@jwt_required()
def karma_rank():
    data = request.json
    student = Student.query.get(data['studentID'])
    if student: 
        if data['vote'] == 'upvote':
            upvote = upvote_review(data['reviewID'])
        else:
            downvote = downvote_review(data['reviewID'])

        if upvote or downvote:
            return jsonify(message = 'Vote added successfully'), 200
        return jsonify(error='Vote unsuccessful'), 400
    return jsonify(error= "Student not found"), 400

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)