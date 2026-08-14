import typer

from aplication import Aplicacion
from matrix_loader import load_matrices_from_json

app = typer.Typer()
calculadora = Aplicacion()

@app.command()
def calcular(operacion: str, archivo_json:str):
    
    with open(archivo_json) as f:
        json_str = f.read()
    matrix_a, matrix_b = load_matrices_from_json(json_str)
    resultado = calculadora.ejecutar(operacion, matrix_a, matrix_b)
    typer.echo(resultado)
    
if __name__ == "__main__":
    app()