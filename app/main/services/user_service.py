import uuid
import datetime
from flask import jsonify
from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            email=data['email'],
            password=data['password'],
            firstname=data['firstname'],
            lastname=data['lastname']
        )
        save_changes(new_user)
        db.session.refresh(new_user)
        return new_user, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(id):
    return User.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
