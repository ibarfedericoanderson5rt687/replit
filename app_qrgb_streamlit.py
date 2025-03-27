import streamlit as st
from PIL import Image
import qrcode
import io
import base64

def generar_qr(texto, color_fondo, color_qr):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=color_qr, back_color=color_fondo)
    return img

def main():
    st.title("Generador de Códigos QR Personalizados")
    st.write("Desarrollado por Ibar Federico Anderson con asistencia de la IA de Replit")
    st.info("Este proyecto fue desarrollado como parte de una serie de herramientas educativas sobre códigos QR", icon="ℹ️")
    
    # Entrada de texto para el código QR
    texto_qr = st.text_input("Introduce el texto o URL para el código QR:", "https://github.com/ibarfedericoanderson/ScriptPythonAppQRGB")
    
    # Selección de colores
    col1, col2 = st.columns(2)
    with col1:
        color_qr = st.color_picker("Color del código QR:", "#000000")
    with col2:
        color_fondo = st.color_picker("Color de fondo:", "#FFFFFF")
    
    # Botón para generar el QR
    if st.button("Generar código QR"):
        if texto_qr:
            qr_img = generar_qr(texto_qr, color_fondo, color_qr)
            
            # Mostrar la imagen
            st.image(qr_img, caption="Tu código QR personalizado")
            
            # Opción para descargar
            buf = io.BytesIO()
            qr_img.save(buf, format="PNG")
            byte_im = buf.getvalue()
            btn = st.download_button(
                label="Descargar código QR",
                data=byte_im,
                file_name="codigo_qr.png",
                mime="image/png"
            )
        else:
            st.error("Por favor, introduce algún texto para generar el código QR")
    
    st.markdown("---")
    st.markdown("""
    ### Desarrollado con la IA de Replit
    Este proyecto fue creado con la asistencia de Claude en Replit.
    """)
    
    st.markdown("---")
    st.markdown("""
    **Autor: Ibar Federico Anderson** | **Proyecto Open Source**
    * [Perfil GitHub](https://github.com/ibarfedericoanderson) 
    * [Repositorio del Proyecto](https://github.com/ibarfedericoanderson/ScriptPythonAppQRGB) 
    * [App Web en Streamlit Cloud](https://appqrgbpythonappapp-kz8zenrno2ybehz4zgkccc.streamlit.app/)
    """)

if __name__ == "__main__":
    main()