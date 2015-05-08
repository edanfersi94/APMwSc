"""
	UNIVERSIDAD SIMON BOLIVAR
	Departamento de Computacion y Tecnologia de la Informacion.
	CI-3715 - Ingenieria de Software I (CI-3715)
	Abril - Julio 2015
	
    AUTORES:
        Nicolas Manan.      Carnet: 06-39883
        Edward Fernandez.   Carnet: 10-11121
	
	DESCRIPCION: Script que contiene los metodos requeridos para trabajar con la tabla
				 "Dpt" de la base de datos dada.

"""

#-------------------------------------------------------------------------------

# Librerias a utilizar.

import os
import sys

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../data')
import model

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#-------------------------------------------------------------------------------

# Se realiza la conexion con la bases de datos para realizar cambios en ella.
DBSession = sessionmaker(bind=model.engine)
session = DBSession()

# Clase que tendra las diferentes funcionalidades de la tabla "Dpt".
class clsDpt():

	#-------------------------------------------------------------------------------
	
	def insert_dpt(self, newIdDpt, newNameDpt):
		"""
			@brief Funcion que permite insertar un nuevo dpt en la base de datos.
			
			@param newIdDpt  : Identificador del dpt a insertar.
			@param newNameDpt: Nombre del dpt a insertar.
			
			@return True si se inserto el dpt dado. De lo contrario False.
		"""
	
		# Booleanos que indican si el tipo es el correcto.
		nameIsStr = type(newNameDpt) == str
		idIsInt = type(newIdDpt) == int
		
		if ( nameIsStr and  idIsInt ):
			# Booleanos que indican si cumplen con los limites.
			nameLenValid = 1 <= len(newNameDpt) <= 50
			idIsPositive = newIdDpt > 0
		
			if (nameLenValid and idIsPositive):
				query1 = self.find_idDpt(newIdDpt)
				query2 = self.find_nameDpt(newNameDpt)
				
				if ( (query1 == []) and (query2 == []) ):	
					newDpt = model.Dpt(newIdDpt, newNameDpt)
					session.add(newDpt)
					session.commit()
					return( True )
		
		return( False )
	
	#-------------------------------------------------------------------------------
	
	def find_idDpt(self, idDpt):
		"""
			@brief Funcion que realiza la busqueda del dpt cuyo identificador
				   sea "idDpt".
			
			@param idDpt: Identificador del dpt a buscar.
			
			@return lista que contiene las tuplas obtenidas del subquery. De lo 
					contrario retorna la lista vacia.
		"""
		
		idIsInt = type(idDpt) == int
		
		if ( idIsInt ):
			result = session.query(model.Dpt).filter(model.Dpt.iddpt==idDpt).all()
			return( result )
		
		return( [] )
	
	#-------------------------------------------------------------------------------
	def find_nameDpt(self, nameDpt):
		"""
			@brief Funcion que realiza la busqueda de los dpts cuyo identificador
				   sea "nameDpt".
			
			@param nameDpt: Nombre del dpt a buscar.
			
			@return lista que contiene las tuplas obtenidas del subquery. De lo 
					contrario retorna la lista vacia.
		"""
	
		nameIsStr = type(nameDpt) == str
		
		if ( nameIsStr ):
			result = session.query(model.Dpt).filter(model.Dpt.namedpt==nameDpt).all()
			return( result )
		
		return( [] )
	
	#-------------------------------------------------------------------------------
	
	def find_listIdDpt(self):
		"""
			@brief Funcion que devuelve los identificadores de los diferentes dpts
			que se encuentran almacenados en la base de datos.
			
			@param no admite parametros.
			
			@return lista con la consulta solicitada.
		"""
		
		result = session.query(model.Dpt.iddpt.label('id')).all()
		return( result )
	
	#-------------------------------------------------------------------------------
	def find_listNameDpt(self):
		"""
			@brief Funcion que devuelve los nombres de los diferentes dpts que se
				   encuentran almacenados en la base de datos.
			
			@param no admite parametros.
			
			@return lista con la consulta solicitada.
		"""
		
		result = session.query(model.Dpt.namedpt.label('name')).all()
		return( result )
	
	#-------------------------------------------------------------------------------
	
	def modify_idDpt(self, oldIdDpt, newIdDpt):
		"""
			@brief Funcion que modifica el id de un dpt dado por "newIdDpt".
			
			@param oldIdDpt	: id del dpt a modificar.
			@param newIdDpt: nuevo id para el dpt dado.
			
			@return True si se modifico el dpt dado. De lo contrario False.
		"""
		
		# Booleanos que indican si el tipo es el correcto.
		newIdIsInt = type(newIdDpt) == int
		oldIdIsInt = type(oldIdDpt) == int
		
		if ( newIdIsInt and oldIdIsInt ):
			# Booleanos que indican si cumplen con los limites.
			newIdIsPositive = newIdDpt > 0
			oldIdIsPositive = oldIdDpt > 0
			
			if ( newIdIsPositive and  oldIdIsPositive ):
				query1 = self.find_idDpt(oldIdDpt)
				query2 = self.find_idDpt(newIdDpt)
				
				if (( query1 != [] ) and ( query2 == [])):
					session.query(model.Dpt).filter(model.Dpt.iddpt==oldIdDpt).\
					update({'iddpt':(newIdDpt)})
					session.commit()
					return( True )
		
		return( False )
	
	#--------------------------------------------------------------------------------
	
	def modify_nameDpt(self, idDpt, newNameDpt):
		"""
			@brief Funcion que modifica el nombre de un dpt dado por "newNameDpt".
			
			@param idDpt	  : id del dpt a modificar.
			@param newNameDpt: nuevo nombre para el dpt dado.
			
			@return True si se modifico el dpt dado. De lo contrario False.
		"""
		
		# Booleanos que indican si el tipo es el correcto.
		nameIsStr = type(newNameDpt) == str
		idIsInt = type(idDpt) == int
		
		if ( nameIsStr and  idIsInt ):
			# Booleanos que indican si se cumplen los limites.
			nameLenValid = 1 <= len(newNameDpt) <= 50
			idIsPositive = idDpt > 0
			
			if ( nameLenValid and idIsPositive ):
				query1 = self.find_idDpt(idDpt)
				query2 = self.find_nameDpt(newNameDpt)
				
				if (( query1 != [] ) and ( query2 == [])):
					session.query(model.Dpt).filter(model.Dpt.iddpt==idDpt).\
					update({'namedpt':(newNameDpt)})
					session.commit()
					return( True )
		
		return( False )
	
	#--------------------------------------------------------------------------------	
	
	def delete_dpt(self, idDpt):
		"""
			@brief Funcion que elimina el dpt cuyo identificador sea "idDpt".
			
			@param idDpt: Identificador del dpt a eliminar.
			
			@return True si elimina el dpt dado. De lo contrario False.
		"""
		
		idIsInt = type(idDpt) == int 
		
		if ( idIsInt ):
			query = self.find_idDpt( idDpt )
				
			if ( query != [] ):
				session.query(model.Dpt).filter(model.Dpt.iddpt==idDpt).delete()
				session.commit()
				return( True )
	
		return( False )
	
	#-------------------------------------------------------------------------------