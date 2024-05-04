import porcentajes
import click

@click.group()
def mycommands():
    pass

@click.command()
@click.option("--name", prompt="Ingrese su nombre", help="Este comando te explica como usar este archivo")
def hello(name):
    click.echo(f"Hello {name}!")

@click.command()
@click.argument("pc1", type=float)
@click.argument("pc2", type=float)
@click.argument("pp", type=float)
def calcular_notas(pc1,pc2,pp):
    nota = porcentajes.corte(pc1,pc2,pp)
    print(f"Nota definitiva del corte: {nota}")

@click.command()
@click.argument("nota", type=float)
@click.argument("ponderacion", type=int)
def equivalente(nota, ponderacion):
    equivalente = porcentajes.equivalente(nota,ponderacion)
    print(f"El equivalente de la nota es: {equivalente}")

@click.command()
@click.argument("pc1", type=float, required=0)
@click.argument("pc2", type=float, required=0)
@click.argument("pp", type=float, required=0)
@click.argument("notasfile", type=click.Path(exists=False), required=0)
@click.option("-c", "--corte", prompt="Indique el número del corte ", type=int ,help="Debe escribir el número del corte primero, seguido de las notas de las dos pruebas cortas y luego de la nota parcial")
def registrar_corte(corte, pc1, pc2, pp, notasfile):
    filename = notasfile if notasfile is not None else "notas.txt"
    definitiva = porcentajes.corte(pc1,pc2,pp)
    with open(filename, "a+") as f:
        f.write(f"Corte {corte}: Prueba corta 1: [{pc1}], Prueba corta 2: [{pc2}], Parcial: [{pp}], Definitiva del corte: [{definitiva}]\n")

mycommands.add_command(hello)
mycommands.add_command(calcular_notas)
mycommands.add_command(equivalente)
mycommands.add_command(registrar_corte)

if __name__ == "__main__":
    mycommands()