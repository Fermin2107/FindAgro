from flask import Flask
from config import Config
from extensions import db

from routes.prestadores import prestadores_bp
from routes.servicios import servicios_bp
from routes.valoraciones import valoraciones_bp
from routes.eventos import eventos_bp
from routes.metricas import metricas_bp

import models.usuario    # noqa: F401
import models.prestador # noqa: F401
import models.servicio  # noqa: F401
import models.valoracion # noqa: F401
import models.evento    # noqa: F401

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(prestadores_bp, url_prefix="/prestadores")
    app.register_blueprint(servicios_bp, url_prefix="/servicios")
    app.register_blueprint(valoraciones_bp, url_prefix="/valoraciones")
    app.register_blueprint(eventos_bp, url_prefix="/eventos")
    app.register_blueprint(metricas_bp) # sin prefijo por REST

    @app.route("/ping")
    def ping():
        return {"message": "pong"}

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
