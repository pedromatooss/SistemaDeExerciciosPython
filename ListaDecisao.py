def executar():
    print("ESTRUTURA DE DECISÃO\n")
    opcao = int(input("EXERCICIOS (1 ao 10) ou 0 para sair: "))

    match opcao:
        case 0:
            return

        case 1:
            print("Número Maior---------------")
            n1 = int(input("Numero 1: "))
            n2 = int(input("Numero 2: "))

            if n1 > n2:
                print(f"Maior: {n1}")
            elif n2 > n1:
                print(f"Maior: {n2}")
            else:
                print("São iguais")
        case 2: 
            print("Par ou Impar-----------------")
            num = int(input("Digite um número: "))
            if  num % 2 == 0: 
                print("Número é Par")
            else: 
                print("Número é impar")
        case 4: 
            print("Confirmação de Letra---------")
            letra = input("Digite F ou M: ")
            if letra.upper() == "F":
                print("FEMININO")
            elif letra.upper() == "M": 
                print("MASCULINO")
            else: 
                print("Outro")
        case 5: 
            print("Vogal ou Consoante-----------")
            letra = input("Digite uma letra do alfabeto: ")
            if letra.lower() == ("a" or "o" or "e" or "i" or "u"):
                print("É uma vogal")
            else: 
                print("É uma consoante")
            
        case 6: 
            print("RESULTADO FINAL--------------")
            n1 = int(input("Digite a primeira nota: "))
            n2 = int(input("Digite a segunda nota: "))
            media = (n1 + n2)/2
            print(f"A média:{media}") 
            if media >= 7 and media < 10:
                print("Aprovado!")
            elif media == 10: 
                print("Aprovado com distinção!")
            else: 
                print("Reprovado!")
        case 7: 
            print("Numero maior-----------------")
            num = []
            for i in range(3):
                n = int(input(f"Digite o número {i+1}: "))
                num.append(n)

            maior = num[0]

            for n in num: 
                if n > maior: 
                    maior = n
            
            print("Maior numero é ", maior)
        case 8: 
            print("Maior e Menor numero---------")
            numero = []
            for i in range(3):
                n = int(input("Digite um numero: "))
                numero.append(n)
            maior = numero[0]
            menor = numero[0]

            for n in numero:
                if n > maior:
                    maior = n
            print("Maior Numero: ", maior)
            
            for n in numero: 
                if n < menor: 
                    menor = n
            print("Menor numero", menor)


        case 9: 
            print("Calculo de Economia-----------")
            produtos = []
            for i in range(3): 
                preco = int(input(f"diga o preço do produto {i+1}: "))
                produtos.append(preco)

            menorPreco = produtos[0]
            for preco in produtos: 
                if preco < menorPreco: 
                    menorPreco = preco
            print(f"Você tá pobre, compra o desse preço: {menorPreco}")

        case 10: 
            print("Decrescente-------------------")
            num = []
            for i in range(3): 
                n = int(input(f"Digite um numero: "))
                num.append(n)

            #for n in num: 
              
        case _:
            print("Opção inválida!")