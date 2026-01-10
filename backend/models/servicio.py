from extensions import db

class Servicio(db.Model):
    """
    Modelo Servicio: representa un tipo de trabajo/servicio que ofrece un prestador.
    Relación: muchos servicios a un prestador (prestador -> servicios).
    """
    __tablename__ = "servicios"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)  # ej: "Cosecha"
    descripcion = db.Column(db.Text, nullable=True)
    prestador_id = db.Column(db.Integer, db.ForeignKey('prestadores.id'), nullable=False)

    def to_dict(self):
        """Representación limpia del servicio"""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "prestador_id": self.prestador_id,
        }
