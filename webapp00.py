# MEU PRIMEIRO WEB APP
import streamlit as st
from ACTlib01 import *
url = ""
db = Ler_Googleplanilas(url)
escrever(db)


# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("não é o primeito mais é o decimo")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("fesfe10")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("fesfe mais do que 10")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

