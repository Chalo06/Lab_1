"""Interfaz base para las operaciones de la calculadora de matrices."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List


class Operacion(ABC):
    """Contrato base que deben implementar todas las operaciones."""

    def __init__(self) -> None:
        self.matrices: Dict[str, List[List[float]]] = {}

    @abstractmethod
    def SetMatrix(self, index: str, matrix: List[List[float]]) -> None:
        """Guarda una matriz bajo un identificador (ej. "matrixA")."""
        pass

    @abstractmethod
    def Compute(self) -> Any:
        """Calcula el resultado usando las matrices ya cargadas."""
        pass

    @abstractmethod
    def Clear(self) -> None:
        """Limpia las matrices almacenadas."""
        pass