from flask import Flask, request, Response, render_template
import os # needed for cloud9

# might want to use gevent for production (.monkey, .pywsgi)
#import gevent
#import gevent.monkey
#from gevent.pywsgi import WSGIServer
#gevent.monkey.patch_all()

app = Flask(__name__)
port = os.environ["PORT"] # Needed for running on Cloud 9
ip = os.environ["IP"]     # Needed for running on Cloud 9

# Helper Functions

def audience_stream(): 
    #SSE message format is 'data: <Content> \n\n'
    content = 'Test'
    return "data:  %s \n\n " % content
    
# end of helper functions

@app.route('/config')
def working():
    # ToDo need to add a browser check
    return "Flask up and running on http//" + ip + " : " + port


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
    
# provides the presentation the URL to listen out on    
@app.route('/audience')
def sse_request():
    return Response(
            audience_stream(),
            mimetype='text/event-stream')
            

#The members of the Audience simply www.xx.xx/ to access the presentation
@app.route('/')
def page():
    return render_template('presentation.html') # will need polyfills for older browsers and IE<10


if __name__=='__main__':
    app.run(host=ip, port=port) #ip and port required for Cloud 9
    
# If using gevent
#if __name__ == '__main__':
#    http_server = WSGIServer(('127.0.0.1', 8001), app)
#    http_server.serve_forever()
