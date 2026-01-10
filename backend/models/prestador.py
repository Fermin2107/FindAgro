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

    # Relación 1 a 1: un prestador tiene un usuario
    usuario = db.relationship("Usuario", backref=db.backref("prestador", uselist=False))

    # Relación 1 a muchos: un prestador ofrece varios servicios (relación se define en Servicio)
    servicios = db.relationship("Servicio", backref="prestador", cascade="all, delete-orphan")

    # Relación 1 a muchos: un prestador puede tener varias valoraciones
    valoraciones = db.relationship("Valoracion", backref="prestador", cascade="all, delete-orphan")

    def to_dict(self, include_servicios=False, include_valoracion=False):
        data = {
            "id": self.id,
            "usuario": self.usuario.to_dict() if self.usuario else None,
            "descripcion": self.descripcion,
            "telefono": self.telefono,
            "localidad": self.localidad,
            "latitud": self.latitud,
            "longitud": self.longitud,
            "activo": self.activo,
        }
        if include_servicios:
            data["servicios"] = [s.to_dict() for s in self.servicios]
        if include_valoracion:
            vals = [v.puntaje for v in self.valoraciones]
            data["promedio_valoracion"] = round(sum(vals)/len(vals), 1) if vals else None
            data["cantidad_valoraciones"] = len(vals)
        return data
