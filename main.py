import streamlit as st
from codificar_qr import generar_qr
from decodificar_qr import leer_qr

st.set_page_config(page_title="Generador de QR", page_icon="📷", layout="centered")
st.title("📷Tu generador y lector de codigo QR de confianza" ) 

opcion = st.radio("Seleccione 1 opcion:", ["Generar Qr", "Leer Qr"])

if opcion == "Generar Qr":
    
    texto = st.text_input("Ingrese el texto o enlace: ")     

    if st.button("Generar Qr"): 
        if texto:
         img_qr = generar_qr(texto)

        if img_qr is not None: 
            st.success("Código QR generado con éxito.")
            st.image(img_qr)

        else: 
            st.error("Por favor, ingrese un texto o enlace para generar el QR")


elif opcion == "Leer Qr": 
    imagen_qr = st.file_uploader("Sube una imagen de un código QR", type=["png", "jpg", "jpeg"])

    if imagen_qr and st.button("Leer Qr"): 
        resultado = leer_qr(imagen_qr)

        if resultado is not None: 
            st.success(f"URL o texto: {resultado}")
        else: 
            st.error("No se pudo leer el código QR. Asegúrate de que la imagen sea clara.")