import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  root: ".", // asegura que frontend/ es root
  build: {
    outDir: "dist",
    emptyOutDir: true
  }
});
