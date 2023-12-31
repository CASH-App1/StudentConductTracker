from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import create_staff

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_staff('bob', 'bobpass', 'bob@email.com', 'Bob', 'Doe')
    return jsonify(message='db initialized!')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)