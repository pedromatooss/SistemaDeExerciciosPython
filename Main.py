import os
import time

import Hanoi
import ListaSequencial
import ListaDecisao
import ListaRepeticao


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


tempo = 3

while True:
    limpar_tela()

    print("EXERCICIOS PYTHON-------")
    print("1 - ESTRUTURA SEQUENCIAL")
    print("2 - ESTRUTURA DECISÃO")
    print("3 - ESTRUTURA REPETIÇÃO")
    print("4 - TORRE DE HANOI RESOLUÇÃO")
    print("0 - SAIR")

    try:
        opcao = int(input("Escolha: "))
    except:
        print("Digite um número válido!")
        time.sleep(tempo)
        continue

    limpar_tela()

    match opcao:
        case 0:
            print("Saindo...")
            for i in range(3):
                time.sleep(1)
                print("...")
            break

        case 1:
            ListaSequencial.executar()

        case 2:
            ListaDecisao.executar()

        case 3:
            ListaRepeticao.executar()

        case 4: 
            x = int(input("Digite o número de pilhas da torre: "))
            Hanoi.executar(x)

        case _:
            print("Opção inválida!")

    time.sleep(tempo)