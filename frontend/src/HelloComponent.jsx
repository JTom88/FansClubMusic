import React, { useEffect, useContext } from "react";
import { Context } from "./store/appContext";  // Importamos el contexto

function HelloComponent() {
  const { store, actions } = useContext(Context);  // Usamos el contexto para acceder al estado y las acciones

  // Usamos useEffect para obtener el mensaje cuando el componente se monte
  useEffect(() => {
    actions.fetchMessage();  // Llamamos a la acción para obtener el mensaje
  }, [actions]);

  return (
    <div>
      <h1>{store.message || "Cargando..."}</h1>  {/* Mostramos el mensaje */}
    </div>
  );
}

export default HelloComponent;
