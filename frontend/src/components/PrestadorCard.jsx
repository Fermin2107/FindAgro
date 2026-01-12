import React from "react";

// Card resumida de prestador, usada en listado
export default function PrestadorCard({ prestador, onClick }) {
  return (
    <div
      className="bg-white rounded-lg shadow p-4 mb-3 cursor-pointer border hover:border-green-600 transition"
      onClick={onClick}
      tabIndex={0}
      role="button"
    >
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h3 className="font-semibold text-lg mb-2 text-green-800">{prestador.usuario_id ? `Prestador #${prestador.id}` : "Prestador"}</h3>
          <p className="text-gray-700">{prestador.descripcion}</p>
          <div className="mt-1">
            <span className="text-green-700 text-sm font-medium">
              {prestador.localidad}
            </span>
            <span className="mx-2 text-gray-400">·</span>
            <span className="text-sm text-gray-700">
              {prestador.servicios.map(s => s.nombre).join(", ")}
            </span>
          </div>
        </div>
        <div className="mt-3 sm:mt-0 text-right flex flex-col items-end">
          <div className="text-yellow-600 text-base">
            {prestador.promedio_valoracion !== null && (
              <span>
                {"★ ".repeat(Math.round(prestador.promedio_valoracion))}
                <span className="text-gray-600">{prestador.promedio_valoracion} / 5</span>
              </span>
            )}
            {prestador.promedio_valoracion === null && (
              <span className="text-gray-400">Sin valoraciones aún</span>
            )}
          </div>
          <span className="text-xs text-gray-500">{prestador.cantidad_valoraciones} valoraciones</span>
        </div>
      </div>
    </div>
  );
}
