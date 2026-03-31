def executar():
    print("ESTRUTURA SEQUENCIAL\n")
    opcao = int(input("EXERCICIOS (1 ao 10) ou 0 para sair: "))

    match opcao:
        case 0:
            return

        case 1:
            print("Enviar um numero-----------")
            x = int(input("Digite um numero: "))
            print(f"O numero é {x}")

        case 2:
            print("Somar Números--------------")
            x = int(input("Digite um numero: "))
            y = int(input("Digite outro numero: "))
            print(f"Soma: {x + y}")

        case 3:
            print("Calculo de nota-------------")
            n1 = int(input("Nota 1: "))
            n2 = int(input("Nota 2: "))
            n3 = int(input("Nota 3: "))
            n4 = int(input("Nota 4: "))
            print(f"Média: {(n1+n2+n3+n4)/4}")

        case 4:
            print("conversor de Metros----------")
            metros = int(input("Metros: "))
            print(f"Em cm: {metros * 100}")

        case 5:
            print("calulo de Raio---------------")
            raio = int(input("Raio: "))
            print(f"Área: {3.14 * raio**2}")

        case _:
            print("Opção inválida!")