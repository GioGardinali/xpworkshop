

def converter(valor, taxa):
    if taxa <= 0:
        return -1
    if valor < 0:
        return -1
    if valor == 0:
        return 0
    resultado = (valor / taxa) * 0.989
    return  round(resultado, 2)