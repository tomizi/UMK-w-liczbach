import os
import pandas as pd
import numpy as np
import streamlit as st
import openpyxl
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path






st.set_page_config(page_title='UMK w liczbach', page_icon = ':page_facing_up:',initial_sidebar_state='expanded',layout='wide')

DF = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='nauczyciele',dtype={'Rok':int})
DF2 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',dtype={'Lata':str})
DF3 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',dtype={'Rok':str},sheet_name='podział')

DF4 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Granty_złożone',dtype={'Rok':int})
DF5 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='nauczyciele_wydziały',dtype={'Rok':str})
DF6 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Granty_przyznane',dtype={'Rok':int})

DF7 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='L_kier_stud',dtype={'Rok':str})
DF8 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='N-wni',dtype={'Rok':int})
DF9 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Z-czni',dtype={'Rok':int})
#DF7 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Wyjazdy',dtype={'Rok':int})
#DF8 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Przyjazdy')

lata = [2019,2020,2021]
wydziały = ['Matematyki i Informatyki',
                                                    'Chemii','Humanistyczny','Fizyki, Astronomii i Informatyki Stosowanej','Filozofii i Nauk Społecznych',
                                                    'Nauk Biologicznych i Weterynaryjnych','Nauk Ekonomicznych i Zarządzania','Nauk Historycznych','Nauk o Ziemi i Gospodarki Przestrzennej',
                                                    'Nauk o Polityce i Bezpieczeństwie','Prawa i Administracji','Sztuk Pięknych','Teologiczny','Lekarski',
                                                    'Farmaceutyczny','Nauk o Zdrowiu','Ogółem']
kolor = {'fioletowy':'rgb(170,40,150)','niebieski':'rgb(0,175,250)','zielony':'rgb(0,165,80)','oliwkowy':'rgb(170,210,60)','pomarańczowy':'rgb(255,130,30)','czerwony':'rgb(250,20,20)'}
kolwyd = {'Nauk Biologicznych i Weterynaryjnych':kolor['zielony'],
           'Chemii':kolor['oliwkowy'],'Humanistyczny':kolor['niebieski'],'Fizyki, Astronomii i Informatyki Stosowanej':kolor['oliwkowy'],
          'Filozofii i Nauk Społecznych':kolor['fioletowy'],'Matematyki i Informatyki':kolor['oliwkowy'],'Nauk Ekonomicznych i Zarządzania':kolor['fioletowy'],
          'Nauk Historycznych':kolor['niebieski'],
          'Nauk o Ziemi i Gospodarki Przestrzennej':kolor['zielony'],'Nauk o Polityce i Bezpieczeństwie':kolor['fioletowy'],'Prawa i Administracji':kolor['fioletowy'],'Sztuk Pięknych':kolor['pomarańczowy'],
          'Teologiczny':kolor['niebieski'],'Lekarski':kolor['czerwony'],'Farmaceutyczny':kolor['czerwony'],'Nauk o Zdrowiu':kolor['czerwony'],'Ogółem':'rgb(0,80,170)'}



        
        
        
        
        
        
sekcja = st.sidebar.radio(
    'Wybierz sekcję:',
    ('Strona główna','Studenci','Pracownicy','Badania naukowe')
 )
#st.sidebar.image('', use_column_width=True)

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
[data-testid="stAppViewContainer"] > .main {background-image: url("https://login.umk.pl/themes/umk/images/logo-umk.png");
background-size:400px,400px;
background-position: 1150px 100px;
background-repeat: no-repeat;
background-attachment: local;}
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








