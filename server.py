from flask import Flask, render_template,jsonify,request
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

@app.route("/recipe", methods = ['POST', 'GET'])
def recipe():
    pie={'name':'Apple pie', 'ingredients' : ['flour','sugar']
            }
    pie_ingredient = ''        
    if request.method == 'POST':
      pie_ingredient = request.form['ingredient']
      print('pie_ingredient',pie_ingredient)
      pie['ingredients'].append(pie_ingredient)
    #else:
    return render_template("recipe.html", pie=pie) 

if __name__ == "__main__":
  app.run()