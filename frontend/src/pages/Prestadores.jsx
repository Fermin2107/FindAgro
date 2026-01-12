import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { getPrestadores } from "../api/prestadores";
import PrestadorCard from "../components/PrestadorCard";

export default function Prestadores() {
  const [prestadores, setPrestadores] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    setLoading(true);
    getPrestadores()
      .then(setPrestadores)
      .catch(() => setError("No se pudieron cargar los prestadores"))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4 text-green-900">Prestadores disponibles</h2>
      {loading && <div className="text-green-700">Cargando...</div>}
      {error && <div className="text-red-600">{error}</div>}
      {!loading && !error && prestadores.length === 0 && (
        <div className="text-gray-500 mt-8">No hay prestadores disponibles.</div>
      )}
      <div>
        {prestadores.map((p) => (
          <PrestadorCard
            key={p.id}
            prestador={p}
            onClick={() => navigate(`/prestadores/${p.id}`)}
          />
        ))}
      </div>
    </div>
  );
}
