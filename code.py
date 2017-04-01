import web

urls = ("/", "index")
app = web.application(urls, globals())

myform = form.Form(
                   form.Textbox("boe"),
                   form.Textbox("bax",
                                form.notnull,
                                form.regexp('\d+', 'Must be a digit'),
                                form.Validator('Must be more than 5', lambda x:int(x)>5)),
                   form.Textarea('moe'),
                   form.Checkbox('curly'), 
                   form.Dropdown('french', ['mustard', 'fries', 'wine'])) 

def GET(self):
    todos = db.select('todo')
    return render.index(todos)

class index:
    def GET(self):
        return  """<html>
            <head>
            <title>Fairy Tale</title>
            </head>
            <body>
            <h1>Fairy Tale</h1>
            <img src="/static/logo.png" alt="SAP Logo" width="300px" height="300px"/>
            </body></html>"""

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
