import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { getPrestadorDetalle } from "../api/prestadores";
import { registrarEvento } from "../api/eventos";
import PanelPrestadorMetricas from "../components/PanelPrestadorMetricas";

export default function PrestadorDetalle() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [prestador, setPrestador] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    setLoading(true);
    getPrestadorDetalle(id)
      .then(setPrestador)
      .catch(() => setError("No se pudo cargar el prestador"))
      .finally(() => setLoading(false));
    // Registrar la vista del perfil
    registrarEvento({ prestador_id: id, tipo_evento: "view" }).catch(() => {});
  }, [id]);

  if (loading) return <div className="text-green-700">Cargando...</div>;
  if (error) return <div className="text-red-600">{error}</div>;
  if (!prestador) return null;

  // Registro de contacto en botón
  function handleContact(canal) {
    registrarEvento({ prestador_id: id, tipo_evento: "contact", canal }).catch(() => {});
    // continuar navegación/contacto real si existe
  }

  return (
    <div>
      {/* ... otros datos ... */}
      <PanelPrestadorMetricas prestadorId={id} />
      <div className="mt-6 flex gap-2">
        <button onClick={() => handleContact("whatsapp")}>Contactar por WhatsApp</button>
        <button onClick={() => handleContact("telefono")}>Contactar por Teléfono</button>
        <button onClick={() => handleContact("email")}>Contactar por Email</button>
      </div>
    </div>
  );
}
