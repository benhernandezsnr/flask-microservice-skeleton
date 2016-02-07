import flask
from app.models.skeleton import Skeleton, db

blueprint = flask.Blueprint('skeleton_v1', __name__)


class SkeletonResponseData(object):
    @classmethod
    def get_data(cls, skeleton):
        data = {}
        data['id'] = skeleton.id
        data['name'] = skeleton.name
        return data


@blueprint.route('/skeleton', methods=['GET'])
def list_skeleton():
    skeletons = Skeleton.query.all()

    result = [SkeletonResponseData.get_data(skeleton) for skeleton in skeletons]
    flask.current_app.logger.info(result)
    return flask.jsonify({'result': result})


@blueprint.route('/skeleton', methods=['POST'])
def create_skeleton():
    data = flask.request.get_json()
    flask.current_app.logger.info(data)

    skeleton = Skeleton(name=data['name'])

    db.session.add(skeleton)
    db.session.commit()

    result = SkeletonResponseData.get_data(skeleton)
    return flask.jsonify({'result': result})


@blueprint.route('/skeleton/<id>', methods=['GET'])
def get_skeleton(id):
    skeleton = Skeleton.query.get_or_404(id)
    result = SkeletonResponseData.get_data(skeleton)
    return flask.jsonify({'result': result})
