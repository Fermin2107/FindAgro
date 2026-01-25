import React, { useEffect, useState } from "react";
import { getPrestadorMetricas } from "../api/eventos";

export default function PanelPrestadorMetricas({ prestadorId }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    getPrestadorMetricas(prestadorId)
      .then(setData)
      .catch(() => setData(null))
      .finally(() => setLoading(false));
  }, [prestadorId]);

  if (loading) return <div className="text-gray-500">Cargando métricas...</div>;
  if (!data) return <div className="text-red-500">No disponible</div>;

  return (
    <div className="my-4 bg-green-50 rounded p-3 border border-green-200">
      <h4 className="font-semibold text-green-700 mb-2">Métricas del Prestador</h4>
      <div className="space-y-1 text-sm">
        <div>Total vistas: <span className=" font-bold">{data.total_vistas}</span></div>
        <div>Total contactos: <span className=" font-bold">{data.total_contactos}</span></div>
        <div>
          Contactos por canal:
          <ul className="ml-3 list-disc text-gray-700">
            {Object.entries(data.contactos_por_canal).map(([canal, n]) =>
              <li key={canal}>{canal}: <span className=" font-bold">{n}</span></li>
            )}
          </ul>
        </div>
        <div>
          Últimos 7 días - Vistas: <span className=" font-bold">{data.ultimos_7_dias.vistas}</span>, Contactos: <span className=" font-bold">{data.ultimos_7_dias.contactos}</span>
        </div>
        <div>
          Últimos 30 días - Vistas: <span className=" font-bold">{data.ultimos_30_dias.vistas}</span>, Contactos: <span className=" font-bold">{data.ultimos_30_dias.contactos}</span>
        </div>
      </div>
    </div>
  );
}
