from flask import Blueprint, request, jsonify
from extensions import db
from models.usuario import Usuario
from models.prestador import Prestador
from models.servicio import Servicio

prestadores_bp = Blueprint("prestadores", __name__)

def json_ok(data, code=200):
    return jsonify({"success": True, "data": data}), code

def json_error(message, code=400):
    return jsonify({"success": False, "error": message}), code

@prestadores_bp.route("/", methods=["GET"])
def listar_prestadores():
    localidad = request.args.get("localidad")
    servicio_q = request.args.get("servicio")
    query = Prestador.query.filter_by(activo=True)
    if localidad:
        query = query.filter(Prestador.localidad.ilike(f"%{localidad}%"))
    if servicio_q:
        query = query.join(Servicio).filter(Servicio.nombre.ilike(f"%{servicio_q}%"))
    prestadores = query.all()
    return json_ok([p.to_dict() for p in prestadores])

@prestadores_bp.route("/<int:prestador_id>", methods=["GET"])
def obtener_prestador(prestador_id):
    p = Prestador.query.filter_by(id=prestador_id, activo=True).first()
    if not p:
        return json_error("Prestador no encontrado", 404)
    return json_ok(p.to_dict())

@prestadores_bp.route("/", methods=["POST"])
def crear_prestador():
    data = request.get_json()
    usuario_id = data.get("usuario_id")
    if not usuario_id:
        return json_error("usuario_id es obligatorio", 400)
    usuario = Usuario.query.get(usuario_id)
    if not usuario:
        return json_error("Usuario no encontrado", 404)
    if hasattr(usuario, "prestador") and usuario.prestador:
        return json_error("El usuario ya es prestador", 400)
    nuevo = Prestador(
        usuario_id=usuario_id,
        descripcion=data.get("descripcion"),
        telefono=data.get("telefono"),
        localidad=data.get("localidad"),
        latitud=data.get("latitud"),
        longitud=data.get("longitud"),
        activo=True
    )
    db.session.add(nuevo)
    db.session.commit()
    return json_ok(nuevo.to_dict(), 201)
