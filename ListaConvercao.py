import streamlit as st
def executar():
    st.write("CONVERSOR\n")
    st.write("DECIMAL PARA BINARIO - 1")
    st.write("BINARIO PARA DECIMAL - 2")

    opcao = int(st.number_input("Digite sua opção:", min_value=0, max_value=2, step=1))

    match opcao:
        case 0: 
            return
        case 1:
            #decimal para binario
            binarios = []
            numero = st.number_input("Digite um numero: ")

            while numero > 0: 
                binario = numero % 2
                binarios.append(binario)
                numero = numero // 2


            st.write(binarios[::-1])
        case 2:
            #binario para decimal
            binarios = st.text_input("Digite um numero binario: ")#em python isso funciona pq é lido como uma lista de caracteres
            if st.button("Converter"):
                decimal = 0
                for i, char in enumerate(reversed(binarios)):
                    if char == '1':
                        decimal += 2 ** i       
                st.write(decimal)
        case _:
            st.write("opção invalida tente novamente")