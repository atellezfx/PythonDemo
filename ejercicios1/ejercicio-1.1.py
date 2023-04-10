# Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# Diferencias de duración
diferencia_con_min = 1 - (dalto_curso / otros_cursos_min)
print(f"El curso de Dalto dura un {diferencia_con_min:.2%} que el más rápido")

diferencia_con_max = 1 - (dalto_curso / otros_cursos_max)
print(f"El curso de Dalto dura un {diferencia_con_max:.2%} que el más lento")

diferencia_con_promedio = 1 - (dalto_curso / otros_cursos_promedio)
print(f"El curso de Dalto dura un {diferencia_con_promedio:.2%} que el promedio")
