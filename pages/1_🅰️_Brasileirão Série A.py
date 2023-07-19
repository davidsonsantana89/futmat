import streamlit as st
import pandas as pd
import numpy as np

#página do Brasileirão Série A

st.set_page_config(page_title='🅰️ Brasileirão Série A',
                   page_icon='🅰️')

st.write("# 🅰️ Brasileirão Série A")

st.write('### Em construção.⛏️🚧')

########## INSERÇÃO DE DADOS ##############
# data_url = r"D:\STREAMLIT\futmat\planilhas\serie-a\serie-a-gols.csv"

DATA_URL = "https://github.com/davidsonsantana89/futmat/tree/main/planilhas/serie-a"
data = pd.read_csv(DATA_URL,sep=';')
# st.write(data)

# hist_values = np.histogram()