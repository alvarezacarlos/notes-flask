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
# 403 Forbidden - usuario no tiene permisos a acceder a  los recursos