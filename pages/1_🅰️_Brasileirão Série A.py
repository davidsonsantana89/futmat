import streamlit as st
import pandas as pd
import numpy as np

#página do Brasileirão Série A

st.set_page_config(page_title='🅰️ Brasileirão Série A',
                   page_icon='🅰️')

st.write("# 🅰️ Brasileirão Série A")

# st.write('### Em construção.⛏️🚧')

########## INSERÇÃO DE DADOS ##############
# DATA_URL = r"D:\STREAMLIT\futmat\planilhas\serie-a\serie-a-gols.csv"

def get_data():
    return pd.read_csv(DATA_URL, sep=',')

DATA_URL = "https://github.com/davidsonsantana89/futmat/blob/main/planilhas/serie-a/serie-a-gols.csv"
df = get_data()
st.write(df)

# hist_values = np.histogram()