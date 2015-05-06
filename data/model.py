# Librerias a utilizar.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

import settings

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
	
	def __rep__(self):
		return "<User('%s','%s','%s','%s','%d','%d' )>" % (self.fullname,self.username,self.password,self.email,self.iddpt,self.idrole)


# Tabla Departamento.
class Dpt(db):
	__tablename__ = 'dpt'
	iddpt = Column(Integer, primary_key = True)
	namedpt = Column(String(50), unique = True)
	users = relationship('User', backref = 'dpt')

	def __init__(self, iddpt, namedpt, users):
		self.iddpt = iddpt
		self.namedpt = namedpt
		self.users = users
		
	def __rep__(self):
		return "<DPT('%d', '%s')>" % (self.iddpt,self.namedpt)

# Tabla Role.
class Role(db):
	__tablename__ = 'role'
	idrole = Column(Integer, primary_key = True)
	namerole = Column(String(50), unique = True)
	users = relationship('User', backref = 'role')

	def __init__(self, idrole, namerole):
		self.idrole = idrole
		self.namerole = namerole
		
	def __rep__(self):
		return "<ROLE('%d', '%s')>" % (self.idrole,self.namerole)
#-------------------------------------------------------------------------------

engine = create_engine(URL(**settings.DATABASE))	
db.metadata.create_all(engine)
