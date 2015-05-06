"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Edward Fernandez.   Carnet: 10-11121
		Nicolas

    DESCRIPCION: 
		
"""
#-------------------------------------------------------------------------------

# Librerias a utilizar.

# Configuracion de la base de datos a utilizar.
import settings

from sqlalchemy.engine.url import URL
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

#-------------------------------------------------------------------------------

db = declarative_base()

#-------------------------------------------------------------------------------

# Tablas de la base de datos a definir.

# Tabla Usuario.
class User(db):
	__tablename__ = 'user'
	fullname = Column(String(50), unique = True)
	username = Column(String(16), primary_key = True)
	password = Column(String(16), unique = True)
	email = Column(String(30), unique = True)
	iddpt = Column(Integer, ForeignKey('dpt.iddpt'), nullable = False)
	idrole = Column(Integer, ForeignKey('role.idrole'), unique = True)
	
	def __init__(self,fullname, username, password, email, iddpt, idrole):
		self.fullname = fullname
		self.username = username
		self.password = password
		self.email = email
		self.iddpt = iddpt
		self.idrole = idrole

# Tabla Departamento.
class Dpt(db):
	__tablename__ = 'dpt'
	iddpt = Column(Integer, primary_key = True)
	namedpt = Column(String(50), unique = True)
	users = relationship('User', backref = 'dpt', cascade="all, delete, delete-orphan")

	def __init__(self, iddpt, namedpt, users):
		self.iddpt = iddpt
		self.namedpt = namedpt
		self.users = users

# Tabla Role.
class Role(db):
	__tablename__ = 'role'
	idrole = Column(Integer, primary_key = True)
	namerole = Column(String(50), unique = True)
	users = relationship('User', backref = 'role', cascade="all, delete, delete-orphan")

	def __init__(self, idrole, namerole):
		self.idrole = idrole
		self.namerole = namerole
		
#-------------------------------------------------------------------------------

# Se crea el motor que almacenara los datos en el directorio local.
engine = create_engine(URL(**settings.DATABASE))	

# Se crean todas las tablas definidas en el motor antes construidos.
db.metadata.create_all(engine)