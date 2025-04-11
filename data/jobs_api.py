import flask
import datetime
from flask import jsonify, make_response, request
from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_news():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'news':
                [item.to_dict(only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date',
                                    'is_finished')) for item in jobs]
        }
    )

@blueprint.route('/api/jobs/<job_id>', methods=['GET'])
def get_one_news(job_id):
    db_sess = db_session.create_session()
    try:
        if int(job_id):
            job = db_sess.query(Jobs).get(job_id)
            if not job:
                return make_response(jsonify({'error': 'Not found'}), 404)
            return jsonify(
                {
                    'job': job.to_dict(only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date',
                                              'is_finished'))
                }
            )
    except ValueError:
        return make_response(jsonify({'error': 'Bad Request'}), 400)

@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    try:
        if int(request.json['team_leader']) and str(request.json['job']) and int(request.json['work_size']) and \
            str(request.json['collaborators']) and datetime.datetime.strptime(request.json['start_date'], '%Y-%m-%d') and \
                datetime.datetime.strptime(request.json['end_date'], '%Y-%m-%d') and type(request.json['is_finished']) is bool:
            ...
    except ValueError:
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    job = Jobs(
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        start_date=datetime.datetime.strptime(request.json['start_date'], '%Y-%m-%d'),
        end_date=datetime.datetime.strptime(request.json['end_date'], '%Y-%m-%d'),
        is_finished=request.json['is_finished']
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'id': job.id})

@blueprint.route('/api/jobs/<job_id>', methods=['PUT'])
def update_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return make_response(jsonify({'error': 'Not found'}), 404)
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    try:
        if int(request.json['team_leader']) and str(request.json['job']) and int(request.json['work_size']) and \
            str(request.json['collaborators']) and datetime.datetime.strptime(request.json['start_date'], '%Y-%m-%d') and \
                datetime.datetime.strptime(request.json['end_date'], '%Y-%m-%d') and type(request.json['is_finished']) is bool:
            ...
    except ValueError:
        return make_response(jsonify({'error': 'Bad request'}), 400)
    job.team_leader = request.json['team_leader']
    job.job = request.json['job']
    job.work_size = request.json['work_size']
    job.collaborators = request.json['collaborators']
    job.start_date = datetime.datetime.strptime(request.json['start_date'], '%Y-%m-%d')
    job.end_date = datetime.datetime.strptime(request.json['end_date'], '%Y-%m-%d')
    job.is_finished = request.json['is_finished']
    db_sess.commit()
    return jsonify({'id': job.id})

@blueprint.route('/api/jobs/<job_id>', methods=['DELETE'])
def delete_news(job_id):
    try:
        if int(job_id):
            pass
    except ValueError:
        return make_response(jsonify({'error': 'Bad Request'}), 400)
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})
