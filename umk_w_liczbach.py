import os
import pandas as pd
import numpy as np
import streamlit as st
import openpyxl
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

DF = pd.read_excel(io='UMKwLiczbach.xlsx',engine='openpyxl',sheetname='Studenci')

sekcja = st.sidebar.radio(
    'Wybierz sekcję:',
    ('Strona główna','Studenci','Administracja','Wydziały','Granty')
 )
if sekcja == 'Strona główna':
    st.title('Strona główna')
if sekcja == 'Studenci':
    st.title('Studenci')
    st.dataframe(DF)
if sekcja == 'Administracja':
    st.title('Admnistracja')
if sekcja == 'Wydziały':
    st.title('Wydziały')
if sekcja == 'Granty':
    st.title('Granty')

    
'''
global df, l, zl, df1, z1
#zl = pd.DataFrame()
l = []
if uploaded_file is not None:
    print(uploaded_file)
    try:
        for i in range(len(uploaded_file)):
            df = pd.read_excel(uploaded_file[i],usecols='C,K')
            l.append(df)
    except Exception as e:
        st.write(str(e))
        st.write('Złe rozszerzenie pliku. Może być tylko .xlsx!')
        

    try:
        st.subheader('Złączone pliki')
        zl = pd.concat(l,ignore_index=True)
        st.write(zl)
    except Exception as e:
        st.write('Czekam na dane')
        
    
    try:
        st.header(':green_book: Unikatowi producenci i ich RKMH')
        z = zl.drop_duplicates('Producent',ignore_index=True)
        st.download_button(label = 'Pobierz plik', data = z.to_csv(index=False,encoding = 'utf-8'),file_name = 'Porównanie_IPRA.csv', mime = "text/csv")
        st.write(z)
    except Exception as e:
        print(e)
        st.write('Czekam na dane')   
        
    if uploaded_file1 is not None:
        try:
            df1 = pd.read_excel(uploaded_file1,usecols='C,K')
        except Exception as e:
            print(e)
            st.write('Złe rozszerzenie pliku. Może być tylko .xlsx!')
            
    try:
        st.subheader('Plik z ostatniego miesiąca')
        st.write(df1)
    except Exception as e:
        print(e)
        st.write('Czekam na dane')
        
    try:
        st.header(':green_book: dane o producentach co byli, a nie ma ich w pliku z ostatniego miesiąca')
        z1 = z[~z['Producent'].isin(df1.Producent)].reset_index().iloc[:,1:3]
        st.download_button(label = 'Pobierz plik', data = z1.to_csv(index=False,encoding = 'utf-8'),file_name = 'Odeszli.csv', mime = "text/csv")
        st.write(z1)
    except Exception as e:
        print(e)
        st.write('Czekam na dane')
'''
