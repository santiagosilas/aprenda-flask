from flask import Flask

def create_application():

    app = Flask(__name__)

    app.config['DEBUG'] = True
    with app.app_context():
        from . import routes
        

    return app



