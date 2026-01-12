import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./pages/Home";
import Prestadores from "./pages/Prestadores";
import PrestadorDetalle from "./pages/PrestadorDetalle";

export default function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/prestadores" element={<Prestadores />} />
          <Route path="/prestadores/:id" element={<PrestadorDetalle />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}
