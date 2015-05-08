"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Nicolas Manan.      Carnet: 06-39883
        Edward Fernandez.   Carnet: 10-11121

	DESCRIPCION: Script que contiene los metodos requeridos para trabajar con la tabla
			     "Role" de la base de datos dada.
	
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
			
			@param newIdRole  : Identificador del rol a insertar.
			@param newNameRole: Nombre del rol a insertar.
			
			@return True si se inserto el rol dado. De lo contrario False.
		"""
		
		# Booleanos que indican si el tipo es el correcto.
		nameIsStr = type(newNameRole) == str
		idIsInt = type(newIdRole) == int
	
		if ( nameIsStr and  idIsInt ):
			# Booleanos que indican si cumplen con los limites.
			nameLenValid = 1 <= len(newNameRole) <= 50
			idIsPositive = newIdRole > 0
		
			if (nameLenValid and idIsPositive):
				query1 = self.find_idRole(newIdRole)
				query2 = self.find_nameRole(newNameRole)
				
				if ( (query1 == []) and (query2 == []) ):	
					newRole = model.Role(newIdRole, newNameRole)
					session.add(newRole)
					session.commit()
					return( True )
		
		return( False )
		
	#-------------------------------------------------------------------------------
	
	def find_idRole(self, idRole):
		"""
			@brief Funcion que realiza la busqueda del rol cuyo identificador
				   sea "idRole".
			
			@param idRole: Identificador del rol a buscar.
			
			@return lista que contiene las tuplas obtenidas del subquery. De lo 
					contrario retorna la lista vacia.
		"""
		
		idIsInt = type(idRole) == int
		
		if ( idIsInt ):
			result = session.query(model.Role).filter(model.Role.idrole==idRole).all()
			return( result )
		return( [] )
	
	#-------------------------------------------------------------------------------
	def find_nameRole(self, nameRole):
		"""
			@brief Funcion que realiza la busqueda de los roles cuyo identificador
				   sea "nameRole".
				   
			@param nameRole: Nombre del rol a buscar.
			
			@return lista que contiene las tuplas obtenidas del subquery. De lo 
					contrario retorna la lista vacia.
		"""
		
		nameIsStr = type(nameRole) == str
		
		if ( nameIsStr ):
			result = session.query(model.Role).filter(model.Role.namerole==nameRole).all()
			return( result )
		return( [] )
		
	#-------------------------------------------------------------------------------
	
	def find_listIdRole(self):
		"""
			@brief Funcion que devuelve los identificadores de los diferentes roles
				   que se encuentran almacenados en la base de datos.
			
			@param no admite parametros.
			
			@return lista con la consulta solicitada.
		"""
		
		result = session.query(model.Role.idrole.label('id')).all()
		return( result )
		
	#-------------------------------------------------------------------------------
	def find_listNameRole(self):
		"""
			@brief Funcion que devuelve los nombres de los diferentes roles que se
				   encuentran almacenados en la base de datos.
			
			@param no admite parametros.
			
			@return lista con la consulta solicitada.
		"""
		
		result = session.query(model.Role.namerole.label('name')).all()
		return( result )
	
	#-------------------------------------------------------------------------------

	def modify_idRole(self, idRole, newIdRole):
		"""
			@brief Funcion que modifica el id de un rol dado por "newIdRole".
			
			@param idRole	: id del rol a modificar.
			@param newIdRole: nuevo id para el rol dado.
			
			@return True si se modifico el rol dado. De lo contrario False.
		"""
		
		# Booleanos que indican si el tipo es el correcto.
		newIdIsInt = type(newIdRole) == int
		oldIdIsInt = type(idRole) == int
		
		if ( newIdIsInt and oldIdIsInt ):
			# Booleanos que indican si cumplen con los limites.
			newIdIsPositive = newIdRole > 0
			oldIdIsPositive = idRole > 0
			
			if ( newIdIsPositive and  oldIdIsPositive ):
				query1 = self.find_idRole(idRole)
				query2 = self.find_idRole(newIdRole)
				
				if (( query1 != [] ) and ( query2 == [])):
					session.query(model.Role).filter(model.Role.idrole==idRole).\
						update({'idrole':(newIdRole)})
					session.commit()
					return( True )
		
		return( False )

	#--------------------------------------------------------------------------------

	def modify_nameRole(self, idRole, newNameRole):
		"""
			@brief Funcion que modifica el nombre de un rol dado por "newNameRole".
			
			@param idRole	  : id del rol a modificar.
			@param newNameRole: nuevo nombre para el rol dado.
			
			@return True si se modifico el rol dado. De lo contrario False.
		"""
		
		# Booleanos que indican si el tipo es el correcto.
		nameIsStr = type(newNameRole) == str
		idIsInt = type(idRole) == int
		
		if ( nameIsStr and  idIsInt ):
			# Booleanos que indican si se cumplen los limites.
			nameLenValid = 1 <= len(newNameRole) <= 50
			idIsPositive = idRole > 0
			
			if ( nameLenValid and idIsPositive ):
				query1 = self.find_idRole(idRole)
				query2 = self.find_nameRole(newNameRole)
				
				if (( query1 != [] ) and ( query2 == [])):
					session.query(model.Role).filter(model.Role.idrole==idRole).\
						update({'namerole':(newNameRole)})
					session.commit()
					return( True )
					
		return( False )
	
	#--------------------------------------------------------------------------------	
	
	def delete_role(self, idRole):
		"""
			@brief Funcion que elimina el rol cuyo identificador sea "idRole".
			
			@param idRole: Identificador del rol a eliminar.
			
			@return True si elimina el rol dado. De lo contrario False.
		"""
		
		idIsInt = type(idRole) == int 
		
		if ( idIsInt ):
			query = self.find_idRole( idRole )
			
			if ( query != [] ):
				session.query(model.Role).filter(model.Role.idrole==idRole).delete()
				session.commit()
				return( True )
		
		return( False )

	#-------------------------------------------------------------------------------