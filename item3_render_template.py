from flask import Flask, request, url_for, redirect, abort,render_template

app = Flask(__name__)
app.debug = True

@app.route("/users/<user_name>", methods=['POST', 'GET'])
def create_user(user_name):
    return render_template('users.html') 
    # user.html is an html document located in the /templates folder.
    # flask automatically looks for this template to locate the html documents.

@app.route("/users", methods=['GET'])
def users():    
    user_name='Balu'
    return redirect(url_for('create_user', user_name=user_name))