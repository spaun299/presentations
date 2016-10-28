from flask.app import Flask
from .blueprints import register_blueprints
import config
import logging
from logging.handlers import RotatingFileHandler


def init_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.template_folder = config.template_folder
    handler = RotatingFileHandler(config.log_path, maxBytes=10000,
                                  backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    register_blueprints(app)
    return app
