# DECISIONS

## Fecha

15/10/2026

## Decisión

Implementar la función `registrar_estudiante()` como primera
funcionalidad del sistema de Registro de Notas Universitario.

## Justificación

Debido a que el registro de estudiantes es la base para las demás
funcionalidades del sistema, se decidió implementar primero esta
función antes del registro de notas y cálculo de promedios.

La función implementada es:

### registrar_estudiante(codigo, nombre)

Responsabilidad:

- Registrar un estudiante utilizando un código único.
- Evitar registros duplicados dentro del sistema.
- Almacenar la información del estudiante en la estructura
  de datos principal.

### Criterio arquitectónico aplicado

Se aplicó el principio de Responsabilidad Única
(Single Responsibility Principle - SRP),
perteneciente a los principios SOLID.

La función `registrar_estudiante()` tiene una única
responsabilidad: gestionar el registro de estudiantes.

Las funcionalidades relacionadas con notas, promedios y
eliminación de registros fueron separadas en funciones
independientes para mantener un bajo acoplamiento y facilitar
el mantenimiento del sistema.

### Beneficios obtenidos

- Mayor claridad en la lógica del sistema.
- Menor acoplamiento entre funcionalidades.
- Facilidad para realizar pruebas unitarias.
- Mejor mantenibilidad del código.
- Mayor facilidad para extender el sistema en futuras
  iteraciones.
- Cumplimiento de buenas prácticas de Clean Code y PEP 8.
