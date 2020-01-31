from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'id': fields.String(description='user Identifier'),
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
        'firstname': fields.String(required=True, description='user firstname'),
        'lastname': fields.String(required=True, description='user lastname')
    })
