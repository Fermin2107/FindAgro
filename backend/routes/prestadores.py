from flask import Blueprint, request, jsonify
from extensions import db
from models.usuario import Usuario
from models.prestador import Prestador
from models.servicio import Servicio

prestadores_bp = Blueprint("prestadores", __name__)

def success_response(data, code=200):
    return jsonify({"success": True, "data": data}), code

def error_response(message, code=400):
    return jsonify({"success": False, "error": message}), code

# ----------- Rutas públicas existentes ----------- #
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
    results = []
    for p in prestadores:
        vals = [v.puntaje for v in p.valoraciones]
        promedio = round(sum(vals)/len(vals), 1) if vals else None
        results.append({
            "id": p.id,
            "usuario": p.usuario.to_dict() if p.usuario else None,
            "descripcion": p.descripcion,
            "telefono": p.telefono,
            "localidad": p.localidad,
            "latitud": p.latitud,
            "longitud": p.longitud,
            "activo": p.activo,
            "servicios": [s.to_dict() for s in p.servicios],
            "promedio_valoracion": promedio,
            "cantidad_valoraciones": len(vals),
        })
    return success_response(results)

@prestadores_bp.route("/<int:prestador_id>", methods=["GET"])
def obtener_prestador(prestador_id):
    p = Prestador.query.filter_by(id=prestador_id, activo=True).first()
    if not p:
        return error_response("Prestador no encontrado", 404)
    vals = p.valoraciones
    puntajes = [v.puntaje for v in vals]
    promedio = round(sum(puntajes)/len(puntajes), 1) if puntajes else None
    data = {
        "id": p.id,
        "usuario": p.usuario.to_dict() if p.usuario else None,
        "descripcion": p.descripcion,
        "telefono": p.telefono,
        "localidad": p.localidad,
        "latitud": p.latitud,
        "longitud": p.longitud,
        "activo": p.activo,
        "servicios": [s.to_dict() for s in p.servicios],
        "promedio_valoracion": promedio,
        "cantidad_valoraciones": len(puntajes),
        "valoraciones": [v.to_dict() for v in sorted(vals, key=lambda x: x.creado_en, reverse=True)[:10]],
    }
    return success_response(data)

# ----------- Endpoint nuevo: Crear Prestador ----------- #
@prestadores_bp.route("/", methods=["POST"])
def crear_prestador():
    """
    Crea un nuevo prestador asociado a un usuario.
    Input JSON:
    {
      "usuario_id": 1,
      "descripcion": "Servicios de siembra y cosecha",
      "telefono": "11-1234-5678",
      "localidad": "Pergamino",
      "latitud": -33.89,
      "longitud": -60.57
    }
    """
    data = request.get_json()
    usuario_id = data.get("usuario_id")
    if not usuario_id:
        return error_response("usuario_id es obligatorio", 400)
    usuario = Usuario.query.get(usuario_id)
    if not usuario:
        return error_response("Usuario no encontrado", 404)
    if hasattr(usuario, "prestador") and usuario.prestador:
        return error_response("El usuario ya es prestador", 400)
    # Crear prestador
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
    return success_response(nuevo.to_dict())
