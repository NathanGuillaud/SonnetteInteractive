#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import os

nom = "photo-"+time.strftime("%Y-%m-%d-%H-%M")+".jpg"
print(nom)
os.system('sh photo.sh '+ nom)    #Récupération du script correspondant
os.system('sh uploadphoto.sh '+ nom) #Upload uniquement la photo sur le drive
