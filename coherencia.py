from base_conocimiento import base_conocimiento

def verificar_coherencia():
    for enfermedad, sintomas in base_conocimiento.items():
        if not sintomas:
            print(f"Error: {enfermedad} no tiene síntomas definidos")