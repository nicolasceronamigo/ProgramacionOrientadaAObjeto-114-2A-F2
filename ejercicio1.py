# Implementa una función son_anagramas(a: str, b: str) ->
# bool que determine si dos cadenas son anagramas entre sí.

# Reglas
# Ignora espacios en blanco (espacio, tab, salto de línea).
# No distingue entre mayúsculas y minúsculas.
# Considera el resto de caracteres tal cual (letras con tilde, signos, números).

# Definición de anagrama
# Dos cadenas son anagramas si, tras normalizarlas, contienen
# exactamente las mismas letras con la misma frecuencia.

# Requisitos
# No usar clases ni librerías externas.
# No imprimir dentro de la función.

def son_anagramas(a:str, b:str) -> bool:
    a_min = a.lower()
    b_min = b.lower()
    
    a_sin_espacio = a_min.replace(" ", "")
    b_sin_espacio = b_min.replace(" ", "")
    
    if len(a_sin_espacio) == len(b_sin_espacio):
        dicc_letras_a = {}
        dicc_letras_b = {}
        for posicion in range(len(a_sin_espacio)):
            if a_sin_espacio[posicion] in dicc_letras_a.keys():
                dicc_letras_a[a_sin_espacio[posicion]] += 1
            else:
                dicc_letras_a[a_sin_espacio[posicion]] = 1
            if b_sin_espacio[posicion] in dicc_letras_b.keys():
                dicc_letras_b[b_sin_espacio[posicion]] += 1
            else:
                dicc_letras_b[b_sin_espacio[posicion]] = 1
        return dicc_letras_b == dicc_letras_a
    else:
        return False


print(son_anagramas("o mOr a", "R OOM a"))
print("")
print(son_anagramas("Ao mor", "R OM aa"))