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

class clsRole():

	def insert_role(self, newIdRole, newNameRole):
		newRole = model.Role(newIdRole, newNameRole)
		session.add(newRole)
		session.commit()



"""
Prueba.
		
role1 = clsRole()
role1.insert_roles(1,'departamento1')
role1.insert_roles(2,'departamento2')
role1.insert_roles(3,'departamento3')

"""