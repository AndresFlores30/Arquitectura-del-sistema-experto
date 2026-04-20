def obtener_sintomas():
    entrada = input("Ingresa síntomas separados por coma: ")
    sintomas = [s.strip() for s in entrada.split(",")]
    return sintomas