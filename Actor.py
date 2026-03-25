class Actor(GameObject):
    def __init__(self, nombre: str, integridad: int):
        super().__init__(nombre)
        self._integridad : int = integridad

    def esta_vivo(self) -> bool:
        return self._integridad > 0

    @abstractmethod
    def obtener_reporte(self) -> str:
        pass
