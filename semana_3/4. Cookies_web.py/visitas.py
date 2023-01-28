import web #WEB PY
import time #IMPORTAMOS EL TIEMPO


class Visitas:
    def GET(self, nombre):  
        try:
            cookie = web.cookies()
            dia_ingreso = time.strftime("%d/%m/%y") #DIA
            hora_ingreso = time.strftime("%I:%M:%S") #HORA
            visitas = 0 #VISITAS
            print(cookie)
            if nombre: #SI HAY UN NOMBRE LO IMPRIMIRA
                web.setcookie("nombre",nombre,expires="",domain=None)
            else:
                nombre = "Anonimo" #DEL CASO CONTRARIO SERA ANONIMO
                web.setcookie("nombre",nombre,expires="",domain=None)
            if cookie.get("visitas"):
                visitas = int(cookie.get("visitas"))
                visitas += 1 #SUMA UNA VISITA 
                web.setcookie("visitas", str(visitas), expires="", domain=None) 
            else:
                web.setcookie("visitas", str(1), expires="", domain=None)
                visitas = "1"
                
            return ("No. visitas:" + str(visitas) + " | "+ 
            " Usuario: "  + nombre + " | " + 
            " Dia de ingreso:" + str(dia_ingreso) + " | " + 
            " Hora de Ingreso:" + str(hora_ingreso)) 
        except Exception as e:
            return "Error " + str(e.args)