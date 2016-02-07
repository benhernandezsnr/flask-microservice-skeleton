import flask

blueprint = flask.Blueprint('hello_v1', __name__)


@blueprint.route('/', methods=['GET'])
def get():
    return 'Hello World! From %s environment' % flask.current_app.environment
