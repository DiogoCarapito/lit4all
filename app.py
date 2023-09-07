import streamlit as st
import pandas as pd

st.title("LIT4ALL")

#st.subheader("Bem-vindo ao LIT4ALL!")
#st.write("A plataforma de partilha de folhetos do ACES Sintra")

query = st.text_input("pesquisar folhetos...")

st.write(query)