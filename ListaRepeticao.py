def executar():
    print("ESTRUTURA DE REPETIÇÃO\n")
    opcao = int(input("EXERCICIOS (1 ao 10) ou 0 para sair: "))

    match opcao:
        case 1: 
            print("Loop Simples------------")
            loop = True
            while loop: 
                nota = int(input("digite uma nota de 0 a 10: "))
                if (nota > 10 or nota < 0):
                    print("nota invalida, tente novamente")
                else: 
                    print("Obrigado pela nota XD")
                    loop = False
        case 2: 
            print("Usuario e senha----------")
            loop = True
            while loop: 
                usuario = input("Digite seu Nome de usuario: ")   
                senha = input("Digite a sua senha: ")           
                if (usuario == senha):
                    print("Senha igual ao Usuario, Digite uma nova senha: ")
                else: 
                    loop = False
        case _:
            print("opcao invalida!")
            