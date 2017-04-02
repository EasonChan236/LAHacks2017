import web
import os
from videoGenerationAPI import generateSentenceVideo
from web import form

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form(
                   form.Textarea('Text',form.notnull, rows=50, cols=70, description = "Text Content"))
#render = web.template.render('templates')
class index:
    #def GET(self):
     #   form = myform()
        # make sure you create a copy of the form by calling it (line above) 
        # Otherwise changes will appear globally
       
        #return render.formtest(form)
    
    def POST(self):
        form = myform()
        if not form.validates():
            render = web.template.render('templates')
            return render.formtest(form)
        else:
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.
            # db.insert('content', form.Textarea)
            i = web.input()
            #try:
            #    os.remove('somefile.txt')
            #except OSError:
            #    pass
            #with open('somefile.txt', 'a') as the_file:
            #    the_file.write(i.Text)
            #os.system("python bingImageAPI.py")
            generateSentenceVideo('China is big', '1.mp4', '1', '1');

            return "Great success!"

if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
