import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meu Site Streamlit")

with st.container():
    st.subheader("Meu primeiro site Streamlit-Python")
    st.title("Dashboard de Contratos")
    st.write("Informaçoes sobre os contratos fechados pela Hash$Co ao longo de maio")
    st.write("Quer aprender python? [Clique aqui](https://www.google.com)")


@st.cache_data
def carregarDados():
    tabela = pd.read_csv("resultados.csv")
    return tabela


with st.container():
    st.write("---")
    qtde_dias = st.selectbox("Selecione o periodo", ["7D", '21D', '31D'])
    num_dias = int(qtde_dias.replace("D", ""))
    dados = carregarDados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x="Data", y="Contratos")

