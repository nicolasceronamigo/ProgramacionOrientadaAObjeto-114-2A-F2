from clases.tienda import Tienda
from clases.mascota import Mascota

tienda1 = Tienda("Veterinaria1")
tienda2 = Tienda("Veterinaria2")

mascota1 = Mascota("nombre_mascota_1", "especie1", 1)
mascota2 = Mascota("nombre_mascota_2", "especie2", 2)
mascota3 = Mascota("nombre_mascota_3", "especie3", 3)

tienda1.registrar_mascota(mascota1)
tienda1.registrar_mascota(mascota2)
tienda1.registrar_mascota(mascota3)

tienda1.consultar_listado()
print("")
print(tienda1.buscar_mascota("nombre_mascota_3"))
print("")
print(tienda1.buscar_mascota("nombre_mascota_4"))
print("")
print(tienda1.calcular_edad_promedio_mascotas())
print("")
print(tienda2.calcular_edad_promedio_mascotas())
print("")
print(tienda1.ver_estado_registro())
print("")
print(tienda2.ver_estado_registro())
print("")
print(tienda1.ver_estado_registro(True))
print("")
print(tienda2.ver_estado_registro(True))