
from bateria import Bateria
from estacion_base import EstacionBase
from herramienta import Herramienta
from obstaculo import Obstaculo


class Robot:
    """Clase Base (Superclase) Robot."""
    def __init__(self, bateria_carga: int, posicionX: float, posicionY: float, voltaje_bat: float, marca_bat: str, estacion_base: EstacionBase):
        self.__bateria = bateria_carga         # - int bateria
        self._posicionX = posicionX            # # float posicionX
        self._posicionY = posicionY            # # float posicionY
        
        # Composición: El robot es dueño de su batería; se instancia internamente.
        self.__bateria_obj = Bateria(voltaje_bat, marca_bat)
        
        # Agregación: Lista de herramientas que el robot puede llevar (opcional)
        self._herramientas = []

        # Asociación obligatoria (Se pasa por parámetro al nacer) Puede ser opcional
        self._estacion_base = estacion_base

    def encender(self) -> bool:
        print("Robot encendiéndose...")
        return True

    def mover(self, x: float, y: float) -> None:
        self._posicionX = x
        self._posicionY = y
        print(f"Robot movido a la posición X: {x}, Y: {y}")

    def getBateria(self) -> int:
        return self.__bateria

    def agregar_herramienta(self, herramienta: Herramienta) -> None:
        """Método de agregación para asociar herramientas al robot."""
        self._herramientas.append(herramienta)
        print(f"Herramienta '{herramienta.get_nombre()}' agregada al robot.")

    # --- Relación de Dependencia / Uso ---
    def analizar_obstaculo(self, obstaculo: Obstaculo) -> None:
        """El Robot usa la clase Obstaculo de manera temporal pasándola como parámetro."""
        print("Analizando presencia de obstáculos...")
        distancia = obstaculo.calcularDistancia()
        if distancia < 2.0:
            print(f"¡Alerta! Obstáculo detectado a corta distancia ({distancia}m). Deteniendo robot.")
        else:
            print(f"Camino libre. Distancia al obstáculo: {distancia}m.")

    def reportar_a_base(self) -> None:
        """Usa la asociación obligatoria con la estación base."""
        print("Reportando estado a la estación base asignada...")
        self._estacion_base.transmitir_datos()