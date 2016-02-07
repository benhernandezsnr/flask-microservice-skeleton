import flask

blueprint = flask.Blueprint('health', __name__)


@blueprint.route('/ping', methods=['GET'])
def ping():
    return flask.jsonify({'status': 'success'})
