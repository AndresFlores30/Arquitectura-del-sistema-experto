from base_conocimiento import base_conocimiento

def explicar(diagnosticos):
    for enfermedad in diagnosticos:
        print(f"\nDiagnóstico: {enfermedad}")
        print("Basado en los síntomas:", base_conocimiento[enfermedad])