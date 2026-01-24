from app import app, db
from models import Prestador

prestadores = [
    Prestador(
        nombre="AgroServicios La Huella",
        tipo="Contratista rural",
        servicios="Siembra directa, Cosecha, Pulverización, Fertilización",
        zona="Pergamino y alrededores",
        telefono="2477-456789",
        email="agrolahuella@gmail.com",
        descripcion="Contratista con 12 años de experiencia en agricultura extensiva."
    ),
    Prestador(
        nombre="Campo Fértil Servicios",
        tipo="Empresa agrícola",
        servicios="Pulverización, Fertilización",
        zona="Sur de Santa Fe",
        telefono="3462-332211",
        email="contacto@campofertil.com",
        descripcion="Empresa familiar con maquinaria moderna y atención personalizada."
    ),
    Prestador(
        nombre="El Trigal",
        tipo="Prestador independiente",
        servicios="Cosecha de trigo y soja",
        zona="Norte de Buenos Aires",
        telefono="11-55667788",
        email="eltrigal@gmail.com",
        descripcion="Servicio rápido y prolijo en campaña."
    )
]

with app.app_context():
    db.session.bulk_save_objects(prestadores)
    db.session.commit()
    print("✅ Prestadores cargados correctamente")
