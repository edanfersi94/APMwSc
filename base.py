
# Librerias a usar.
from flask import Flask, request
from flask.ext.script import Manager, Server
from random import SystemRandom

# Creacion de la instancia de la aplicacion.
app = Flask(__name__)

# Se crea un manejador para la aplicacion.
manager = Manager(app)
manager.add_command("runserver", Server(
	use_debugger = True,
	use_reloader = True,
	host = '0.0.0.0')
)


# Codigo a ejecutarse cuando se accede a '/'
@app.route('/')
def index():
	# Manejador de la aplicacion raiz.
	return app.send_static_file('index.html')

	
#
from app.APMwSc.identificacion import identificacion as ide
app.register_blueprint(ide)
	
	
if __name__ == '__main__':
	
	# Configuracion de una clave secreta que servira para verificar
	# la autentidad de los requisitos.
	 
	app.config.update(
		SECRET_KEY = repr(SystemRandom().random())
	)
	manager.run()