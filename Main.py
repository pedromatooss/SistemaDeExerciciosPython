import os
import time
import streamlit as st

import Hanoi
import ListaSequencial
import ListaDecisao
import ListaRepeticao
import ListaTipagem
import ListaConvercao


st.set_page_config(
    page_title="Exercicios Python",
    page_icon="🐍",
    layout="wide"
)

with st.sidebar: 
    st.title("🐍 Exercicios Python")
    st.divider()

    opcao = st.radio(
        label = "Selecione um módulo: ",
        options=[
           "1 - ESTRUTURA SEQUENCIAL",
           "2 - ESTRUTURA DECISÃO",
           "3 - ESTRUTURA REPETIÇÃO",
           "4 - TORRE DE HANOI",
           "5 - TIPAGEM EM PYTHON",
           "6 - CONVERSOR DE BINARIOS",
           "0 - SAIR"
        ]
    )
    match opcao:
        case "1 - Estrutura Sequencial":
            st.header("Estrutura Sequencial")
            st.divider()
            if st.button("▶ Executar"):
                ListaSequencial.executar()

        case "2 - Estrutura de Decisão":
            st.header("Estrutura de Decisão")
            st.divider()
            if st.button("▶ Executar"):
                ListaDecisao.executar()

        case "3 - Estrutura de Repetição":
            st.header("Estrutura de Repetição")
            st.divider()
            if st.button("▶ Executar"):
                ListaRepeticao.executar()

        case "4 - TORRE DE HANOI":
            st.header("Torre de Hanoi")
            st.divider()
            pilhas = st.number_input("Número de discos:", min_value=1, max_value=20, value=3)
            if st.button("▶ Executar"):
                Hanoi.executar(pilhas)

        case "5 - Tipagem em Python":
            st.header("Tipagem em Python")
            st.divider()
            if st.button("▶ Executar"):
                ListaTipagem.executar()

        case "6 - CONVERSOR DE BINARIOS":
            st.header("Conversor de Binários")
            st.divider()
            ListaConvercao.executar()

        case "0 - SAIR":
            st.header("Até logo!")
            st.info("Feche a aba do navegador para encerrar.")

    