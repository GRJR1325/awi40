import web

urls = (
    '/', 'formulario' 
)

app = web.application(urls, globals())
render = web.template.render("templates/")

class Formulario:
    def GET(self):
        return render.formulario()

    def POST(self):
        form = web.input()
        print(type(form))
        return form["nombre"]
    
if __name__ == "__main__":
    web.config.debug= False
    app.run()
