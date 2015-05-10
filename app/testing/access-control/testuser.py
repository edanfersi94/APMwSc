"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Nicolas Manan.      Carnet: 06-39883
        Edward Fernandez.   Carnet: 10-11121
		

    DESCRIPCION: Script que contiene los casos de prueba del modulo 
				 "user.py"
	
"""

#------------------------------------------------------------------------------------

# Librerias a utilizar.

import os
import sys

# PATH que permite utilizar al modulo "dpt.py"
sys.path.append('../../business/access-control')
from user import clsUser, session

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../data')
import model

import unittest

class TestUser(unittest.TestCase):

    #.-------------------------------------------------------------------.  
    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsUser.
    def test1ObjectExist(self):
        tempUser = clsUser()
        self.assertIsNotNone( tempUser )
        session.query( model.User ).delete()  # Se limpia la base de datos.

    #.-------------------------------------------------------------------.  
    # FUNCION BUSCAR.
    
    #.............................................................
    ## FUNCION Nº1: find_fullname
	
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 2: Buscar un nombre de usuario que exista en la base de datos.
    def test2find_fullnameExist(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.

        newIdRole = 1
        newNameRole = 'rolprobando1'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()   
        
        newIdDpt = 1
        newNameDpt = 'rolprobando1'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()                   
        
        
        newFullname = 'Edward Fernandez'
        newUsername = 'edanfersi94'
        newPassword = 'cacacacata'
        newEmail = 'eanfersi@hotmail.com'
        newIddpt = 1
        newIdrole = 1
        newUser = model.User(newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole)
        session.add(newUser)
        session.commit()        
		
        tempUser = clsUser()
        fullname = 'Edward Fernandez'
        query = tempUser.find_fullname( fullname )
        boolR = True 
        for element in query:
            if element.fullname != fullname:
                boolR = False
        self.assertTrue( boolR )
        
    # Test 3: Buscar un nombre de un usuario que no exista en la base de 
    #		  datos.
    def test3find_fullnameNoExist(self):
        tempUser = clsUser()
        fullname = 'Pedro Fernandez'
        query = tempUser.find_fullname( fullname )
        self.assertEqual( query, [] )
        
    ### CASOS INVALIDOS( Casos Maliciosos ).
    # Test 4: Buscar un entero como nombre de un usuario.
    def test4find_fullnameNumber(self):
        tempUser = clsUser()
        fullname = 12345
        query = tempUser.find_fullname( fullname )
        self.assertEqual( query, [] )
        
    # Test 5: Buscar el string vacio como nombre de usuario.
    def test5find_fullnameEmptyString(self):
        tempUser = clsUser()
        fullname = ''
        query = tempUser.find_fullname( fullname )
        self.assertEqual( query, [] )
        
    # Test 6: Buscar None como nombre de usuario.	
    def test6find_fullnameNone(self):
        tempUser = clsUser()
        fullname = None
        query = tempUser.find_fullname( fullname )
        self.assertEqual( query, [] )
			
	#.............................................................
    ## FUNCION Nº2: find_username
	
	### CASOS VALIDOS( Casos Interiores ).
    # Test 7: Buscar un username que exista en la base de datos.
    def test7find_usernameExist(self):
        tempUser = clsUser()
        username = 'edanfersi94'
        query = tempUser.find_username( username )
        boolR = True 
        for element in query:
            if element.username != username:
                boolR = False
        self.assertTrue( boolR )
        
    # Test 8: Buscar un username que no exista en la base de datos.
    def test8find_usernameNoExist(self):
        tempUser = clsUser()
        username = 'nicoals'
        query = tempUser.find_username( username )
        self.assertEqual( query, [] )
        
    ### CASOS INVALIDOS( Casos Maliciosos ).
    # Test 9: Buscar un entero como username de un usuario.
    def test9find_usernameNumber(self):
        tempUser = clsUser()
        username = 12345
        query = tempUser.find_username( username )
        self.assertEqual( query, [] )
        
	# Test 10: Buscar el string vacio como username de usuario.
    def test_10find_usernameEmptyString(self):
        tempUser = clsUser()
        username = ''
        query = tempUser.find_username( username )
        self.assertEqual( query, [] )
        
    # Test 11: Buscar None como nombre de usuario.	
    def test_11find_usernameNone(self):
        tempUser = clsUser()
        username = None
        query = tempUser.find_username( username )
        self.assertEqual( query, [] )    

    #.............................................................
    ## FUNCION Nº3: find_email

	### CASOS VALIDOS( Casos Interiores ).
    # Test 12: Buscar un email que exista en la base de datos.
    def test_12find_emailExist(self):
        tempUser = clsUser()
        email = 'eanfersi@hotmail.com'
        query = tempUser.find_email( email )
        self.assertTrue( query[0].email == email )
        
    # Test 13: Buscar un email que no exista en la base de datos.
    def test_13find_emailNoExist(self):
        tempUser = clsUser()
        email = 'nicolas@hotmail.com'
        query = tempUser.find_email( email )
        self.assertEqual( query , [] )
                
	### CASOS INVALIDOS( Casos Maliciosos ).
    # Test 14: Buscar un entero como email de un usuario.
    def test_14find_emailNumber(self):
        tempUser = clsUser()
        email = 12345
        query = tempUser.find_email( email )
        self.assertEqual( query, [] )
        
	# Test 15: Buscar el string vacio como email de usuario.
    def test_15find_emailEmptyString(self):
        tempUser = clsUser()
        email = ''
        query = tempUser.find_email( email )
        self.assertEqual( query, [] )
        
	# Test 16: Buscar None como email de usuario.	
    def test_16find_emailNone(self):
        tempUser = clsUser()
        email = None
        query = tempUser.find_email( email )
        self.assertEqual( query, [] )  
	
    #.............................................................
    ## FUNCION Nº4: find_idDpt

	### CASOS VALIDOS( Casos Interiores ).
    # Test 17: Buscar un id de departamento que exista en la base de datos.
    def test_17find_idDptExist(self):
        tempUser = clsUser()
        idDpt = 1
        query = tempUser.find_idDpt( idDpt )
        self.assertIsNotNone( query[0] )
        
    # Test 18: Buscar un id de departamento que no exista en la base de datos.
    def test_18find_idDptNoExist(self):
        tempUser = clsUser()
        idDpt = 12
        query = tempUser.find_idDpt( idDpt )
        self.assertEqual( query , [] )
                
	### CASOS INVALIDOS( Casos Maliciosos ).
    # Test 19: Buscar un string como id de dpt de un usuario.
    def test_19find_idDptString(self):
        tempUser = clsUser()
        idDpt = 'What?'
        query = tempUser.find_idDpt( idDpt )
        self.assertEqual( query, [] )
        
	# Test 20: Buscar un float como id de dpt de un usuario.
    def test_20find_idDptFloat(self):
        tempUser = clsUser()
        idDpt = 2.0
        query = tempUser.find_idDpt(idDpt )
        self.assertEqual( query, [] )

	# Test 20: Buscar un numero negativo como id de dpt de un usuario.
    def test_20find_idDptnegative(self):
        tempUser = clsUser()
        idDpt = -2
        query = tempUser.find_idDpt(idDpt )
        self.assertEqual( query, [] )
        
	# Test 22: Buscar None como id de dpt de usuario.	
    def test_22find_idDptNone(self):
        tempUser = clsUser()
        idDpt = None
        query = tempUser.find_idDpt( idDpt )
        self.assertEqual( query, [] ) 
	
    #.............................................................
    ## FUNCION Nº5: find_idRole

	### CASOS VALIDOS( Casos Interiores ).
    # Test 23: Buscar un id de role que exista en la base de datos.
    def test_23find_idRoleExist(self):
        tempUser = clsUser()
        idRole = 1
        query = tempUser.find_idRole( idRole )
        self.assertIsNotNone( query[0] )
        
    # Test 24: Buscar un id de role que no exista en la base de datos.
    def test_24find_idRoleNoExist(self):
        tempUser = clsUser()
        idRole = 12
        query = tempUser.find_idRole( idRole )
        self.assertEqual( query , [] )
                
	### CASOS INVALIDOS( Casos Maliciosos ).
    # Test 25: Buscar un string como id de role de un usuario.
    def test_25find_idRoleString(self):
        tempUser = clsUser()
        idRole = 'What?'
        query = tempUser.find_idRole( idRole )
        self.assertEqual( query, [] )
        
	# Test 26: Buscar un float como id de role de un usuario.
    def test_26find_idRoleFloat(self):
        tempUser = clsUser()
        idRole = 2.0
        query = tempUser.find_idRole(idRole )
        self.assertEqual( query, [] )

	# Test 27: Buscar un numero negativo como id de role de un usuario.
    def test_27find_idRoleNegative(self):
        tempUser = clsUser()
        idRole = -2
        query = tempUser.find_idRole(idRole )
        self.assertEqual( query, [] )        
        
	# Test 28: Buscar None como id de role de usuario.	
    def test_28find_idRoleNone(self):
        tempUser = clsUser()
        idRole = None
        query = tempUser.find_idRole( idRole )
        self.assertEqual( query, [] ) 

    #.............................................................		
	## FUNCION Nº6: find_listFullname
    ### CASOS VALIDOS( Casos Interiores ).
    
    # Test 29: Se buscan los fullnames que se encuentran en la base
    #          de datos y dicha base se encuentra vacia.
    def test_29find_listFullnameEmptyBase(self):
        session.query(model.User).delete()  # Se limpia la base de datos.
        session.query(model.Dpt).delete() 
        session.query(model.Role).delete()  
        tempUser = clsUser()
        query = tempUser.find_listFullname()
        self.assertEqual(query,[])  
    
    # Test 30: Se buscan los fullnames que se encuentran en la base
    #          de datos y dicha base tiene una sola tupla.
    def test_30find_listFullnameneTuple(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdRole = 3
        newNameRole = 'rolprobando'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()   
        
        newIdDpt = 3
        newNameDpt = 'dptprobando'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()                   
        
        
        newFullname = 'Nicolas Manana'
        newUsername = 'Nicolag'
        newPassword = 'krakatoa'
        newEmail = 'nico@hotmail.com'
        newIddpt = 3
        newIdrole = 3
        newUser = model.User(newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole)
        session.add(newUser)
        session.commit()    
                                
        tempUser = clsUser()
        query = tempUser.find_listFullname()
        respEsp = 'Nicolas Manana'
        self.assertTrue( query[0].name == respEsp )  
    
    # Test 31: Se buscan los fullnames que se encuentran en la
    #          base de datos y dicha base tiene al menos dos tuplas.
    def test_31find_listFullnameAlmost2Tuples(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdRole = 4
        newNameRole = 'rolprobando2'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()   
        
        newIdDpt = 4
        newNameDpt = 'dptprobando2'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()                   
        
        
        newFullname = 'Jose Manuel Perez'
        newUsername = 'kino'
        newPassword = 'krakatoa'
        newEmail = 'elnico23@hotmail.com'
        newIddpt = 4
        newIdrole = 4
        newUser = model.User(newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole)
        session.add(newUser)
        session.commit()        
                                
        tempUser = clsUser()
        query = tempUser.find_listFullname()
        resultEsp = [('Nicolas Manana',),('Jose Manuel Perez',)]
        self.assertTrue( query[:-1] == resultEsp[:-1] )  

    #.............................................................		
	## FUNCION Nº7: find_listUsername
    ### CASOS VALIDOS( Casos Interiores ).
    
    # Test 32: Se buscan los usernames que se encuentran en la
    #          base de datos y dicha base se encuentra vacia.
    def test_32find_listUsernameEmptyBase(self):
        session.query(model.User).delete()  # Se limpia la base de datos.
        session.query(model.Dpt).delete()
        session.query(model.Role).delete()
        tempUser = clsUser()
        query = tempUser.find_listUsername()
        self.assertEqual(query,[])  
    
    # Test 33: Se buscan los usernames que se encuentran en la
    #          base de datos y dicha base tiene una sola tupla.
    def test_33find_listIdUsernameOneTuple(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        newIdRole = 3
        newNameRole = 'rolprobando'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()   
        
        newIdDpt = 3
        newNameDpt = 'dptprobando'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()                   
        
        
        newFullname = 'Nicolas Manana'
        newUsername = 'Nicolag'
        newPassword = 'krakatoa'
        newEmail = 'elnico@hotmail.com'
        newIddpt = 3
        newIdrole = 3
        newUser = model.User(newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole)
        session.add(newUser)
        session.commit()    
                                
        tempUser = clsUser()
        query = tempUser.find_listUsername()
        respEsp = 'Nicolag'
        self.assertTrue( query[0].user == respEsp )  
    
    # Test 34: Se buscan los usernames que se encuentran en la
    #          base de datos y dicha base tiene al menos dos tuplas.
    def test_34find_listUsernameAlmost2Tuples(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdRole = 4
        newNameRole = 'rolprobando2'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()   
        
        newIdDpt = 4
        newNameDpt = 'dptprobando2'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()                   
        
        
        newFullname = 'Nicolas Manana'
        newUsername = 'kino'
        newPassword = 'krakatoa'
        newEmail = 'nico23@hotmail.com'
        newIddpt = 4
        newIdrole = 4
        newUser = model.User(newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole)
        session.add(newUser)
        session.commit()        
                                
        tempUser = clsUser()
        query = tempUser.find_listUsername()
        respEsp = [('Nicolag',),('kino',)]
        self.assertTrue( query[:-1] == respEsp[:-1] )  

    #.............................................................		
	## FUNCION Nº8: find_listEmail
    ### CASOS VALIDOS( Casos Interiores ).
    
    # Test 35: Se buscan los emails que se encuentran en la
    #          base de datos y dicha base se encuentra vacia.
    def test_35find_listEmailEmptyBase(self):
        session.query(model.User).delete()  # Se limpia la base de datos.
        session.query(model.Dpt).delete()  
        session.query(model.Role).delete()  
        tempUser = clsUser()
        query = tempUser.find_listEmail()
        self.assertEqual(query,[])  
    
    # Test 36: Se buscan los emails que se encuentran en la
    #          base de datos y dicha base tiene una sola tupla.
    def test_36find_listEmailOneTuple(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        newIdRole = 3
        newNameRole = 'rolprobando'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()   
        
        newIdDpt = 3
        newNameDpt = 'dptprobando'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()                   
        
        
        newFullname = 'Nicolas Manana'
        newUsername = 'Nicolag'
        newPassword = 'krakatoa'
        newEmail = 'elnico@hotmail.com'
        newIddpt = 3
        newIdrole = 3
        newUser = model.User(newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole)
        session.add(newUser)
        session.commit()    
                                
        tempUser = clsUser()
        query = tempUser.find_listEmail()
        respEsp = 'elnico@hotmail.com'
        self.assertTrue( query[0].email == respEsp )  
    
    # Test 37: Se buscan los emails que se encuentran en la
    #          base de datos y dicha base tiene al menos dos tuplas.
    def test_37find_listEmailsAlmost2Tuples(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdRole = 4
        newNameRole = 'rolprobando2'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()   
        
        newIdDpt = 4
        newNameDpt = 'dptprobando2'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()                   
        
        
        newFullname = 'Nicolas Manana'
        newUsername = 'kino'
        newPassword = 'krakatoa'
        newEmail = 'elnico23@hotmail.com'
        newIddpt = 4
        newIdrole = 4
        newUser = model.User(newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole)
        session.add(newUser)
        session.commit()        
                                
        tempUser = clsUser()
        query = tempUser.find_listEmail()
        resultEsp = [('elnico@hotmail.com',),('elnico23@hotmail.com',)]
        self.assertTrue( query[:-1] == resultEsp[:-1] )  
        
    #.............................................................	
	## FUNCION Nº9: find_listIdDpt
    ### CASOS VALIDOS( Casos Interiores ).
    
    # Test 38: Se buscan los id de los dpts que se encuentran en la
    #          base de datos y dicha base se encuentra vacia.
    def test_38find_listIdDptEmptyBase(self):
        session.query(model.User).delete()  # Se limpia la base de datos.
        session.query(model.Dpt).delete()
        session.query(model.Role).delete()
        tempUser = clsUser()
        query = tempUser.find_listIdDpt()
        self.assertEqual(query,[])  
    
    # Test 39: Se buscan los id de los dpts que se encuentran en la
    #          base de datos y dicha base tiene una sola tupla.
    def test_39find_listIdDptOneTuple(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        newIdRole = 3
        newNameRole = 'rolprobando'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()   
        
        newIdDpt = 3
        newNameDpt = 'dptprobando'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()                   
        
        
        newFullname = 'Nicolas Manana'
        newUsername = 'Nicolag'
        newPassword = 'krakatoa'
        newEmail = 'elnico@hotmail.com'
        newIddpt = 3
        newIdrole = 3
        newUser = model.User(newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole)
        session.add(newUser)
        session.commit()    
                                
        tempUser = clsUser()
        query = tempUser.find_listIdDpt()
        respEsp = 3
        self.assertTrue( query[0].dpt == respEsp )  
    
    # Test 40: Se buscan los id de los roles que se encuentran en la
    #          base de datos y dicha base tiene al menos dos tuplas.
    def test_40find_listIdRoleAlmost2Tuples(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdRole = 4
        newNameRole = 'rolprobando2'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()   
        
        newIdDpt = 4
        newNameDpt = 'dptprobando2'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()                   
        
        
        newFullname = 'Nicolas Manana'
        newUsername = 'kino'
        newPassword = 'krakatoa'
        newEmail = 'elnico23@hotmail.com'
        newIddpt = 4
        newIdrole = 4
        newUser = model.User(newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole)
        session.add(newUser)
        session.commit()        
                                
        tempUser = clsUser()
        query = tempUser.find_listIdRole()
        resultEsp = [(3,),(4,)]
        self.assertTrue( query[:-1] == resultEsp[:-1] )  
    
    #.............................................................		
	## FUNCION Nº10: find_listIdRole
    ### CASOS VALIDOS( Casos Interiores ).
    
    # Test 41: Se buscan los id de los roles que se encuentran en la
    #          base de datos y dicha base se encuentra vacia.
    def test_41find_listIdRoleEmptyBase(self):
        session.query(model.User).delete()  # Se limpia la base de datos.
        session.query(model.Role).delete()
        session.query(model.Dpt).delete()
        tempUser = clsUser()
        query = tempUser.find_listIdRole()
        self.assertEqual(query,[])  
    
    # Test 42: Se buscan los id de los roles que se encuentran en la
    #          base de datos y dicha base tiene una sola tupla.
    def test_42find_listIdRoleOneTuple(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        newIdRole = 3
        newNameRole = 'rolprobando'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()   
        
        newIdDpt = 3
        newNameDpt = 'dptprobando'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()                   
        
        
        newFullname = 'Nicolas Manana'
        newUsername = 'Nicolag'
        newPassword = 'krakatoa'
        newEmail = 'elnico@hotmail.com'
        newIddpt = 3
        newIdrole = 3
        newUser = model.User(newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole)
        session.add(newUser)
        session.commit()    
                                
        tempUser = clsUser()
        query = tempUser.find_listIdRole()
        respEsp = 3
        self.assertTrue( query[0].role == respEsp )  
    
    # Test 43: Se buscan los id de los roles que se encuentran en la
    #          base de datos y dicha base tiene al menos dos tuplas.
    def test_43find_listIdRoleAlmost2Tuples(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdRole = 4
        newNameRole = 'rolprobando2'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()   
        
        newIdDpt = 4
        newNameDpt = 'dptprobando2'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()                   
        
        
        newFullname = 'Nicolas Manana'
        newUsername = 'kino'
        newPassword = 'krakatoa'
        newEmail = 'elnico23@hotmail.com'
        newIddpt = 4
        newIdrole = 4
        newUser = model.User(newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole)
        session.add(newUser)
        session.commit()        
                                
        tempUser = clsUser()
        query = tempUser.find_listIdRole()
        resultEsp = [(3,),(4,)]
        self.assertTrue( query[:-1] == resultEsp[:-1] )  
    
    #.............................................................		
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.


    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.

    """
        #.-------------------------------------------------------------------.  
        # FUNCION ELIMINAR.
        
        ### CASOS VALIDOS( Casos Interiores ).
        # Test 100: El usuario a eliminar existe en la base de datos.
        def test_100Delete_userExist(self):
            tempUser = clsUser()
            userDelete = 'edanfersi94'
            result = tempRole.delete_username( userDelete )
            self.assertTrue( result )
    
        # Test 101: El usuario a eliminar no existe en la base de datos.
        def test_101Delete_userNoExist(self):
            tempUser = clsUser()
            userDelete = 'edanfersi94'
            result = tempRole.delete_username( userDelete )
            self.assertTrue( result )
            
        ### CASOS INVALIDOS( Casos Malicia )
        # Test 102: El username del usuario a eliminar es un numero.
        def test_102Delete_userNoExist(self):
            tempUser = clsUser()
            userDelete = 1234567
            result = tempRole.delete_username( userDelete )
            self.assertTrue( result )
        
        # Test 103: El username del usuario a eliminar es la cadena vacia.
        def test_103Delete_userNoExist(self):
            tempUser = clsUser()
            userDelete = ''
            result = tempRole.delete_username( userDelete )
            self.assertTrue( result )
    
        # Test 104: El username del usuario a eliminar es None.
        def test_104Delete_roleIdNone(self):
            tempUser = clsUser()
            userDelete = None
            result = tempRole.delete_username( userDelete )
            self.assertTrue( result )
        
        #.-------------------------------------------------------------------.  
    """