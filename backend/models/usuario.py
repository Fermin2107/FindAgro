from extensions import db

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # "usuario" o "prestador"

    def to_dict(self):
        """Devuelve una representación segura del usuario (sin password)"""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "tipo": self.tipo,
        }
