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

#------------------------------------------------------------------------------------

# Librerias a utilizar.

import os
import sys

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../data')
import model

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#------------------------------------------------------------------------------------

# Se realiza la conexion con la bases de datos para realizar cambios en ella.
DBSession = sessionmaker(bind=model.engine)
session = DBSession()

# Clase que tendra las diferentes funcionalidades de la tabla "Role".
class clsRole():

	#-------------------------------------------------------------------------------
	
	def insert_role(self, newIdRole, newNameRole):
		"""
			@brief Funcion que permite insertar un nuevo rol en la base de datos.
			
			@param newIdRole: Identificador del rol a insertar.
			@param newNameRole: Nombre del rol a insertar.
			
			@return void.
		"""
		
		newRole = model.Role(newIdRole, newNameRole)
		session.add(newRole)
		session.commit()
		
	#-------------------------------------------------------------------------------
	
	def find_IdRole(self, idRole):
		"""
			@brief Funcion que realiza la busqueda del rol cuyo identificador
				   sea "idRole".
			
			@param idRole: Identificador del rol a buscar.
			
			@return subquery con la consulta solicitada.
		"""
		
		result = session.query(model.Role).filter(model.Role.idrole==idRole).all()
		return(result)
	
	#-------------------------------------------------------------------------------
	def find_NameRole(self, nameRole):
		"""
			@brief Funcion que realiza la busqueda de los roles cuyo identificador
				   sea "nameRole".
			@return subquery con la consulta solicitada.
		"""
		result = session.query(model.Role).filter(model.Role.namerole==nameRole).all()
		return(result)
		
	#-------------------------------------------------------------------------------
	
	def find_listIdRole(self):
		"""
			@brief Funcion que devuelve los identificadores de los diferentes roles
				   que se encuentran almacenados en la base de datos.
			
			@param no admite parametros.
			
			@return subquery con la consulta solicitada.
		"""
		result = session.query(model.Role.idrole.label('id')).all()
		return(result)
		
	#-------------------------------------------------------------------------------
	def find_listNameRole(self):
		"""
			@brief Funcion que devuelve los nombres de los diferentes roles que se
				   encuentran almacenados en la base de datos.
			
			@param no admite parametros.
			
			@return subquery con la consulta solicitada.
		"""
		result = session.query(model.Role.namerole.label('name')).all()
		return(result)
	
	#-------------------------------------------------------------------------------
	
	def delete_role(self, roleId):
		"""
			@brief Funcion que elimina el rol cuyo identificador sea "roleId".
			
			@param roleId: Identificador del rol a eliminar.
			
			@return void.
		"""
		session.query(model.Role).filter(model.Role.idrole==roleId).delete()
		session.commit()

	#-------------------------------------------------------------------------------

"""
role1 = clsRole()
# PRUEBA: Insertar.

role1.insert_roles(2,'departamento2')
role1.insert_roles(3,'departamento3')


#role1.insert_role(1,'departamento1')
result = role1.find_IdRole(1)
for v in result:
	print(v.namerole)
result = role1.find_NameRole("departamento3")
for v in result:
	print(v.idrole)
result = role1.find_listNameRole()
for v in result:
	print(v.name_label)
result = role1.find_listIdRole()
for v in result:
	print(v.id_label)
# PRUEBA: Eliminar
#result = role1.find_IdRole(1)
#role1.delete_role(1)
#role1.rolling_back_role()
"""