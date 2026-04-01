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
            print("Conversor de Metros----------")
            metros = int(input("Metros: "))
            print(f"Em cm: {metros * 100}")

        case 5:
            print("Calulo de Raio---------------")
            raio = int(input("Raio: "))
            print(f"Área: {3.14 * raio**2}")
        
        case 6:
            print("Area do Quadrado-------------")
            lado = int(input("Lado: "))
            print(f"Área: {lado * lado}")

        case 7:
            print("Calculo de Salario------------")
            horas = int(input("Horas trabalhadas no Mês: "))
            ganho = int(input("Salario por hora: "))
            print(f"Salario do mês {horas * ganho}")

        case 8: 
            print("Temperatura em Celsius---------")

        case 9:
            print("Temperatura em Fahrenheit------")

        case 10: 
            print("Calculos com 3 números---------")
            x = int(input(""))
            y = int(input(""))
            z = int(input(""))
            print(f"O produto do dobro do primeiro com metade do segundo {(x * 2) * (y / 2)}")
            print(f"A soma do triplo do primeiro com o Terceiro{(x * 3) + z}")
            print(f"O terceiro elevadoao cubo {z ** 3}")

        case _:
            print("Opção inválida!")