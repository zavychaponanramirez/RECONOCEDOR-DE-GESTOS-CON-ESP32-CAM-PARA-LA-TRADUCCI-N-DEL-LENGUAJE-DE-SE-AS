#Instalar e importar las librerias
import numpy as np
import handDetector as hand
import time
import cv2
 
#Abrir una cámara para capturar video
url='http://192.168.137.117/480x320.jpg'
cap = cv2.VideoCapture(url)
 
detector = hand.handDetector() #Crear un objeto para encontar puntos de referencia de la mano
 
while True:

    cap.open(url)
    ret, img = cap.read() # Captura frame por frame

    if ret:
    
        img = detector.findHands(img) # Buscar mano/s en la imagen
        
        lmList, bbox = detector.findPosition(img) #Devuelve los puntos de referencia y el recuadro que encierra la mano
        
        
        if len(lmList) != 0: #Verificar si hay mano
            
            fingers = detector.fingersUp() #Verificar si los dedos estan levantados

            
            #Reconocimiento de gestos de la mano

            if all(num == 0 for num in fingers):
                print("Mano Cerrada")
            elif all(num == 1 for num in fingers):
                print("Mano Abierta")
            elif fingers[0] == 1:
                print("Pulgar arriba")
            elif fingers[1] == 1:
                print("Indice arriba")
            elif fingers[2] == 1:
                print("Medio arriba")
            elif fingers[3] == 1:
                print("Anular arriba")
            elif fingers[4] == 1:
                print("Menique arriba")
     
        
        cv2.imshow("Image", img) #Mostrar imagen
        
    if cv2.waitKey(1) == ord('q'): #Presionar la letra q del teclado para cerrar
        break
    
cap.release() #Liberar camara
cv2.destroyAllWindows() #Destruir o cerrar las ventanas
