from estacion_base import EstacionBase
from herramienta import Herramienta
from obstaculo import Obstaculo
from robot_limpiador import RobotLimpiador


if __name__ == "__main__":

    # 1. Primero creamos la Estación Base (Asociación)
    base_central = EstacionBase("EB-001", "Laboratorio Principal")
    
    # 2. Crear un Robot Limpiador (Composición integrada de Batería)
    limpiador = RobotLimpiador(
        bateria=85, 
        posicionX=0.0, 
        posicionY=0.0, 
        voltaje_bat=12.5, 
        marca_bat="Duracell", 
        base_central=base_central,
        capacidadContenedor=2
    )
    
    limpiador.encender()
    limpiador.mover(3.5, 2.0)
    limpiador.aspirar()
    limpiador.reportar_a_base()
    print(f"Batería actual: {limpiador.getBateria()}%")

    # 3. Agregar una Herramienta (Agregación)
    escoba = Herramienta("Cepillo lateral", 0.5)
    limpiador.agregar_herramienta(escoba)

    print("-" * 40)

    # 4. Interactuar con un Obstáculo (Dependencia)
    obstaculo = Obstaculo(1.2)
    limpiador.analizar_obstaculo(obstaculo)