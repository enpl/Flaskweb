from flask import Flask, g, make_response, Response, request, session
from datetime import timedelta

app = Flask(__name__)
app.debug = True #use only debug

app.config['SERVER_NAME'] = 'local.com:5000'

app.config.update(
    SECRET_KEY = 'X1243yRH!mMwf',
    SESSION_COOKIE_NAME = 'pyweb_flask_session',
    PERMANENT_SESSION_LIFETIME=timedelta(31)
)

@app.route('/delsess')
def delsess():
    if session.get('Token'):
        del session['Token']
    return "Session이 삭제되었습니다."

@app.route('/wc')
def wc():
    key = request.args.get('key')
    val = request.args.get('val')
    res = Response("Set Cookie")
    res.set_cookie(key, val)
    session['Token'] = '123X'
    return make_response(res)

@app.route('/rc')
def rc():
    key = request.args.get('key') #token
    val = request.cookies.get(key)
    return "cookie[" + key + "] =" + val + ", " + session.get('Token')

@app.route("/sd")
def helloworld_local():
    return "Hello Local.com!"

@app.route("/sd", subdomain="g")
def helloworld_glocal():
    return "Hello G.Local.com!!!"

@app.route('/reqenv')
def reqenv():
    return ('REQUEST_METHOD: %(REQUEST_METHOD) s <br>'
            'SCRIPT_NAME: %(SCRIPT_NAME) s') % request.environ

# @app.before_request
# def before_request():
#     print("before_request!!")
#     g.str = "한글"

@app.route("/gg")
def helloworld2():
    return "Hello World!" + getattr(g, 'str', '111')

@app.route('/res1')
def res1():
    custom_res = Response("Custom Response", 200, {'test': 'ttt'})
    return make_response(custom_res)

@app.route("/")
def helloworld():
    return "Hello Flask World!!!!!!!"

@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [('Content-Type', 'text/plain'),
                    ('Content-Length', str(len(body)))]
        start_response('200 OK', headers)
        return [body]

    return make_response(application)

@app.route('/rp')
def rp():
    q = request.args.getlist('q')
    return "q= %s" % str(q)

