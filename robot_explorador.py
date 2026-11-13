
from robot import Robot


class RobotExplorador(Robot):
    """Subclase RobotExplorador que hereda de Robot."""
    def __init__(self, bateria: int, posicionX: float, posicionY: float, voltaje_bat: float, marca_bat: str, base_central: EstacionBase, tipoCamara: str):
        super().__init__(bateria, posicionX, posicionY, voltaje_bat, marca_bat, base_central)
        self.__tipoCamara = tipoCamara  # - String tipoCamara

    def tomarFoto(self) -> None:
        print(f"Tomando fotografía con la cámara tipo: {self.__tipoCamara}.")