import React from "react";
import { useNavigate } from "react-router-dom";

export default function Home() {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh] text-center">
      <h1 className="text-3xl font-bold text-green-700 leading-tight">
        Tu Red de Prestadores Rurales
      </h1>
      <p className="mt-4 text-gray-800 text-lg max-w-md">
        Buscá, compará y contactá prestadores para tu campo.
        Una sola plataforma para servicios de siembra, cosecha, y más.
        <br />
        <span className="block text-green-900 font-semibold mt-2">Sin intermediarios.</span>
      </p>
      <button
        className="mt-8 px-8 py-2 text-lg rounded bg-green-700 text-white hover:bg-green-800 transition font-medium shadow"
        onClick={() => navigate("/prestadores")}
      >
        Buscar prestadores
      </button>
    </div>
  );
}
