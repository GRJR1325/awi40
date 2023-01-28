import web

urls = (
    '/', 'Tablas' 
)

app = web.application(urls, globals())
render = web.template.render("templates/")

class Tablas:
    def GET(self):
        datos = [
            ["1","Dejah"],
            ["2","Julio"],
            ["3","Nuevo"]
        ]
        return render.tables(datos)
            #['id':'1','nombres':"Dejah"],
if __name__ == "__main__":
    web.config.debug= True
    app.run()