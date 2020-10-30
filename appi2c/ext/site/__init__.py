from appi2c.ext.site.site_routes import bp


def init_app(app):
    app.register_blueprint(bp)
