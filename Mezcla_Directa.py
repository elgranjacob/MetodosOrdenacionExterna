def merge_sort(lista, depth=0):
    print(f"Dividiendo: {lista}")
    
    if len(lista) < 2:
        print(f"Lista base alcanzada: {lista}")
        return lista
    
    middle = len(lista) // 2
    left = merge_sort(lista[:middle], depth + 1)
    right = merge_sort(lista[middle:], depth + 1)
    
    merged = merge(left, right)
    print(f"Fusionando: {left} + {right} -> {merged}")
    return merged

def merge(lista1, lista2):
    result = []
    i, j = 0, 0
    
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
    
    result += lista1[i:]
    result += lista2[j:]
    return result

lista = [31, 3, 88, 1, 4, 2, 42]
print("Proceso de Merge Sort:")
merge_sort_result = merge_sort(lista)
print("\nResultado final:", merge_sort_result)
