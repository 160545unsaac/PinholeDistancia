#Librerias
import numpy as np
import argparse
import cv2

#Cargar imagen
image = cv2.imread('Pelota02.jpg')
output = np.asarray(image, dtype = np.float32)

#Convertir a escala de grises
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    

#Se le aplica un filtro
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

#Se muestra la imagen resultante
cv2.imshow('video2',thresh)

#Se duplica la imagen
output=image.copy()

#Se detectan los circulos en la imagen
circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, 2,400, param1=100, param2=60, minRadius=20,maxRadius=500) 
#Se dibujan los circulos detectados
if circles is not None:
	#Convierte coordenadas a enteros 
	circles = np.round(circles[0, :]).astype("int")
	#Bucle que recorre las coordenadas de los circulos
	for (x, y, r) in circles:
		#Dibujar circulo y rectangulo en el medio
		cv2.circle(image, (x, y), r, (0, 255, 0), 2)
		cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
		radio = r
		
	#Muestra la imagen final
	cv2.imshow("output", np.hstack([image]))


#Calculo de diametro
diametroPixel = 2*radio
print('Diametro: ',diametroPixel, 'px')

#Declaracion de variables
#Diametro real: 22cm
diametroReal = 22/100
#Distancia focal camara: 35mm
dFocal = 35/1000
#Tamanio Pixel: 6.21296 * 10-5 m
tPixel = (6.21296)/100000
#Calculo de la distancia real por formula de Pinhole
distanciaReal = (dFocal*diametroReal)/(diametroPixel*tPixel)

print('Distancia Real: ',distanciaReal, 'm')










