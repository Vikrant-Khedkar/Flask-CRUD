from flask import Flask, request, jsonify,logging
from pymongo import MongoClient
from blueprints.users import users_blueprint
from config import client, db, collection
from logging.config import dictConfig

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "flask.log",
                "formatter": "default",
            },
        },

        "root": {"level": "DEBUG", "handlers": ["console","file"]},
    }
)


app = Flask(__name__)
app.register_blueprint(users_blueprint)


@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.logger.info('Starting Flask application')
    app.run(debug=True)

