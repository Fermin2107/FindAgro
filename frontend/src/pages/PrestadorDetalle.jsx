import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { getPrestadorDetalle } from "../api/prestadores";

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
  }, [id]);

  if (loading) return <div className="text-green-700">Cargando...</div>;
  if (error) return <div className="text-red-600">{error}</div>;
  if (!prestador) return null;

  return (
    <div>
      <button
        className="mb-4 px-4 py-1 text-green-700 border border-green-700 rounded hover:bg-green-50"
        onClick={() => navigate(-1)}
      >
        &larr; Volver
      </button>
      <div className="bg-white rounded shadow p-5">
        <h2 className="text-xl font-bold mb-1 text-green-900">Prestador #{prestador.id}</h2>
        <p className="text-gray-700 mb-2">{prestador.descripcion}</p>
        <div className="mb-2">
          <strong className="text-green-700">Localidad:</strong>{" "}
          <span>{prestador.localidad || "Sin info"}</span>
        </div>
        <div className="mb-2">
          <strong className="text-green-700">Servicios:</strong>{" "}
          {prestador.servicios.length === 0 ? (
            <span className="text-gray-500">Sin servicios registrados</span>
          ) : (
            <ul className="list-disc list-inside">
              {prestador.servicios.map((s) => (
                <li key={s.id}>{s.nombre} <span className="text-gray-500 text-xs">{s.descripcion}</span></li>
              ))}
            </ul>
          )}
        </div>
        <div className="mb-2 flex items-center gap-2">
          <strong className="text-green-700">Promedio:</strong>
          {prestador.promedio_valoracion !== null ? (
            <span>
              {prestador.promedio_valoracion} / 5
              <span className="text-yellow-600 ml-1">{"★".repeat(Math.round(prestador.promedio_valoracion))}</span>
            </span>
          ) : (
            <span className="text-gray-500">Sin valoraciones</span>
          )}
          <span className="ml-3 text-xs text-gray-500">{prestador.cantidad_valoraciones} valoraciones</span>
        </div>
        <div className="mt-4">
          <h3 className="font-medium text-green-800 mb-1">Valoraciones</h3>
          {prestador.valoraciones && prestador.valoraciones.length > 0 ? (
            <ul>
              {prestador.valoraciones.map((v) => (
                <li
                  key={v.id}
                  className="text-gray-800 mb-2 border-b pb-1"
                >
                  <div className="text-yellow-700 font-semibold">
                    {"★".repeat(v.puntaje)}
                  </div>
                  {v.comentario && <div className="italic">{v.comentario}</div>}
                  <div className="text-xs text-gray-500">
                    {new Date(v.creado_en).toLocaleDateString()}
                  </div>
                </li>
              ))}
            </ul>
          ) : (
            <div className="text-gray-500">No hay valoraciones.</div>
          )}
        </div>
        <div className="mt-6 flex flex-col sm:flex-row gap-2">
          <button className="bg-green-100 border border-green-700 text-green-700 px-4 py-2 rounded font-semibold cursor-pointer hover:bg-green-200">
            Contactar (simulado)
          </button>
          <button className="bg-green-100 border border-green-700 text-green-700 px-4 py-2 rounded font-semibold cursor-pointer hover:bg-green-200">
            Solicitar servicio (simulado)
          </button>
          <button className="bg-green-100 border border-yellow-700 text-yellow-700 px-4 py-2 rounded font-semibold cursor-pointer hover:bg-yellow-100">
            Valorar prestador (simulado)
          </button>
        </div>
      </div>
    </div>
  );
}
