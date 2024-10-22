    # Vamos a crear una página WEB con múltiples columnas y mútiples páginas dentro de la misma web.

import streamlit as st  # importamos la librería de streamlit.

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
