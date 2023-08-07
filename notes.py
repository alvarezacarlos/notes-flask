# flask intallation

# ambiente virtual
"""nos permite manejas distintas versiones de los modulos
"""

# crear un ambiente virtual
# py -3 -m venv venv
"""este comando crea una carpeta dentro de nuestro proyecto que se llamara venv y luego activaremos los ambientes virtuales
"""

# activar los ambientes virtuales
# . venv/bin/activate
"""nos mostrara el mansaje (venv) en la linea de comando indicando que ya tenemos activados los ambientes virtuales.
Ahora si podemos instalar flask y los demas modulos que necesitamos"""

# instalar flask
# pip install Flask
"""una ves instalado entraremos al espacio de trabajo"""


# Hola mundo en flask
from flask import Flask #importamos flask
app = Flask(__name__) #creamos nuestra app

@app.route("/") #declaramos la ruta raiz
def index(): #creamos la funcion que se ejecutara al visitar la ruta /
    return 'Hola Mundo' #solo retornada el mensaje Hola Mundo


# finalmente necesitamos decirle a Flask donde se encuentra nuestra aplicacion
"""para ello ejecutamos el siguiente comando por terminal: 
    export FLASK_APP=holamundo.py    
    or 
    set FLASK_APP=h`olamundo.py    
"""

# start Flask server
"""next we can run the command: "flask run" to start the Flask Server and get the local url such as: http://127.0.0.1:5000/, once we visit this url we can see the "Hola Mundo message"
"""

#....................................... codigo completo - item1-the-basis
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


# habilitar el modo de desarrollo, el cual permite que el servicio detecte los cambios y recargue el servidos automaticamente
"""export FLASK_ENV=development"""


# http request to the url using terminal
# curl -X post http://localhost:5000/posts/1

#sending jason con curl
# curl -d "{}"
# -d es la data que le enviaremos al aservicio
#  "{}" aca ira data an json format

#sending fromulario data con curl
# curl -d "key1=data1&key2=data2" -X POST http://localhost:5000


#....................................... item2-url_for-redirect
from flask import Flask, request, url_for, redirect, abort

app = Flask(__name__)
app.debug = True

@app.route("/users/<user_name>", methods=['POST', 'GET'])
def create_user(user_name):
    print(f'Estas en la seccion de creacion de usuario {user_name}')
    return f'Estas en la seccion de creacion de usuario {user_name}'

@app.route("/users", methods=['GET'])
def users():
    abort(403)
    # user_name = request.form["user_name"]
    user_name='Balu'
    # print('URL: ',url_for('create_user', user_name=user_name)) #url_for receives the function name to access the route defined in the function decorator. Once we create the url we can then use it to redirect the user to that function and render the content or html/xml template that fuction renders.
    return redirect(url_for('create_user', user_name=user_name))
    # return f'Hola {user_name}.'

# abortando peticiones - codigos http
# 401 usuario no autorizado
# 403 Forbidden - usuario no tiene permisos a acceder a  los recursositem2-url_for-redirect


#....................................... 
# flask run -h 192.168.1.103