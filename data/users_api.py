import flask
import datetime
from flask import jsonify, make_response, request
from . import db_session
from .users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)

@blueprint.route('/api/users')
def get_news():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email',
                              'modified_date')) for item in users]
        }
    )

@blueprint.route('/api/users/<int:users_id>', methods=['GET'])
def get_one_user(users_id):
    db_sess = db_session.create_session()
    try:
        if int(users_id):
            user = db_sess.query(User).get(users_id)
            if not user:
                return make_response(jsonify({'error': 'Not found'}), 404)
            return jsonify(
                {
                    'user': user.to_dict(
                        only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email',
                              'modified_date'))
                }
            )
    except ValueError:
        return make_response(jsonify({'error': 'Bad Request'}), 400)

@blueprint.route('/api/users', methods=['POST'])
def create_users():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'modified_date']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    try:
        if str(request.json['surname']) and str(request.json['name']) and int(request.json['age']) and \
            str(request.json['position']) and datetime.datetime.strptime(request.json['modified_date'], '%Y-%m-%d') and \
            str(request.json['speciality']) and str(request.json['address']) and str(request.json['email']):
            ...
    except ValueError:
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    user = User(
        surname=request.json['surname'],
        name=request.json['name'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email'],
        modified_date=datetime.datetime.strptime(request.json['modified_date'], '%Y-%m-%d')
    )
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'id': user.id})

@blueprint.route('/api/users/<user_id>', methods=['PUT'])
def update_job(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return make_response(jsonify({'error': 'Not found'}), 404)
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'modified_date']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    try:
        if str(request.json['surname']) and str(request.json['name']) and int(request.json['age']) and \
                str(request.json['position']) and datetime.datetime.strptime(request.json['modified_date'],
                                                                             '%Y-%m-%d') and \
                str(request.json['speciality']) and str(request.json['address']) and int(request.json['email']):
            ...
    except ValueError:
        return make_response(jsonify({'error': 'Bad request'}), 400)
    user.surname = request.json['surname']
    user.name = request.json['name']
    user.age = request.json['age']
    user.position = request.json['position']
    user.speciality = request.json['speciality']
    user.address = request.json['address']
    user.email = request.json['email']
    user.modified_date = datetime.datetime.strptime(request.json['modified_date'], '%Y-%m-%d')
    db_sess.commit()
    return jsonify({'id': user.id})

@blueprint.route('/api/users/<int:users_id>', methods=['DELETE'])
def delete_users(users_id):
    try:
        if int(users_id):
            pass
    except ValueError:
        return make_response(jsonify({'error': 'Bad Request'}), 400)
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(users_id)
    if not user:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})

