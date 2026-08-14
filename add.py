"""Operacion de suma de dos matrices."""

from Operaciones import Operacion
from matrix_operations import matrix_sum

class Add(Operacion):
    
    """Suma dos matrices del mismo tamano usando matrixA y matrixB."""
    
    def SetMatrix(self, index: str, matrix: list[list[float]]) -> None:
        
        """Guarda una matriz bajo el identificador indicado.

        Args:
            index: Identificador de la matriz ("matrixA" o "matrixB").
            matrix: Matriz a almacenar como lista de listas de floats.
        """
        
        self.matrices[index] = matrix
        
    def Compute(self):
        
        """Calcula la suma de matrixA y matrixB.

        Returns:
            Matriz resultado de sumar matrixA con matrixB.

        Raises:
            KeyError: Si matrixA o matrixB no fueron cargadas con SetMatrix.
            ValueError: Si las matrices no tienen las mismas dimensiones.
        """
        
        return matrix_sum(self.matrices["matrixA"], self.matrices["matrixB"])
    
    def Clear(self) -> None:
        """Limpia las matrices almacenadas."""
        
        self.matrices = {}
        
        
        