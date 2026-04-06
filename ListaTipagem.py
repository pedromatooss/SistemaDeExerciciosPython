import time
import os
from typing import TypeVar, Type, Optional, Union
from utils import pedir_tipado

T = TypeVar('T')

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#---- EXercicios ---

def ex_hints_basicos():
    print("=== Type Hints Básicos ===")
    def somar(a: int, b: int) -> int: 
        return a + b
    
    def apresentar(nome: str, idade: int) -> str: 
        return f"{nome} tem {idade} anos"

    a = pedir_tipado("Número 1: ", int)
    b = pedir_tipado("Número 2: ", int)
    print(f"Soma: {somar(a, b)}")
    nome = input("Seu nome: ")
    idade = pedir_tipado("Sua idade: ", int)
    print(apresentar(nome, idade))

# --- Quiz --- 

PERGUNTAS_QUIZ = [
    {"expr": "3 / 2",           "resposta": "float",  "dica": "Divisão em Python 3 sempre retorna float"},
    {"expr": "3 // 2",          "resposta": "int",    "dica": "Divisão inteira retorna int"},
    {"expr": "[1, 2, 3]",       "resposta": "list",   "dica": "Colchetes = list"},
    {"expr": "(1,)",            "resposta": "tuple",  "dica": "Vírgula dentro do parêntese = tuple"},
    {"expr": "{1, 2, 3}",       "resposta": "set",    "dica": "Chaves sem chave:valor = set"},
    {"expr": "1 == 1.0",        "resposta": "bool",   "dica": "Comparações retornam bool"},
    {"expr": "len('python')",   "resposta": "int",    "dica": "len() sempre retorna int"},
    {"expr": "None",            "resposta": "NoneType","dica": "None tem seu próprio tipo"},
]#DIcionario com perguntas


def quiz_tipagem():
    print("=== Quiz de Tipagem ===")
    print("Adivinhe o tipo de cada expressão Python!\n")
    acertos = 0

    for i, q in enumerate(PERGUNTAS_QUIZ, 1):
        print(f"[{i}/{len(PERGUNTAS_QUIZ)}] Qual o tipo de:  {q['expr']}")
        resposta = input("Seu palpite: ").strip()

        if resposta.lower() == q["resposta"].lower():
            print("  Correto!\n")
            acertos += 1
        else:
            print(f"  Errado. Era '{q['resposta']}' — {q['dica']}\n")

    print(f"Resultado: {acertos}/{len(PERGUNTAS_QUIZ)} acertos")
    if acertos == len(PERGUNTAS_QUIZ):
        print("Perfeito! Você domina os tipos Python!")
    elif acertos >= len(PERGUNTAS_QUIZ) // 2:
        print("Bom resultado! Continue praticando.")
    else:
        print("Revise os tipos básicos e tente novamente!")



# --- Menu do modulo Tipagem --- 

def executar():
    while True:
        limpar_tela()
        print("TIPAGEM EM PYTHON -------")
        print("1 - Type Hints Básicos")
        print("2 - Quiz de Tipagem")
        print("0 - Voltar")

        try:
            opcao = int(input("Escolha: "))
        except:
            continue

        limpar_tela()

        match opcao: 
            case 0: 
                print("Número Errado")
                return
            case 1:
                ex_hints_basicos()
            case 2: 
                quiz_tipagem()
            case _:
                print("Opção inválida!")
            
        input("\nPressione Enter para continuar...")
                