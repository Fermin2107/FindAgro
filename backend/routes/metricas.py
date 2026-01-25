from flask import Blueprint, jsonify
from sqlalchemy import func, and_
from datetime import datetime, timedelta
from models.evento import Evento
from models.prestador import Prestador

metricas_bp = Blueprint("metricas", __name__)

def json_ok(data, code=200):
    return jsonify({"success": True, "data": data}), code

def json_error(message, code=400):
    return jsonify({"success": False, "error": message}), code

@metricas_bp.route("/prestadores/<int:prestador_id>/metricas", methods=["GET"])
def obtener_metricas(prestador_id):
    prestador = Prestador.query.get(prestador_id)
    if not prestador:
        return json_error("Prestador no encontrado", 404)
    now = datetime.utcnow()
    d7 = now - timedelta(days=7)
    d30 = now - timedelta(days=30)

    
    total_vistas = Evento.query.filter_by(prestador_id=prestador_id, tipo_evento="view").count()
    total_contactos = Evento.query.filter_by(prestador_id=prestador_id, tipo_evento="contact").count()

    
    canales = ["whatsapp", "telefono", "email"]
    contactos_por_canal = {}
    for canal in canales:
        cnt = Evento.query.filter_by(prestador_id=prestador_id, tipo_evento="contact", canal=canal).count()
        contactos_por_canal[canal] = cnt

    
    vistas_7d = Evento.query.filter_by(prestador_id=prestador_id, tipo_evento="view").filter(Evento.created_at >= d7).count()
    contactos_7d = Evento.query.filter_by(prestador_id=prestador_id, tipo_evento="contact").filter(Evento.created_at >= d7).count()

   
    vistas_30d = Evento.query.filter_by(prestador_id=prestador_id, tipo_evento="view").filter(Evento.created_at >= d30).count()
    contactos_30d = Evento.query.filter_by(prestador_id=prestador_id, tipo_evento="contact").filter(Evento.created_at >= d30).count()

    return json_ok({
        "total_vistas": total_vistas,
        "total_contactos": total_contactos,
        "contactos_por_canal": contactos_por_canal,
        "ultimos_7_dias": {"vistas": vistas_7d, "contactos": contactos_7d},
        "ultimos_30_dias": {"vistas": vistas_30d, "contactos": contactos_30d}
    })
