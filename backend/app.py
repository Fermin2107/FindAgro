from flask import Flask
from config import Config
from extensions import db

# Importar routes (blueprints) y modelos para que SQLAlchemy conozca las clases
from routes.prestadores import prestadores_bp

# Importamos los modelos para registrar las clases antes de db.create_all()
# (esto evita que falten tablas)
import models.usuario  # noqa: F401
import models.prestador  # noqa: F401
import models.servicio  # noqa: F401
import models.valoracion  # noqa: F401

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensión
    db.init_app(app)

    # Registrar blueprints
    app.register_blueprint(prestadores_bp, url_prefix="/prestadores")

    # Ruta de salud
    @app.route("/ping")
    def ping():
        return {"message": "pong"}

    # Crear tablas (si no existen) en contexto de app
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
