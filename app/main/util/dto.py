from flask_restplus import Namespace, fields
from app.main import ma


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'id': fields.Integer,
        'email': fields.String(description='user email address'),
        'password': fields.String(description='user password'),
        'firstname': fields.String(description='user firstname'),
        'lastname': fields.String(description='user lastname')
    })
    user_form = api.model('user_form', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
        'firstname': fields.String(required=True, description='user firstname'),
        'lastname': fields.String(required=True, description='user lastname')
    })


class UserSchema(ma.Schema):
    class Meta:
        fields = ('email', 'password')
