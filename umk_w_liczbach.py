import os
import pandas as pd
import numpy as np
import streamlit as st
import openpyxl
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path





st.set_page_config(page_title='UMK w liczbach', page_icon = ':page_facing_up:', layout='wide')

DF = pd.read_excel(io='UMKwLiczbach.xlsx',engine='openpyxl',sheet_name='Studenci')

st.markdown('<style>body {background-color: #ff0099;}</style>', unsafe_allow_html=True)
sekcja = st.sidebar.radio(
    'Wybierz sekcję:',
    ('Strona główna','Studenci','Administracja','Wydziały','Granty')
 )

if sekcja == 'Strona główna':
    new_title = '<b style="font-family:sans-serif;text-align: center; color:rgb(0, 80, 170); font-size: 62px;">Strona główna ***</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    
if sekcja == 'Studenci':
    st.title('Studenci')
    st.dataframe(DF)
    st.multiselect("Something", ["something1", "something2", "something3"])
if sekcja == 'Administracja':
    st.title('Admnistracja')
if sekcja == 'Wydziały':
    st.title('Wydziały')
    st.button('test')
if sekcja == 'Granty':
    st.title('Granty')

hide_st_style = """
            <style>
            #MainMenu {visibility: visible;background-color: #0050AA;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            radio {color: #0050AA;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown(
"""
<style>
span[data-baseweb="radio button"] {
  background-color: #0050AA !important;
}
</style>
""",
    unsafe_allow_html=True,
)






