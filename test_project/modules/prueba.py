from omniauto import ui, data

@ui()
def saludar(nombre: str):
    return f"Hola {nombre} desde TestPyPI!"

@data()
def sumar(a: int, b: int):
    return a + b