if sekcja == 'Strona główna':
    new_title = '<b style="color:rgb(0, 80, 170); font-size: 62px;">Strona główna</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('---')
    st.title('UNIWERSYTET MIKOŁAJA KOPERNIKA W TORUNIU')
    st.subheader('Uniwersytet podzielony jest na wydziały. Każdy wydział ma unikatowe logo, które charakteryzuje kolor ' +
	      'i pozycja mniejszego kółka na obwodzie większego niebieskiego koła. Poniższa grafika przedstawia loga poszczególnych ' + 
	      'wydziałów. Warto zapoznać się z barwami jednostek, ponieważ są one częścią wizualizacji znajdujących się na pozostałych stronach.'+ 
	      ' Ich znajomość ułatwi interpretację wykresów.')
    st.image('https://www.umk.pl/siw/galeria_inspiracje/UMKins8.jpg')
    
    
    
    
    
    
if sekcja == 'Studenci':
    new_title = '<b style="color:rgb(0, 80, 170); font-size: 62px;">Studenci</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('---')
    
    st.header('Liczba kierunków studiów w latach 2009-2021')
    st.plotly_chart(px.bar(DF7,x='Rok',y='Liczba',width=1400,height=500).update_traces(marker_color='rgb(0,80,170)',texttemplate="%{y:}",
	textposition='inside',marker_line_color='rgb(0,70,180)',marker_line_width=2.5)
	.update_xaxes(title_font=dict(size=12), title='Lata').update_yaxes(title_font=dict(size=12),title = 'Liczba kierunków').update_layout(font_family='Lato'))
	
	
    st.header('Odsetek studentów niepełnosprawnych w latach 2012-2021 w podziale na rodzaj studiów')
    st.plotly_chart(px.line(DF8,x='Rok',y='Odsetek',color = 'Rodzaj',width=1500,height=500,text='Odsetek',color_discrete_sequence=['rgb(0,80,170)','rgb(0,200,255)','red','rgb(255,50,80)'])
		    .update_traces(marker_color=('rgb(0,80,170)'),textposition="top right",texttemplate = "%{y:.2f}%")
	.update_xaxes(title_font=dict(size=12), title='Rok',range=[2011.95,2022],dtick=1).update_yaxes(title_font=dict(size=12),title = 'Odsetek osób niepełnosprawnych',tickformat=",",range=[-0.05, 3.5])
		    .update_layout(font_family='Lato',separators=','))
	
    st.header('Odsetek studentów zagranicznych w latach 2012-2021 w podziale na rodzaj studiów')
    st.plotly_chart(px.line(DF9,x='Rok',y='Odsetek',color = 'Rodzaj',width=1500,height=500,text='Odsetek',color_discrete_sequence=['rgb(0,80,170)','rgb(0,200,255)','red','rgb(255,50,80)'])
		    .update_traces(marker_color=('rgb(0,80,170)'),textposition="top right",texttemplate = "%{y:.2f}%")
	.update_xaxes(title_font=dict(size=12), title='Rok',range=[2011.95,2022],dtick=1).update_yaxes(title_font=dict(size=12),title = 'Odsetek osób zagranicznych',tickformat=",",range=[-0.05, 5.5])
		    .update_layout(font_family='Lato',separators=','))	
    st.header('Liczba studentów i absolwentów studiów stacjonarnych i niestacjonarnych w latach 2019-2021 na poszczgólnych wydziałach')

    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader('Studia stacjonarne')   
        wydzial = st.selectbox('Wybierz wydział:',wydziały)
        st.plotly_chart(px.bar(DF3[DF3['Wydział']==wydzial],x='Rok',y='Stacjonarne',width=550,height=400).update_traces(marker_color=kolwyd[wydzial],
	texttemplate="%{y:}",textposition='inside',
        marker_line_color='rgb(0,70,180)',marker_line_width=2.5).update_layout(font_family='Lato'))
    with c2:
        st.subheader('Studia niestacjonarne')
        wydzial1 = st.selectbox('Wybierz wydział: ',wydziały)
        #kat1 = st.selectbox('Wybierz kategorię: ', ['Stacjonarne','Niestacjonarne','Razem'])
        st.plotly_chart(px.bar(DF3[DF3['Wydział']==wydzial1],x='Rok',y='Niestacjonarne',width=550,height=400).update_traces(marker_color=kolwyd[wydzial1],texttemplate="%{y:}",
	textposition='inside',marker_line_color='rgb(0,70,180)',marker_line_width=2.5)
			.update_xaxes(title_font=dict(size=18)).update_yaxes(title_font=dict(size=18)).update_layout(font_family='Lato'))
    with c3:
        st.subheader('Razem')   
        wydzial2 = st.selectbox('Wybierz wydział:  ',wydziały)
        st.plotly_chart(px.bar(DF3[DF3['Wydział']==wydzial2],x='Rok',y='Razem',width=550,height=400).update_traces(marker_color=kolwyd[wydzial2],texttemplate="%{y:}",textposition='inside',
        marker_line_color='rgb(0,70,180)',marker_line_width=2.5).update_xaxes(title_font=dict(size=18)).update_yaxes(title_font=dict(size=18)).update_layout(font_family='Lato'))
        
    st.subheader('Liczba studentów i absolwentów studiów stacjonarnych i niestacjonarnych oraz uczestników studiów doktoranckich i słuchaczy studiów podyplomowych w latach 2019-2021')              
    kat = st.selectbox('Wybierz kategorię:',['Studia wyższe stacjonarne','Studia wyższe niestacjonarne','Doktoranckie','Podyplomowe','Razem'])
    st.plotly_chart(px.line(DF2,x='Lata',y=kat,width=1400,height=500,markers=True,text=kat).update_traces(marker_color=('rgb(0,80,170)'),textposition='top right',texttemplate="%{y:,d}",
				line_color=('rgb(0,80,170)')).update_yaxes(tickformat=",").update_layout(font_family='Lato',separators='.,'))      
    
    
    
    
    
    
    
    
    
