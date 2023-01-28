import web

urls = (
    '/', 'Suma' 
)

app = web.application(urls, globals())
render = web.template.render("templates")
class Suma:
    def GET(self):
        return render.formulario()

    def POST(self):
        data = web.input()
        n1 = float(data["n1"])
        n2 = float(data["n2"])
        if data["operator"] == "1":
            result = n1 + n2
            operator = "+"
            return render.result(n1,n2,operator,result)
        elif data["operator"] == "2":
            result = n1 - n2
            operator = "-"
            return render.result(n1,n2,operator,result)
        elif data["operator"] == "3":
            result = n1 * n2
            operator = "X"
            return render.result(n1,n2,operator,result)
        elif data["operator"] == "4":
            result = n1 / n2
            operator = "/"
            return render.result(n1,n2,operator,result)

if __name__ == "__main__":
    web.config.debug= False
    app.run()