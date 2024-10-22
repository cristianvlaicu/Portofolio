    # Vamos a crear una página WEB con múltiples columnas y mútiples páginas dentro de la misma web.

import streamlit as st  # importamos la librería de streamlit.
import pandas

st.set_page_config(layout='wide')  # configuramos una página.

col1, col2 = st.columns(2)  # tendrá dos columnas.


with col1:
    st.image(r'images\Yo1.png')  # en la primera va a aparecer nuestra foto.

with col2:
    st.title('Cristian Vlaicu')  # y en la columna aparecerá el título y un texto descriptivo.
    content = '''   
    My name is Cristian Vlaicu, I am a 35-year-old person who wants to work, earn a good living and get ahead on my own. 
    I am an ambitious person, eager to succeed, live an honest life and create my professional career. 
    I quickly learn everything there is to learn and I do not complain about anything but that ones is not fair, such as a job poorly done.
    '''
    st.info(content)  # esto es para que nos muestre el texto descriptivo.

content2 = '''
Bellow you can finde some of the apps I have built in Python. Feel free to contact me!
'''

st.write(content2)

col3, col4 = st.columns(2)  # creamos otras dos columnas para exponer nuestros proyectos creados.

df = pandas.read_csv('data.csv', sep=';')  # con pandas leemos el archivo csv donde está el resumen de nuestros poryectos (nombre, descrpción, enlace web y una fotos descrptiva de cada proyecto).

with col3:
    for index, row in df[:10].iterrows():  # recorremos las 10 primeras filas (uno a uno) de la data frame (es una lista de Diccionario) que ha generado pandas del archivo csv.
        st.header(row['title'])            # y mostramos la clave 'title' del diccionario row(fila).

with col4:
    for index, row in df[10:].iterrows():  # recorremos las 10 últimas filas (uno a uno) de la data frame (es una lista de Diccionario) que ha generado pandas del archivo csv.
        st.header(row['title'])            # y mostramos la clave 'title' del diccionario row(fila).