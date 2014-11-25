# all the imports
import sqlite3
from flask import Flask
from flask import request
import database
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to the songbook api :) There will be a list of functions on this page later'

@app.route('/getSong')
def get_song():
	songId = request.args.get('id')
	return songId
    
@app.route('/collectionInfo')
def collection_info():
    return 'Hello World!'

@app.route('/test')
def test():
    return 'Hello World!'



if __name__ == '__main__':
    app.run("0.0.0.0")
  