if sekcja == 'Pracownicy':
    new_title = '<b style="color:rgb(0, 80, 170); font-size: 60px;">Nauczyciele akademiccy i administracja</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('---')
    
    st.header("Liczba nauczycieli akademickich w poszczególnych grupach w latach 2019-2021")
    k1,k2,k3 = st.columns(3)
    
    with k1:
        st.subheader("Grupa badawcza")
        rok = st.selectbox('Wybierz rok:', lata[::-1])
        fig = go.Figure(data=[go.Pie(labels=DF[(DF['badawcza']!=0) & (DF['Rok']==rok)].sort_values(by='badawcza')['Stanowisko'][::-1],
				     values=DF[(DF['badawcza']!=0) & (DF['Rok']==rok)].sort_values(by='badawcza')['badawcza'][::-1])])
        fig.update_traces(textinfo='value+percent',marker=dict( colors=['#0050AA','#0262cf','#157aed','#2188fc'],line=dict(color='#0050AA', width=2)))
        fig.update_layout(legend=dict(x=0,y=1.2),margin=dict(t=80, b=100, l=0, r=100),font_family='Lato',separators=',')
        st.plotly_chart(fig)
    with k2:
        st.subheader("Grupa badawczo-dydaktyczna")
        rok1 = st.selectbox('Wybierz rok: ', lata[::-1])
        fig = go.Figure(data=[go.Pie(labels=DF[(DF['badawcza-dydaktyczna']!=0) & (DF['Rok']==rok1)].sort_values(by='badawcza-dydaktyczna')['Stanowisko'][::-1],
				     values=DF[(DF['badawcza-dydaktyczna']!=0) & (DF['Rok']==rok1)].sort_values(by='badawcza-dydaktyczna')['badawcza-dydaktyczna'][::-1])])
        fig.update_traces(textinfo='value+percent',marker=dict( colors=['#0050AA','#0262cf','#157aed','#2188fc'],line=dict(color='#0050AA', width=2)))
        fig.update_layout(legend=dict(x=0,y=1.2),margin=dict(t=80, b=100, l=0, r=100),font_family='Lato',separators=',')
        st.plotly_chart(fig)     
    with k3:
        st.subheader("Grupa dydaktyczna")
        rok2 = st.selectbox('Wybierz rok:  ', lata[::-1])
        fig = go.Figure(data=[go.Pie(labels=DF[(DF['dydaktyczna']!=0) & (DF['Rok']==rok2)].sort_values(by='dydaktyczna')['Stanowisko'][::-1],
				     values=DF[(DF['dydaktyczna']!=0) & (DF['Rok']==rok2)].sort_values(by='dydaktyczna')['dydaktyczna'][::-1])])
        fig.update_traces(textinfo='value+percent',marker=dict( colors=['#0050AA','#0262cf','#157aed','#2188fc','#51a2fc'],line=dict(color='#0050AA', width=2)))
        fig.update_layout(legend=dict(x=-0.3,y=1.2),margin=dict(t=80, b=100, l=0, r=160),font_family='Lato',separators=',')
        st.plotly_chart(fig)
    

    st.header('Porównanie liczby nauczycieli akademickich w latach 2019-2021 na wybranych wydziałach')
    ck1,ck2 = st.columns(2)
    wydział = ck1.selectbox("Wybierz wydział:",DF5['Jednostka Organizacyjna'].unique()[:-5])
    wydział1 = ck2.selectbox("Wybierz wydział: ",DF5['Jednostka Organizacyjna'].unique()[:-5][DF5[DF5['Jednostka Organizacyjna'] == wydział].index.tolist()[0]+1:])
    fig = px.line(DF5[DF5['Jednostka Organizacyjna'].isin([wydział,wydział1])],x='Rok',
		  y='Liczba nauczycieli akademickich',color='Jednostka Organizacyjna',width=1400,height=500,symbol_sequence= ['circle'],
		  markers=True,color_discrete_sequence=[kolwyd[wydział], kolwyd[wydział1]],text='Liczba nauczycieli akademickich').update_traces(marker_color=('rgb(0,80,170)'),
		  textposition="top right").update_xaxes(autorange="reversed").update_layout(font_family='Lato').add_annotation(x=1, y=int(DF5[(DF5['Rok']=='2020') & (DF5['Jednostka Organizacyjna']==wydział)]['Liczba nauczycieli akademickich']),
            text=wydział,showarrow=True,font=dict(size=16),ax=50,ay=-50).add_annotation(x=1, y=int(DF5[(DF5['Rok']=='2020') & (DF5['Jednostka Organizacyjna']==wydział1)]['Liczba nauczycieli akademickich']),
            text=wydział1,showarrow=True,arrowhead=1,font=dict(size=16),ax=-50,ay=50)
    st.plotly_chart(fig)
    
      
      
      

      
      
      
      
      
