import React from "react";
import { Jumbotron } from "../../componentes/Jumbotron/Jumbotron";
import Jumbo_Registro from "../../assets/imagenes_jumbotron/Jumbo_Registro.jpg";
import { FormRegistro } from "../../componentes/FormRegistro/FormRegistro";


export const PageRegistro = () => {
    return (
        <div className="bg-color mb-3">
            <Jumbotron imagenFondo={{ backgroundImage: `url(${Jumbo_Registro})`, backgroundPosition: 'center 10%' }} subtitulo={"Lo siento, no me arrepiento"} referencia={'registro'} />
            <div className="text-center align-items-center d-flex">
                <FormRegistro />
            </div>
        </div>
    )
}