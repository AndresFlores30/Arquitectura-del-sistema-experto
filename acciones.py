def ejecutar_accion(diagnostico):
    if "gripe" in diagnostico:
        print("Recomendación: reposo y tomar líquidos")
    elif "resfriado" in diagnostico:
        print("Recomendación: usar descongestionante")
    else:
        print("Consulta a un médico")