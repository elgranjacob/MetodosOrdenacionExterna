def dividir_lista(lista, tamano_chunk):
    
    print(f"\nDividiendo lista en chunks de tamaño {tamano_chunk}...")
    chunks = [lista[i:i + tamano_chunk] for i in range(0, len(lista), tamano_chunk)]
    for idx, chunk in enumerate(chunks):
        print(f"Chunk {idx}: {chunk}")
    return chunks


def intercalar_listas(lista1, lista2):
    
    print(f"Intercalando: {lista1} y {lista2}")
    resultado = []
    i = j = 0

    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])

    print(f"Resultado de la intercalación: {resultado}")
    return resultado


def ordenar_por_intercalacion(lista, tamano_chunk):
    
    print("\n=== Paso 1: Dividir y ordenar chunks ===")
    chunks = dividir_lista(lista, tamano_chunk)
    chunks = [sorted(chunk) for chunk in chunks]

    for idx, chunk in enumerate(chunks):
        print(f"Chunk ordenado {idx}: {chunk}")

   
    print("\n=== Paso 2: Intercalar chunks ===")
    iteracion = 1
    while len(chunks) > 1:
        print(f"\n--- Iteración {iteracion} ---")
        nuevos_chunks = []
        for i in range(0, len(chunks), 2):
            if i + 1 < len(chunks):
                print(f"Intercalando chunks {i} y {i + 1}")
                nuevo_chunk = intercalar_listas(chunks[i], chunks[i + 1])
                nuevos_chunks.append(nuevo_chunk)
            else:
                print(f"Chunk {i} pasa sin cambios")
                nuevos_chunks.append(chunks[i])
        chunks = nuevos_chunks

        for idx, chunk in enumerate(chunks):
            print(f"Chunk actualizado {idx}: {chunk}")
        iteracion += 1

    return chunks[0] if chunks else []



if __name__ == "__main__":
    lista_grande = [38, 27, 43, 3, 9, 82, 10, 56, 34, 29, 15, 72, 6, 50, 33]
    tamano_chunk = 5 
    print("Lista original:", lista_grande)

    lista_ordenada = ordenar_por_intercalacion(lista_grande, tamano_chunk)
    print("\nLista ordenada final:", lista_ordenada)
