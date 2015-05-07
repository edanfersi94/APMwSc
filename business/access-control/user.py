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

class clsUser():

	def insert_user(self, newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole):
		newUser = model.User(newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole)
		session.add(newUser)
		session.commit()

    #-----------------------------------------------------------------------

    def find_fullname(self, fullname):
        result = session.query(model.User).filter(model.User.fullname==fullname).all()
        return(result)

    def find_username(self, username):
        result = session.query(model.User).filter(model.User.username==username).all()
        return(result)

    def find_password(self, user):
        result = session.query(model.User.password).filter(model.User.username==user).all()
        return(result)
    
    def find_email(self, email):
        result = session.query(model.User).filter(model.User.email==email).all()
        return(result)
    
    def find_idDpt(self, idDpt):
        result = session.query(model.User).filter(model.User.iddpt==idDpt).all()
        return(result)
    
    def find_idRole(self, idRole):
        result = session.query(model.User).filter(model.User.idrole==idRole).all()
        return(result)

    #--------------------------------------------------------------------
    
    def find_listFullname(self):
        result = session.query(model.User.fullname.label('name')).all()
        return(result)
    
    def find_listUsername(self):
        result = session.query(model.User.username.label('user')).all()
        return(result)
       
    def find_listEmail(self):
        result = session.query(model.User.email.label('email')).all()
        return(result)

    def find_listIdDpt(self):
        result = session.query(model.User.iddpt.label('id')).all()
        return(result)
        
    def find_listIdRole(self):
        result = session.query(model.User.idrole.label('role')).all()
        return(result)

    #--------------------------------------------------------------------

    def modify_fullname(self, fullname, newFullname):
        session.query(model.User).filter(model.User.fullname==fullname).\
            update({'fullname':(newFullname)})
        session.commit()
        
    def modify_username(self, username, newUsername):
        session.query(model.User).filter(model.User.username==username).\
            update({'username':(newUsername)})
        session.commit()

    def modify_password(self, password, newPassword):
        session.query(model.User).filter(model.User.password==password).\
            update({'password':(newPassword)})
        session.commit()

    def modify_email(self, email, newEmail):
        session.query(model.User).filter(model.User.email==email).\
            update({'email':(newEmail)})
        session.commit()

    def modify_idDpt(self, idDpt, newIdDpt):
        session.query(model.User).filter(model.User.iddpt==idDpt).\
            update({'iddpt':(newIdDpt)})
        session.commit()
        
    def modify_idRole(self, idRole, newIdRole):
        session.query(model.User).filter(model.User.idrole==idRole).\
            update({'idrole':(newIdRole)})
        session.commit()

    #--------------------------------------------------------------------
        
    def delete_username(self, username):
        session.query(model.User).filter(model.User.username==username).delete()
        session.commit()

