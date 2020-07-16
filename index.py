import flask import Flask 

app = Flask(__name__)

@app.route('/')
@app.route('/home')

def home():
    render_template('index.html')
    