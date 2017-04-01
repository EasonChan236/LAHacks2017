import web
from web import form

render = web.template.render('templates/')

db = web.database(dbn='mysql', db = 'content')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form(
                   form.Textarea('Text',form.notnull, rows=50, cols=70, description = "Text Content"))

class index:
    def GET(self):
        form = myform()
        # make sure you create a copy of the form by calling it (line above) 
        # Otherwise changes will appear globally
        
        return render.formtest(form)
    
    def POST(self):
        form = myform()
        if not form.validates():
            return render.formtest(form)
        else:
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.
            # db.insert('content', form.Textarea)
            i = web.input()
            n = db.insert('todo2', title=i.Text)
            return "Grrreat success!"

if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
