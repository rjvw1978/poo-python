class Herramienta:
    """Clase Herramienta en relación de Agregación con Robot."""
    def __init__(self, nombre: str, peso: float):
        self.__nombre = nombre  # - String nombre
        self.__peso = peso      # - float peso

    def get_nombre(self) -> str:
        return self.__nombre

    def get_peso(self) -> float:
        return self.__peso