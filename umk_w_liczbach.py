import os
import pandas as pd
import numpy as np
import streamlit as st
import openpyxl
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from streamlit_option_menu import option_menu




st.set_page_config(page_title='UMK w liczbac', page_icon = ':bar_chart:',initial_sidebar_state='expanded')


lata = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
kolor = {'fioletowy':'rgb(170,40,150)','niebieski':'rgb(0,175,250)','zielony':'rgb(0,165,80)','oliwkowy':'rgb(170,210,60)','pomarańczowy':'rgb(255,130,30)','czerwony':'rgb(250,20,20)'}
kolwyd1 = {'Nauk Biologicznych i Weterynaryjnych (od 2019)':kolor['oliwkowy'],'Biologii i Ochrony Środowiska (2012-2018)':kolor['zielony'],'Filologiczny (2010-2018)':kolor['niebieski'],
           'Chemii':kolor['oliwkowy'],'Humanistyczny (2010-2018)':kolor['niebieski'],'Humanistyczny (od 2019)':kolor['niebieski'],'Fizyki, Astronomii i Informatyki Stosowanej':kolor['oliwkowy'],
          'Filozofii i Nauk Społecznych (od 2019)':kolor['fioletowy'],'Matematyki i Informatyki':kolor['oliwkowy'],'Nauk Ekonomicznych i Zarządzania':kolor['fioletowy'],
          'Nauk Historycznych':kolor['niebieski'],'Nauk o Ziemi (2012-2018)':kolor['zielony'],'Nauk Pedagogicznych (2010-2018)':kolor['fioletowy'],'Politologii i Studiów Międzynarodowych (2010-2018)':kolor['fioletowy'],
          'Nauk o Ziemi i Gospodarki Przestrzennej (od 2019)':kolor['oliwkowy'],'Nauk o Polityce i Bezpieczeństwie (od 2019)':kolor['fioletowy'],'Prawa i Administracji':kolor['fioletowy'],'Sztuk Pięknych':kolor['pomarańczowy'],
          'Teologiczny':kolor['zielony'],'Lekarski':kolor['czerwony'],'Farmaceutyczny':kolor['czerwony'],'Nauk o Zdrowiu':kolor['czerwony'],'Ogółem':'rgb(0,80,170)','Ogółem UMK':'rgb(0,80,170)',
	 'Interdyscyplinarne Centrum Nowoczesnych Technologii':kolor['oliwkowy'],'Biologii i Nauk o Ziemi (2010-2011)':kolor['zielony']}
kolwyd = {'Nauk Biologicznych i Weterynaryjnych':kolor['zielony'],'Biologii i Ochrony Środowiska':kolor['zielony'],'Filologiczny':kolor['niebieski'],
           'Chemii':kolor['oliwkowy'],'Humanistyczny':kolor['niebieski'],'Fizyki, Astronomii i Informatyki Stosowanej':kolor['oliwkowy'],
          'Filozofii i Nauk Społecznych':kolor['fioletowy'],'Matematyki i Informatyki':kolor['oliwkowy'],'Nauk Ekonomicznych i Zarządzania':kolor['fioletowy'],
          'Nauk Historycznych':kolor['niebieski'],'Nauk o Ziemi':kolor['zielony'],'Nauk Pedagogicznych':kolor['fioletowy'],'Politologii i Studiów Międzynarodowych':kolor['fioletowy'],
          'Nauk o Ziemi i Gospodarki Przestrzennej':kolor['oliwkowy'],'Nauk o Polityce i Bezpieczeństwie':kolor['fioletowy'],'Prawa i Administracji':kolor['fioletowy'],'Sztuk Pięknych':kolor['pomarańczowy'],
          'Teologiczny':kolor['zielony'],'Lekarski':kolor['czerwony'],'Farmaceutyczny':kolor['czerwony'],'Nauk o Zdrowiu':kolor['czerwony'],'Ogółem UMK':'rgb(0,80,170)','Ogółem':'rgb(0,80,170)',
	 'Interdyscyplinarne Centrum Nowoczesnych Technologii':kolor['oliwkowy'],'Biologii i Nauk o Ziemi':kolor['zielony'],'Nauk Politologii i Studiów Międzynarodowych':kolor['fioletowy'],}

pr_cy = {'Ogółem UMK':'rgb(0,70,180)','Nauczyciele akademiccy':'rgb(0,175,250)','Profesorowie':'rgb(170,40,150)','Adiunkci':'rgb(250,20,20)','Asystenci i lektorzy':'rgb(255,130,30)','Nienauczyciele':'rgb(255,205,0)','Średnia krajowa':'rgb(204,204,204)'}
pr_cy1 = {'Ogółem UMK':0,'Nauczyciele akademiccy':1,'Profesorowie':2,'Adiunkci':3,'Asystenci i lektorzy':4,'Nienauczyciele':5,'Średnia krajowa':6}


        
        
        
        


   


streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css?family=Lato&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Lato';
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)





st.markdown(
    """
<style>
[data-testid="stHeader"]{background-color: rgba(0,0,0,0);}
[class="css-1bh6xo1 e1fqkh3o2"]{
background-color: #0050AA;}
[class="st-bh st-bl st-bm st-bn st-bo st-bp st-az st-b4 st-bq st-br st-bs st-bt st-bu st-bv st-bw st-bx st-by st-bz st-b2 st-c0"]{
background-color: #FFCD00;}
[class="st-d9 st-cl st-bx st-da st-db st-c6 st-dc st-dd st-de"]{
font-family: 'Lato';}
[class="css-1atbdv8 e1fqkh3o1"]{
color: rgb(255,255,255);}
[class="st-av st-aw st-ax st-ay st-cl st-c6 st-b7 st-b4 st-b5 st-cn st-co st-cp st-cq st-cr st-cs st-ct st-cu st-cv st-cw st-b2 st-c2 st-ce st-dz st-e0 st-e1 st-e2 st-d1"]{
border-bottom-color: #0050AA;
border-top-color: #0050AA;
border-right-color: #0050AA;
border-left-color: #0050AA;}
section[data-testid="stSidebar"] label[class="css-1p2iens effi0qh3"]{
color: rgb(255,255,255);}
[class="st-bz st-cd st-ce st-ae st-af st-ag st-ah st-ai st-aj"]{
font-family: 'Lato';
color: rgb(255,255,255);}
</style>
""",
    unsafe_allow_html=True)
