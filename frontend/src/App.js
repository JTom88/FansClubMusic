import React from "react";
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import injectContext from "./store/appContext.js";
import { Navbar } from "./componentes/Navbar/Navbar.jsx"
import { Home } from "./paginas/Home/Home.jsx";
import { PageRegistro } from "./paginas/PageRegistro/PageRegistro"


function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <div className="App-content">
        <div className="page-content">
          <Routes>
            <Route path='/' element={<Home />} />
            <Route path='/formularioregistro' element={<PageRegistro />} />

          </Routes>
        </div>

      </div>
    </BrowserRouter>
  );
}

export default injectContext(App);  
