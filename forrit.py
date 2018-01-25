import os
from bottle import route, run, static_file, request, error

@route("/")
def index():
    return "<h2>Hello bottle, web framework</h2>" \
           "<a href ='/verk2a'>Verkefni 2a</a><br></br>" \
           "<a href ='/verk2b'>Verkefni 2b</a>"

@route("/verk2a")
def verk2a():
    return "<h2>Verkefni 2a</h2>" \
           "<a href ='/verk2a/1'>Page 1</a><br></br>" \
           "<a href ='/verk2a/2'>Page 2</a><br></br>" \
           "<a href ='/verk2a/3'>Page 3</a>"

@route("/verk2a/<n>")
def param(n):
    return "This is my page " + n + "<br></br>" \
           "<a href ='/verk2a'>Til baka</a>" \

@route("/verk2b")
def verkb():
    return "<a href='/result?verk2b=mynd1'><img src='/static/mynd1.jpg' width='200'><br></br><a/>" \
           "<a href='/result?verk2b=mynd2'><img src='/static/mynd2.jpg' width='200'><br></br><a/>" \
           "<a href='/result?verk2b=mynd3'><img src='/static/mynd3.jpg' width='200'><br></br><a/>"

@route("/result")
def result():
    verk2b = request.query.verk2b
    return "Þú valdir " + verk2b + "<br></br>" \
            '<img src="/static/'+ verk2b +'.jpg" width="200" >'

@route("/static/<filename>")
def server_static(filename):
    return static_file(filename, root="./static")

@error(404)
def error404(error):
    return "Þessi síða er ekki til"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000))
