import porcentajes
import json_manager
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
def calcular_nota_total_corte(pc1,pc2,pp):
    assert pc1 > 20 or pc2 > 20 or pp > 20, 'Las notas no pueden ser mayores a 20'
    nota = porcentajes.corte(pc1,pc2,pp)
    print(f"Nota definitiva del corte: {nota}")

@click.command()
@click.argument("nota", type=float)
@click.argument("ponderacion", type=int)
def equivalente(nota, ponderacion):
    assert nota <= 20, 'Las notas no pueden ser mayores a 20'
    equivalente = porcentajes.equivalente(nota,ponderacion)
    print(f"El equivalente de la nota es: {equivalente}")

@click.command()
@click.argument("pc1", type=float, required=0)
@click.argument("pc2", type=float, required=0)
@click.argument("pp", type=float, required=0)
@click.argument("notasfile", type=click.Path(exists=False), required=0)
@click.option("-c", "--corte", prompt="Indique el número del corte ", type=int ,help="Debe escribir el número del corte primero, seguido de las notas de las dos pruebas cortas y luego de la nota parcial")
def calcular_corte(corte, pc1, pc2, pp, notasfile):
    assert pc1 <= 20 or pc2 <= 20 or pp <= 20, 'Las notas no pueden ser mayores a 20'
    filename = notasfile if notasfile is not None else "notas.txt"
    definitiva = porcentajes.corte(pc1,pc2,pp)
    with open(filename, "a+") as f:
        f.write(f"Corte {corte}: Prueba corta 1: [{pc1}], Prueba corta 2: [{pc2}], Parcial: [{pp}], Definitiva del corte: [{definitiva}]\n")

@click.command()
def leer_cortes():
    corte = json_manager.read_json()
    for data in corte:
        print(f"{data['corte']} - {data['pc1']} - {data['pc2']} - {data['pp']} - {data['defi']}")

@click.command()
@click.argument("pc1", type=int, required=0)
@click.argument("pc2", type=int, required=0)
@click.argument("pp", type=int, required=0)
@click.argument("defi", type=float, required=False)
@click.option("--corte", required=True, help="Indique el número del corte que desea registrar")
@click.pass_context
def registrar_corte(ctx, corte, pc1,pc2,pp, defi):
    if not corte:
        ctx.fail('Falta el número de corte o ha ingresado un dato no valido')
    else:
        assert pc1 <= 20 or pc2 <= 20 or pp <= 20, 'Las notas no pueden ser mayores a 20'
        data = json_manager.read_json()
        new_corte = len(data) + 1
        defi = porcentajes.corte(pc1,pc2,pp)
        update_corte = {
            "corte": new_corte,
            "pc1": pc1,
            "pc2": pc2,
            "pp": pp,
            "defi": defi
        }
        data.append(update_corte)
        json_manager.write_json(data)
        print('Datos registrados satisfactoriamente')
        

mycommands.add_command(hello)
mycommands.add_command(calcular_nota_total_corte)
mycommands.add_command(equivalente)
mycommands.add_command(calcular_corte)
mycommands.add_command(leer_cortes)
mycommands.add_command(registrar_corte)

if __name__ == "__main__":
    mycommands()