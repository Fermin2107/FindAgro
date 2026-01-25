from extensions import db
from datetime import datetime

class Evento(db.Model):
    __tablename__ = "eventos"
    id = db.Column(db.Integer, primary_key=True)
    prestador_id = db.Column(db.Integer, db.ForeignKey('prestadores.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=True)
    tipo_evento = db.Column(db.String(20), nullable=False)  # "view" | "contact"
    canal = db.Column(db.String(20), nullable=True)         # "whatsapp" | "telefono" | "email" | null
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    prestador = db.relationship("Prestador", backref="eventos")
