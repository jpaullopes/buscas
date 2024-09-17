def main():
    #exemplo de dados númericos agora
    lista = [5, 3, 8, 1, 9, 2, 7, 4, 6]
    lista_ordenada = quick_sort(lista)
    valor_pesquisado = int(input('Informe o valor que você quer encontrar: '))
    posicao = busca_binaria(lista_ordenada,valor_pesquisado)
    
    if posicao == -1:
        print("O valor não foi encontrado")
    else:
        print(lista_ordenada)
        print(f'O valor {valor_pesquisado} está na posição número [{posicao}]')


#lembrando que para encontrar o valor, a lista tem que estar organizada
def busca_binaria(lista,valor,criterio = lambda a:a):
    left = 0
    right = len(lista) - 1

    while left <= right:
        meio = (left + right) // 2
        if criterio(lista[meio]) == valor:
            return meio
        elif criterio(lista[meio]) < valor:
            left = meio + 1
        elif criterio(lista[meio]) > valor:
            right = meio - 1
    #se o valor nao foi encontrado
    return -1


def quick_sort(lista,criterio = lambda a : a,reverse = False):
    if len(lista) < 2:
        return lista
    
    pivot = lista[0]
    left = [i for i in lista[1:] if criterio(i) < criterio(pivot)]
    right = [i for i in lista[1:] if criterio(i) >= criterio(pivot)]
    if reverse:
        return quick_sort(right, criterio, reverse) + [pivot] + quick_sort(left, criterio, reverse)
    return quick_sort(left, criterio, reverse) + [pivot] + quick_sort(right, criterio, reverse)
   

main()

