// Funciones para consumir la API de prestadores y sus detalles

const API_URL = https://github.com/Fermin2107/FindAgro || "http://localhost:5000";

// Listar prestadores (con filtros opcionales)
export async function getPrestadores({ localidad = "", servicio = "" } = {}) {
  const params = new URLSearchParams();
  if (localidad) params.append("localidad", localidad);
  if (servicio) params.append("servicio", servicio);
  const res = await fetch(`${API_URL}/prestadores/?${params.toString()}`);
  if (!res.ok) throw new Error("Error al cargar prestadores");
  const data = await res.json();
  return data.data;
}

// Obtener detalle de un prestador por id
export async function getPrestadorDetalle(id) {
  const res = await fetch(`${API_URL}/prestadores/${id}`);
  if (!res.ok) throw new Error("Error al cargar prestador");
  const data = await res.json();
  return data.data;
}
