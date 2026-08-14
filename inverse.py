"""Operacion de inversa de una matriz cuadrada."""

from Operaciones import Operacion
from matrix_operations import matrix_inverse

class Inverse(Operacion):
    """Calcula la inversa de matrixA."""
    
    def SetMatrix(self, index: str, matrix: list[list[float]]) -> None:
        
        """Guarda una matriz bajo el identificador indicado.

        Args:
            index: Identificador de la matriz ("matrixA" o "matrixB").
            matrix: Matriz a almacenar como lista de listas de floats.
        """
        
        self.matrices[index] = matrix
        
    def Compute(self):
        
        """Calcula la inversa de matrixA.

        Returns:
            Matriz inversa de matrixA.

        Raises:
            Error: Si matrixA no fue cargada con SetMatrix.
            ValueError: Si matrixA no es cuadrada o no tiene inversa.
        """

        return matrix_inverse(self.matrices["matrixA"])
    
    def Clear(self) -> None:
        """Limpia las matrices almacenadas."""
        self.matrices = {}
        
        
        