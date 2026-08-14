"""Carga de matrices desde formato JSON."""
import json


class MatrixFormatError(Exception):
    """Las dimensiones que vienen en el JSON no coinciden con los datos."""


def load_matrix_from_dict(matrix_dict):
    """Convierte una matriz en formato dict (rows, cols, data) a floats."""
    rows = matrix_dict["rows"]
    cols = matrix_dict["cols"]
    data = matrix_dict["data"]

    if len(data) != rows or any(len(row) != cols for row in data):
        raise MatrixFormatError("Las dimensiones no coinciden con los datos")

    return [[float(value) for value in row] for row in data]


def load_matrices_from_json(json_str):
    """Lee un JSON con matrixA y matrixB y devuelve ambas ya listas para usar."""
    payload = json.loads(json_str)
    matrix_a = load_matrix_from_dict(payload["matrixA"])
    matrix_b = load_matrix_from_dict(payload["matrixB"])
    return matrix_a, matrix_b