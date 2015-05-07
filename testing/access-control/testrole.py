"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Nicolas Manan.      Carnet: 06-39883
        Edward Fernandez.   Carnet: 10-11121
		

    DESCRIPCION: Script que contiene los casos de prueba del modulo "role.py"
	
"""

#------------------------------------------------------------------------------------

# Librerias a utilizar.

import os
import sys

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../business/access-control')
from role import clsRole, session

sys.path.append('../../data')
import model

import unittest

class TestRole(unittest.TestCase):
    
    #.-------------------------------------------------------------------.  
    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsRole.
    def test1ObjectExist(self):
        tempRole = clsRole()
        self.assertIsNotNone(tempRole)
        session.query(model.Role).delete()  # Se limpia la base de datos.
    
    #.-------------------------------------------------------------------.  
    # FUNCION BUSCAR.
    
    #.............................................................
    ## FUNCION Nº1: find_IdRole
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 2: Buscar el id de un rol que exista. 
    def test2find_IdRoleExist(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdRole = 1
        newNameRole = 'rolprobando1'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()   
        
        tempRole = clsRole()
        idRole = 1
        query = tempRole.find_IdRole( idRole )
        self.assertIsNotNone( query[0] )
    
    # Test 3: Buscar el id de un rol que no exista.
    def test3find_IdRoleNotExist(self):
        tempRole = clsRole()
        idRole = 1000
        query = tempRole.find_IdRole( idRole )
        self.assertEqual(query,[])
    
    ### CASOS INVALIDOS( Casos Malicia )
    # Test 4: El id del rol a buscar es un string.
    def test4find_IdRoleString(self):
        tempRole = clsRole()
        idRole = '1'
        result = tempRole.find_IdRole( idRole )
        self.assertEqual(result,[])
    
    # Test 5: El id del rol a buscar es un float.
    def test5find_IdRoleFloat(self):
        tempRole = clsRole()
        idRole = 1.01
        result = tempRole.find_IdRole( idRole )
        self.assertEqual(result,[])  

    # Test 6: El id del rol a buscar es nulo.
    def test6find_IdRoleNone(self):
        tempRole = clsRole()
        idRole = None
        result = tempRole.find_IdRole( idRole )
        self.assertEqual(result,[])  
    
    #.............................................................
    ## FUNCION Nº2: find_NameRole
    ### CASOS VALIDOS( Casos Interiores ).
    
    # Test 7: Buscar el nombre de un rol existente.
    def test7find_NameRoleExist(self):
        tempRole = clsRole()
        nameRole = 'rolprobando1'
        result = tempRole.find_NameRole( nameRole )
        self.assertIsNotNone(result[0])
    
    # Test 8: Buscar el nombre de un rol que no existe.    
    def test8find_NameRoleNotExist(self):
        tempRole = clsRole()
        nameRole = 'role10'
        result = tempRole.find_NameRole( nameRole )
        self.assertEqual(result,[])    
    
    ### CASOS INVALIDOS( Casos Malicia )
    # Test 9: Buscar un entero como nombre de un rol.
    def test_9find_NameRoleNumber(self):
        tempRole = clsRole()
        nameRole = 1
        result = tempRole.find_NameRole( nameRole )
        self.assertEqual(result,[])
        
    # Test 10: Buscar el string vacio como nombre de un rol.
    def test_10find_NameRoleEmptyString(self):
        tempRole = clsRole()
        nameRole = ""
        result = tempRole.find_NameRole( nameRole )
        self.assertEqual(result,[])
        
    # Test 11: Buscar el elemento nulo como nombre de un rol.
    def test_11find_NameRoleEmpty(self):
        tempRole = clsRole()
        nameRole = None
        result = tempRole.find_NameRole( nameRole )
        self.assertEqual(result,[])   
        
    #.............................................................
    ## FUNCION Nº3: find_listIdRole
    ### CASOS VALIDOS( Casos Interiores ).
    
    # Test 12: Se buscan los id de los roles que se encuentran en la
    #          base de datos y dicha base se encuentra vacia.
    def test_12find_listIdRoleEmptyBase(self):
        session.query(model.Role).delete()  # Se limpia la base de datos.
        tempRole = clsRole()
        result = tempRole.find_listIdRole()
        self.assertEqual(result,[])  
    
    # Test 13: Se buscan los id de los roles que se encuentran en la
    #          base de datos y dicha base tiene una sola tupla.
    def test_13find_listIdRoleOneTuple(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdRole = 50
        newNameRole = 'role50'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()      
                                
        tempRole = clsRole()
        result = tempRole.find_listIdRole()
        self.assertTrue( result[0].id == 50 )  
    
    # Test 14: Se buscan los id de los roles que se encuentran en la
    #          base de datos y dicha base tiene al menos dos tuplas.
    def test_14find_listIdRoleAlmost2Tuples(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdRole = 51
        newNameRole = 'role51.0'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()      
                                
        tempRole = clsRole()
        result = tempRole.find_listIdRole()
        resultEsp = [(50,),(51,)]
        self.assertTrue( result[:-1] == resultEsp[:-1] )      

    #.............................................................
    ## FUNCION Nº4: find_listNamedRole
    ### CASOS VALIDOS( Casos Interiores ).
    
    # Test 15: Se buscan los nombres de los roles que se encuentran en la
    #          base de datos y dicha base se encuentra vacia.
    def test_15find_listNameRoleEmptyBase(self):
        session.query(model.Role).delete()  # Se limpia la base de datos.
        tempRole = clsRole()
        result = tempRole.find_listNameRole()
        self.assertEqual(result,[])  
    
    # Test 16: Se buscan los nombres de los roles que se encuentran en la
    #          base de datos y dicha base tiene una sola tupla.
    def test_16find_listNameRoleOneTuple(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdRole = 50
        newNameRole = 'role50'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()      
                                
        tempRole = clsRole()
        result = tempRole.find_listNameRole()
        self.assertTrue( result[0].name == 'role50' )  
    
    # Test 17: Se buscan los nombres de los roles que se encuentran en la
    #          base de datos y dicha base tiene al menos dos tuplas.
    def test_17find_listNameRoleAlmost2Tuples(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdRole = 51
        newNameRole = 'role51'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()      
                                
        tempRole = clsRole()
        result = tempRole.find_listNameRole()
        resultEsp = [('role50',),('role51',)]
        self.assertTrue( result[:-1] == resultEsp[:-1] )   
    
    #.............................................................
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 18: Insertar un rol que no existe.
    def test_18insert_roleNoExist(self):
        session.query(model.Role).delete()  # Se limpia la base de datos.
        tempRole = clsRole()
        newIdRole = 2
        newNameRole = 'role2.0'
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertTrue(result)
    
    # Test 19: Insertar un rol que ya existe.
    def test_19insert_roleExist(self):
        tempRole = clsRole()
        newIdRole = 2
        newNameRole = 'role2.0'
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertFalse(result)
        
    # Test 20: El id del rol a insertar no existe pero el nombre si.
    def test_20insert_roleIdNotExistNameExist(self):
        tempRole = clsRole()
        newIdRole = 20
        newNameRole = 'role2.0'
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertFalse(result)
        
    # Test 21: El id del rol a insertar existe pero el nombre no.
    def test_21insert_roleIdExistNameNotExist(self):
        tempRole = clsRole()
        newIdRole = 2
        newNameRole = 'roleDePrueba'
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertFalse(result)
    
    ### CASOS VALIDOS( Casos Fronteras )
    # Test 22: Se insertara un rol que no existe en la base de datos y
    #          el tam del nombre es igual a 1.
    def test_22insert_roleIdNoExistNameLen1(self):
        tempRole = clsRole()
        newIdRole = 10
        newNameRole = '1'
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertTrue(result)

    # Test 23: Se insertara un rol que no existe en la base de datos y
    #          el tam del nombre es igual a 50.
    def test_23insert_roleIdNoExistNameLen50(self):
        tempRole = clsRole()
        newIdRole = 11
        newNameRole = 'r'*50
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertTrue(result)
        
    # Test 24: Se insertara un rol que no existe en la base de datos y
    #          el id del mismo es igual a 1 (menor valor posible).
    def test_24insert_roleIdNoExistIqualOne(self):
        tempRole = clsRole()
        newIdRole = 1
        newNameRole = 'role1'
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertTrue(result)
        
    # Test 25: Se insertara un rol que no existe en la base de datos y
    #          el id del mismo es un numero muy grande.
    def test_25insert_roleIdNoExistIqualBigNumber(self):
        tempRole = clsRole()
        newIdRole = (2**31)-1
        newNameRole = 'roleBig'
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertTrue(result)
        
    ### CASOS VALIDOS( Casos Esquinas )
    # Test 26: Se insertara un rol que no existe en la base de datos.
    #          El id del mismo es igual a 1 y su nombre es de longitud
    #          igual a 1.
    def test_26insert_roleIdNoExistIqual1NameLen1(self):
        session.query(model.Role).delete()  # Se limpia la base de datos.
        tempRole = clsRole()
        newIdRole = 1
        newNameRole = 'r'
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertTrue(result)
        
    # Test 27: Se insertara un role que no existe en la base de datos.
    #          El id del mismo es igual a 1 y su nombre es de longitud
    #          igual a 50.
    def test_27insert_roleIdNoExistIqual1NameLen50(self):
        session.query(model.Role).delete()  # Se limpia la base de datos.
        tempRole = clsRole()
        newIdRole = 1
        newNameRole = 'r'*50
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertTrue(result)

    # Test 28: Se insertara un rol que no existe en la base de datos.
    #          El id del mismo es igual a (2**31)-1 y su nombre es de
    #          longitud igual a 1.
    def test_28insert_roleIdNoExistIqualBigNumberNameLen1(self):
        session.query(model.Role).delete()  # Se limpia la base de datos.
        tempRole = clsRole()
        newIdRole = (2**31)-1
        newNameRole = 'r'
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertTrue(result)

    # Test 29: Se insertara un rol que no existe en la base de datos.
    #          El id del mismo es igual a (2**31)-1 y su nombre es de
    #          igual a 50.
    def test_29insert_roleIdNoExistIqualBigNumberNameLen50(self):
        session.query(model.Role).delete()  # Se limpia la base de datos.
        tempRole = clsRole()
        newIdRole = (2**31)-1
        newNameRole = 'r'*50
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertTrue(result)
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    # Test 30: El id del rol a insertar es valido pero el nombre es 
    #          la cadena vacia.
    def test_30insert_roleIdNoExistNameLen0(self):
        tempRole = clsRole()
        newIdRole = 25
        newNameRole = ''
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertFalse(result)

    # Test 31: El id del rol a insertar es valido pero el nombre es
    #          una cadena de 51 caracteres.
    def test_31insert_roleIdNoExistNameLen51(self):
        tempRole = clsRole()
        newIdRole = 25
        newNameRole = 'r'*51
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertFalse(result)

    # Test 32: El id del rol a insertar es valido pero el nombre es 
    #          un numero.
    def test_32insert_roleIdNoExistNameNumber(self):
        tempRole = clsRole()
        newIdRole = 25
        newNameRole = 123456
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertFalse(result)

    # Test 33: El id del rol a insertar es un numero negativo.
    def test_33insert_roleIdNegative(self):
        tempRole = clsRole()
        newIdRole = -25
        newNameRole = 'roleDePrueba'
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertFalse(result)
        
    # Test 34: El id del rol a insertar es un string.
    def test_34insert_roleIdString(self):
        tempRole = clsRole()
        newIdRole = '25'
        newNameRole = 'roleDePrueba'
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertFalse(result)
        
    # Test 35: El id del rol a insertar es un float.
    def test_35insert_roleIdFloat(self):
        tempRole = clsRole()
        newIdRole = 25.01
        newNameRole = 'roleDePrueba'
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertFalse(result)
 
    # Test 36: El id del rol a insertar es None.
    def test_36insert_roleIdNone(self):
        tempRole = clsRole()
        newIdRole = None
        newNameRole = 'roleDePrueba'
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertFalse(result)

    #.............................................................

    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    #.............................................................
    ## FUNCION Nº1: modify_idRole

    ### CASOS VALIDOS( Casos Interiores ).
    # Test 37: El id del rol a modificar existe en la base de datos y el
    #          nuevo id se encuentra disponible.
    def test_37modify_idRoleOldIdExistNewIdAvailable(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdRole = 51
        newNameRole = 'role51'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit()      
        
        tempRole = clsRole()
        oldIdRole = 51
        newIdRole = 15
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertTrue( result )
 
    # Test 38: El id del rol a modificar existe en la base de datos y el
    #          nuevo id no se encuentra disponible.
    def test_38modify_idRoleOldIdExistNewIdNotAvailable(self):
        tempRole = clsRole()
        oldIdRole = 15
        newIdRole = (2**31)-1
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertFalse( result )

    # Test 39: El id del rol a modificar no existe en la base de datos 
    #          pero el nuevo id se encuentra disponible.
    def test_39modify_idRoleOldIdNotExistNewIdAvailable(self):
        tempRole = clsRole()
        oldIdRole = 111
        newIdRole = 9
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertFalse( result )        
        
    # Test 40: El id del rol a modificar no existe en la base de datos 
    #          y el nuevo id no se encuentra disponible.
    def test_40modify_idRoleOldIdNotExistNewIdNotAvailable(self):
        tempRole = clsRole()
        oldIdRole = 111
        newIdRole = 15
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertFalse( result )        

    ### CASOS VALIDOS( Casos Fronteras )           
    # Test 41: El id del rol a modificar existe en la base de datos y su
    #          valor es igual a 1. El nuevo id se encuentra disponible.
    def test_41modify_idRoleOldIdExistIqual1NewIdAvailable(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdRole = 1
        newNameRole = 'roleDePrueba1'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit() 
        
        tempRole = clsRole()
        oldIdRole = 1
        newIdRole = 150
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertTrue( result )     
    
    # Test 42: El id del rol a modificar existe en la base de datos y su
    #          valor es muy grande. El nuevo id se encuentra disponible.
    def test_42modify_idRoleOldIdExistIqualBigNumberNewIdAvailable(self):
        tempRole = clsRole()
        oldIdRole = (2**31)-1
        newIdRole = 200
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertTrue( result )     
    
    # Test 43: El id del rol a modificar existe en la base de datos. El
    #          nuevo id se encuentra disponible y es igual a 1.
    def test_43modify_idRoleOldIdExistNewIdAvailableIqual1(self):
        tempRole = clsRole()
        oldIdRole = 150
        newIdRole = 1
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertTrue( result )      
    
    # Test 44: El id del rol a modificar existe en la base de datos. El
    #          nuevo id se encuentra disponible y su valor es muy grande.    
    def test_44modify_idRoleOldIdExistNewIdAvailableIqualBigNumber(self):
        tempRole = clsRole()
        oldIdRole = 200
        newIdRole = (2**31)-1
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertTrue( result )  

    ### CASOS VALIDOS( Casos Esquinas )  
    # Test 45: El id del rol a modificar existe en la base de datos y su
    #          valor es muy grande. El nuevo id se encuentra disponible y
    #          su valor es igual a 1.
    def test_45modify_idRoleOldIdExistIqualBigNumberNewIdAvailableIqual1(self):
        session.query(model.Role).delete()  # Se limpia la base de datos.
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdRole = (2**31)-1
        newNameRole = 'roleDePrueba1'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit() 
        
        tempRole = clsRole()
        oldIdRole = (2**31)-1
        newIdRole = 1
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertTrue( result )  
    
    
    # Test 46: El id del rol a modificar existe en la base de datos y su
    #          valor es igual a 1. El nuevo id se encuentra disponible
    #          y su valor es muy grande.
    def test_46modify_idRoleOldIdExistIqual1NewIdAvailable(self):        
        tempRole = clsRole()
        oldIdRole = 1
        newIdRole = (2**31)-1
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertTrue( result )  
        
    ### CASOS INVALIDOS( Casos Malicia ):
    # Test 47: El id dado del rol a modificar es un string.
    def test_47modify_idRoleOldIdString(self):        
        tempRole = clsRole()
        oldIdRole = '1'
        newIdRole = 156
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertFalse( result )  
        
    # Test 48: El id dado del rol a modificar es un numero negativo.    
    def test_48modify_idRoleOldIdNumberNegative(self):        
        tempRole = clsRole()
        oldIdRole = -1
        newIdRole = (2**31)-1
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertFalse( result )  
        
    # Test 49: El id dado del rol a modificar es un float.
    def test_49modify_idRoleOldIdIqualFloat(self):        
        tempRole = clsRole()
        oldIdRole = 1.0
        newIdRole = (2**31)-1
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertFalse( result )  
        
    # Test 50: El id dado del rol a modificar es None.         
    def test_50modify_idRoleOldIdIqualNone(self):        
        tempRole = clsRole()
        oldIdRole = None
        newIdRole = (2**31)-1
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertFalse( result )  
        
    # Test 51: El nuevo id para el rol a modificar es un string.
    def test_51modify_idRoleOldIdExistNewIdString(self):        
        tempRole = clsRole()
        oldIdRole = 1
        newIdRole = '(2**31)-1'
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertFalse( result )  
        
    # Test 52: El nuevo id para el rol a modificar es un numero negativo.    
    def test_52modify_idRoleOldIdExistNewIdNegative(self):        
        tempRole = clsRole()
        oldIdRole = 1
        newIdRole = -20
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertFalse( result )  
        
    # Test 53: El nuevo id para el rol a modificar es un float.
    def test_53modify_idRoleOldIdExistNewIdFloat(self):        
        tempRole = clsRole()
        oldIdRole = 1
        newIdRole = 20.01
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertFalse( result )  
        
    # Test 54: El nuevo id para el rol a modificar es None. 
    def test_54modify_idRoleOldIdExistNewIdNone(self):        
        tempRole = clsRole()
        oldIdRole = 1
        newIdRole = None
        result = tempRole.modify_idRole( oldIdRole, newIdRole )
        self.assertFalse( result )   
        
    ## FUNCION Nº2: modify_nameRole

    ### CASOS VALIDOS( Casos Interiores ).
    # Test 55: El id del rol a modificar existe en la base de datos y el
    #          nuevo nombre se encuentra disponible.
    def test_55modify_nameRoleIdExistNewNameAvailable(self):
        session.query(model.Role).delete()  # Se limpia la base de datos.
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdRole = 3
        newNameRole = 'roleDePrueba1'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit() 
        
        tempRole = clsRole()
        idRole = 3
        newNameRole = 'rolDePruebaX'
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertTrue( result )         
    
    # Test 56: El id del rol a modificar existe en la base de datos y el
    #          nuevo nombre no se encuentra disponible.
    def test_56modify_nameRoleIdExistNewNameNoAvailable(self):
        tempRole = clsRole()
        idRole = 3
        newNameRole = 'rolDePruebaX'
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertFalse( result )  
    
    # Test 57: El id del rol a modificar no existe en la base de datos 
    #          pero el nuevo nombre se encuentra disponible.
    def test_57modify_nameRoleIdNoExistNewNameAvailable(self):
        tempRole = clsRole()
        idRole = 20
        newNameRole = 'rolDePruebaX2'
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertFalse( result ) 
    
    # Test 58: El id del rol a modificar no existe en la base de datos 
    #          y el nuevo nombre no se encuentra disponible.
    def test_58modify_nameRoleIdNoExistNewNameNoAvailable(self):
        tempRole = clsRole()
        idRole = 20
        newNameRole = 'rolDePruebaX'
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertFalse( result )  
    
    ### CASOS VALIDOS( Casos Fronteras )
    
    # Test 59: El id del rol a modificar existe en la base de datos y su
    #          valor es igual a 1. El nuevo nombre se encuentra disponible.
    def test_59modify_nameRoleIdExistIqual1NewNameAvailable(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida. 
        newIdRole = 1
        newNameRole = 'roleDePruebaCaso1'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit() 
        
        tempRole = clsRole()
        idRole = 1
        newNameRole = 'rolDePruebaX3'
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertTrue( result ) 

    # Test 60: El id del rol a modificar existe en la base de datos y su
    #          valor es un numero muy grande. El nuevo nombre se encuentra disponible.     
    def test_60modify_nameRoleIdExistIqualBigNumberNewNameAvailable(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida. 
        newIdRole = (2**31)-1
        newNameRole = 'roleDePruebaCasoBig'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit() 

        tempRole = clsRole()
        idRole = (2**31)-1
        newNameRole = 'rolDePruebaXBig'
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertTrue( result )  
    
    # Test 61: El id del rol a modificar existe en la base de datos. El nuevo 
    #          nombre se encuentra disponible y es de largo 1.
    def test_61modify_nameRoleIdExistNewNameAvailableLen1(self):
        tempRole = clsRole()
        idRole = 3
        newNameRole = '1'
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertTrue( result )  
    
    # Test 62: El id del rol a modificar existe en la base de datos. El nuevo 
    #          nombre se encuentra disponible y es de largo 50.
    def test_62modify_nameRoleIdExistNewNameAvailableLen50(self):
        tempRole = clsRole()
        idRole = 3
        newNameRole = 'x'*50
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertTrue( result )  
    
    ### CASOS VALIDOS( Casos Esquinas )
    # Test 63: El id del rol a modificar existe en la base de datos y su valor es
    #          igual a 1. El nuevo nombre es valido y su longitud es igual a 1.
    def test_63modify_nameRoleIdExistIqual1NewNameAvailableLen1(self):
        tempRole = clsRole()
        idRole = 1
        newNameRole = 'z'
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertTrue( result ) 
    
    # Test 64: El id del rol a modificar existe en la base de datos y su valor es
    #          igual a 1. El nuevo nombre es valido y su longitud es igual a 50.
    def test_64modify_nameRoleIdExistIqual1NewNameAvailableLen50(self):
        tempRole = clsRole()
        idRole = 1
        newNameRole = 'z'*50
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertTrue( result ) 
            
    # Test 65: El id del rol a modificar existe en la base de datos y su valor es
    #          un numero muy grande. El nuevo nombre es valido y su longitud es igual a 1.
    def test_65modify_nameRoleIdExistIqualBigNumberNewNameAvailableLen1(self):
        tempRole = clsRole()
        idRole = (2**31)-1
        newNameRole = 'y'
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertTrue( result ) 

    # Test 66: El id del rol a modificar existe en la base de datos y su valor es
    #          un numeor muy grande. El nuevo nombre es valido y su longitud es igual a 50.
    def test_66modify_nameRoleIdExistIqualBigNumberNewNameAvailableLen50(self):
        tempRole = clsRole()
        idRole = (2**31)-1
        newNameRole = 'y'*50
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertTrue( result ) 

    ### CASOS INVALIDOS( Casos Malicia )
    # Test 67: El id dado del rol a modificar es un string.
    def test_67modify_nameRoleIdString(self):        
        tempRole = clsRole()
        idRole = '1'
        newNameRole = 'rolePrueba'
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertFalse( result )    
        
    # Test 68: El id dado del rol a modificar es un numero negativo.    
    def test_68modify_nameRoleIdNegative(self):        
        tempRole = clsRole()
        idRole = -1
        newNameRole = 'rolePrueba'
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertFalse( result )   

    # Test 69: El id dado del rol a modificar es un float.
    def test_69modify_nameRoleIdFloat(self):        
        tempRole = clsRole()
        idRole = 1.0
        newNameRole = 'rolePrueba'
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertFalse( result )   
        
    # Test 70: El id dado del rol a modificar es None.         
    def test_70modify_nameRoleIdNone(self):        
        tempRole = clsRole()
        idRole = None
        newNameRole = 'rolePrueba'
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertFalse( result )   
    
    # Test 71: El nuevo nombre para el rol a modificar es un string vacio.
    def test_71modify_nameRoleNewNameIsEmpty(self):        
        tempRole = clsRole()
        idRole = 1
        newNameRole = ''
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertFalse( result )    
        
    # Test 72: El nuevo nombre para el rol a modificar es de longitu 51.    
    def test_72modify_nameRoleNewNameLen51(self):        
        tempRole = clsRole()
        idRole = 1
        newNameRole = 'r'*51
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertFalse( result )   

    # Test 73: El nuevo nombre para el rol a modificar es un numero.
    def test_73modify_nameRoleNewNameIsNumber(self):        
        tempRole = clsRole()
        idRole = 1
        newNameRole = 12345
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertFalse( result )   
        
    # Test 74: El nuevo nombre para el rol a modificar es None. 
    def test_74modify_nameRoleNewNameNone(self):        
        tempRole = clsRole()
        idRole = 1
        newNameRole = None
        result = tempRole.modify_nameRole( idRole, newNameRole )
        self.assertFalse( result )   


    #.............................................................
    #.-------------------------------------------------------------------.  
    # FUNCION ELIMINAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 75: El rol a eliminar existe en la base de datos.
    def test_75Delete_roleExist(self):
        tempRole = clsRole()
        idRoleDelete = (2**31)-1
        result = tempRole.delete_role( idRoleDelete )
        self.assertTrue(result)

    # Test 76: El rol a eliminar no existe en la base de datos.
    def test_76Delete_roleExist(self):
        tempRole = clsRole()
        idRoleDelete = (2**31)-1
        result = tempRole.delete_role( idRoleDelete )
        self.assertFalse(result)
        
    ### CASOS INVALIDOS( Casos Malicia )
    # Test 77: El id del rol a eliminar es un string.
    def test_77Delete_roleIdString(self):
        tempRole = clsRole()
        idRoleDelete = '1'
        result = tempRole.delete_role( idRoleDelete )
        self.assertFalse(result)
    
    # Test 78: El id a buscar es un float.
    def test_78Delete_roleIdFloat(self):
        tempRole = clsRole()
        idRoleDelete = 1.01
        result = tempRole.delete_role( idRoleDelete )
        self.assertFalse(result) 

    # Test 79: El id a buscar es nulo.
    def test_79Delete_roleIdNone(self):
        tempRole = clsRole()
        idRoleDelete = None
        result = tempRole.delete_role( idRoleDelete )
        self.assertFalse(result)
    
    #.-------------------------------------------------------------------.  