class EstacionBase:
    """Clase para representar una Asociación con el Robot (ej. base de carga/comunicación)."""
    def __init__(self, codigo: str, ubicacion: str):
        self.__codigo = codigo
        self.__ubicacion = ubicacion

    def transmitir_datos(self) -> None:
        print(f"EstacionBase [{self.__codigo}] en '{self.__ubicacion}' sincronizando datos con el robot...")