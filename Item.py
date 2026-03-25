class Item(GameObject):
    def __init__(self, nombre: str, potencia: int, precio: int = 0):
        super().__init__(nombre)
        self.__potencia : int  = potencia
        self.__precio : int = precio

    @property
    def potencia(self):
        return self.__potencia

    def obtener_reporte(self) -> str:
        return f"[ITEM] {self.nombre} (Poder: {self.potencia})"
