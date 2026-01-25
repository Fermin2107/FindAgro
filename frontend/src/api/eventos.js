const API_URL = import.meta.env.VITE_API_URL || "http://localhost:5000";

export async function registrarEvento({ prestador_id, tipo_evento, canal = null, usuario_id = null }) {
  const res = await fetch(`${API_URL}/eventos/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prestador_id, tipo_evento, canal, usuario_id }),
  });
  if (!res.ok) throw new Error("Error al registrar evento");
  const data = await res.json();
  return data.data;
}

export async function getPrestadorMetricas(id) {
  const res = await fetch(`${API_URL}/prestadores/${id}/metricas`);
  if (!res.ok) throw new Error("Error al obtener métricas");
  const data = await res.json();
  return data.data;
}
