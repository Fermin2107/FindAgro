from extensions import db

class Prestador(db.Model):
    __tablename__ = "prestadores"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), unique=True, nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    telefono = db.Column(db.String(30), nullable=True)
    localidad = db.Column(db.String(100), nullable=True)
    latitud = db.Column(db.Float, nullable=True)
    longitud = db.Column(db.Float, nullable=True)
    activo = db.Column(db.Boolean, default=True, nullable=False)

    usuario = db.relationship("Usuario", backref=db.backref("prestador", uselist=False))
    servicios = db.relationship("Servicio", backref="prestador", cascade="all, delete-orphan")
    valoraciones = db.relationship("Valoracion", backref="prestador", cascade="all, delete-orphan")

    def to_dict(self, anidar_servicios=True, incluir_promedio=True):
        vals = [v.puntaje for v in self.valoraciones]
        promedio = round(sum(vals)/len(vals), 1) if vals else None
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "descripcion": self.descripcion,
            "telefono": self.telefono,
            "localidad": self.localidad,
            "latitud": self.latitud,
            "longitud": self.longitud,
            "activo": self.activo,
            "servicios": [s.to_dict() for s in self.servicios] if anidar_servicios else None,
            "promedio_valoracion": promedio if incluir_promedio else None,
            "cantidad_valoraciones": len(vals)
        }
