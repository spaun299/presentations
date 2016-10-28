from flask import Blueprint

index_bp = Blueprint('index', __name__)
static_bp = Blueprint('static', __name__)


def register_blueprints(app):
    from views import index
    app.register_blueprint(index_bp)
    from views import static
    app.register_blueprint(static_bp, url_prefix='/static')
