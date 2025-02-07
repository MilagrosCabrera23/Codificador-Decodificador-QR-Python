import qrcode
import os
import re

texto = ""

def validar_texto(texto): 
    if re.match(r'(https?://[^\s]+)', texto): 
        return True
    
    elif texto is None or len(texto.strip())< 6: 
        return False 
    return True
  

def obtener_nombre_de_img(): 
     carpeta = "qr_codigos"
     os.makedirs(carpeta,exist_ok=True)

     archivos= os.listdir(carpeta) # Lista todos los archivos dentro de la carpeta
     numeros = []
     
     for archivo in archivos: 
        if archivo.startswith("qr_code") and archivo.endswith(".png"): 
            numero = re.findall(r'\d+', archivo)  # Extrae los números del nombre
            if numero:
                numeros.append(int(numero[0]))  # Convierte a entero y lo agrega a la lista

     siguiente_numero = max(numeros) + 1 if numeros else 1
     return os.path.join(carpeta, f"qr_code_{siguiente_numero}.png")


def generar_qr(texto): 
  
  if not validar_texto(texto):
      return None
  
  else: 
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10, border=1)
    qr.add_data(texto) #Agrega el texto o enlace al código QR.
    qr.make(fit=True) #Genera la matriz del código QR con la información añadida.

    img= qr.make_image(fill='black', back_color='white')
    ruta_img = obtener_nombre_de_img()
    img.save(ruta_img)
    
    return ruta_img
                             
    
