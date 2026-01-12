import React from "react";

export default function Layout({ children }) {
  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      <header className="bg-green-700 text-white p-4 text-center font-bold text-xl shadow">
        Plataforma Rural de Servicios del Agro
      </header>
      <main className="flex-1 w-full max-w-2xl mx-auto p-4">{children}</main>
      <footer className="text-xs text-gray-500 py-2 text-center border-t mt-4">
        &copy; {new Date().getFullYear()} Mercado Rural · MVP en validación
      </footer>
    </div>
  );
}
