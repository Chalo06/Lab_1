"""Clase Aplicacion: conecta el nombre de una operacion con su instancia."""

from add import Add
from multiply import Multiply
from inverse import Inverse
from determinant import Determinant
from Operaciones import Operacion

class Aplicacion:
    """Administra las operaciones disponibles de la calculadora de matrices."""
    
    def __init__(self) -> None:
        """Inicializa el diccionario de operaciones soportadas."""
        self.operaciones : dict [str, Operacion] = {
            "suma": Add(),
            "multiplicacion": Multiply(),
            "determinante": Determinant(),
            "inversa": Inverse(),
        }
        
    def obtener_operacion(self, nombre: str) -> Operacion:
        """Busca la instancia de operacion segun su nombre.

        Args:
            nombre: Nombre de la operacion (ej. "suma").

        Returns:
            La instancia de Operacion correspondiente.

        Raises:
            KeyError: Si el nombre no existe en el diccionario de operaciones.
        """
        if nombre not in self.operaciones:
            raise KeyError(f"Operacion '{nombre}' no implementada en la calculadora")
        return self.operaciones[nombre]
    
    def ejecutar(self, nombre:str, matrix_a, matrix_b=None):
        
        """Ejecuta una operacion cargando las matrices necesarias.

        Args:
            nombre: Nombre de la operacion a ejecutar.
            matrix_a: Primera matriz (matrixA).
            matrix_b: Segunda matriz (matrixB), solo para suma/multiplicacion.

        Returns:
            El resultado de Compute() para esa operacion.
        """
        
        operacion = self.obtener_operacion(nombre)
        operacion.Clear()
        operacion.SetMatrix("matrixA", matrix_a)
        if matrix_b is not None:
            operacion.SetMatrix("matrixB", matrix_b)
            
        return operacion.Compute()