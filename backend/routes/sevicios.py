from flask import Blueprint, request, jsonify
from extensions import db
from models.prestador import Prestador
from models.servicio import Servicio

servicios_bp = Blueprint("servicios", __name__)

def json_ok(data, code=200):
    return jsonify({"success": True, "data": data}), code

def json_error(message, code=400):
    return jsonify({"success": False, "error": message}), code

@servicios_bp.route("/", methods=["POST"])
def crear_servicio():
    data = request.get_json()
    prestador_id = data.get("prestador_id")
    nombre = data.get("nombre")
    if not prestador_id or not nombre:
        return json_error("prestador_id y nombre son obligatorios", 400)
    prestador = Prestador.query.get(prestador_id)
    if not prestador:
        return json_error("Prestador no encontrado", 404)
    nuevo = Servicio(
        nombre=nombre,
        descripcion=data.get("descripcion"),
        prestador_id=prestador_id
    )
    db.session.add(nuevo)
    db.session.commit()
    return json_ok(nuevo.to_dict(), 201)
