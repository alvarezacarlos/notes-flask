from flask import Flask, request

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return 'Estas en la seccion de Inicio'


@app.route("/contact")
def contact():
    return 'Estas en la seccion de contacto'


@app.route("/users/<usuario>")
def users(usuario):    
    return f'Estas en la seccion de Usuarios {usuario}'

@app.route("/users", methods=['POST'])
def create_user():    
    # print(request.form)    
    return f'Hola {request.form["name"]} tienes {request.form["age"]}.'

    
@app.route("/posts/<post_id>", methods=['GET', 'POST'])
def posts(post_id):
    if request.method == 'GET':
        return f'GET - Estas en la seccion de Post. Post_ID: {post_id}'
    if request.method == 'POST':
        return f'POST - Estas en la seccion de Post. Post_ID: {post_id}'
    return f'Invalid Method - Estas en la seccion de Post. Post_ID: {post_id}'