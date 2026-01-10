from flask import Blueprint, request, jsonify
from extensions import db
from models.prestador import Prestador
from models.servicio import Servicio
from models.valoracion import Valoracion
from sqlalchemy import func

prestadores_bp = Blueprint("prestadores", __name__)

def success_response(data):
    return jsonify({"success": True, "data": data}), 200

def error_response(message, code=400):
    return jsonify({"success": False, "error": message}), code

@prestadores_bp.route("/", methods=["GET"])
def listar_prestadores():
    """
    GET /prestadores
    Query params (opcionales):
      - localidad: filtrar por localidad (coincidencia parcial, case-insensitive)
      - servicio: filtrar por nombre de servicio (coincidencia parcial)
    Responde: lista de prestadores activos con servicios y resumen de valoraciones.
    """
    localidad = request.args.get("localidad")
    servicio_q = request.args.get("servicio")

    # Base: prestadores activos
    query = Prestador.query.filter_by(activo=True)

    if localidad:
        # coincidencia parcial, case-insensitive
        query = query.filter(Prestador.localidad.ilike(f"%{localidad}%"))

    if servicio_q:
        # join con servicios y filtrar por nombre parcial
        query = query.join(Servicio).filter(Servicio.nombre.ilike(f"%{servicio_q}%"))

    prestadores = query.all()

    results = []
    for p in prestadores:
        # incluir servicios (lista) y resumen de valoraciones (promedio y cantidad)
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
    """
    GET /prestadores/<id>
    Devuelve detalle de un prestador:
      - datos del prestador (incluye usuario mínimo)
      - servicios ofrecidos
      - promedio y lista de valoraciones (limitadas)
    """
    p = Prestador.query.filter_by(id=prestador_id, activo=True).first()
    if not p:
        return error_response("Prestador no encontrado", 404)

    # promedio de valoraciones y listado de valoraciones
    vals = p.valoraciones  # lista de objetos Valoracion
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
        # incluimos las valoraciones más recientes (hasta 10) — puede ajustarse
        "valoraciones": [v.to_dict() for v in sorted(vals, key=lambda x: x.creado_en, reverse=True)[:10]],
    }

    return success_response(data)
