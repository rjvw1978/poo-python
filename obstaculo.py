class Obstaculo:
    """Clase Obstáculo con relación de Dependencia/Uso."""
    def __init__(self, distancia: float):
        self.__distancia = distancia  # - float distancia

    def calcularDistancia(self) -> float:
        print(f"Calculando distancia al obstáculo...")
        return self.__distancia