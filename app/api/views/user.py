"""
User views
"""
from flask import Blueprint, jsonify, request
from sqlalchemy import exc

from app import db
from app.api.models.user import User
from app.api.utils import authenticate, is_admin


user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/users', methods=['POST'])
@authenticate
def add_user(resp):
    """Create a new user"""
    if not is_admin(resp):
        response_object = {
            'status': 'error',
            'message': 'You do not have permission to do that.'
        }
        return jsonify(response_object), 401
    post_data = request.get_json()
    if not post_data:
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        return jsonify(response_object), 422
    username = post_data.get('username')
    email = post_data.get('email')
    password = post_data.get('password')
    try:
        user = User.query.filter_by(email=email).first()
        if user:
            response_object = {
                'status': 'fail',
                'message': 'Sorry. That email already exists.'
            }
            return jsonify(response_object), 422
        user = User.query.filter_by(username=username).first()
        if user:
            response_object = {
                'status': 'fail',
                'message': 'Sorry. That username already exists.'
            }
            return jsonify(response_object), 422
        if not user:
            db.session.add(User(
                username=username,
                email=email,
                password=password))
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': '{0} was added!'.format(email)
            }
            return jsonify(response_object), 201
    except (exc.IntegrityError, ValueError) as e:
        db.session().rollback()
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        return jsonify(response_object), 422


@user_blueprint.route('/users/<user_id>', methods=['GET'])
def get_single_user(user_id):
    """Get single user details"""
    response_object = {
        'status': 'fail',
        'message': 'User does not exist'
    }
    try:
        user = User.query.filter_by(id=int(user_id)).first()
        if not user:
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'data': {
                  'username': user.username,
                  'email': user.email,
                  'created_at': user.created_at
                }
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404


@user_blueprint.route('/users', methods=['GET'])
def get_all_users():
    """Get all users"""
    users = User.query.order_by(User.created_at.desc()).all()
    users_list = []
    for user in users:
        user_object = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at
        }
        users_list.append(user_object)
    response_object = {
        'status': 'success',
        'data': {
          'users': users_list
        }
    }
    return jsonify(response_object), 200
