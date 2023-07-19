import streamlit as st
import pandas as pd
import numpy as np

#página do Brasileirão Série A

st.set_page_config(page_title='🅰️ Brasileirão Série A',
                   page_icon='🅰️')

st.write("# 🅰️ Brasileirão Série A")

st.write('### Em construção.⛏️🚧')

########## INSERÇÃO DE DADOS ##############
@st.cache

DATA_URL = ('https://github.com/davidsonsantana89/futmat/blob/main/planilhas/serie-a/serie-a-gols.xlsx'
)
data = pd.read_excel(DATA_URL)
st.write(data)

# hist_values = np.histogram()