from flask import Blueprint, request, jsonify
from extensions import db
from models.prestador import Prestador
from models.valoracion import Valoracion

valoraciones_bp = Blueprint("valoraciones", __name__)

def json_ok(data, code=200):
    return jsonify({"success": True, "data": data}), code

def json_error(message, code=400):
    return jsonify({"success": False, "error": message}), code

@valoraciones_bp.route("/", methods=["POST"])
def crear_valoracion():
    data = request.get_json()
    prestador_id = data.get("prestador_id")
    puntaje = data.get("puntaje")
    if not prestador_id or puntaje is None:
        return json_error("prestador_id y puntaje son obligatorios", 400)
    try:
        puntaje = int(puntaje)
    except Exception:
        return json_error("puntaje debe ser entero", 400)
    if puntaje < 1 or puntaje > 5:
        return json_error("puntaje debe estar entre 1 y 5", 400)
    prestador = Prestador.query.get(prestador_id)
    if not prestador:
        return json_error("Prestador no encontrado", 404)
    nueva = Valoracion(
        prestador_id=prestador_id,
        puntaje=puntaje,
        comentario=data.get("comentario")
    )
    db.session.add(nueva)
    db.session.commit()
    return json_ok(nueva.to_dict(), 201)
