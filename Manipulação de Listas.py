lista = []
print("-" * 45)
print("Bem vindo ao programa \033[1m'Tudo em volta de listas'\033[m.")
print("Lista de opções: ")
print("\033[1;32;40mAdicionar\033[m")
print("append = adicionar no fim.")
print("extend = adiciona múltiplos elementos (separados por espaço).")
print("insert = adiciona um elemento no índice indicado.")
print("-" * 45)
print("\033[1;31;40mRemover/Limpar\033[m")
print("remove = remove a primeira ocorrência do elemento dado.")
print("pop = remove o elemento no índice especificado.")
print("clear = limpa a lista inteira.")
print("-" * 45)


def msg():
    print(f"Lista atualizada: {lista}")


def pedir_item_unico():
    return input("Digite um item (string única): ").strip()


def pedir_itens_multiplos():
    entrada = input("Digite itens separados por espaço: ").strip()
    # retorna lista de strings
    return entrada.split() if entrada else []


def perguntar_acao():
    return input("O que gostaria de fazer? (append/extend/insert/remove/pop/clear/sair) ").lower().strip()


def deseja_continuar():
    escolher = input("Gostaria de fazer mais alguma coisa? (s/n) ").lower().strip()
    return escolher in ("s", "sim", "claro", "obvio")


def confirmar_saida():
    saida = input("Tem certeza que deseja sair? (s/n) ").lower().strip()
    if saida in ("s", "sim", "claro", "obvio", "concerteza", "yha"):
        print("Programa encerrado.")
        return True
    return False


while True:
    acao = perguntar_acao()

    if acao == "append":
        item = pedir_item_unico()
        if item:
            lista.append(item)
            msg()
        else:
            print("Nenhum item informado.")

    elif acao == "extend":
        itens = pedir_itens_multiplos()
        if itens:
            lista.extend(itens)
            msg()
        else:
            print("Nenhum item informado para extender.")

    elif acao == "insert":
        item = pedir_item_unico()
        try:
            indice = int(input("Em qual índice deseja inserir? "))
            # Ajusta índice negativo e acima do tamanho naturalmente pelo insert
            lista.insert(indice, item)
            msg()
        except ValueError:
            print("Índice inválido. Digite um número inteiro.")

    elif acao == "remove":
        if not lista:
            print("A lista está vazia. Nada para remover.")
        else:
            item = pedir_item_unico()
            try:
                lista.remove(item)  # remove a primeira ocorrência do valor exato
                msg()
            except ValueError:
                print(f"Item '{item}' não encontrado na lista.")

    elif acao == "pop":
        if not lista:
            print("A lista está vazia. Nada para remover.")
        else:
            try:
                indice = int(input("Qual índice deseja remover? "))
                # valida índice
                if -len(lista) <= indice < len(lista):
                    removido = lista.pop(indice)
                    print(f"Removido: {removido}")
                    msg()
                else:
                    print("Índice fora do intervalo da lista.")
            except ValueError:
                print("Índice inválido. Digite um número inteiro.")

    elif acao == "clear":
        if not lista:
            print("A lista já está vazia.")
        else:
            lista.clear()
            print("Lista limpa.")
            msg()

    elif acao == "sair":
        if confirmar_saida():
            break

    else:
        print("Comando inválido, tente novamente.")

    # pergunta somente após executar uma ação
    if not deseja_continuar():
        if confirmar_saida():
            break
