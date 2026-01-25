from flask import Blueprint, request, jsonify
from extensions import db
from models.evento import Evento
from models.prestador import Prestador

eventos_bp = Blueprint("eventos", __name__)

def json_ok(data, code=200):
    return jsonify({"success": True, "data": data}), code

def json_error(message, code=400):
    return jsonify({"success": False, "error": message}), code

@eventos_bp.route("/", methods=["POST"])
def crear_evento():
    data = request.get_json()
    prestador_id = data.get("prestador_id")
    tipo_evento = data.get("tipo_evento")  # "view" | "contact"
    canal = data.get("canal")  # "whatsapp" | "telefono" | "email" | None
    usuario_id = data.get("usuario_id")    # puede ser null

    if not prestador_id or tipo_evento not in ("view", "contact"):
        return json_error("prestador_id y tipo_evento son obligatorios", 400)
    if canal and canal not in ("whatsapp", "telefono", "email"):
        return json_error("canal inválido", 400)
    prestador = Prestador.query.get(prestador_id)
    if not prestador:
        return json_error("Prestador no encontrado", 404)

    nuevo = Evento(
        prestador_id=prestador_id,
        usuario_id=usuario_id,
        tipo_evento=tipo_evento,
        canal=canal
    )
    db.session.add(nuevo)
    db.session.commit()
    return json_ok({
        "id": nuevo.id,
        "prestador_id": nuevo.prestador_id,
        "usuario_id": nuevo.usuario_id,
        "tipo_evento": nuevo.tipo_evento,
        "canal": nuevo.canal,
        "created_at": nuevo.created_at.isoformat(),
    }, 201)
