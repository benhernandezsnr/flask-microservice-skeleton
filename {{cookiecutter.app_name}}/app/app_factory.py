class AppFactory(object):
    @classmethod
    def setup(cls, app):
        cls.setup_config(app)
        cls.setup_db(app)
        cls.setup_api_v1(app)

    @classmethod
    def setup_db(cls, app):
        from models import db
        db.init_app(app)

    @classmethod
    def setup_config(cls, app):
        app.config.from_object('app.config.common')
        if app.environment:
            app.config.from_object('app.config.%s' % app.environment)

    @classmethod
    def setup_api_v1(cls, app):
        import api.v1.hello
        import api.v1.skeleton
        import api.health

        app.register_blueprint(api.health.blueprint, url_prefix='/health')
        app.register_blueprint(api.v1.hello.blueprint, url_prefix='/v1')
        app.register_blueprint(api.v1.skeleton.blueprint, url_prefix='/v1')
