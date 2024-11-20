import React from "react";
import { Jumbotron } from "../../componentes/Jumbotron/Jumbotron";
import imgJumbo from "../../assets/imagenes_jumbotron/JumboHome.png";
import { SliderHome } from "../../componentes/SliderHome/SliderHome";

export const Home = () => {
  return (
    <div className="bg-color mb-3">
      <div>
        <Jumbotron
          imagenFondo={{
            backgroundImage: `url(${imgJumbo})`,
            backgroundPosition: "center 10%",
          }}
          subtitulo={"Ya no se me para el tiempo"}
          referencia={"home"}
        ></Jumbotron>
      </div>
      <div className="mt-3">
        <SliderHome />
      </div>
      {/* <div>
        <AgendaConciertos />
      </div>
      <div>
        <Videos />
      </div> */}
    </div>
  );
};
