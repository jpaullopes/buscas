def main():
    #exemplos de dados do tipo string
    lista = ['frt', 'rtyu', 'arty', 'aeio', 'catacu', 'faxutio']
    #um exemplo de pesquisa, encontrar uma string com certo tamanho
    valor_pesquisado = int(input('Informe o tamanho da string que você quer encontrar: '))
    posicao = busca_linear_geral(lista,valor_pesquisado,lambda a : len(a))

    if posicao == -1:
        print("O valor não foi encontrado")
    else:
        print(lista)
        print(f'O valor {valor_pesquisado} está na posição número [{posicao}]')

#uma busca linear baseada em um criterio
def busca_linear_geral(lista,valor,criterio = lambda x:x):
    for i in range(len(lista)):
        if criterio(lista[i]) == valor:
            return i
    return - 1


main()