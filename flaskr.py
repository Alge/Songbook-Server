# all the imports
import sqlite3
from flask import Flask
import database
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to the songbook api :) There will be a list of functions on this page later'

@app.route('/getSong')
def hello_world():
    return 'Hello World!'
    
@app.route('/collectionInfo')
def hello_world():
    return 'Hello World!'

@app.route('/')
def hello_world():
    return 'Hello World!'



if __name__ == '__main__':
    app.run("0.0.0.0")
  
