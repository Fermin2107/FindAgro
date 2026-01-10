from extensions import db

class Servicio(db.Model):
    __tablename__ = "servicios"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    prestador_id = db.Column(db.Integer, db.ForeignKey('prestadores.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "prestador_id": self.prestador_id,
        }
