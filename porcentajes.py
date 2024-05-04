def corte(pc1,pc2,pp):
    corte_total = pc1*0.05 + pc2*0.05 + pp*0.15
    return corte_total

def pruebaCorta(nota):
    total = nota * 0.05
    return total

def equivalente(nota, pond):
    total = nota * (pond/100)
    return total