"""Prueba de las operaciones de matrices sobre datos en formato JSON.

Verifica que la carga y las cuatro operaciones funcionen
correctamente usando dos matrices cuadradas 3x3."""
from matrix_loader import load_matrices_from_json
from matrix_operations import (
    matrix_sum,
    matrix_multiply,
    matrix_determinant,
    matrix_inverse,
)

JSON_MATRICES = """
{
  "matrixA": {
    "rows": 3, "cols": 3,
    "data": [[2.0, 0.0, 1.0], [1.0, 3.0, 2.0], [0.0, 1.0, 4.0]]
  },
  "matrixB": {
    "rows": 3, "cols": 3,
    "data": [[1.0, 2.0, 0.0], [0.0, 1.0, 3.0], [2.0, 0.0, 1.0]]
  }
}
"""


def main():
    """Ejecuta las cuatro operaciones sobre las matrices y muestra los resultados."""
    matrix_a, matrix_b = load_matrices_from_json(JSON_MATRICES)

    print("matrixA:", matrix_a)
    print("matrixB:", matrix_b)

    print("\nSuma:", matrix_sum(matrix_a, matrix_b))
    print("Multiplicacion:", matrix_multiply(matrix_a, matrix_b))
    print("Determinante A:", matrix_determinant(matrix_a))
    print("Determinante B:", matrix_determinant(matrix_b))
    print("Inversa A:", matrix_inverse(matrix_a))
    print("Inversa B:", matrix_inverse(matrix_b))


if __name__ == "__main__":
    main()