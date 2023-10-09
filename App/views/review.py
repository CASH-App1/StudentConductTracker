from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

from App.controllers import *

review_views = Blueprint('review_views', __name__, template_folder='../templates')

@review_views.route('/review', methods=['PUT'])
@login_required
def karma_rank():
    data = request.json
    if data['vote'] == 'upvote':
        upvote = upvote(data['reviewID'])
    else:
        downvote = downvote(data['reviewID'])

    if upvote:
        return jsonify(message = 'Vote added successfully'), 200
    return jsonify(error='Vote unsuccessful'), 500

