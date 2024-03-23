from flask import Flask

def create_app():
    
    # Crear aplicación de flask
    app = Flask(__name__)
    
    #Registrar vistas
    from blogr import home
    app.register_blueprint(home.bp)
    
    from blogr import auth
    app.register_blueprint(auth.bp)
    
    from blogr import post
    app.register_blueprint(post.bp)
    
    return app