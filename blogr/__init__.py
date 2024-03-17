from flask import Flask

def create_app():
    
    # Crear aplicación de flask
    app = Flask(__name__)
    
    return app