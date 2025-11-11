from clases.persona import Persona

persona1 = Persona("nombre_persona_1", "apellido_persona_1", "telefono_persona_1", "corre_elec_persona_1")

print(persona1.get_nombre())

print(persona1.correo_elec)

persona1.set_correo_elec="nuevocorreo@email.com"

print(persona1.correo_elec)