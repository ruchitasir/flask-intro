from flask import Flask, render_template,jsonify
from random import randint
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/profile/<username>")
def profile(username):
  return "You're viewing {}'s profile.".format(username)

@app.route("/r/<subreddit>")
def redit(subreddit):
  return "Welcome to the {} subreddit!".format(subreddit)


@app.route("/multiply/<int:num1>/<int:num2>")
def multiply(num1, num2):
  result = num1 * num2
  return str(result)  

@app.route("/greeting")
def index():
    return render_template("index.html", name='Akilah') 


@app.route("/greeting/<name>")
def greeting(name):
    return render_template("index.html", name=name) 

ingredients = ['apples','pineapple','mangoes']
@app.route("/pie")
def pie():
    return jsonify({'pie ingredient': ingredients[0]})    

ingredients = ['apples','pineapple','mangoes']
@app.route("/piee")
def pie_random():
    index = randint(0,2)
    return jsonify({'pie ingredient': ingredients[index]})     

if __name__ == "__main__":
  app.run()