if sekcja == 'Badania naukowe':
    new_title = '<b style="color:rgb(0, 80, 170); font-size: 62px;">Badania naukowe</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('---')
    st.header('Kwota grantów wnioskowana do NCN w latach 2019-2021 w podziale na jednostki')
    roki = st.selectbox('Wybierz rok:',lata)
    kw = pd.DataFrame(DF4[DF4['Rok']==roki].groupby('Jednostka')['Kwota wnioskowana[zł]'].agg(np.sum)).sort_values(by='Kwota wnioskowana[zł]')[::-1]
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

    fig = go.Figure()
    fig.add_trace(go.Bar(x=y,y=x,orientation='h',text=y,
                        textfont=dict( size=10,color='black')))
    fig.update_traces(marker_color=barwa,marker_line_color='black',marker_line_width=1.5,
                      textposition='outside',texttemplate = "<b>%{x:,t}")
    fig.update_xaxes(title='Kwota wnioskowana[zł]')
    fig.update_yaxes(title='Jednostka')

    fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),
                                height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=100, l=0, r=200),font_family='Lato')

    st.plotly_chart(fig)
	
    st.header('Kwota grantów przyznana od NCN w latach 2019-2021 w podziale na jednostki')
    roki2 = st.selectbox('Wybierz rok:  ',lata)
    kw1 = pd.DataFrame(DF6[DF6['Rok']==roki2].groupby('Jednostka')['Kwota przyznana[zł]'].agg(np.sum)).sort_values(by='Kwota przyznana[zł]')[::-1]
    x = kw1.index[::-1]
    y = kw1['Kwota przyznana[zł]'][::-1]
    kw1 = kw1.reset_index()
    kw1['kolor']=' '
    for j,i in enumerate(kw1['Jednostka']):
        if i in list(kolwyd.keys()):
            kw1['kolor'][j] = kolwyd[i]
        else:
            kw1['kolor'][j] = 'rgb(0,70,180)'
    barwa3 = kw1['kolor'][::-1]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=y,y=x,orientation='h',text=y,
                        textfont=dict( size=10,color='black')))
    fig.update_traces(marker_color=barwa3,marker_line_color='black',marker_line_width=1.5,
                      textposition='outside',texttemplate = "<b>%{x:,t}")
    fig.update_xaxes(title='Kwota przyznana[zł]')
    fig.update_yaxes(title='Jednostka')

    fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),
                                height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=100, l=0, r=200),font_family='Lato')

    st.plotly_chart(fig) 
     

    
    st.header('Wnioski grantowe złożone do NCN w latach 2019-2021 w podziale na jednostki')      
	      
    roki1 = st.selectbox('Wybierz rok: ',lata)
    lw = pd.DataFrame(DF4[DF4['Rok']==roki1].groupby('Jednostka')['Liczba wniosków'].agg(np.sum)).sort_values(by='Liczba wniosków')[::-1]
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

    fig = go.Figure()
    fig.add_trace(go.Bar(x=y,y=x,orientation='h',text=y,
                        textfont=dict( size=12,color='black')))
    fig.update_traces(marker_color=barwa1,marker_line_color='black',marker_line_width=1.5,
                      textposition='outside',texttemplate = "<b>%{x:}")
    fig.update_xaxes(title='Liczba wniosków')
    fig.update_yaxes(title='Jednostka')

    fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),
                                height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=100, l=0, r=200),font_family='Lato',
                                separators =',')

    st.plotly_chart(fig)
	
	
    
    
    st.header('Liczba grantów przyznanych od NCN w latach 2019-2021 w podziale na jednostki')      
	      
    roki4 = st.selectbox('Wybierz rok:   ',lata)
    lg = pd.DataFrame(DF6[DF6['Rok']==roki4].groupby('Jednostka')['Liczba grantów'].agg(np.sum)).sort_values(by='Liczba grantów')[::-1]
    x = lg.index[::-1]
    y = lg['Liczba grantów'][::-1]


    lg = lg.reset_index()
    lg['kolor']=' '
    for j,i in enumerate(lg['Jednostka']):
        if i in list(kolwyd.keys()):
            lg['kolor'][j] = kolwyd[i]
        else:
            lg['kolor'][j] = 'rgb(0,70,180)'
    barwa4 = lg['kolor'][::-1]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=y,y=x,orientation='h',text=y,
                        textfont=dict( size=12,color='black')))
    fig.update_traces(marker_color=barwa4,marker_line_color='black',marker_line_width=1.5,
                      textposition='outside',texttemplate = "<b>%{x:}")
    fig.update_xaxes(title='Liczba wniosków')
    fig.update_yaxes(title='Jednostka')

    fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),
                                height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=100, l=0, r=200),font_family='Lato',
                                separators =',')

    st.plotly_chart(fig)
    
    

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            [data-testid="stDecoration"]{background-image: linear-gradient(90deg,#FFCD00 ,#0050AA );height: 0.25rem;}
            [class="stActionButton"] {visibility: hidden;}
            
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)





#css-gr05f0 e1fqkh3o1
#
#css-1adrfps e1fqkh3o2
#css-qrbaxs effi0qh3
