from buscador import (
    buscar_hoteles,
    buscar_restaurantes,
    buscar_actividades
)

from repositorio import (
    obtener_hoteles,
    obtener_restaurantes,
    obtener_actividades
)


class ServicioRecomendaciones:

    def __init__(self):

        self.hoteles = obtener_hoteles()

        self.restaurantes = obtener_restaurantes()

        self.actividades = obtener_actividades()


    def buscar(self,
               ciudad,
               presupuesto,
               fecha_inicio,
               fecha_fin,
               intereses):

        hoteles = buscar_hoteles(

            self.hoteles,

            ciudad,

            presupuesto,

            fecha_inicio,

            fecha_fin

        )

        restaurantes = buscar_restaurantes(

            self.restaurantes,

            ciudad,

            presupuesto

        )

        actividades = buscar_actividades(

            self.actividades,

            ciudad,

            intereses

        )

        return {

            "hoteles": hoteles,

            "restaurantes": restaurantes,

            "actividades": actividades

        }
