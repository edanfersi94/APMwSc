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

class clsDpt():

    def insert_dpt(self, newIdDpt, newNameDpt):

        query = self.find_idDpt(newIdDpt)
        query1 = self.find_nameDpt(newNameDpt)
        if (query == [] and query1 == [] ):
            newDpt = model.Dpt(newIdDpt, newNameDpt)
            session.add(newDpt)
            session.commit()
            return True
        return False
    
    def find_idDpt(self, idDpt):

        if(type(idDpt) == int):
            result = session.query(model.Dpt).filter(model.Dpt.iddpt==idDpt).all()
            return(result)
        return([])
    
    def find_nameDpt(self,nameDpt):
        if(type(nameDpt) == str):
            result = session.query(model.Dpt).filter(model.Dpt.namedpt==nameDpt).all()
            return(result)
        return([])
    
    def find_listIdDpt(self):

        result = session.query(model.Dpt.iddpt.label('id')).all()
        return(result)
    
    def find_listNameDpt(self):
        result = session.query(model.Dpt.namedpt.label('name')).all()
        return(result)
        
    def modify_idDpt(self, idDpt, newIdDpt):
        session.query(model.Dpt).filter(model.Dpt.iddpt==idDpt).\
            update({'iddpt':(newIdDpt)})
        session.commit()
        
    def modify_nameDpt(self, nameDpt, newNameDpt):
        session.query(model.Dpt).filter(model.Dpt.namedpt==nameDpt).\
            update({'namedpt':(newNameDpt)})
        session.commit()
    
    def delete_idDpt(self, idDpt):
        session.query(model.Dpt).filter(model.Dpt.iddpt==idDpt).delete()
        session.commit()

        
dpt1 = clsDpt()
#dpt1.insert_dpt(1,'dpt1')
#dpt1.insert_dpt(2,'dpt2')
#dpt1.insert_dpt(3,'dpt3')
result = dpt1.find_idDpt(3)
for v in result:
	print(v.namedpt)
       
result = dpt1.find_listIdDpt()
for v in result:
	print(v.id)
    
result = dpt1.find_idDpt(2)
#dpt1.delete_idDpt(2)
#role1.rolling_back_role()

dpt1.modify_idDpt(3, 2)