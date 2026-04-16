import streamlit as st

def executar():
    st.write("ESTRUTURA SEQUENCIAL\n")
    opcao = st.number_input("EXERCICIOS (1 ao 10) ou 0 para sair: ")

    match opcao:
        case 0:
            return

        case 1:
            st.write("Enviar um numero-----------")
            x = st.number_input("Digite um numero: ")
            st.write(f"O numero é {x}")

        case 2:
            st.write("Somar Números--------------")
            x = st.number_input("Digite um numero: ")
            y = st.number_imput("Digite outro numero: ")
            st.write(f"Soma: {x + y}")

        case 3:
            st.write("Calculo de nota-------------")
            n1 = st.number_input("Nota 1: ")
            n2 = st.number_input("Nota 2: ")
            n3 = st.number_input("Nota 3: ")
            n4 = st.number_imput("Nota 4: ")
            st.write(f"Média: {(n1+n2+n3+n4)/4}")

        case 4:
            st.write("Conversor de Metros----------")
            metros = st.number_input("Metros: ")
            st.write(f"Em cm: {metros * 100}")

        case 5:
            st.write("Calulo de Raio---------------")
            raio = st.number_input("Raio: ")
            st.write(f"Área: {3.14 * raio**2}")
        
        case 6:
            st.write("Area do Quadrado-------------")
            lado = st.number_input("Lado: ")
            st.write(f"Área: {lado * lado}")

        case 7:
            st.write("Calculo de Salario------------")
            horas = st.number_input("Horas trabalhadas no Mês: ")
            ganho = st.number_input("Salario por hora: ")
            st.write(f"Salario do mês {horas * ganho}")

        case 8: 
            st.write("Temperatura em Celsius---------")

        case 9:
            st.write("Temperatura em Fahrenheit------")

        case 10: 
            st.write("Calculos com 3 números---------")
            x = st.number_input("")
            y = st.number_input("")
            z = st.number_input("")
            st.write(f"O produto do dobro do primeiro com metade do segundo {(x * 2) * (y / 2)}")
            st.write(f"A soma do triplo do primeiro com o Terceiro{(x * 3) + z}")
            st.write(f"O terceiro elevadoao cubo {z ** 3}")

        case _:
            st.write("Opção inválida!")