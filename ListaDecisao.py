def executar():
    print("ESTRUTURA DE DECISÃO\n")
    opcao = int(input("EXERCICIOS (1 ao 10) ou 0 para sair: "))

    match opcao:
        case 0:
            return

        case 1:
            n1 = int(input("Numero 1: "))
            n2 = int(input("Numero 2: "))

            if n1 > n2:
                print(f"Maior: {n1}")
            elif n2 > n1:
                print(f"Maior: {n2}")
            else:
                print("São iguais")

        case _:
            print("Opção inválida!")