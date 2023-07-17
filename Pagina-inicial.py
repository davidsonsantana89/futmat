import streamlit as st

st.set_page_config(page_title='Página Inicial',
                   page_icon='🏡')

st.write('# Sejam-vindos ao FutMat ⚽🎲📊')

st.sidebar.success("Selecione uma opção acima.")

st.markdown("""
            Neste app vocês encontram análises estatísticas sobre os campeonatos brasileiros Série
            A e B, feitas pelo Professor Davidson Santana👨🏽‍🏫.
            
            👈🏽Selecione uma das opções ao lado para navegar entre as análises para o Brasileirão Série A ou B.
            """)