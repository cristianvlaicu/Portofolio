    # Creamos la página dentro de la carpeta pages donde pondremos el programa para que nos manden un email con preguntas o mensajes.

import streamlit as st
from send_email import send_email  # llamamos al módulo que envía los emails a nuestra cuenta con el email y mensaje de más abajo (lo que teclee el usuario)

st.header("Questions? don't worry! Contact me Here:")  # título de la página.

with st.form(key="email_form"):                        # creamos el formulario con la clave email_form (obligatorio crear la clave).
    user_email = st.text_input("Your Email Address:")
    raw_message = st.text_area('Your message please:')

        # creamos el mensaje en este formato para poder ver el asunto del mensaje y con ese salto de línea en medio mas el From vemos el email del que lo ha mandado (usuario).
    message = f"""\
Subject: New email from Portofolio:

From: {user_email}
{raw_message}
"""

        # creamos el botón que una vez pulsado, manda el email del usuario a nuestro email que hemos configurado. Va dentro del with porque pertenece al formulario.
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)  # llamamos a la función antes creada cuando se pulsa el botón submit.
        st.info("Your email was sent successfully")