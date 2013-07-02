from flask import Flask
import os

app = Flask(__name__)
port = os.environ["PORT"] # Needed for running on Cloud 9
ip = os.environ["IP"]     # Needed for running on Cloud 9


@app.route('/')
def working():
    return "Flask up and running on http//" + ip + " : " + port

@app.route('/presentations')
def presentations():
    return "Presentations Folder"

if __name__=='__main__':
    app.run(host=ip, port=port) #ip and port required for Cloud 9
