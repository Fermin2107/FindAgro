from flask import Blueprint, request, jsonify
from extensions import db
from models.prestador import Prestador
from models.valoracion import Valoracion

valoraciones_bp = Blueprint("valoraciones", __name__)

def success_response(data, code=200):
    return jsonify({"success": True, "data": data}), code

def error_response(message, code=400):
    return jsonify({"success": False, "error": message}), code

@valoraciones_bp.route("/", methods=["POST"])
def crear_valoracion():
    """
    Crea una valoración abierta para un prestador.
    Input JSON:
    {
      "prestador_id": 1,
      "puntaje": 5,
      "comentario": "Muy buen servicio"
    }
    """
    data = request.get_json()
    prestador_id = data.get("prestador_id")
    puntaje = data.get("puntaje")
    if not prestador_id or puntaje is None:
        return error_response("prestador_id y puntaje son obligatorios", 400)
    try:
        puntaje = int(puntaje)
    except (TypeError, ValueError):
        return error_response("puntaje debe ser entero", 400)
    if puntaje < 1 or puntaje > 5:
        return error_response("puntaje debe ser entre 1 y 5", 400)
    prestador = Prestador.query.get(prestador_id)
    if not prestador:
        return error_response("Prestador no encontrado", 404)
    nueva = Valoracion(
        prestador_id=prestador_id,
        puntaje=puntaje,
        comentario=data.get("comentario")
    )
    db.session.add(nueva)
    db.session.commit()
    return success_response(nueva.to_dict(), 201)
