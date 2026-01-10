from flask import Flask
from config import Config
from extensions import db
from models.usuario import Usuario

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones con la app
    db.init_app(app)

    # Simple ruta de salud
    @app.route("/ping")
    def ping():
        return {"message": "pong"}

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
