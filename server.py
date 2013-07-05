from flask import Flask, request, Response, render_template, redirect, url_for

import os # needed for cloud9

import gevent
import gevent.monkey
from gevent.pywsgi import WSGIServer
gevent.monkey.patch_all()

app = Flask(__name__)
message = 'null'
id = 1
port = os.environ["PORT"] # Needed for running on Cloud 9
ip = os.environ["IP"] # Needed for running on Cloud 9

# Helper Functions

def audience_stream(message):
	global id
	idm = id
	
	#SSE message format is 'data: <Content> \n\n'
	return "id:%s\n" % idm + "data:%s\n\n" % message

# end of helper functions
# system tests
@app.route('/config')
def working():
    # ToDo need to add a browser check
    return "Flask up and running on http//" + ip + " : " + port

@app.route('/demo')
def demo():
    return render_template('demopres.html')


# Lists the available presentations

@app.route('/presentations')
def presentations():
    return "Presentations Folder"

#presenter selects presentation from presentations folder
#presenter tells '/' which presention.html file to send to browser.
#presenter.html sends the navigation messages via XHR

@app.route('/presenter')
def presenter():
    return render_template('presenter.html') # needs to be WinPhone 7 compliant


@app.route('/next') # sets audience_stream message to next
def next():
    global message
    message = 'Next'
    global id
    id = id+1 
    return redirect(url_for('presenter'))

@app.route('/prev') # sets audience_stream message to prev
def prev():
    global message
    message = 'Prev'
    global id
    id = id+1 
    return redirect(url_for('presenter'))


# provides the presentation the URL to listen out on
@app.route('/audience')
def sse_request():
	return Response(
	audience_stream(message),
	mimetype='text/event-stream'
	)

#The members of the Audience simply www.xx.xx/ to access the presentation
@app.route('/')
def page():
    return render_template('streamdemo.html') # will need polyfills for older browsers and IE<10




#if __name__=='__main__':
 #   app.run(host=ip, port=port)
 #app.debug=True 
 #app.run(threaded=True)

# If using gevent
if __name__ == '__main__':
  #http_server = WSGIServer(('127.0.0.1', 8001), app)
  print port
  http_server = WSGIServer((ip, 8080), app)
  http_server.serve_forever()
