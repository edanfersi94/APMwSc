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
sys.path.append('../../business/access-control')
from role import clsRole

import unittest

class TestRole(unittest.TestCase):
    
    #.----------------------------------------------------.
   
    # Test 1: Se crea el objeto clsRole.
    def test1ObjectExist(self):
        tempRole = clsRole()
        self.assertIsNotNone(tempRole)
    
    #.----------------------------------------------------.
    
    # FUNCION BUSCAR.
    
    ## FUNCION: fin_IdRole
    ### CASOS VALIDOS.
    
    # Test 2: Buscar un id que exista.
    def test2find_IdRoleExist(self):
        tempRole = clsRole()
        query = tempRole.find_IdRole(idRole = 1)
        self.assertIsNotNone(query[0])

    # Test 3: Buscar un id que no exista.
    def test3find_IdRoleNotExist(self):
        tempRole = clsRole()
        query = tempRole.find_IdRole(idRole = 1000)
        self.assertEqual(query,[])    


    ### CASOS INVALIDOS.
    #### Casos Malicia.
    
    # Test 4: El id a buscar es un string.
    def test4find_IdRoleStringNumber(self):
        tempRole = clsRole()
        result = tempRole.find_IdRole('1')
        self.assertEqual(result,[])     
        
    # Test 5: El id a buscar es un numero negativo.
    def test5find_IdRoleNegative(self):
        tempRole = clsRole()
        result = tempRole.find_IdRole(-1)
        self.assertEqual(result,[])      
    
    # Test 6: El id a buscar es un float.
    def test6find_IdRoleFloat(self):
        tempRole = clsRole()
        result = tempRole.find_IdRole(1.0)
        self.assertEqual(result,[])      
    
    # Test 7: El id a buscar es nulo.
    def test7find_IdRoleNone(self):
        tempRole = clsRole()
        result = tempRole.find_IdRole(None)
        self.assertEqual(result,[])  
        
    ## FUNCION: find_NameRole
    ### CASOS VALIDOS.
    
    # Test 8: Buscar un nombre existente.
    def test8find_NameRoleExist(self):
        tempRole = clsRole()
        result = tempRole.find_NameRole('role1')
        self.assertIsNotNone(result[0])
    
    # Test 9: Buscar un nombre que no existe.    
    def test9find_NameRoleNotExist(self):
        tempRole = clsRole()
        result = tempRole.find_NameRole('role10')
        self.assertEqual(result,[])
        
    ### CASOS INVALIDOS.
    #### Casos Malicia.
    
    # Test 10: Buscar un entero como nombre.
    def test_10find_NameRoleNumber(self):
        tempRole = clsRole()
        result = tempRole.find_NameRole(1)
        self.assertEqual(result,[])
        
    # Test 11: Buscar el string vacio.    
    def test_11find_NameRoleEmptyString(self):
        tempRole = clsRole()
        result = tempRole.find_NameRole("")
        self.assertEqual(result,[])
        
    # Test 12: El nombre a buscar es None
    def test_12find_NameRoleEmpty(self):
        tempRole = clsRole()
        result = tempRole.find_NameRole(None)
        self.assertEqual(result,[])
    
    ## FUNCION: find_listIdRole.
    ### CASOS VALIDOS

    ## FUNCION: find_listNameRole.
    ### CASOS VALIDOS

    
    #.----------------------------------------------------.
    
    # FUNCION INSERTAR.
    ### CASOS VALIDOS(Interiores).
    
    # Test 13: Insertar un role que no existe.
    def test_13Insert_roleNoExist(self):
        tempRole = clsRole()
        result = tempRole.insert_role(2,'role2.0')
        self.assertTrue(result)
    
    # Test 14: Insertar un role que ya existe.
    def test_14Insert_roleExist(self):
        tempRole = clsRole()
        result = tempRole.insert_role(2,'role2.0')
        self.assertFalse(result)
    
    ### CASOS INVALIDOS(Fronteras):
    # Test 15: El id a insertar no existe pero el nombre si.
    def test_15Insert_roleIdIdNotExistNameExist(self):
        tempRole = clsRole()
        result = tempRole.insert_role(5,'role2.0')
        self.assertFalse(result)
        
    # Test 16: El id a insertar existe pero el nombre no.
    def test_16Insert_roleIdIdExistNameNotExist(self):
        tempRole = clsRole()
        result = tempRole.insert_role(2,'role2.1')
        self.assertFalse(result)
        
    def test_17Insert_roleIdExistNameLen1(self):
        tempRole = clsRole()
        result = tempRole.insert_role(10,'1')
        self.assertTrue(result)

    def test_18Insert_roleIdExistNameLen50(self):
        tempRole = clsRole()
        nameRole = 'r'*50
        result = tempRole.insert_role(11,nameRole)
        self.assertTrue(result)
        
    def test_19Insert_roleIdExistNameLen0(self):
        tempRole = clsRole()
        result = tempRole.insert_role(12,'')
        self.assertFalse(result)

    def test_20Insert_roleIdExistNameLen51(self):
        tempRole = clsRole()
        nameRole = 'r'*51
        result = tempRole.insert_role(12,nameRole)
        self.assertFalse(result)
        
    def test_21Insert_roleIdExistNameLen25(self):
        tempRole = clsRole()
        nameRole = 'r'*25
        result = tempRole.insert_role(13,nameRole)
        self.assertTrue(result)
        
    
    