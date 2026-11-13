
from estacion_base import EstacionBase
from robot import Robot

class RobotLimpiador(Robot):
    """Subclase RobotLimpiador que hereda de Robot."""
    def __init__(self, bateria: int, posicionX: float, posicionY: float, voltaje_bat: float, marca_bat: str, base_central: EstacionBase,  capacidadContenedor: int):
        super().__init__(bateria, posicionX, posicionY, voltaje_bat, marca_bat, base_central)
        self.__capacidadContenedor = capacidadContenedor  # - int capacidadContenedor

    def aspirar(self) -> None:
        print(f"RobotLimpiador aspirando. Capacidad del contenedor: {self.__capacidadContenedor}L.")