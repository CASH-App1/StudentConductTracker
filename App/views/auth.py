from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

from.index import index_views

from App.controllers import (
    create_user,
    jwt_authenticate,
    login 
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

'''
API Routes
'''
@auth_views.route('/login', methods=['POST'])
def user_login():
  data = request.json
  token = jwt_authenticate(data['username'], data['password'])
  if not token:
    return jsonify(message='Incorrect username or password'), 401
  return jsonify(token=token), 200


@auth_views.route('/signup', methods=['POST'])
def user_():
    data = request.json
    user = create_user(username = data['username'], password = data['password'])
    if user:
        return jsonify(message='Account created successfully'), 201
    return jsonify(error='Username already taken'), 400
