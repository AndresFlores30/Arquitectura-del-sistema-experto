from memoria_trabajo import memoria_trabajo
from entrada_datos import obtener_sintomas
from inferencia import inferir
from acciones import ejecutar_accion
from explicacion import explicar
from coherencia import verificar_coherencia
from aprendizaje import aprender

# 1. Verificar coherencia
verificar_coherencia()

# 2. Obtener síntomas
memoria_trabajo.extend(obtener_sintomas())

# 3. Inferencia
diagnosticos = inferir(memoria_trabajo)

# 4. Resultados
if diagnosticos:
    explicar(diagnosticos)
    ejecutar_accion(diagnosticos)
else:
    print("No se pudo determinar un diagnóstico")

    # 5. Aprendizaje
    nueva_enfermedad = input("¿Cuál era la enfermedad? ")
    aprender(nueva_enfermedad, memoria_trabajo)