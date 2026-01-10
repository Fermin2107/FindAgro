from extensions import db
from datetime import datetime

class Valoracion(db.Model):
    __tablename__ = "valoraciones"
    id = db.Column(db.Integer, primary_key=True)
    prestador_id = db.Column(db.Integer, db.ForeignKey('prestadores.id'), nullable=False)
    puntaje = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.Text, nullable=True)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "prestador_id": self.prestador_id,
            "puntaje": self.puntaje,
            "comentario": self.comentario,
            "creado_en": self.creado_en.isoformat()
        }
