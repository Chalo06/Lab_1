"""Operacion de multiplicacion de dos matrices."""

from Operaciones import Operacion
from matrix_operations import matrix_multiply

class Multiply(Operacion):
    """Operacion de multiplicacion de dos matrices."""
    
    def SetMatrix(self, index: str, matrix: list[list[float]]) -> None:
        
        """Guarda una matriz bajo el identificador indicado.

        Args:
            index: Identificador de la matriz ("matrixA" o "matrixB").
            matrix: Matriz a almacenar como lista de listas de floats.
        """
        
        self.matrices[index] = matrix
        
    def Compute(self):
        
        """Calcula el producto matricial de matrixA por matrixB.

        Returns:
            Matriz resultado de multiplicar matrixA por matrixB.

        Raises:
            KeyError: Si matrixA o matrixB no fueron cargadas con SetMatrix.
            ValueError: Si las dimensiones no son compatibles para multiplicar.
        """
        
        return matrix_multiply(self.matrices["matrixA"], self.matrices["matrixB"])
    
    def Clear(self) -> None:
        
        """Limpia las matrices almacenadas."""
        
        self.matrices = {}
        
        
        