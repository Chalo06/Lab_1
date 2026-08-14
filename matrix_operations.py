"""Operaciones de matrices: suma, multiplicación, determinante e inversa."""


def matrix_sum(a, b):
    """Suma dos matrices del mismo tamaño, posición por posición."""
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones")
    return [
        [a[i][j] + b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


def matrix_multiply(a, b):
    """Multiplica A por B. Las columnas de A deben coincidir con las filas de B."""
    if len(a[0]) != len(b):
        raise ValueError("Las dimensiones no son compatibles para multiplicar")

    result = [[0.0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            result[i][j] = sum(a[i][k] * b[k][j] for k in range(len(b)))
    return result


def matrix_determinant(m):
    """Calcula el determinante de una matriz cuadrada por cofactores.

    Solo funciona con matrices NxN, ya que el determinante no existe
    para matrices rectangulares.
    """
    n = len(m)
    if n != len(m[0]):
        raise ValueError("El determinante requiere una matriz cuadrada")

    if n == 1:
        return m[0][0]
    if n == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    det = 0.0
    for col in range(n):
        minor = [row[:col] + row[col + 1:] for row in m[1:]]
        det += ((-1) ** col) * m[0][col] * matrix_determinant(minor)
    return det


def matrix_inverse(m):
    """Calcula la inversa de una matriz cuadrada usando la adjunta.

    Requiere que la matriz sea cuadrada y que su determinante no sea cero.
    """
    n = len(m)
    if n != len(m[0]):
        raise ValueError("La inversa requiere una matriz cuadrada")

    det = matrix_determinant(m)
    if det == 0:
        raise ValueError("La matriz no tiene inversa")

    if n == 1:
        return [[1 / m[0][0]]]

    cofactors = []
    for i in range(n):
        row = []
        for j in range(n):
            minor = [r[:j] + r[j + 1:] for k, r in enumerate(m) if k != i]
            row.append(((-1) ** (i + j)) * matrix_determinant(minor))
        cofactors.append(row)

    adjugate = [[cofactors[j][i] for j in range(n)] for i in range(n)]
    return [[val / det for val in row] for row in adjugate]