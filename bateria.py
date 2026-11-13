class Bateria:
    """Clase Batería en relación de Composición con Robot."""
    def __init__(self, voltaje: float, marca: str):
        self.__voltaje = voltaje  # - float voltaje
        self.__marca = marca      # - String marca

    def recargar(self) -> None:
        print(f"Recargando la batería marca {self.__marca} ({self.__voltaje}V)...")