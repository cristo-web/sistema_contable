"""
Módulo para la gestión de un libro diario contable.
Permite registrar transacciones y obtener resúmenes financieros.
"""
from typing import List, Dict, Any

class LibroDiario:
    """
    Clase que representa un libro diario contable.
    Permite agregar transacciones y calcular totales de ingresos y egresos.
    """

    def __init__(self) -> None:
        """Inicializa una nueva instancia del Libro Diario con una lista vacía de transacciones."""
        self.transacciones: List[Dict[str, Any]] = []

    def agregar_transaccion(self, fecha: str, descripcion: str, monto: float, tipo: str) -> None:
        """
        Agrega una nueva transacción al libro diario después de validar los datos.

        Args:
            fecha (str): La fecha de la transacción (ej. '2025-01-28').
            descripcion (str): Descripción breve de la transacción.
            monto (float): El valor monetario de la transacción. Debe ser positivo.
            tipo (str): El tipo de transacción. Debe ser 'ingreso' o 'egreso'.

        Raises:
            ValueError: Si el monto es negativo o el tipo no es válido.
        """
        # Validación de datos
        if monto <= 0:
            raise ValueError("El monto debe ser un número positivo.")

        tipo_normalizado = tipo.lower()
        if tipo_normalizado not in ["ingreso", "egreso"]:
            raise ValueError("El tipo de transacción debe ser 'ingreso' o 'egreso'.")

        self.transacciones.append({
            "fecha": fecha,
            "descripcion": descripcion,
            "monto": monto,
            "tipo": tipo_normalizado
        })

    def obtener_resumen(self) -> Dict[str, float]:
        """
        Calcula el total de ingresos y egresos registrados.

        Returns:
            Dict[str, float]: Un diccionario con las claves 'total_ingresos',
                              'total_egresos' y 'balance_neto'.
        """
        total_ingresos = 0.0
        total_egresos = 0.0

        for transaccion in self.transacciones:
            if transaccion["tipo"] == "ingreso":
                total_ingresos += transaccion["monto"]
            else:
                total_egresos += transaccion["monto"]

        # Separación de lógica de presentación: Retornamos datos, no texto
        return {
            "total_ingresos": total_ingresos,
            "total_egresos": total_egresos,
            "balance_neto": total_ingresos - total_egresos
        }

# Ejemplo de uso (bloque main para pruebas)
if __name__ == "__main__":
    LIBRO = LibroDiario()
    try:
        LIBRO.agregar_transaccion("2025-01-28", "Venta de servicios", 500.0, "ingreso")
        LIBRO.agregar_transaccion("2025-01-29", "Pago de luz", 120.50, "egreso")

        # Obtenemos los datos crudos
        REPORTE = LIBRO.obtener_resumen()

        # Capa de presentación (impresión) separada de la lógica
        print("Resumen Financiero:")
        print(f"Ingresos: ${REPORTE['total_ingresos']:.2f}")
        print(f"Egresos:  ${REPORTE['total_egresos']:.2f}")
        print(f"Balance:  ${REPORTE['balance_neto']:.2f}")

    except ValueError as e:
        print(f"Error al registrar transacción: {e}")
