def mostrar_encabezado_escuela():
    print("Instituto x")
    print("Reporte y evaluacion de calificaciones")
    
def nota_minima_aprobatoria():
    return 6.0

def evaluar_rendimiento(nota_final):
    if nota_final < 7.0:
        return "Reprobado"
    elif 7.0 <= nota_final <= 9.4:
        return "Aprobado"
    elif nota_final >= 9.5:
        return "Excelente"

def calcular_promedio_ponderado(nota_examenes, nota_tareas):
    calificacion_final = (nota_examenes * 0.70) + (nota_tareas * 0.30)
    return round (calificacion_final, 1)

def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    nota_final= calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima= nota_minima_aprobatoria()
    estado_academico= evaluar_rendimiento(nota_final)

    print(f"Alumno: {nombre_alumno}" )
    print(f"Nota final: {nota_final}")
    print(f"Estado academico: {estado_academico}")
    if nota_final < nota_minima:
        print("El estudiante necesita presentar examen extraordinario")
mostrar_encabezado_escuela()
generar_boleta("Ana", 8.5, 9.0)