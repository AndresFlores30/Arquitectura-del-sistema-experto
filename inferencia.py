from base_conocimiento import base_conocimiento

def inferir(memoria):
    resultados = []
    for enfermedad, sintomas in base_conocimiento.items():
        if all(s in memoria for s in sintomas):
            resultados.append(enfermedad)
    return resultados