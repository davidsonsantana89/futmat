import streamlit as st
import pandas as pd
import numpy as np

#página do Brasileirão Série A

st.set_page_config(page_title='🅰️ Brasileirão Série A',
                   page_icon='🅰️')

st.write("# 🅰️ Brasileirão Série A")

# st.write('### Em construção.⛏️🚧')

########## INSERÇÃO DE DADOS ##############

DATA_URL = "https://raw.githubusercontent.com/davidsonsantana89/futmat/main/planilhas/serie-a/serie-a-gols.csv"

def get_data():
    return pd.read_csv(DATA_URL, sep=';')
df = get_data()
# st.write(df)


tab1, tab2, tab3 = st.tabs(["Primeiro Tempo", "Segundo Tempo", "Jogo Inteiro"])

with tab1:

    ########## TOTAL DE GOLS MARCADOS SOMENTE NO PRIMEIRO TEMPO ##############
    st.write("### Total de gols marcados no primeiro tempo de cada partida")
    hist_values = np.histogram(df['Goals_HT'])[0]

    st.bar_chart(hist_values)

with tab2:

    ########## TOTAL DE GOLS MARCADOS SOMENTE NO SEGUNDO TEMPO ##############
    st.write("### Total de gols marcados no segundo tempo de cada partida")
    hist_values = np.histogram(df['Goals_2H'])[0]

    st.bar_chart(hist_values)


with tab3:

    ########## TOTAL DE GOLS MARCADOS NO JOGO INTEIRO ##############
    st.write("### Total de gols marcados no jogo inteiro")
    hist_values = np.histogram(df['Goals_FT'])[0]

    st.bar_chart(hist_values)