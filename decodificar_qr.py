import cv2
import numpy  as np


def convertir_a_img_opencv2(imagen_qr):
   
   byte_archivo = np.frombuffer(imagen_qr.read(), dtype=np.uint8)   
   return cv2.imdecode(byte_archivo, cv2.IMREAD_COLOR)
   

def leer_qr(imagen_qr): 
   imagen = convertir_a_img_opencv2(imagen_qr)

   detector_qr = cv2.QRCodeDetector() 
   #El guion bajo (_) se utiliza en este contexto para indicar que no te interesa el valor de esa posición en la tupla,solo importa el texto.
   texto_qr, _, _ = detector_qr.detectAndDecode(imagen)
   
   if not  texto_qr: 
     raise  ValueError("Lo siento,no se encontró contenido en el QR")
   
   else: 
      return texto_qr