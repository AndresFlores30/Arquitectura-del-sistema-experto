from base_conocimiento import base_conocimiento

def aprender(enfermedad, sintomas):
    if enfermedad in base_conocimiento:
        print(f"Actualizando conocimiento de {enfermedad}")
        base_conocimiento[enfermedad] = list(set(base_conocimiento[enfermedad] + sintomas))
    else:
        print(f"Aprendiendo nueva enfermedad: {enfermedad}")
        base_conocimiento[enfermedad] = sintomas