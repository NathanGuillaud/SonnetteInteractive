#!/usr/bin/env python
#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO         # Importation des librairies qui gerent les ports
import time                     # Importation de la librairie temps
from grovepi import *
from grove_rgb_lcd import *
import os

bouton = 2    #Port du bouton
test = True

while test:        #boucle infinie
    button_status= digitalRead(bouton)    #Read the Button status
    if button_status:    #Si le bouton a été appuyé
        #Prendre la photo, l'enregistrer et afficher un message su l'écran
	#setText("Appuyer pour\nlaisser message")
	setText("Test")
	setRGB(150,150,150)
#        os.system('sh photo.sh')    #Récupération du script correspondant

        timeout = time.time() + 5    #on créé une valeur de temps avant la fin de la boucle
        while test and time.time() < timeout:        #boucle infinie pendant 5s
            button_status= digitalRead(bouton)    #R
	            if button_status:    #Si le bouton a été appuyé
		test = False
                #Enregistrement du message audio et afficher un message sur l'écran
                #os.system('sh ')    #Récupération du script correspondant
	test = False
