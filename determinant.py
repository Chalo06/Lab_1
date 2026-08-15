"""Operacion de determinante de una matriz cuadrada."""

from Operaciones import Operacion
from matrix_operations import matrix_determinant

class Determinant(Operacion):
    """Calcula el determinante de matrixA."""
    
    def SetMatrix(self, index: str, matrix: list[list[float]]) -> None:
        """Guarda una matriz bajo el identificador indicado.

        Args:
            index: Identificador de la matriz ("matrixA" o "matrixB").
            matrix: Matriz a almacenar como lista de listas de floats.
        """
        
        self.matrices[index] = matrix
        """Calcula el determinante de matrixA.

        Returns:
            Determinante de matrixA como float.

        Raises:
            Error: Si matrixA no fue cargada con SetMatrix.
            ValueError: Si matrixA no es cuadrada.
        """
        
    def Compute(self):
        return matrix_determinant(self.matrices["matrixA"])
    
    def Clear(self) -> None:
        
        """Limpia las matrices almacenadas."""
        
        self.matrices = {}
        
        
        