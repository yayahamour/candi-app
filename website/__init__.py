from flask import Flask

def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    
    from .views import views
    from .auth import auth
    from .users import users

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(users, url_prefix='/')

    return app