import web

class Visitas:
    def GET(self, nombre):
        try:
            cookie = web.cookies()
            visitas = 0 
            print(cookie)
            if nombre:
                web.setcookie("nombre",nombre,expires="",domain=None)
            else:
                nombre = "Anonimo"
                web.setcookie("nombre",nombre,expires="",domain=None)
            if cookie.get("visitas"):
                visitas = int(cookie.get("visitas"))
                visitas += 1 #SUMA UNA VISITA 
                web.setcookie("visitas", str(visitas), expires="", domain=None) 
                #REGRESA LA CANTIDAD DE VISIAS
            else:
                web.setcookie("visitas", str(1), expires="", domain=None)
                visitas = "1"
                
            return "visitas" + str(visitas) + "Nombre" + nombre
        except Exception as e:
            return "Error " + str(e.args)
