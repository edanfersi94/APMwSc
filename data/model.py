"""
	UNIVERSIDAD SIMON BOLIVAR
	Departamento de Computacion y Tecnologia de la Informacion.
	Ingeniería de Software I (CI-3715)
	Abril - Julio 2015

	AUTORES:
		Nicolas
		Edward Fernandez.   Carnet: 10-11121
	

	DESCRIPCION: 

	Versión 0.1 05-05-2015

"""
# Librerias a utilizar.
from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy

# Configuración de la base de datos.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
	 'postgresql://BMO@localhost/BMO'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

#-------------------------------------------------------------------------------
# Tablas de la base de datos a definir.

# Tabla Usuario.
class User(db.Model):
	__tablename__ = 'user'
	fullname = db.Column(db.String(50), unique = True)
	username = db.Column(db.String(16), primary_key = True)
	password = db.Column(db.String(16), unique = True)
	email = db.Column(db.String(30), unique = True)
	iddpt = db.Column(db.Integer, db.ForeignKey('dpt.iddpt'), nullable = False)
	idrole = db.Column(db.Integer, db.ForeignKey('role.idrole'), unique = True)

	def __init__(self,fullname, username, password, email, iddpt, idrole):
		self.fullname = fullname
		self.username = username
		self.password = password
		self.email = email
		self.iddpt = iddpt
		self.idrole = idrole

# Tabla Departamento.
class Dpt(db.Model):
	__tablename__ = 'dpt'
	iddpt = db.Column(db.Integer, primary_key = True)
	namedpt = db.Column(db.String(50), unique = True)
	users = db.relationship('User', backref = 'dpt')

	def __init__(self, iddpt, namedpt, users):
		self.iddpt = iddpt
		self.namedpt = namedpt
		self.users = users

# Tabla Role.
class Role(db.Model):
	__tablename__ = 'role'
	idrole = db.Column(db.Integer, primary_key = True)
	namerole = db.Column(db.String(50), unique = True)
	users = db.relationship('User', backref = 'role')

	def __init__(self, iddpt, namedpt, users):
		self.idrole = idrole
		self.namerole = namerole
		self.users = users

#-------------------------------------------------------------------------------