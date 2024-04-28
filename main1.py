#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

def abrirArchivo():
    miBase=[]
    with open('info.json',encoding="utf-8") as openfile:
        miBase= json.load(openfile)
    return miBase   
     

def guardarArchivo(miData):
    with open("info.json","w") as outfile:          
        json.dump(miData,outfile)

        print("Ingrese la opcion a visualizar\n(1) Camper\n(2) Trainer\n(3) Coordinador\n")

x=int(input("ingresa1"))

miInfo=[]
if (x==1):
    miInfo=abrirArchivo()
    for i in miInfo[0]["inscripciones"]: 
        print("################") 
        print(i["id"])
        print(i["nombre"])
        print(i["apellido"])
        print(i["direccion"])
        print(i["acudiente"])
        print(i["telefono_celular"])
        print(i["telefono_fijo"])
        print(i["estado"][0]["cursando"])
        print(i["riesgo"][0]["bajo"])
        print("################")
        