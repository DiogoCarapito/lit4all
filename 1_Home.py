import streamlit as st
import pandas as pd

def search_result_display(result):
    st.write(result)

st.title("LIT4ALL")

query = st.text_input("pesquisar folhetos...")

