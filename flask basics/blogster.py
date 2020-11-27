#import flask
from flask import Flask, render_template

#Create an app

app = Flask(__name__)

#Create a route/homepage for the flask

@app.route('/', methods = ['GET'])

#Create Function

def home():
	return render_template('index.html')

#Declaring a new route

@app.route('/about', methods = ['GET'])
def about(): 
	return render_template('about.html')

if __name__ == '__main__':
	app.run(port = 9000, debug= True)