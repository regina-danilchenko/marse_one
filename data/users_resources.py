from flask_restful import reqparse, Resource, abort
from data import db_session
from .users import User
import datetime
from flask import jsonify


def error(user_id):
    session = db_session.create_session()
    user = session.query(User).get(int(user_id))
    if not user:
        abort(404, message=f"Users {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        error(user_id)
        session = db_session.create_session()
        user = session.query(User).get(int(user_id))
        return jsonify({'users': user.to_dict(
            only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'modified_date'))})

    def delete(self, user_id):
        error(user_id)
        session = db_session.create_session()
        user = session.query(User).get(int(user_id))
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


parser = reqparse.RequestParser()
parser.add_argument('surname', required=True)
parser.add_argument('name', required=True)
parser.add_argument('age', required=True, type=int)
parser.add_argument('position', required=True)
parser.add_argument('speciality', required=True)
parser.add_argument('address', required=True)
parser.add_argument('email', required=True)
parser.add_argument('modified_date', required=True)

class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'modified_date'))
            for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            modified_date=datetime.datetime.strptime(args['modified_date'], '%Y-%m-%d')
        )
        session.add(user)
        session.commit()
        return jsonify({'id': user.id})