st.markdown("""<style>.appview-container .main .block-container{max-width: 1200px;}</style>""",unsafe_allow_html=True)

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 250px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width: 250px;
        margin-left: -250px;
    }
     
    """,
    unsafe_allow_html=True,
)



sekcja = option_menu(None, ["Strona główna", "Studenci i absolwenci", "Pracownicy", 'Badania naukowe'], 
    icons=['house-fill', 'mortarboard-fill', "person-workspace", 'calculator'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "rgb(255,205,0)"},
        "icon": {"color": "white", "font-size": "20px"}, 
        "nav-link": {"font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "rgb(255,205,0)"},
        "nav-link-selected": {"background-color": "rgb(0,70,180)"},
    }
    )

if sekcja == 'Strona główna':
    st.markdown('---')
    st.title('Uniwersytet Mikołaja Kopernika w Toruniu w liczbach')
    st.markdown('<div style="text-align: justify; font-size: 25px;">Uniwersytet Mikołaja Kopernika jest jednym z 43 uniwersytetów publicznych w Polsce i jedną z 10 uczelni w programie „Inicjatywa Doskonałości - Uczelnia Badawcza”. '+
		' Zatrudnia ponad 4 000 pracowników i kształci w ramach różnych form studiów ponad 19 000 studentów. '+
		'Niniejsza aplikacja ma na celu prezentację wizualną danych dotyczących tej znakomitej uczelni. '+
		'Dane pochodzą ze sprawozdań Rektora UMK za lata 2010-2022 i prezentują stan na ostatni dzień danego roku.</div>', unsafe_allow_html=True)
    st.markdown(' ')
    st.markdown('<div style="text-align: justify; font-size: 25px;">Uniwersytet podzielony jest na wydziały. Każdy z wydziałów posiada unikatowe logo, które charakteryzuje kolor '+
		'oraz pozycja mniejszego kółka na obwodzie większego niebieskiego koła. Poniższa grafika przedstawia loga poszczególnych '+
		'wydziałów. Warto zapoznać się z barwami jednostek, ponieważ są one częścią wizualizacji znajdujących się na pozostałych stronach. '+
		' Ich znajomość ułatwi interpretację wykresów.</div>', unsafe_allow_html=True)
    st.image('Image/UMKlog1.png',use_column_width=True)
    
    
    
    
    
    
elif sekcja == 'Studenci i absolwenci':
    #kod właściwy
    st.markdown('---')
    sekcja1 = option_menu(None, ["Studenci i absolwenci", "Porównanie wydziałów", 'Stypendia'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "rgb(255,205,0)"},
        "icon": {"color": "white", "font-size": "18px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "rgb(255,205,0)"},
        "nav-link-selected": {"background-color": "rgb(0,70,180)"},
    }
    )
    
    
    if sekcja1 == 'Studenci i absolwenci':
        DF7 = pd.read_pickle('pick/L_kier_stud.pickle')
        DF7['Rok'] = DF7['Rok'].astype('str')
        DF8 = pd.read_pickle('pick/N-wni.pickle')
        DF8['Rok'] = DF8['Rok'].astype('int')
        DF9 = pd.read_pickle('pick/Z-czni.pickle')
        DF9['Rok'] = DF9['Rok'].astype('int')
        DF10 = pd.read_pickle('pick/Stacjonarne.pickle')
        DF10['Rok'] = DF10['Rok'].astype('int')
        DF10['Wydział'] = DF10['Wydział'].replace(['Ogółem'],'Ogółem UMK')
        DF11 = pd.read_pickle('pick/Niestacjonarne.pickle')
        DF11['Rok'] = DF11['Rok'].astype('int')
        DF11['Wydział'] = DF11['Wydział'].replace(['Ogółem'],'Ogółem UMK')
        DF12 = pd.read_pickle('pick/doktoranci.pickle')
        DF12['Rok'] = DF12['Rok'].astype('int')
        DF12['Wydział'] = DF12['Wydział'].replace(['Ogółem'],'Ogółem UMK')
        DF13 = pd.read_pickle('pick/Podyplomowe.pickle')
        DF13['Rok'] = DF13['Rok'].astype('int')
        DF14 = pd.read_pickle('pick/Ogółem.pickle')
        DF14['Rok'] = DF14['Rok'].astype('int')

        DF15 = pd.read_pickle('pick/Stud_og.pickle')
        DF15['Rok'] = DF15['Rok'].astype('int')
        DF15['Wydział'] = DF15['Wydział'].replace(['Ogółem'],'Ogółem UMK')

	
        DF17 = pd.read_pickle('pick/Absolwenci.pickle')
        DF17['Rok'] = DF17['Rok'].astype('int')
        DF17['Rodzaj'] = DF17['Rodzaj'].replace(['Ogółem'],'Ogółem UMK')
        DF17a = pd.read_pickle('pick/Absolwenci1.pickle')
        DF17a['Rok'] = DF17a['Rok'].astype('int')
        #DF17a['Forma kształcenia'] = DF17a['Forma kształcenia'].replace(['Ogółem'],'Ogółem UMK')
	
        
        st.header('Liczba kierunków studiów')
        st.plotly_chart(px.bar(DF7,x='Rok',y='Liczba',width=1400,height=500).update_traces(marker_color='rgb(0,80,170)',texttemplate="%{y:}",hovertemplate = '<br>Liczba kierunków: <b>%{y:}</b><br>',
	      textposition='inside',textfont=dict( size=14))
	       .update_xaxes(title_font=dict(size=12), title='Rok akademicki').update_yaxes(title_font=dict(size=12),title = 'Liczba kierunków',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")),use_container_width=True)

   
        st.header('Liczba uczestników studiów w podziale na wydziały')
        q1, q2 = st.columns(2)
        kat34 = q1.selectbox('Wybierz kategorię : ',['Studia stacjonarne i niestacjonarne','Studia stacjonarne','Studia niestacjonarne','Studia doktoranckie'])


        fig = px.bar(DF13,x='Rok',y='Liczba',width=1500,height=500).update_xaxes(dtick=1).update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba uczestników',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_traces(hovertemplate = '<br>Liczba uczestników: <b>%{y:}</b><br>',textfont=dict( size=14),marker_color='rgb(0,70,180)',texttemplate="%{y:}",textposition='inside').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"))
        fig1 = px.bar(DF14,x='Rok',y='Liczba',width=1500,height=500).update_xaxes(dtick=1).update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba uczestników',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_traces(hovertemplate = '<br>Liczba uczestników: <b>%{y:}</b><br>',textfont=dict( size=14),marker_color='rgb(0,70,180)',texttemplate="%{y:}",textposition='inside').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"))
        if kat34 == 'Studia stacjonarne':
            wydzial34 = q2.selectbox('Wybierz wydział : ',DF12['Wydział'].unique(),index=0)
            st.plotly_chart(px.bar(DF10[DF10['Wydział']==wydzial34],x='Rok',y='Liczba',width=1500,height=500)
    			.update_traces(marker_color=kolwyd1[wydzial34],texttemplate="%{y:}",textposition='inside',textfont=dict( size=14),hovertemplate = '<br>Liczba uczestników: <b>%{y:}</b><br>')
    			.update_xaxes(dtick=1)
    			.update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba uczestników',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray')
    			.update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")),use_container_width=True)
        elif kat34 == 'Studia niestacjonarne':
            wydzial34 = q2.selectbox('Wybierz wydział : ',DF12['Wydział'].unique(),index=0)
            st.plotly_chart(px.bar(DF11[DF11['Wydział']==wydzial34],x='Rok',y='Liczba',width=1500,height=500)
    			.update_traces(marker_color=kolwyd1[wydzial34],texttemplate="%{y:}",textposition='inside',textfont=dict( size=14),hovertemplate = '<br>Liczba uczestników: <b>%{y:}</b><br>')
    			.update_xaxes(dtick=1)
    			.update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba uczestników',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray')
    			.update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")),use_container_width=True)
        elif kat34 == 'Studia doktoranckie':
            wydzial34 = q2.selectbox('Wybierz wydział : ',DF12['Wydział'].unique(),index=0)
            st.plotly_chart(px.bar(DF12[DF12['Wydział']==wydzial34],x='Rok',y='Liczba',width=1500,height=500)
    			.update_traces(hovertemplate = '<br>Liczba uczestników: <b>%{y:}</b><br>',textfont=dict( size=14),marker_color=kolwyd1[wydzial34],texttemplate="%{y:}",textposition='inside').update_xaxes(dtick=1).update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba uczestników',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray')
    			.update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")),use_container_width=True)
        elif kat34 == 'Studia podyplomowe':
            st.plotly_chart(fig,use_container_width=True)
        elif kat34 == 'Studia stacjonarne i niestacjonarne':
            wydzial34 = q2.selectbox('Wybierz wydział : ',DF12['Wydział'].unique(),index=0)
            st.plotly_chart(px.bar(DF15[DF15['Wydział']==wydzial34],x='Rok',y='Liczba',width=1500,height=500)
    			.update_traces(marker_color=kolwyd1[wydzial34],texttemplate="%{y:}",textposition='inside',textfont=dict( size=14),hovertemplate = '<br>Liczba uczestników: <b>%{y:}</b><br>')
    			.update_xaxes(dtick=1)
    			.update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba uczestników',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray')
    			.update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")),use_container_width=True)
        elif kat34 == 'Ogółem':
            st.plotly_chart(fig1,use_container_width=True)
	
	
	
        st.header('Liczba absolwentów uniwersytetu')
        ab = st.selectbox('Wybierz kategorię:    ',['Ogółem','Studia stacjonarne i niestacjonarne','Studia stacjonarne','Studia niestacjonarne','Studia doktoranckie','Studia podyplomowe'])	
        st.plotly_chart(px.bar(DF17a[(DF17a['Forma kształcenia']==ab)],x='Rok',y='Liczba',width=1500,height=500)
		    .update_traces(marker_color='rgb(0,70,180)',texttemplate="%{y:}",textposition='inside',textfont=dict( size=14,color='white'),hovertemplate = '<br>Liczba absolwentów: <b>%{y:}</b><br>')
		    .update_xaxes(dtick=1)
		    .update_yaxes(tickformat=" ",title='Liczba absolwentów',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray')
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")),use_container_width=True)
	
        st.header('Zmiana liczby uczestników studiów i absolwentów uniwersytetu w stosunku do roku poprzedniego (w %)')
        kat43 = st.selectbox('Wybierz kategorię :   ',['Ogółem UMK','Studia stacjonarne','Studia niestacjonarne','Studia doktoranckie','Studia podyplomowe'])
        st.plotly_chart(px.line(DF17[DF17['Rodzaj']==kat43],x='Rok',y='Zmiana[%]',color = 'Kategoria',hover_name="Kategoria",markers=True,width=1500,height=500,color_discrete_sequence=['rgb(255,205,0)','rgb(0,70,180)'])
		    .update_traces(hovertemplate = '<br>Zmiana liczby studentów i absolwentów: <b>%{y:,.2f}%</b><br>'+"<extra></extra>",textposition="top right",texttemplate = "%{y:,.2f}%",textfont=dict( size=14))
	        .update_xaxes(title_font=dict(size=12), title='Rok',range=[2010.95,2022+1/5],dtick=1,showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside')
		    .update_yaxes(title_font=dict(size=12),title = 'Zmiana liczby studentów/absolwentów[%]',tickformat=",",range=[-50,50],zeroline=True, zerolinewidth=4, zerolinecolor='rgba(0,0,0,1)',showline=False,linewidth=1,gridwidth=1,gridcolor='gray')                        
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"),use_container_width=True)
        st.write('Wartości poniżej 0 oznaczają spadek liczby studentów względem roku poprzedniego, a powyżej - wzrost.')
        
        
        
        st.header('Procent uczestników z zagranicy z uwzględnieniem formy kształcenia')
        st.plotly_chart(px.line(DF9,x='Rok',y='Odsetek',color = 'Forma kształcenia',hover_name="Forma kształcenia",width=1500,height=500,markers=True,color_discrete_sequence=['rgb(0,80,170)','rgb(0,175,250)','rgb(250,20,20)','rgb(255,205,0)'])
    		    .update_traces(textposition="top right",hovertemplate = '<br>Procent uczestników z zagranicy: <b>%{y:,.2f}%</b><br>'+"<extra></extra>",texttemplate = "%{y:.2f}%",textfont=dict( size=14))
    	.update_xaxes(title_font=dict(size=12), title='Rok',range=[2011.95,2022+1/5],dtick=1,showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside')
    		    .update_yaxes(title_font=dict(size=12),title = 'Procent uczestników z zagranicy',tickformat=",",rangemode='tozero',showline=False,linewidth=1,gridwidth=1,gridcolor='gray')
    		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"),use_container_width=True)
        
        
        st.header('Procent uczestników z niepełnosprawnościami z uwzględnieniem formy kształcenia')
        st.plotly_chart(px.line(DF8,x='Rok',y='Odsetek',color = 'Forma kształcenia',hover_name="Forma kształcenia",width=1500,height=500,markers=True,color_discrete_sequence=['rgb(0,80,170)','rgb(0,175,250)','rgb(250,20,20)','rgb(255,205,0)'])
    		    .update_traces(textposition="top right",hovertemplate = '<br>Procent uczestników z niepełnosprawnościami: <b>%{y:,.2f}%</b><br>'+"<extra></extra>",texttemplate = "%{y:,.2f}%",textfont=dict( size=14))
    	.update_xaxes(title_font=dict(size=12), title='Rok',range=[2011.95,2022+1/5],dtick=1,showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside').update_yaxes(title_font=dict(size=12),title = 'Procent uczestników z niepełnosprawnościami',tickformat=",",rangemode='tozero',showline=False,linewidth=1,gridwidth=1,gridcolor='gray')
    		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"),use_container_width=True)
	
	
	
    
    elif sekcja1 == 'Porównanie wydziałów':
        DF10 = pd.read_pickle('pick/Stacjonarne.pickle')
        DF10['Rok'] = DF10['Rok'].astype('int')
        DF10['Wydział'] = DF10['Wydział'].replace(['Ogółem'],'Ogółem UMK')
        
        DF11 = pd.read_pickle('pick/Niestacjonarne.pickle')
        DF11['Rok'] = DF11['Rok'].astype('int')
        DF11['Wydział'] = DF11['Wydział'].replace(['Ogółem'],'Ogółem UMK')
        DF12 = pd.read_pickle('pick/doktoranci.pickle')
        DF12['Rok'] = DF12['Rok'].astype('int')
        DF12['Wydział'] = DF12['Wydział'].replace(['Ogółem'],'Ogółem UMK')
        
        DF15 = pd.read_pickle('pick/Stud_og.pickle')
        DF15['Rok'] = DF15['Rok'].astype('int')
        DF15['Wydział'] = DF15['Wydział'].replace(['Ogółem'],'Ogółem UMK')
      
        DF19 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Wydz_sr',dtype={'Rok':int})
        DF19a = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Wydz_sr_stacjo',dtype={'Rok':int})
        DF19b = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Wydz_sr_niestacjo',dtype={'Rok':int})
        DF19c = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Wydz_sr_dokt',dtype={'Rok':int})
        
        
        st.header('Porównanie liczby uczestników studiów na wybranych wydziałach')
        kat09 = st.selectbox('Wybierz kategorię :   ',['Studia stacjonarne i niestacjonarne','Studia stacjonarne','Studia niestacjonarne','Studia doktoranckie'])
        wydz746 = st.multiselect('Wybierz wydział:       ',DF12[DF12['Wydział']!='Ogółem UMK']['Wydział'].unique(),['Farmaceutyczny','Matematyki i Informatyki'])
        gz3 = st.radio('Średnio na 1 wydział UMK - Włącz/Wyłącz:',('Włącz','Wyłącz'))
      
        if (gz3 == 'Włącz') and (kat09 == 'Studia stacjonarne i niestacjonarne'):
            fig77 = px.bar(DF15[(DF15['Wydział'].isin(wydz746))].sort_values(by=['Wydział','Rok']),x='Rok',y='Liczba',barmode = 'group',hover_name="Wydział", color='Wydział',width=1500,height=500,color_discrete_sequence=list(map(lambda x: kolwyd1[x],sorted(wydz746))),pattern_shape="Wydział").update_yaxes(rangemode='tozero',tickformat=",",showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',title='Liczba uczestników').update_traces(hovertemplate = 'Liczba uczestników studiów stacjonarnych i niestacjonarnych: <b>%{y:}</b>',textfont=dict( size=14),texttemplate="%{y:}",textposition='inside').update_xaxes(dtick=1).update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
            fig52 = px.line(DF19,x='Rok',y='Liczba',color_discrete_sequence=['rgb(0,80,170)'],markers=True).update_traces(hovertemplate = '<br>Średnia liczba uczestników studiów stacjonarnych i niestacjonarnych: <b>%{y:,.2f}</b><br>',textfont=dict( size=14),textposition="top left",texttemplate = "%{y:.2f}").update_yaxes(tickformat=",").update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
            fig77.add_trace(fig52.data[0])
            st.plotly_chart(fig77,use_container_width=True)
        elif (gz3 == 'Wyłącz') and (kat09 == 'Studia stacjonarne i niestacjonarne'):
            st.plotly_chart(px.bar(DF15[(DF15['Wydział'].isin(wydz746))].sort_values(by=['Wydział','Rok']),x='Rok',y='Liczba',barmode = 'group',hover_name="Wydział", color='Wydział',width=1500,height=500,color_discrete_sequence=list(map(lambda x: kolwyd1[x],sorted(wydz746))),pattern_shape="Wydział").update_yaxes(tickformat=",",showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',title='Liczba uczestników').update_traces(hovertemplate = 'Liczba uczestników studiów stacjonarnych i niestacjonarnych: <b>%{y:}</b>',textfont=dict( size=14),texttemplate="%{y:}",textposition='inside').update_xaxes(dtick=1).update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=','),use_container_width=True)
        elif (gz3 == 'Włącz') and (kat09 == 'Studia stacjonarne'):
            fig77 = px.bar(DF10[(DF10['Wydział'].isin(wydz746))].sort_values(by=['Wydział','Rok']),x='Rok',y='Liczba',barmode = 'group',hover_name="Wydział", color='Wydział',width=1500,height=500,color_discrete_sequence=list(map(lambda x: kolwyd1[x],sorted(wydz746))),pattern_shape="Wydział").update_yaxes(rangemode='tozero',tickformat=",",showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',title='Liczba uczestników').update_traces(hovertemplate = 'Liczba uczestników studiów stacjonarnych: <b>%{y:}</b>',textfont=dict( size=14),texttemplate="%{y:}",textposition='inside').update_xaxes(dtick=1).update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
            fig52 = px.line(DF19a,x='Rok',y='Liczba',color_discrete_sequence=['rgb(0,80,170)'],markers=True).update_traces(hovertemplate = '<br>Średnia liczba uczestników studiów stacjonarnych: <b>%{y:,.2f}</b><br>',textfont=dict( size=14),textposition="top left",texttemplate = "%{y:.2f}").update_yaxes(tickformat=",").update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
            fig77.add_trace(fig52.data[0])
            st.plotly_chart(fig77,use_container_width=True)
        elif (gz3 == 'Wyłącz') and (kat09 == 'Studia stacjonarne'):
            st.plotly_chart(px.bar(DF10[(DF10['Wydział'].isin(wydz746))].sort_values(by=['Wydział','Rok']),x='Rok',y='Liczba',barmode = 'group',hover_name="Wydział", color='Wydział',width=1500,height=500,color_discrete_sequence=list(map(lambda x: kolwyd1[x],sorted(wydz746))),pattern_shape="Wydział").update_yaxes(tickformat=",",showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',title='Liczba uczestników').update_traces(hovertemplate = 'Liczba uczestników studiów stacjonarnych: <b>%{y:}</b>',textfont=dict( size=14),texttemplate="%{y:}",textposition='inside').update_xaxes(dtick=1).update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=','),use_container_width=True)
        elif (gz3 == 'Włącz') and (kat09 == 'Studia niestacjonarne'):
            fig77 = px.bar(DF11[(DF11['Wydział'].isin(wydz746))].sort_values(by=['Wydział','Rok']),x='Rok',y='Liczba',barmode = 'group',hover_name="Wydział", color='Wydział',width=1500,height=500,color_discrete_sequence=list(map(lambda x: kolwyd1[x],sorted(wydz746))),pattern_shape="Wydział").update_yaxes(rangemode='tozero',tickformat=",",showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',title='Liczba uczestników').update_traces(hovertemplate = 'Liczba uczestników studiów niestacjonarnych: <b>%{y:}</b>',textfont=dict( size=14),texttemplate="%{y:}",textposition='inside').update_xaxes(dtick=1).update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
            fig52 = px.line(DF19b,x='Rok',y='Liczba',color_discrete_sequence=['rgb(0,80,170)'],markers=True).update_traces(hovertemplate = '<br>Średnia liczba uczestników studiów niestacjonarnych: <b>%{y:,.2f}</b><br>',textfont=dict( size=14),textposition="top left",texttemplate = "%{y:.2f}").update_yaxes(tickformat=",").update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
            fig77.add_trace(fig52.data[0])
            st.plotly_chart(fig77,use_container_width=True)
        elif (gz3 == 'Wyłącz') and (kat09 == 'Studia niestacjonarne'):
            st.plotly_chart(px.bar(DF11[(DF11['Wydział'].isin(wydz746))].sort_values(by=['Wydział','Rok']),x='Rok',y='Liczba',barmode = 'group',hover_name="Wydział", color='Wydział',width=1500,height=500,color_discrete_sequence=list(map(lambda x: kolwyd1[x],sorted(wydz746))),pattern_shape="Wydział").update_yaxes(tickformat=",",showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',title='Liczba uczestników').update_traces(hovertemplate = 'Liczba uczestników studiów niestacjonarnych: <b>%{y:}</b>',textfont=dict( size=14),texttemplate="%{y:}",textposition='inside').update_xaxes(dtick=1).update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=','),use_container_width=True) 
        elif (gz3 == 'Włącz') and (kat09 == 'Studia doktoranckie'):
            fig77 = px.bar(DF12[(DF12['Wydział'].isin(wydz746))].sort_values(by=['Wydział','Rok']),x='Rok',y='Liczba',barmode = 'group',hover_name="Wydział", color='Wydział',width=1500,height=500,color_discrete_sequence=list(map(lambda x: kolwyd1[x],sorted(wydz746))),pattern_shape="Wydział").update_yaxes(rangemode='tozero',tickformat=",",showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',title='Liczba uczestników').update_traces(hovertemplate = 'Liczba uczestników studiów doktoranckich: <b>%{y:}</b>',textfont=dict( size=14),texttemplate="%{y:}",textposition='inside').update_xaxes(dtick=1).update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
            fig52 = px.line(DF19c,x='Rok',y='Liczba',color_discrete_sequence=['rgb(0,80,170)'],markers=True).update_traces(hovertemplate = '<br>Średnia liczba uczestników studiów doktoranckich: <b>%{y:,.2f}</b><br>',textfont=dict( size=14),textposition="top left",texttemplate = "%{y:.2f}").update_yaxes(tickformat=",").update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
            fig77.add_trace(fig52.data[0])
            st.plotly_chart(fig77,use_container_width=True)
        elif (gz3 == 'Wyłącz') and (kat09 == 'Studia doktoranckie'):
            st.plotly_chart(px.bar(DF12[(DF12['Wydział'].isin(wydz746))].sort_values(by=['Wydział','Rok']),x='Rok',y='Liczba',barmode = 'group',hover_name="Wydział", color='Wydział',width=1500,height=500,color_discrete_sequence=list(map(lambda x: kolwyd1[x],sorted(wydz746))),pattern_shape="Wydział").update_yaxes(tickformat=",",showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',title='Liczba uczestników').update_traces(hovertemplate = 'Liczba uczestników studiów doktoranckich: <b>%{y:}</b>',textfont=dict( size=14),texttemplate="%{y:}",textposition='inside').update_xaxes(dtick=1).update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=','),use_container_width=True)
            
        st.header('Zmiana liczby uczestników studiów w stosunku do roku poprzedniego w podziale na wydziały')
        kat099 = st.selectbox('Wybierz kategorię :     ',['Studia stacjonarne i niestacjonarne','Studia stacjonarne','Studia niestacjonarne','Studia doktoranckie'])
        wydz1 = st.multiselect('Wybierz wydział :    ',DF12['Wydział'].unique(),['Ogółem UMK','Matematyki i Informatyki'])
        if kat099 == 'Studia stacjonarne i niestacjonarne':
            st.plotly_chart(px.line(DF15[(DF15['Wydział'].isin(wydz1))].sort_values(by=['Wydział','Rok']),x='Rok',y='Zmiana',hover_name="Wydział",color='Wydział',width=1400,height=500,symbol='Wydział',markers=True,color_discrete_sequence=list(map(lambda x: kolwyd1[x],sorted(wydz1))))
        		    .update_traces(marker_size=10,textposition='top right',texttemplate="%{y:,d}",textfont=dict( size=14),hovertemplate='Zmiana liczby uczestników studiów stacjonarnych i niestacjonarnych: <b>%{y:,.2f}%</b>')
        		    .update_xaxes(showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside',range=[2011-1/5,2022+1/5],dtick=1)
        		    .update_yaxes(tickformat = ' ',rangemode='tozero',zeroline=True, zerolinewidth=4, zerolinecolor='rgba(0,0,0,1)',showline=False,linewidth=1,gridwidth=1,gridcolor='gray',title='Zmiana liczby uczestników studiów[%]')
        		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"),use_container_width=True)
        elif kat099 == 'Studia stacjonarne':
            st.plotly_chart(px.line(DF10[(DF10['Wydział'].isin(wydz1))].sort_values(by=['Wydział','Rok']),x='Rok',y='Zmiana',hover_name="Wydział",color='Wydział',width=1400,height=500,symbol='Wydział',markers=True,color_discrete_sequence=list(map(lambda x: kolwyd1[x],sorted(wydz1))))
        		    .update_traces(marker_size=10,textposition='top right',texttemplate="%{y:,d}",textfont=dict( size=14),hovertemplate='Zmiana liczby uczestników studiów stacjonarnych: <b>%{y:,.2f}%</b>')
        		    .update_xaxes(showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside',range=[2011-1/5,2022+1/5],dtick=1)
        		    .update_yaxes(tickformat = ' ',rangemode='tozero',zeroline=True, zerolinewidth=4, zerolinecolor='rgba(0,0,0,1)',showline=False,linewidth=1,gridwidth=1,gridcolor='gray',title='Zmiana liczby uczestników studiów[%]')
        		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"),use_container_width=True)
        elif kat099 == 'Studia niestacjonarne':
            st.plotly_chart(px.line(DF11[(DF11['Wydział'].isin(wydz1))].sort_values(by=['Wydział','Rok']),x='Rok',y='Zmiana',hover_name="Wydział",color='Wydział',width=1400,height=500,symbol='Wydział',markers=True,color_discrete_sequence=list(map(lambda x: kolwyd1[x],sorted(wydz1))))
        		    .update_traces(marker_size=10,textposition='top right',texttemplate="%{y:,d}",textfont=dict( size=14),hovertemplate='Zmiana liczby uczestników studiów niestacjonarnych: <b>%{y:,.2f}%</b>')
        		    .update_xaxes(showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside',range=[2011-1/5,2022+1/5],dtick=1)
        		    .update_yaxes(tickformat = ' ',rangemode='tozero',zeroline=True, zerolinewidth=4, zerolinecolor='rgba(0,0,0,1)',showline=False,linewidth=1,gridwidth=1,gridcolor='gray',title='Zmiana liczby uczestników studiów[%]')
        		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"),use_container_width=True)
        elif kat099 == 'Studia doktoranckie':
            st.plotly_chart(px.line(DF12[(DF12['Wydział'].isin(wydz1))].sort_values(by=['Wydział','Rok']),x='Rok',y='Zmiana',hover_name="Wydział",color='Wydział',width=1400,height=500,symbol='Wydział',markers=True,color_discrete_sequence=list(map(lambda x: kolwyd1[x],sorted(wydz1))))
        		    .update_traces(marker_size=10,textposition='top right',texttemplate="%{y:,d}",textfont=dict( size=14),hovertemplate='Zmiana liczby uczestników studiów doktoranckich: <b>%{y:,.2f}%</b>')
        		    .update_xaxes(showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside',range=[2011-1/5,2022+1/5],dtick=1)
        		    .update_yaxes(tickformat = ' ',rangemode='tozero',zeroline=True, zerolinewidth=4, zerolinecolor='rgba(0,0,0,1)',showline=False,linewidth=1,gridwidth=1,gridcolor='gray',title='Zmiana liczby uczestników studiów[%]')
        		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"),use_container_width=True)    
        st.write('Wartości poniżej 0 oznaczają spadek liczby studentów względem roku poprzedniego, a powyżej - wzrost.')
    
    
    elif sekcja1 == 'Stypendia':
        DF20 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Styp_min1',dtype={'Rok':int})
        
        
        st.header('Stypendia ministra w podziale na wydziały wraz ze współczynnikiem skuteczności (w %)')
        r = st.selectbox('Wybierz rok : ', lata[::-1],index=0)
        lg = pd.DataFrame(DF20[DF20['Rok']==r].groupby('Wydział')['Przyznane'].agg(np.sum)).sort_values(by='Przyznane')[::-1]
        if not lg.empty:
                lg.loc[' '] = None
        x = lg.index[::-1]
        y = lg['Przyznane'][::-1]
        lg = lg.reset_index()
        lg['kolor']=' '
        for j,i in enumerate(lg['Wydział']):
            if i in list(kolwyd.keys()):
                lg['kolor'][j] = kolwyd[i]
            else:
                lg['kolor'][j] = 'rgb(0,70,180)'
        barwa4 = lg['kolor'][::-1]
        barwa4[::-1].loc[17] = 'rgb(0,70,180)'
        
        lg1 = pd.DataFrame(DF20[DF20['Rok']==r].groupby('Wydział')['Złożone'].agg(np.sum)).sort_values(by='Złożone')[::-1]
        if not lg1.empty:
                lg1.loc[' '] = None
        x1 = lg1.index[::-1]
        y1 = lg1['Złożone'][::-1]
        lg1 = lg1.reset_index()
        lg1['kolor']=' '
        for j,i in enumerate(lg1['Wydział']):
            if i in list(kolwyd.keys()):
                lg1['kolor'][j] = kolwyd[i]
            else:
                lg1['kolor'][j] = 'rgb(0,70,180)'
        barwa5 = lg1['kolor'][::-1]
        barwa5[::-1].loc[17] = 'rgb(0,70,180)'
        fig = go.Figure()      
           
        fig.add_trace(go.Bar(x=y,y=x,orientation='h',hovertemplate = '<br>Stypendia przyznane: <b>%{x:}</b><br>'+"<extra></extra>",
        textfont=dict( size=12,color='black'),marker_color=barwa4,name='Przyznany',legendrank=1))
           
        fig.add_trace(go.Bar(x=y1,y=x1,orientation='h',hovertemplate = '<br>Wnioski złożone: <b>%{x:}</b><br>'+"<extra></extra>",
           			textfont=dict( size=12,color='black'),marker_color=barwa5,marker_pattern_shape="x",name='Złożony',
			     legendrank=2
           		      ))
        fig.update_xaxes(title='Liczba wniosków').update_traces(marker_line_color='black',marker_line_width=1.5)
        fig.update_yaxes(title='Wydział')
        fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),
           				height=800,width=1500,plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),barmode='group',legend_traceorder='reversed',
           				separators =',',showlegend=True,legend_title_text='Rodzaj wniosku',margin=dict(t=100, b=0, l=180, r=50),legend_orientation='h',legend_x=-0.1,legend_yanchor='top',legend_y=1.1)
           
        st.plotly_chart(fig,use_container_width=True)
    
    
        
             	       
        lg7 = pd.DataFrame(DF20[DF20['Rok']==r].groupby('Wydział')['Skuteczność'].agg(np.sum)).sort_values(by='Skuteczność')[::-1]
        x7 = lg7.index[::-1]
        y7 = lg7['Skuteczność'][::-1]
    
    
        lg7 = lg7.reset_index()
        lg7['kolor']=' '
        for j,i in enumerate(lg7['Wydział']):
            if i in list(kolwyd.keys()):
                lg7['kolor'][j] = kolwyd[i]
            else:
                lg7['kolor'][j] = 'rgb(0,70,180)'
        barwa7 = lg7['kolor'][::-1]
    
        fig7 = go.Figure()
        fig7.add_trace(go.Bar(x=y7,y=x7,orientation='h',hovertemplate = '<br>Skuteczność: <b>%{x:,.2f}%</b><br>'+"<extra></extra>",
                            textfont=dict( size=12,color='black')))
        fig7.update_traces(marker_color=barwa7,marker_line_color='black',marker_line_width=1.5
                          )
        fig7.update_xaxes(title='Współczynnik skuteczności [%]',range=[0,105])
        fig7.update_yaxes(title='Wydział')
    
        fig7.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),
                                    height=600,width=1600,plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),barmode='group',
                                    separators =',',autosize=False,margin=dict(t=100, b=0, l=180, r=50))
    
        st.plotly_chart(fig7,use_container_width=True)
        st.write('Współczynnik skuteczności jest określony jako stosunek liczby otrzymanych stypendiów do złożonych wniosków (w %).')
	
    
    
    
   
    
    
    
     
    
    
    
elif sekcja == 'Pracownicy':
    
    st.markdown('---')
    sekcja2 = option_menu(None, ["Pracownicy", "Nauczyciele akademiccy", 'Wynagrodzenie'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "rgb(255,205,0)"},
        "icon": {"color": "white", "font-size": "18px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "rgb(255,205,0)"},
        "nav-link-selected": {"background-color": "rgb(0,70,180)"},})
    
    #kod właściwy
    if sekcja2 == 'Pracownicy':
        DF21 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Nacz_og',dtype={'Rok':int})
        DF22 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Prac',dtype={'Rok':int})
        DF23 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Pr_pl',dtype={'Rok':int})
        DF27 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Pr_npwni',dtype={'Rok':int})
        
        DF21['Rodzaj'] = DF21['Rodzaj'].replace(['Ogółem'],'Ogółem UMK')
        DF22['Rodzaj'] = DF22['Rodzaj'].replace(['Ogółem'],'Ogółem UMK')
        st.header('Liczba pracowników uniwersytetu')
        pr = st.selectbox('Wybierz kategorię : ', ['Ogółem UMK','Nauczyciele akademiccy','Pracownicy niebędący nauczycielami akademickimi'])
        st.plotly_chart(px.bar(DF21[DF21['Rodzaj']==pr],x='Rok',y='Liczba',color='Jednostka',width=1400,height=500,color_discrete_sequence=['rgb(255,205,0)','rgb(250,20,20)']).update_traces(customdata=DF21[DF21['Rodzaj']==pr].groupby('Rok')['Liczba'].agg(np.sum)[::-1],texttemplate="%{y:}",hovertemplate = '<br>Liczba ogółem: <b>%{customdata}</b><br>'+"<extra></extra>",
        	textposition='inside',textfont=dict( size=14))
        	.update_xaxes(title_font=dict(size=12), title='Rok',dtick=1).update_yaxes(title_font=dict(size=12),title = 'Liczba pracowników',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"), legend_title_text='Kampus'),use_container_width=True)
	
        st.header('Zmiana liczby pracowników uniwersytetu w stosunku do roku poprzedniego')
        pr1 = st.selectbox('Wybierz kategorię   : ', ['Ogółem UMK','Nauczyciele akademiccy','Pracownicy niebędący nauczycielami akademickimi'])
        st.plotly_chart(px.line(DF22[DF22['Rodzaj']==pr1],x='Rok',y='Zmiana',color = 'Jednostka',width=1500,height=500,color_discrete_sequence=['rgb(250,20,20)','rgb(255,205,0)','rgb(0,70,180)'],markers=True)
		    .update_traces(textposition="top right",texttemplate = "%{y:.2f}%",textfont=dict( size=14),hovertemplate = '<br>Zmiana liczby pracowników: <b>%{y:,.2f}%</b><br>'+"<extra></extra>")
	        .update_xaxes(title_font=dict(size=12), title='Rok',range=[2012.95,2022.5],dtick=1,showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside')
		    .update_yaxes(title_font=dict(size=12),title = 'Zmiana liczby pracowników[%]',tickformat=",",range=[-8,8],zeroline=True, zerolinewidth=4, zerolinecolor='rgba(0,0,0,1)',showline=False,linewidth=1,gridwidth=1,gridcolor='gray')                        
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x", legend_title_text='Kampus'),use_container_width=True)
        st.write('Wartości poniżej 0 oznaczają spadek liczby pracowników względem roku poprzedniego, a powyżej - wzrost.')
	
	
        st.header('Liczba pracowników niebędących nauczycielami akademickimi przypadających na jednego nauczyciela na uniwersytecie')
        st.plotly_chart(px.line(DF22[DF22['Rodzaj']=='Nauczyciele akademiccy'],x='Rok',y='Stosunek',color = 'Jednostka',width=1500,height=500,color_discrete_sequence=['rgb(250,20,20)','rgb(255,205,0)','rgb(0,70,180)'],markers=True)
		    .update_traces(textposition="top right",texttemplate = "%{y:.2f}",textfont=dict( size=14),hovertemplate = '<br>Stosunek liczby nienauczycieli do nauczycieli: <b>%{y:,.2f}</b><br>'+"<extra></extra>")
	        .update_xaxes(title_font=dict(size=12), title='Rok',range=[2011.95,2022.5],dtick=1,showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside')
		    .update_yaxes(title_font=dict(size=12),title = 'Stosunek liczby nienauczycieli do nauczycieli',tickformat=",",rangemode='tozero',showline=False,linewidth=1,gridwidth=1,gridcolor='gray')                        
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"), legend_title_text='Kampus', separators=',',hovermode="x"),use_container_width=True)

        st.header("Struktura pracowników w podziale na płeć i kampusy")
        y1, y2 = st.columns([1,5])
        with y1:
            rok1 = st.selectbox('Wybierz rok :', lata[::-1])
        with y2:
            fig7 = go.Figure(data=[go.Pie(labels=DF23[DF23['Rok']==rok1].sort_values(by='Płeć')['Płeć'],sort=False,
				     values=DF23[DF23['Rok']==rok1].sort_values(by='Płeć')['Liczba'])])
            fig7.update_traces(textfont=dict( size=14),textinfo='value+percent',marker=dict( colors=['rgb(255,205,0)','rgb(255,220,0)','rgb(0,80,170)','rgb(0,80,220)']),direction ='clockwise',hovertemplate = '<b>%{label}</b>'+"<extra></extra>")
            fig7.update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',margin=dict(t=0, b=0, l=20, r=0),showlegend=True)
            st.plotly_chart(fig7,use_container_width=True)
        
        st.header('Liczba pracowników z niepełnosprawnościami na uniwersytecie')
        st.plotly_chart(px.bar(DF27,x='Rok',y='Liczba',color='Jednostka',width=1400,height=500,color_discrete_sequence=['rgb(255,205,0)','rgb(250,20,20)']).update_traces(customdata=DF27.groupby('Rok')['Liczba'].agg(np.sum)[::-1],texttemplate="%{y:}",textfont=dict( size=14),
    	textposition='inside',hovertemplate = '<br>Liczba ogółem: <b>%{customdata}</b><br>'+'<extra></extra>')
    	.update_xaxes(title_font=dict(size=12), title='Rok',dtick=1).update_yaxes(title_font=dict(size=12),title = 'Liczba pracowników z niepełnosprawnościami',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_layout(legend_title_text='Kampus', plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")),use_container_width=True)
        
        
    elif sekcja2 == 'Nauczyciele akademiccy':
        DF = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='nauczyciele',dtype={'Rok':int})
        
        DF24 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Pr_wydz',dtype={'Rok':int})
        DF25 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Pr_sr',dtype={'Rok':int})
        DF35 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Awanse',dtype={'Rok':float})
        DF26 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Pr_St',dtype={'Rok':int})
        
        
        DF24['Wydział'] = DF24['Wydział'].replace(['Ogółem'],'Ogółem UMK')
        DF26['Wydział'] = DF26['Wydział'].replace(['Ogółem'],'Ogółem UMK')
        st.header("Liczba nauczycieli akademickich na uniwersytecie w poszczególnych grupach")
        rok9 = st.selectbox('Wybierz rok:', [2019,2020,2021,2022][::-1])
        xyz,yxz,zxy = st.columns([1,2,1])
        yxz.image('Image/legenda.png', use_column_width=True)
        k1,k2,k3 = st.columns(3)
        with k1:
            fig = go.Figure(data=[go.Pie(labels=DF[(DF['badawcza']!=0) & (DF['Rok']==rok9)]['Stanowisko'],sort=False,
				     values=DF[(DF['badawcza']!=0) & (DF['Rok']==rok9)]['badawcza'])])
            fig.update_traces(textfont=dict( size=14),textinfo='value+percent',marker=dict( colors=['rgb(0,165,80)','rgb(170,210,60)','rgb(250,20,20)','rgb(255,130,30)']),direction ='clockwise',hovertemplate = '<b>%{label}</b>'+"<extra></extra>")
            fig.update_layout(title="<b>Grupa badawcza</b>",legend=dict(x=0,y=1.2),margin=dict(t=80, b=0, l=0, r=100),plot_bgcolor='white',font=dict(family='Lato',size=16,color="Black"),separators=',',showlegend=False,title_x=0.15,title_y=0.95)
            st.plotly_chart(fig,use_container_width=True)
        with k2:
            fig = go.Figure(data=[go.Pie(labels=DF[(DF['badawcza-dydaktyczna']!=0) & (DF['Rok']==rok9)]['Stanowisko'],sort=False,
				     values=DF[(DF['badawcza-dydaktyczna']!=0) & (DF['Rok']==rok9)]['badawcza-dydaktyczna'])])
            fig.update_traces(textfont=dict( size=14),textinfo='value+percent',marker=dict( colors=['rgb(0,165,80)','rgb(170,210,60)','rgb(250,20,20)','rgb(255,130,30)']),direction ='clockwise',hovertemplate = '<b>%{label}</b>'+"<extra></extra>")
            fig.update_layout(title="<b>Grupa badawczo-dydaktyczna</b>",legend=dict(x=0,y=1.2),margin=dict(t=80, b=0, l=0, r=100),plot_bgcolor='white',font=dict(family='Lato',size=16,color="Black"),separators=',',showlegend=False,title_x=0,title_y=0.95)
            st.plotly_chart(fig,use_container_width=True)     
        with k3 :
            fig = go.Figure(data=[go.Pie(labels=DF[(DF['dydaktyczna']!=0) & (DF['Rok']==rok9)]['Stanowisko'],sort=False,
				     values=DF[(DF['dydaktyczna']!=0) & (DF['Rok']==rok9)]['dydaktyczna'])])
            fig.update_traces(textfont=dict( size=14),textinfo='value+percent',marker=dict( colors=['rgb(0,165,80)','rgb(170,210,60)','rgb(250,20,20)','rgb(255,130,30)','rgb(255,205,0)']),direction ='clockwise',hovertemplate = '<b>%{label}</b>'+"<extra></extra>")
            fig.update_layout(title="<b>Grupa dydaktyczna</b>",legend=dict(x=0,y=0),margin=dict(t=80, b=0, l=0, r=100),plot_bgcolor='white',font=dict(family='Lato',size=16,color="Black"),separators=',',title_x=0.1,title_y=0.95,showlegend=False)
            st.plotly_chart(fig,use_container_width=True)



        st.header('Porównanie liczby nauczycieli akademickich na wybranych wydziałach')
        
        wydz313 = st.multiselect('Wybierz wydział   :    ',DF24[DF24['Wydział']!='Ogółem UMK']['Wydział'].unique(),['Farmaceutyczny','Matematyki i Informatyki'])
        gz = st.radio('Średnio na 1 wydział UMK - Włącz/Wyłącz:',('Włącz','Wyłącz'))
        fig4 = px.bar(DF24[(DF24['Wydział'].isin(wydz313))].sort_values(by=['Wydział','Rok']),x='Rok',y='Liczba',barmode = 'group', color='Wydział',width=1500,height=500,color_discrete_sequence=list(map(lambda x: kolwyd1[x],sorted(wydz313))),pattern_shape="Wydział").update_yaxes(rangemode='tozero',tickformat=",",showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',title='Liczba nauczycieli akademickich').update_traces(textfont=dict( size=14),texttemplate="%{y:}",textposition='inside',hovertemplate = 'Liczba nauczycieli akademickich: <b>%{y:}</b>').update_xaxes(dtick=1).update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
        if gz == 'Włącz':
	        fig5 = px.line(DF25,x='Rok',y='Liczba',color_discrete_sequence=['rgb(0,80,170)'],markers=True).update_traces(textfont=dict( size=14),textposition="top left",texttemplate = "%{y:.2f}",hovertemplate = 'Średnia liczba nauczycieli akademickich: <b>%{y:,.2f}</b>').update_yaxes(tickformat=",").update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
	        fig4.add_trace(fig5.data[0])
	        st.plotly_chart(fig4,use_container_width=True)
        else:
            st.plotly_chart(fig4,use_container_width=True)


        st.header('Zmiana liczby nauczycieli akademickich w stosunku do roku poprzedniego w podziale na wydziały')
        wydz31 = st.multiselect('Wybierz wydział   :  ',DF24['Wydział'].unique(),['Ogółem UMK','Matematyki i Informatyki'])
        st.plotly_chart(px.line(DF24[(DF24['Wydział'].isin(wydz31))].sort_values(by=['Wydział','Rok']),x='Rok',y='Zmiana',color='Wydział',width=1400,height=500,symbol='Wydział',markers=True,color_discrete_sequence=list(map(lambda x: kolwyd1[x],sorted(wydz31))))
		    .update_traces(marker_size=10,textposition='top right',texttemplate="%{y:,.2f}%",textfont=dict( size=14),hovertemplate = 'Zmiana liczby nauczycieli akademickich: <b>%{y:,.2f}%</b>')
		    .update_yaxes(title='Zmiana liczby nauczycieli[%]',tickformat=",",showline=False,linewidth=1,gridwidth=1,gridcolor='gray',zeroline=True, zerolinewidth=4, zerolinecolor='rgba(0,0,0,1)')
		    .update_xaxes(dtick=1,range=[np.min(DF24[(DF24['Wydział'].isin(wydz31)) & (DF24['Zmiana'].notna())]['Rok'])-1/5,np.max(DF24[(DF24['Wydział'].isin(wydz31)) & (DF24['Zmiana'].notna())]['Rok'])+1/5],showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside')
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"),use_container_width=True)
        st.write('Wartości poniżej 0 oznaczają spadek liczby pracowników względem roku poprzedniego, a powyżej - wzrost.')


        st.header('Liczba studentów przypadających na jednego nauczyciela akademickiego w podziale na wydziały')  	
        wydz19 = st.multiselect('Wybierz wydział :  ',DF24['Wydział'].unique(),['Ogółem UMK','Matematyki i Informatyki'])
        st.plotly_chart(px.line(DF26[(DF26['Wydział'].isin(wydz19))].sort_values(by=['Wydział','Rok']),x='Rok',y='Stosunek',color='Wydział',width=1400,height=500,symbol='Wydział',markers=True,color_discrete_sequence=list(map(lambda x: kolwyd1[x],sorted(wydz19))))
		    .update_traces(marker_size=10,textposition='top right',texttemplate="%{y:,.2f}",textfont=dict( size=14),hovertemplate = 'Liczba studentów przypadających na jednego nauczyciela akademickiego: <b>%{y:,.2f}</b>')
		    .update_yaxes(tickformat=",",rangemode='tozero',showline=False,linewidth=1,gridwidth=1,gridcolor='gray',title='Stosunek liczby studentów do nauczycieli')
		    .update_xaxes(dtick=1,showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside',range=[2010-1/5,2022+1/5])
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"),use_container_width=True)

        st.header('Awanse nauczycieli akademickich (liczba uzyskanych tytułów i stopni)')
        aw = st.selectbox('Wybierz kategorię :         ', ['Profesor','Doktor habilitowany','Doktor'])
        st.plotly_chart(px.bar(DF35[DF35['Tytuł']==aw],x='Rok',y='Liczba',color='Jednostka',width=1400,height=500,color_discrete_sequence=['rgb(255,205,0)','rgb(250,20,20)']).update_traces(customdata=DF35[DF35['Tytuł']==aw].groupby('Rok')['Liczba'].agg(np.sum)[::-1],texttemplate="%{y:}",textfont=dict( size=14),
	      textposition='inside',hovertemplate = '<br>Liczba ogółem: <b>%{customdata}</b><br>'+'<extra></extra>')
	      .update_xaxes(title_font=dict(size=12), title='Rok',dtick=1).update_yaxes(title_font=dict(size=12),title = 'Liczba awansów',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_layout(legend_title_text='Kampus', plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")),use_container_width=True)
	
    
    elif sekcja2 == 'Wynagrodzenie':
        DF28 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Wynagrodzenie',dtype={'Rok':int})
        DF30 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Inflacja1',dtype={'Rok':float,'dr':str})
        DF28['Kategoria'] = DF28['Kategoria'].replace(['Ogółem'],'Ogółem UMK')
        st.header('Przeciętne wynagrodzenie brutto pracowników uniwersytetu')
        wydz318 = st.multiselect('Wybierz kategorię   :  ',DF28['Kategoria'].unique(),['Ogółem UMK','Średnia krajowa'])
        st.plotly_chart(px.line(DF28[DF28['Kategoria'].isin(wydz318)].sort_values(by=['Kategoria','Rok'],key=lambda x: x.map(pr_cy1)),x='Rok',y='Wynagrodzenie',color='Kategoria',width=1400,height=500,markers=True,color_discrete_sequence=list(map(lambda x: pr_cy[x],sorted(wydz318,key=lambda x: pr_cy1[x]))))
    		    .update_traces(textposition='top right',texttemplate="%{y:}",textfont=dict( size=14),hovertemplate = '<br>Przeciętne wynagrodzenie brutto: <b>%{y:}zł</b><br>'+'<extra></extra>')
    		    .update_yaxes(title='Przeciętne wynagrodzenie brutto',tickformat=",",zeroline=True, zerolinewidth=1, zerolinecolor='rgba(0,0,0,0.5)',rangemode='tozero',showline=False,linewidth=1,gridwidth=1,gridcolor='gray')
    		    .update_xaxes(dtick=1,range=[np.min(DF28[(DF28['Kategoria'].isin(wydz318)) & (DF28['Wynagrodzenie'].notna())]['Rok'])-1/5,np.max(DF28[(DF28['Kategoria'].isin(wydz318)) & (DF28['Wynagrodzenie'].notna())]['Rok'])+1/5],showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside')
    		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"),use_container_width=True)
        st.write('Średnia krajowa na podstawie danych GUS https://bdl.stat.gov.pl/bdl/start')
    	
      
    	
    	
    
        st.header('Zmiana przeciętnego wynagrodzenia brutto pracowników uniwersytetu w stosunku do roku poprzedniego [w %]')
    
        wydz31 = st.multiselect('Wybierz kategorię  :    ',DF28['Kategoria'].unique(),['Ogółem UMK','Średnia krajowa'])
        gz1 = st.radio('Inflacja w odniesieniu do analogicznego miesiąca roku poprzedniego - Włącz/Wyłącz:',('Włącz','Wyłącz'))
        fig44 = px.line(DF28[(DF28['Kategoria'].isin(wydz31))].sort_values(by=['Kategoria','Rok'],key=lambda x: x.map(pr_cy1)),x='Rok',y='Zmiana', color='Kategoria',width=1500,height=500,markers=True,color_discrete_sequence=list(map(lambda x: pr_cy[x],sorted(wydz31,key=lambda x: pr_cy1[x])))).update_yaxes(tickformat=",",showline=False,linewidth=1,gridwidth=1,gridcolor='gray',zeroline=True, zerolinewidth=4, zerolinecolor='rgba(0,0,0,1)',title='Zmiana przeciętnego wynagrodzenia brutto[%]').update_traces(textfont=dict( size=14),texttemplate="%{y:.2f}%",textposition='top right',hovertemplate = '<br>Zmiana przeciętnego wynagrodzenia brutto: <b>%{y:,.2f}%</b><br>'+'<extra></extra>').update_xaxes(dtick=1,range=[2012+9/12,2021+3/12],showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x")
        if gz1 == 'Włącz':
            fig44 = px.line(DF28[(DF28['Kategoria'].isin(wydz31))].sort_values(by=['Kategoria','dr'],key=lambda x: x.map(pr_cy1)),x='dr',y='Zmiana', color='Kategoria',width=1500,height=500,markers=True,color_discrete_sequence=list(map(lambda x: pr_cy[x],sorted(wydz31,key=lambda x: pr_cy1[x]))),custom_data=['dr']).update_yaxes(tickformat=",",showline=False,linewidth=1,gridwidth=1,gridcolor='gray',zeroline=True, zerolinewidth=4, zerolinecolor='rgba(0,0,0,1)',title='Zmiana przeciętnego wynagrodzenia brutto[%]').update_traces(textfont=dict( size=14),texttemplate="%{y:.2f}%",textposition='top right',hovertemplate = '<br>Zmiana przeciętnego wynagrodzenia brutto: <b>%{y:,.2f}%</b><br>'+'<extra></extra>').update_xaxes(tickformat="%Y",showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside',range=['2013-9','2023-3'],title='Rok').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode='x')
            fig55 = px.line(DF30,x='dr',y='Inflacja',color_discrete_sequence=['#d62728'],markers=True,custom_data=['dr1']).update_traces(textfont=dict( size=14),textposition="top left",texttemplate = "%{y:.2f}%",hovertemplate ='<br>Okres: <b>%{customdata}</b><br>'+'<i>Inflacja w Polsce</i>: <b>%{y:,.2f}%</b>'+'<extra></extra>').update_yaxes(tickformat=",",showline=False,linewidth=1,gridwidth=1,gridcolor='gray').update_xaxes(tickformat="%m-%Y",showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
            fig44.add_trace(fig55.data[0])
            st.plotly_chart(fig44,use_container_width=True)
        else:
            st.plotly_chart(fig44,use_container_width=True)
        st.write('Wartości poniżej 0 oznaczają spadek przeciętnego wynagrodzenia brutto względem roku poprzedniego, a powyżej - wzrost.')
        st.write('Dane o inflacji  https://stat.gov.pl/obszary-tematyczne/ceny-handel/wskazniki-cen/wskazniki-cen-towarow-i-uslug-konsumpcyjnych-pot-inflacja-/roczne-wskazniki-cen-towarow-i-uslug-konsumpcyjnych/')
    

   
    
    
      
      
      

      
      
      
      
      
elif sekcja == 'Badania naukowe':

    st.markdown('---')
    sekcja3 = option_menu(None, ["Granty Narodowego Centrum Nauki", 'Granty ministerstwa właściwego ds. nauki'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "rgb(255,205,0)"},
        "icon": {"color": "white", "font-size": "18px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "rgb(255,205,0)"},
        "nav-link-selected": {"background-color": "rgb(0,70,180)"},
    }
    )
    
    
    if sekcja3 == 'Granty Narodowego Centrum Nauki':
        DF4 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Granty_złożone',dtype={'Rok':int})
        DF6 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Granty_przyznane',dtype={'Rok':int})
        DF31 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Sukces',dtype={'Rok':int})
        
        
        st.header('Granty Narodowego Centrum Nauki')
        roki = st.selectbox('Wybierz rok:   '   ,lata[::-1])
        li = st.selectbox('Wybierz podsumowanie:',['Liczba','Kwota'])
        if (li == 'Kwota'):
            kw = pd.DataFrame(DF4[DF4['Rok']==roki].groupby('Jednostka')['Kwota wnioskowana[zł]'].agg(np.sum)).sort_values(by='Kwota wnioskowana[zł]')[::-1]
            if not kw.empty:
                kw.loc[' '] = None
            x = kw.index[::-1]
            y = kw['Kwota wnioskowana[zł]'][::-1]
            
            
            kw = kw.reset_index()
            kw['kolor']=' '
            for j,i in enumerate(kw['Jednostka']):
                if i in list(kolwyd.keys()):
                    kw['kolor'][j] = kolwyd[i]
                else:
                    kw['kolor'][j] = 'rgb(0,70,180)'
            barwa = kw['kolor'][::-1]
            barwa[::-1].loc[17] = 'rgb(0,70,180)'
            
            
            kw1 = pd.DataFrame(DF6[DF6['Rok']==roki].groupby('Jednostka')['Kwota przyznana[zł]'].agg(np.sum)).sort_values(by='Kwota przyznana[zł]')[::-1]
            if not kw1.empty:
                kw1.loc[' '] = None
            x1 = kw1.index[::-1]
            y1 = kw1['Kwota przyznana[zł]'][::-1]
            kw1 = kw1.reset_index()
            kw1['kolor']=' '
            for j,i in enumerate(kw1['Jednostka']):
                if i in list(kolwyd.keys()):
                    kw1['kolor'][j] = kolwyd[i]
                else:
                    kw1['kolor'][j] = 'rgb(0,70,180)'
            barwa3 = kw1['kolor'][::-1]
            barwa3[::-1].loc[17] = 'rgb(0,70,180)'
            fig = go.Figure()
            fig.add_trace(go.Bar(x=y1,y=x1,orientation='h',
                                textfont=dict( size=12,color='black'),marker_color=barwa3,marker_line_color='black',marker_line_width=1.5,name='Przyznany',
                              textposition='outside',hovertemplate = '<br>Kwota przyznanych grantów: <b>%{x:,}zł</b><br>'+"<extra></extra>",legendrank=1))
        
            fig.add_trace(go.Bar(x=y,y=x,orientation='h',
            				textfont=dict( size=12,color='black'),marker_color=barwa,marker_line_color='black',marker_line_width=1.5,name='Złożony',marker_pattern_shape="x",
            			      textposition='outside',hovertemplate = '<br>Kwota wnioskowana: <b>%{x:,}zł</b><br>'+"<extra></extra>",legendrank=2))
            fig.update_xaxes(title='Kwota[zł]')
            fig.update_yaxes(title='Wydział')
            fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title_x=0.5,legend_traceorder='reversed',
            					height=800,width=1400,plot_bgcolor='white',margin=dict(t=100, b=0, l=180, r=50),font=dict(family='Lato',size=18,color="Black"),showlegend=True,legend_orientation='h',legend_x=-0.1,legend_yanchor='top',legend_y=1.1,
    			 legend_title_text='Rodzaj wniosku')
            
            st.plotly_chart(fig,use_container_width=True)
    	    
        elif (li == 'Liczba'):
            lw = pd.DataFrame(DF4[DF4['Rok']==roki].groupby('Jednostka')['Liczba wniosków'].agg(np.sum)).sort_values(by='Liczba wniosków')[::-1]
            if not lw.empty:
                lw.loc[' '] = None
            x = lw.index[::-1]
            y = lw['Liczba wniosków'][::-1]
            
            
            lw = lw.reset_index()
            lw['kolor']=' '
            for j,i in enumerate(lw['Jednostka']):
                if i in list(kolwyd.keys()):
                    lw['kolor'][j] = kolwyd[i]
                else:
                    lw['kolor'][j] = 'rgb(0,70,180)'
            barwa1 = lw['kolor'][::-1]
            barwa1[::-1].loc[17] = 'rgb(0,70,180)'
            
            lg = pd.DataFrame(DF6[DF6['Rok']==roki].groupby('Jednostka')['Liczba grantów'].agg(np.sum)).sort_values(by='Liczba grantów')[::-1]
            if not lg.empty:
                lg.loc[' '] = None
            x1 = lg.index[::-1]
            y1 = lg['Liczba grantów'][::-1]
        
        
            lg = lg.reset_index()
            lg['kolor']=' '
            for j,i in enumerate(lg['Jednostka']):
                if i in list(kolwyd.keys()):
                    lg['kolor'][j] = kolwyd[i]
                else:
                    lg['kolor'][j] = 'rgb(0,70,180)'
            barwa4 = lg['kolor'][::-1]
            barwa4[::-1].loc[17] = 'rgb(0,70,180)'
        
            fig = go.Figure()
            fig.add_trace(go.Bar(x=y1,y=x1,orientation='h',
                                textfont=dict( size=12,color='black'),marker_color=barwa4,marker_line_color='black',marker_line_width=1.5,name='Przyznany',
                              textposition='outside',hovertemplate = '<br>Liczba przyznanych grantów: <b>%{x:}</b><br>'+"<extra></extra>",legendrank=1))
        
            
            
            fig.add_trace(go.Bar(x=y,y=x,orientation='h',
            				textfont=dict( size=12,color='black'),marker_color=barwa1,marker_line_color='black',marker_line_width=1.5,name='Złożony',marker_pattern_shape="x",
            			      textposition='outside',hovertemplate = '<br>Wnioski złożone: <b>%{x:}</b><br>'+"<extra></extra>",legendrank=2))
            fig.update_xaxes(title='Liczba wniosków')
            fig.update_yaxes(title='Wydział')
            
            fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title_x=0.5,legend_title_text='Rodzaj wniosku',
            					height=800,width=1600,plot_bgcolor='white',margin=dict(t=100, b=0, l=180, r=50),font=dict(family='Lato',size=18,color="Black"),legend_traceorder='reversed',
            					separators =',',showlegend=True,legend_orientation='h',legend_x=-0.1,legend_yanchor='top',legend_y=1.1)
            
            st.plotly_chart(fig,use_container_width=True)	
        
        else:
            st.write('Dla lat 2012-2018 nie dysponujemy danymi o składanych wnioskach')
        
        
        
        if (roki in [2019,2020,2021,2022]) and (li == 'Liczba') :		       
            kw = pd.DataFrame(DF31[DF31['Rok']==roki].groupby('Jednostka')['Skuteczność'].agg(np.sum)).sort_values(by='Skuteczność')[::-1]
            x = kw.index[::-1]
            y = kw['Skuteczność'][::-1]
    
            kw = kw.reset_index()
            kw['kolor']=' '
            for j,i in enumerate(kw['Jednostka']):
                if i in list(kolwyd.keys()):
                    kw['kolor'][j] = kolwyd[i]
                else:
                    kw['kolor'][j] = 'rgb(0,70,180)'
            barwa = kw['kolor'][::-1]
    
            fig = go.Figure()
            fig.add_trace(go.Bar(x=y,y=x,orientation='h',
            textfont=dict( size=12,color='black')))
            fig.update_traces(marker_color=barwa,marker_line_color='black',marker_line_width=1.5
            ,hovertemplate = '<br>Skuteczność: <b>%{x:,.2f}%</b><br>'+"<extra></extra>")
            fig.update_xaxes(title='Skuteczność [%]')
            fig.update_yaxes(title='Wydział')
    
            fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title='<b>Współczynnik skuteczności',title_x=0.5,
            height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=0, l=180, r=50),font=dict(family='Lato',size=18,color="Black"),separators=',')
    
            st.plotly_chart(fig,use_container_width=True)
            st.write('Współczynnik skuteczności jest określony jako stosunek liczby lub kwoty (odpowiednio) przyznanych grantów do złożonych wniosków (w %).')
            st.write('W 2019 roku Collegium Medicum nie prowadziło rejestru złożonych krajowych wniosków grantowych, dlatego dane dotyczące wniosków odnoszą się tylko do toruńskiej części UMK.')
            st.write('Skuteczność powyżej 100% może wynikać z faktu, że w danym roku przyznano grant, o który wnioskowano w roku wcześniejszym.')
        elif (li == 'Liczba') and (roki not in [2019,2020,2021,2022]) :
            st.write('Dla lat 2012-2018 nie dysponujemy danymi o składanych wnioskach')
            
        if (roki in [2019,2020,2021,2022]) and (li == 'Kwota') :		       
            kw = pd.DataFrame(DF31[DF31['Rok']==roki].groupby('Jednostka')['Skuteczność1'].agg(np.sum)).sort_values(by='Skuteczność1')[::-1]
            x = kw.index[::-1]
            y = kw['Skuteczność1'][::-1]
    
            kw = kw.reset_index()
            kw['kolor']=' '
            for j,i in enumerate(kw['Jednostka']):
                if i in list(kolwyd.keys()):
                    kw['kolor'][j] = kolwyd[i]
                else:
                    kw['kolor'][j] = 'rgb(0,70,180)'
            barwa = kw['kolor'][::-1]
    
            fig = go.Figure()
            fig.add_trace(go.Bar(x=y,y=x,orientation='h',
            textfont=dict( size=12,color='black')))
            fig.update_traces(marker_color=barwa,marker_line_color='black',marker_line_width=1.5
            ,hovertemplate = '<br>Skuteczność: <b>%{x:,.2f}%</b><br>'+"<extra></extra>")
            fig.update_xaxes(title='Skuteczność [%]')
            fig.update_yaxes(title='Wydział')
    
            fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title='<b>Współczynnik skuteczności',title_x=0.5,
            height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=0, l=180, r=50),font=dict(family='Lato',size=18,color="Black"),separators=',')
    
            st.plotly_chart(fig,use_container_width=True)
            st.write('Współczynnik skuteczności jest określony jako stosunek liczby lub kwoty (odpowiednio) przyznanych grantów do złożonych wniosków (w %).')
            st.write('W 2019 roku Collegium Medicum nie prowadziło rejestru złożonych krajowych wniosków grantowych, dlatego dane dotyczące wniosków odnoszą się tylko do toruńskiej części UMK.')
            st.write('Skuteczność powyżej 100% może wynikać z faktu, że w danym roku przyznano grant, o który wnioskowano w roku wcześniejszym.')
        elif (li == 'Kwota') and (roki not in [2019,2020,2021]) :
            st.write('Dla lat 2012-2018 nie dysponujemy danymi o składanych wnioskach')
        
        
    
    elif sekcja3 == 'Granty ministerstwa właściwego ds. nauki':
        DF32 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='MEiN_pr',dtype={'Rok':int})
        DF33 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='MEiN_zl',dtype={'Rok':int})
        DF34 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Sukces_mein',dtype={'Rok':float})
        
        st.header('Granty ministerstwa właściwego ds. nauki')
        roki1 = st.selectbox('Wybierz rok: ',[2015,2016,2017,2018,2019,2020,2021,2022][::-1])
        li1 = st.selectbox('Wybierz podsumowanie: ',['Liczba','Kwota'])
        if (li1 == 'Kwota') and (roki1 > 2018):		       
            kw = pd.DataFrame(DF33[DF33['Rok']==roki1].groupby('Jednostka')['Kwota wnioskowana[zł]'].agg(np.sum)).sort_values(by='Kwota wnioskowana[zł]')[::-1]
            x = kw.index[::-1]
            y = kw['Kwota wnioskowana[zł]'][::-1]
            
            kw = kw.reset_index()
            kw['kolor']=' '
            for j,i in enumerate(kw['Jednostka']):
                if i in list(kolwyd.keys()):
                    kw['kolor'][j] = kolwyd[i]
                else:
                    kw['kolor'][j] = 'rgb(0,70,180)'
            barwa = kw['kolor'][::-1]
            
            
            fig1 = go.Figure()
            fig1.add_trace(go.Bar(x=y,y=x,orientation='h',
            				textfont=dict( size=12,color='black'),marker_color=barwa,marker_line_color='black',marker_line_width=1.5,
            			      hovertemplate = '<br>Kwota wnioskowana: <b>%{x:,}zł</b><br>'+"<extra></extra>"))
            fig1.update_xaxes(title='Kwota wnioskowana[zł]')
            fig1.update_yaxes(title='Wydział')
            
            fig1.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title='<b>Wnioski złożone',title_x=0.5,
            					height=800,width=1600,plot_bgcolor='white',margin=dict(t=100, b=0, l=180, r=50),font=dict(family='Lato',size=18,color="Black"))
            
            st.plotly_chart(fig1,use_container_width=True)
            
        elif (li1 == 'Kwota') and (roki1 <= 2018):		       
            st.write('Dla lat poniżej 2019 roku nie dysponujemy danymi o składanych wnioskach.')
            
        if (li1 == 'Kwota'):		       
            kw1 = pd.DataFrame(DF32[DF32['Rok']==roki1].groupby('Jednostka')['Kwota przyznana[zł]'].agg(np.sum)).sort_values(by='Kwota przyznana[zł]')[::-1]
            x1 = kw1.index[::-1]
            y1 = kw1['Kwota przyznana[zł]'][::-1]
            kw1 = kw1.reset_index()
            kw1['kolor']=' '
            for j,i in enumerate(kw1['Jednostka']):
                if i in list(kolwyd.keys()):
                    kw1['kolor'][j] = kolwyd[i]
                else:
                    kw1['kolor'][j] = 'rgb(0,70,180)'
            barwa3 = kw1['kolor'][::-1]
        
            fig = go.Figure()
            fig.add_trace(go.Bar(x=y1,y=x1,orientation='h',
                                textfont=dict( size=12,color='black'),marker_color=barwa3,marker_line_color='black',marker_line_width=1.5,
                              hovertemplate = '<br>Kwota przyznanych grantów: <b>%{x:,}zł</b><br>'+"<extra></extra>"))
            fig.update_xaxes(title='Kwota przyznana[zł]')
            fig.update_yaxes(title='Wydział')
            fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),
            					height=800,width=1600,plot_bgcolor='white',margin=dict(t=100, b=0, l=180, r=50),font=dict(family='Lato',size=18,color="Black"),title='<b>Granty przyznane',title_x=0.5)
            
            st.plotly_chart(fig,use_container_width=True)
        if (li1 == 'Liczba') and (roki1 > 2018):
            lw = pd.DataFrame(DF33[DF33['Rok']==roki1].groupby('Jednostka')['Liczba wniosków'].agg(np.sum)).sort_values(by='Liczba wniosków')[::-1]
            x = lw.index[::-1]
            y = lw['Liczba wniosków'][::-1]
            
            
            lw = lw.reset_index()
            lw['kolor']=' '
            for j,i in enumerate(lw['Jednostka']):
                if i in list(kolwyd.keys()):
                    lw['kolor'][j] = kolwyd[i]
                else:
                    lw['kolor'][j] = 'rgb(0,70,180)'
            barwa1 = lw['kolor'][::-1]
            
            
            fig1 = go.Figure()
            fig1.add_trace(go.Bar(x=y,y=x,orientation='h',
            				textfont=dict( size=12,color='black'),marker_color=barwa1,marker_line_color='black',marker_line_width=1.5,
            			      hovertemplate = '<br>Wnioski złożone: <b>%{x:}</b><br>'+"<extra></extra>"))
            fig1.update_xaxes(title='Liczba złożonych wniosków')
            fig1.update_yaxes(title='Wydział')
            
            fig1.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title='<b>Wnioski złożone',title_x=0.5,
            					height=800,width=1600,plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),
            					separators =',',margin=dict(t=100, b=0, l=180, r=50))
            
            st.plotly_chart(fig1,use_container_width=True)	
            
        elif (li1 == 'Liczba') and (roki1 <= 2018):
            st.write('Dla lat poniżej 2019 roku nie dysponujemy danymi o składanych wnioskach.')
        if (li1 == 'Liczba'):
            lg = pd.DataFrame(DF32[DF32['Rok']==roki1].groupby('Jednostka')['Liczba grantów'].agg(np.sum)).sort_values(by='Liczba grantów')[::-1]
            x1 = lg.index[::-1]
            y1 = lg['Liczba grantów'][::-1]
        
        
            lg = lg.reset_index()
            lg['kolor']=' '
            for j,i in enumerate(lg['Jednostka']):
                if i in list(kolwyd.keys()):
                    lg['kolor'][j] = kolwyd[i]
                else:
                    lg['kolor'][j] = 'rgb(0,70,180)'
            barwa4 = lg['kolor'][::-1]
        
            fig = go.Figure()
            fig.add_trace(go.Bar(x=y1,y=x1,orientation='h',
                                textfont=dict( size=12,color='black'),marker_color=barwa4,marker_line_color='black',marker_line_width=1.5,
                              hovertemplate = '<br>Liczba przyznanych grantów: <b>%{x:}</b><br>'+"<extra></extra>"))
            fig.update_xaxes(title='Liczba przyznanych grantów')
            fig.update_yaxes(title='Wydział')
            fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title='<b>Granty przyznane',title_x=0.5,
            					height=800,width=1600,plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),
            					separators =',',margin=dict(t=100, b=0, l=180, r=50))
            
            st.plotly_chart(fig,use_container_width=True)

        st.write('Liczba przyznanych grantów może być większa niż złożonych wniosków, gdyż granty mogą być przyznane w roku kalendarzowym następującym po roku złożenia wniosku.')	      
	

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            [data-testid="stDecoration"]{background-image: linear-gradient(90deg,#FFCD00 ,#0050AA );height: 0.25rem;}
            [class="stActionButton"] {visibility: hidden;}
            
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)




#
#css-1adrfps e1fqkh3o2
#css-qrbaxs effi0qh3
