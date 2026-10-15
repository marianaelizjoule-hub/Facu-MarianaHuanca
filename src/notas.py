"""
Proyecto Integrador: Registro de Notas Universitario.

Práctica Semana 1 - Clean Code.
Módulo de gestión de estudiantes.
"""

base_datos = {
    "estudiantes": {},
    "notas": {}
}


def registrar_estudiante(codigo, nombre):
    """
    Registra un estudiante en el sistema.

    Args:
        codigo (str): Código único del estudiante.
        nombre (str): Nombre completo del estudiante.

    Returns:
        bool: True si el registro fue exitoso.
    """
    if codigo in base_datos["estudiantes"]:
        return False

    base_datos["estudiantes"][codigo] = nombre
    return True


def ingresar_nota_parcial():
    """Pendiente de implementación."""
    raise NotImplementedError


def ingresar_nota_final():
    """Pendiente de implementación."""
    raise NotImplementedError


def calcular_promedio():
    """Pendiente de implementación."""
    raise NotImplementedError


def eliminar_registro():
    """Pendiente de implementación."""
    raise NotImplementedError
