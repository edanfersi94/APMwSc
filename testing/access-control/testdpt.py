"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Nicolas Manan.      Carnet: 06-39883
        Edward Fernandez.   Carnet: 10-11121
		

    DESCRIPCION: Script que contiene los casos de prueba del modulo "dpt.py"
	
"""

#------------------------------------------------------------------------------------

# Librerias a utilizar.

import os
import sys

# PATH que permite utilizar al modulo "dpt.py"
sys.path.append('../../business/access-control')
from dpt import clsDpt, session

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../data')
import model

import unittest

class TestDpt(unittest.TestCase):
    
    #.-------------------------------------------------------------------.  
    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsDpt.
    def test1ObjectExist(self):
        tempDpt = clsDpt()
        self.assertIsNotNone( tempDpt )
        session.query( model.Dpt ).delete()  # Se limpia la base de datos.
    
    #.-------------------------------------------------------------------.  
    # FUNCION BUSCAR.
    
    #.............................................................
    ## FUNCION Nº1: find_idDpt
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 2: Buscar el id de un dpt que exista. 
    def test2find_idDptExist(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdDpt = 1
        newnameDpt = 'dptprobando1'
        newDpt = model.Dpt(newIdDpt, newnameDpt) 
        session.add(newDpt)
        session.commit()   
        
        tempDpt = clsDpt()
        idDpt = 1
        query = tempDpt.find_idDpt( idDpt )
        self.assertIsNotNone( query[0] )
    
    # Test 3: Buscar el id de un dpt que no exista.
    def test3find_idDptNotExist(self):
        tempDpt = clsDpt()
        idDpt = 1000
        query = tempDpt.find_idDpt( idDpt )
        self.assertEqual(query,[])
    
    ### CASOS INVALIDOS( Casos Malicia )
    # Test 4: El id del dpt a buscar es un string.
    def test4find_idDptString(self):
        tempDpt = clsDpt()
        idDpt = '1'
        query = tempDpt.find_idDpt( idDpt )
        self.assertEqual(query,[])
    
    # Test 5: El id del dpt a buscar es de tipo float.
    def test5find_idDptFloat(self):
        tempDpt = clsDpt()
        idDpt = 1.01
        query = tempDpt.find_idDpt( idDpt )
        self.assertEqual(query,[])  

    # Test 6: El id del dpt a buscar es nulo.
    def test6find_idDptNone(self):
        tempDpt = clsDpt()
        idDpt = None
        query = tempDpt.find_idDpt( idDpt )
        self.assertEqual(query,[])  
    
    #.............................................................
    ## FUNCION Nº2: find_nameDpt
    ### CASOS VALIDOS( Casos Interiores ).
    
    # Test 7: Buscar el nombre de un dpt existente.
    def test7find_nameDptExist(self):
        tempDpt = clsDpt()
        nameDpt = 'dptprobando1'
        query = tempDpt.find_nameDpt( nameDpt )
        self.assertIsNotNone(query[0])
    
    # Test 8: Buscar el nombre de un dpt que no existe.    
    def test8find_nameDptNotExist(self):
        tempDpt = clsDpt()
        nameDpt = 'dpt10'
        query = tempDpt.find_nameDpt( nameDpt )
        self.assertEqual(query,[])    
    
    ### CASOS INVALIDOS( Casos Malicia )
    # Test 9: Buscar un entero como nombre de un dpt.
    def test_9find_nameDptNumber(self):
        tempDpt = clsDpt()
        nameDpt = 1
        query = tempDpt.find_nameDpt( nameDpt )
        self.assertEqual(query,[])
        
    # Test 10: Buscar el string vacio como nombre de un dpt.
    def test_10find_nameDptEmptyString(self):
        tempDpt = clsDpt()
        nameDpt = ""
        query = tempDpt.find_nameDpt( nameDpt )
        self.assertEqual(query,[])
        
    # Test 11: Buscar el elemento nulo como nombre de un dpt.
    def test_11find_nameDptEmpty(self):
        tempDpt = clsDpt()
        nameDpt = None
        query = tempDpt.find_nameDpt( nameDpt )
        self.assertEqual(query,[])   
        
    #.............................................................
    ## FUNCION Nº3: find_listIdDpt
    ### CASOS VALIDOS( Casos Interiores ).
    
    # Test 12: Se buscan los id de los dpts que se encuentran en la
    #          base de datos y dicha base se encuentra vacia.
    def test_12find_listIdDptEmptyBase(self):
        session.query(model.Dpt).delete()  # Se limpia la base de datos.
        tempDpt = clsDpt()
        query = tempDpt.find_listIdDpt()
        self.assertEqual(query,[])  
    
    # Test 13: Se buscan los id de los dpts que se encuentran en la
    #          base de datos y dicha base tiene una sola tupla.
    def test_13find_listIdDptOneTuple(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdDpt = 50
        newNameDpt = 'dpt50'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()      
                                
        tempDpt = clsDpt()
        query = tempDpt.find_listIdDpt()
        self.assertTrue( query[0].id == 50 )  
    
    # Test 14: Se buscan los id de los dpts que se encuentran en la
    #          base de datos y dicha base tiene al menos dos tuplas.
    def test_14find_listIdDptAlmost2Tuples(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdDpt = 51
        newNameDpt = 'dpt51.0'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add( newDpt )
        session.commit()      
                                
        tempDpt = clsDpt()
        query = tempDpt.find_listIdDpt()
        resultEsp = [(50,),(51,)]
        self.assertTrue( query[:-1] == resultEsp[:-1] )      

    #.............................................................
    ## FUNCION Nº4: find_listNameDpt
    ### CASOS VALIDOS( Casos Interiores ).
    
    # Test 15: Se buscan los nombres de los dpts que se encuentran en la
    #          base de datos y dicha base se encuentra vacia.
    def test_15find_listNameDptEmptyBase(self):
        session.query(model.Dpt).delete()  # Se limpia la base de datos.
        tempDpt = clsDpt()
        query = tempDpt.find_listNameDpt()
        self.assertEqual(query,[])  
    
    # Test 16: Se buscan los nombres de los dpts que se encuentran en la
    #          base de datos y dicha base tiene una sola tupla.
    def test_16find_listNameDptOneTuple(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdDpt = 50
        newNameDpt = 'dpt50'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add( newDpt )
        session.commit()      
                                
        tempDpt = clsDpt()
        query = tempDpt.find_listNameDpt()
        self.assertTrue( query[0].name == 'dpt50' )  
    
    # Test 17: Se buscan los nombres de los dpts que se encuentran en la
    #          base de datos y dicha base tiene al menos dos tuplas.
    def test_17find_listNameDptAlmost2Tuples(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdDpt = 51
        newNameDpt = 'dpt51'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()      
                                
        tempDpt = clsDpt()
        query = tempDpt.find_listNameDpt()
        resultEsp = [('dpt50',),('dpt51',)]
        self.assertTrue( query[:-1] == resultEsp[:-1] )   
    
    #.............................................................
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 18: Insertar un dpt que no existe.
    def test_18insert_dptNoExist(self):
        session.query(model.Dpt).delete()  # Se limpia la base de datos.
        tempDpt = clsDpt()
        newIdDpt = 2
        newNameDpt = 'dpt2.0'
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertTrue(result)
    
    # Test 19: Insertar un dpt que ya existe.
    def test_19insert_dptExist(self):
        tempDpt = clsDpt()
        newIdDpt = 2
        newNameDpt = 'dpt2.0'
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertFalse(result)
        
    # Test 20: El id del dpt a insertar no existe pero el nombre si.
    def test_20insert_dptIdNotExistNameExist(self):
        tempDpt = clsDpt()
        newIdDpt = 20
        newNameDpt = 'dpt2.0'
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertFalse(result)
        
    # Test 21: El id del dpt a insertar existe pero el nombre no.
    def test_21insert_dptIdExistNameNotExist(self):
        tempDpt = clsDpt()
        newIdDpt = 2
        newNameDpt = 'dptDePrueba'
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertFalse(result)
    
    ### CASOS VALIDOS( Casos Fronteras )
    # Test 22: Se insertara un dpt que no existe en la base de datos y
    #          el tam del nombre es igual a 1.
    def test_22insert_dptIdNoExistNameLen1(self):
        tempDpt = clsDpt()
        newIdDpt = 10
        newNameDpt = '1'
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertTrue(result)

    # Test 23: Se insertara un dpt que no existe en la base de datos y
    #          el tam del nombre es igual a 50.
    def test_23insert_dptIdNoExistNameLen50(self):
        tempDpt = clsDpt()
        newIdDpt = 11
        newnameDpt = 'r'*50
        result = tempDpt.insert_dpt( newIdDpt, newnameDpt )
        self.assertTrue(result)
        
    # Test 24: Se insertara un dpt que no existe en la base de datos y
    #          el id del mismo es igual a 1 (menor valor posible).
    def test_24insert_dptIdNoExistIqualOne(self):
        tempDpt = clsDpt()
        newIdDpt = 1
        newNameDpt = 'dpt1'
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertTrue(result)
        
    # Test 25: Se insertara un dpt que no existe en la base de datos y
    #          el id del mismo es un numero muy grande.
    def test_25insert_dptIdNoExistIqualBigNumber(self):
        tempDpt = clsDpt()
        newIdDpt = (2**31)-1
        newNameDpt = 'dptBig'
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertTrue(result)
        
    ### CASOS VALIDOS( Casos Esquinas )
    # Test 26: Se insertara un dpt que no existe en la base de datos.
    #          El id del mismo es igual a 1 y su nombre es de longitud
    #          igual a 1.
    def test_26insert_dptIdNoExistIqual1NameLen1(self):
        session.query(model.Dpt).delete()  # Se limpia la base de datos.
        tempDpt = clsDpt()
        newIdDpt = 1
        newNameDpt = 'r'
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertTrue(result)
        
    # Test 27: Se insertara un dpt que no existe en la base de datos.
    #          El id del mismo es igual a 1 y su nombre es de longitud
    #          igual a 50.
    def test_27insert_dptIdNoExistIqual1NameLen50(self):
        session.query(model.Dpt).delete()  # Se limpia la base de datos.
        tempDpt = clsDpt()
        newIdDpt = 1
        newNameDpt = 'r'*50
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertTrue(result)

    # Test 28: Se insertara un dpt que no existe en la base de datos.
    #          El id del mismo es igual a (2**31)-1 y su nombre es de
    #          longitud igual a 1.
    def test_28insert_dptIdNoExistIqualBigNumberNameLen1(self):
        session.query(model.Dpt).delete()  # Se limpia la base de datos.
        tempDpt = clsDpt()
        newIdDpt = (2**31)-1
        newNameDpt = 'r'
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertTrue(result)

    # Test 29: Se insertara un dpt que no existe en la base de datos.
    #          El id del mismo es igual a (2**31)-1 y su nombre es de
    #          igual a 50.
    def test_29insert_dptIdNoExistIqualBigNumberNameLen50(self):
        session.query(model.Dpt).delete()  # Se limpia la base de datos.
        tempDpt = clsDpt()
        newIdDpt = (2**31)-1
        newNameDpt = 'r'*50
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertTrue(result)
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    # Test 30: El id del dpt a insertar es valido pero el nombre es 
    #          la cadena vacia.
    def test_30insert_dptIdNoExistNameLen0(self):
        tempDpt = clsDpt()
        newIdDpt = 25
        newNameDpt = ''
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertFalse(result)

    # Test 31: El id del dpt a insertar es valido pero el nombre es
    #          una cadena de 51 caracteres.
    def test_31insert_dptIdNoExistNameLen51(self):
        tempDpt = clsDpt()
        newIdDpt = 25
        newNameDpt = 'r'*51
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertFalse(result)

    # Test 32: El id del dpt a insertar es valido pero el nombre es 
    #          un numero.
    def test_32insert_dptIdNoExistNameNumber(self):
        tempDpt = clsDpt()
        newIdDpt = 25
        newNameDpt = 123456
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertFalse(result)

    # Test 33: El id del dpt a insertar es un numero negativo.
    def test_33insert_dptIdNegative(self):
        tempDpt = clsDpt()
        newIdDpt = -25
        newNameDpt = 'dptDePrueba'
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertFalse(result)
        
    # Test 34: El id del dpt a insertar es un string.
    def test_34insert_dptIdString(self):
        tempDpt = clsDpt()
        newIdDpt = '25'
        newNameDpt = 'dptDePrueba'
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertFalse(result)
        
    # Test 35: El id del dpt a insertar es un float.
    def test_35insert_dptIdFloat(self):
        tempDpt = clsDpt()
        newIdDpt = 25.01
        newNameDpt = 'dptDePrueba'
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertFalse(result)
 
    # Test 36: El id del dpt a insertar es None.
    def test_36insert_dptIdNone(self):
        tempDpt = clsDpt()
        newIdDpt = None
        newNameDpt = 'dptDePrueba'
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertFalse(result)

    #.............................................................

    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    #.............................................................
    ## FUNCION Nº1: modify_idDpt

    ### CASOS VALIDOS( Casos Interiores ).
    # Test 37: El id del dpt a modificar existe en la base de datos y el
    #          nuevo id se encuentra disponible.
    def test_37modify_idDptOldIdExistNewIdAvailable(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdDpt = 51
        newNameDpt = 'dpt51'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()      
        
        tempDpt = clsDpt()
        oldIdDpt = 51
        newIdDpt = 15
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertTrue( result )
 
    # Test 38: El id del dpt a modificar existe en la base de datos y el
    #          nuevo id no se encuentra disponible.
    def test_38modify_idDptOldIdExistNewIdNotAvailable(self):
        tempDpt = clsDpt()
        oldIdDpt = 15
        newIdDpt = (2**31)-1
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertFalse( result )

    # Test 39: El id del dpt a modificar no existe en la base de datos 
    #          pero el nuevo id se encuentra disponible.
    def test_39modify_idDptOldIdNotExistNewIdAvailable(self):
        tempDpt = clsDpt()
        oldIdDpt = 111
        newIdDpt = 9
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertFalse( result )        
        
    # Test 40: El id del dpt a modificar no existe en la base de datos 
    #          y el nuevo id no se encuentra disponible.
    def test_40modify_idDptOldIdNotExistNewIdNotAvailable(self):
        tempDpt = clsDpt()
        oldIdDpt = 111
        newIdDpt = 15
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertFalse( result )        

    ### CASOS VALIDOS( Casos Fronteras )           
    # Test 41: El id del dpt a modificar existe en la base de datos y su
    #          valor es igual a 1. El nuevo id se encuentra disponible.
    def test_41modify_idDptOldIdExistIqual1NewIdAvailable(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdDpt = 1
        newNameDpt = 'dptDePrueba1'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit() 
        
        tempDpt = clsDpt()
        oldIdDpt = 1
        newIdDpt = 150
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertTrue( result )     
    
    # Test 42: El id del dpt a modificar existe en la base de datos y su
    #          valor es muy grande. El nuevo id se encuentra disponible.
    def test_42modify_idDptOldIdExistIqualBigNumberNewIdAvailable(self):
        tempDpt = clsDpt()
        oldIdDpt = (2**31)-1
        newIdDpt = 200
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertTrue( result )     
    
    # Test 43: El id del dpt a modificar existe en la base de datos. El
    #          nuevo id se encuentra disponible y es igual a 1.
    def test_43modify_idDptOldIdExistNewIdAvailableIqual1(self):
        tempDpt = clsDpt()
        oldIdDpt = 150
        newIdDpt = 1
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertTrue( result )      
    
    # Test 44: El id del dpt a modificar existe en la base de datos. El
    #          nuevo id se encuentra disponible y su valor es muy grande.    
    def test_44modify_idDptOldIdExistNewIdAvailableIqualBigNumber(self):
        tempDpt = clsDpt()
        oldIdDpt = 200
        newIdDpt = (2**31)-1
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertTrue( result )  

    ### CASOS VALIDOS( Casos Esquinas )  
    # Test 45: El id del dpt a modificar existe en la base de datos y su
    #          valor es muy grande. El nuevo id se encuentra disponible y
    #          su valor es igual a 1.
    def test_45modify_idDptOldIdExistIqualBigNumberNewIdAvailableIqual1(self):
        session.query(model.Dpt).delete()  # Se limpia la base de datos.
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdDpt = (2**31)-1
        newNameDpt = 'dptDePrueba1'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit() 
        
        tempDpt = clsDpt()
        oldIdDpt = (2**31)-1
        newIdDpt = 1
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertTrue( result )  
    
    
    # Test 46: El id del dpt a modificar existe en la base de datos y su
    #          valor es igual a 1. El nuevo id se encuentra disponible
    #          y su valor es muy grande.
    def test_46modify_idDptOldIdExistIqual1NewIdAvailable(self):        
        tempDpt = clsDpt()
        oldIdDpt = 1
        newIdDpt = (2**31)-1
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertTrue( result )  
        
    ### CASOS INVALIDOS( Casos Malicia ):
    # Test 47: El id dado del dpt a modificar es un string.
    def test_47modify_idDptOldIdString(self):        
        tempDpt = clsDpt()
        oldIdDpt = '1'
        newIdDpt = 156
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertFalse( result )  
        
    # Test 48: El id dado del dpt a modificar es un numero negativo.    
    def test_48modify_idDptOldIdNumberNegative(self):        
        tempDpt = clsDpt()
        oldIdDpt = -1
        newIdDpt = (2**31)-1
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertFalse( result )  
        
    # Test 49: El id dado del dpt a modificar es un float.
    def test_49modify_idDptOldIdIqualFloat(self):        
        tempDpt = clsDpt()
        oldIdDpt = 1.0
        newIdDpt = (2**31)-1
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertFalse( result )  
        
    # Test 50: El id dado del dpt a modificar es None.         
    def test_50modify_idDptOldIdIqualNone(self):        
        tempDpt = clsDpt()
        oldIdDpt = None
        newIdDpt = (2**31)-1
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertFalse( result )  
        
    # Test 51: El nuevo id para el dpt a modificar es un string.
    def test_51modify_idDptOldIdExistNewIdString(self):        
        tempDpt = clsDpt()
        oldIdDpt = 1
        newIdDpt = '(2**31)-1'
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertFalse( result )  
        
    # Test 52: El nuevo id para el dpt a modificar es un numero negativo.    
    def test_52modify_idDptOldIdExistNewIdNegative(self):        
        tempDpt = clsDpt()
        oldIdDpt = 1
        newIdDpt = -20
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertFalse( result )  
        
    # Test 53: El nuevo id para el dpt a modificar es un float.
    def test_53modify_idDptOldIdExistNewIdFloat(self):        
        tempDpt = clsDpt()
        oldIdDpt = 1
        newIdDpt = 20.01
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertFalse( result )  
        
    # Test 54: El nuevo id para el dpt a modificar es None. 
    def test_54modify_idDptOldIdExistNewIdNone(self):        
        tempDpt = clsDpt()
        oldIdDpt = 1
        newIdDpt = None
        result = tempDpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertFalse( result )   
   
   #.............................................................     
    ## FUNCION Nº2: modify_nameDpt

    ### CASOS VALIDOS( Casos Interiores ).
    # Test 55: El id del dpt a modificar existe en la base de datos y el
    #          nuevo nombre se encuentra disponible.
    def test_55modify_nameDptIdExistNewNameAvailable(self):
        session.query(model.Dpt).delete()  # Se limpia la base de datos.
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdDpt = 3
        newNameDpt = 'dptDePrueba1'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit() 
        
        tempDpt = clsDpt()
        idDpt = 3
        newNameDpt = 'dptDePruebaX'
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result )         
    
    # Test 56: El id del dpt a modificar existe en la base de datos y el
    #          nuevo nombre no se encuentra disponible.
    def test_56modify_nameDptIdExistNewNameNoAvailable(self):
        tempDpt = clsDpt()
        idDpt = 3
        newNameDpt = 'dptDePruebaX'
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertFalse( result )  
    
    # Test 57: El id del dpt a modificar no existe en la base de datos 
    #          pero el nuevo nombre se encuentra disponible.
    def test_57modify_nameDptIdNoExistNewNameAvailable(self):
        tempDpt = clsDpt()
        IdDpt = 20
        newnameDpt = 'dptDePruebaX2'
        result = tempDpt.modify_nameDpt( IdDpt, newnameDpt )
        self.assertFalse( result ) 
    
    # Test 58: El id del dpt a modificar no existe en la base de datos 
    #          y el nuevo nombre no se encuentra disponible.
    def test_58modify_nameDptIdNoExistNewNameNoAvailable(self):
        tempDpt = clsDpt()
        idDpt = 20
        newNameDpt = 'dptDePruebaX'
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertFalse( result )  
    
    ### CASOS VALIDOS( Casos Fronteras )
    # Test 59: El id del dpt a modificar existe en la base de datos y su
    #          valor es igual a 1. El nuevo nombre se encuentra disponible.
    def test_59modify_nameDptIdExistIqual1NewNameAvailable(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida. 
        newIdDpt = 1
        newNameDpt = 'dptPruebaCaso1'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit() 
        
        tempDpt = clsDpt()
        idDpt = 1
        newNameDpt = 'dptDePruebaX3'
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result ) 

    # Test 60: El id del dpt a modificar existe en la base de datos y su
    #          valor es un numero muy grande. El nuevo nombre se encuentra disponible.     
    def test_60modify_nameDptIdExistIqualBigNumberNewNameAvailable(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida. 
        newIdDpt = (2**31)-1
        newNameDpt = 'dptDePruebaCasoBig'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit() 

        tempDpt = clsDpt()
        idDpt = (2**31)-1
        newNameDpt = 'dptDePruebaXBig'
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result )  
    
    # Test 61: El id del dpt a modificar existe en la base de datos. El nuevo 
    #          nombre se encuentra disponible y es de largo 1.
    def test_61modify_nameDptIdExistNewNameAvailableLen1(self):
        tempDpt = clsDpt()
        idDpt = 3
        newNameDpt = '1'
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result )  
    
    # Test 62: El id del dpt a modificar existe en la base de datos. El nuevo 
    #          nombre se encuentra disponible y es de largo 50.
    def test_62modify_nameDptIdExistNewNameAvailableLen50(self):
        tempDpt = clsDpt()
        idDpt = 3
        newNameDpt = 'x'*50
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result )  
    
    ### CASOS VALIDOS( Casos Esquinas )
    # Test 63: El id del dpt a modificar existe en la base de datos y su valor es
    #          igual a 1. El nuevo nombre es valido y su longitud es igual a 1.
    def test_63modify_nameDptIdExistIqual1NewNameAvailableLen1(self):
        tempDpt = clsDpt()
        idDpt = 1
        newNameDpt = 'z'
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result ) 
    
    # Test 64: El id del dpt a modificar existe en la base de datos y su valor es
    #          igual a 1. El nuevo nombre es valido y su longitud es igual a 50.
    def test_64modify_nameDptIdExistIqual1NewNameAvailableLen50(self):
        tempDpt = clsDpt()
        idDpt = 1
        newNameDpt = 'z'*50
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result ) 
            
    # Test 65: El id del dpt a modificar existe en la base de datos y su valor es
    #          un numero muy grande. El nuevo nombre es valido y su longitud es igual a 1.
    def test_65modify_nameDptIdExistIqualBigNumberNewNameAvailableLen1(self):
        tempDpt = clsDpt()
        idDpt = (2**31)-1
        newNameDpt = 'y'
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result ) 

    # Test 66: El id del dpt a modificar existe en la base de datos y su valor es
    #          un numero muy grande. El nuevo nombre es valido y su longitud es igual a 50.
    def test_66modify_nameDptIdExistIqualBigNumberNewNameAvailableLen50(self):
        tempDpt = clsDpt()
        idDpt = (2**31)-1
        newNameDpt = 'y'*50
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result ) 

    ### CASOS INVALIDOS( Casos Malicia )
    # Test 67: El id dado del dpt a modificar es un string.
    def test_67modify_nameDptIdString(self):        
        tempDpt = clsDpt()
        idDpt = '1'
        newNameDpt = 'dptPrueba'
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertFalse( result )    
        
    # Test 68: El id dado del dpt a modificar es un numero negativo.    
    def test_68modify_nameDptIdNegative(self):        
        tempDpt = clsDpt()
        idDpt = -1
        newNameDpt = 'dptPrueba'
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertFalse( result )   

    # Test 69: El id dado del dpt a modificar es un float.
    def test_69modify_nameDptIdFloat(self):        
        tempDpt = clsDpt()
        idDpt = 1.0
        newNameDpt = 'dptPrueba'
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertFalse( result )   
        
    # Test 70: El id dado del dpt a modificar es None.         
    def test_70modify_nameDptIdNone(self):        
        tempDpt = clsDpt()
        idDpt = None
        newNameDpt = 'dptPrueba'
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertFalse( result )   
    
    # Test 71: El nuevo nombre para el dpt a modificar es un string vacio.
    def test_71modify_nameDptNewNameIsEmpty(self):        
        tempDpt = clsDpt()
        idDpt = 1
        newNameDpt = ''
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertFalse( result )    
        
    # Test 72: El nuevo nombre para el dpt a modificar es de longitu 51.    
    def test_72modify_nameDptNewNameLen51(self):        
        tempDpt = clsDpt()
        idDpt = 1
        newNameDpt = 'r'*51
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertFalse( result )   

    # Test 73: El nuevo nombre para el dpt a modificar es un numero.
    def test_73modify_nameDptNewNameIsNumber(self):        
        tempDpt = clsDpt()
        idDpt = 1
        newNameDpt = 12345
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertFalse( result )   
        
    # Test 74: El nuevo nombre para el dpt a modificar es None. 
    def test_74modify_nameDptNewNameNone(self):        
        tempDpt = clsDpt()
        idDpt = 1
        newNameDpt = None
        result = tempDpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertFalse( result )   


    #.............................................................
    #.-------------------------------------------------------------------.  
    # FUNCION ELIMINAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 75: El dpt a eliminar existe en la base de datos.
    def test_75delete_dptExist(self):
        tempDpt = clsDpt()
        idDptDelete = (2**31)-1
        result = tempDpt.delete_dpt( idDptDelete )
        self.assertTrue( result )

    # Test 76: El dpt a eliminar no existe en la base de datos.
    def test_76delete_dptNoExist(self):
        tempDpt = clsDpt()
        idDptDelete = (2**31)-1
        result = tempDpt.delete_dpt( idDptDelete )
        self.assertFalse( result )
        
    ### CASOS INVALIDOS( Casos Malicia )
    # Test 77: El id del dpt a eliminar es un string.
    def test_77delete_dptIdString(self):
        tempDpt = clsDpt()
        idDptDelete = '1'
        result = tempDpt.delete_dpt( idDptDelete )
        self.assertFalse( result )
    
    # Test 78: El id del dpt a eliminar es un float.
    def test_78delete_dptIdFloat(self):
        tempDpt = clsDpt()
        idDptDelete = 1.01
        result = tempDpt.delete_dpt( idDptDelete )
        self.assertFalse( result ) 

    # Test 79: El id del dpt a eliminar es None.
    def test_79delete_dptIdNone(self):
        tempDpt = clsDpt()
        idDptDelete = None
        result = tempDpt.delete_dpt( idDptDelete )
        self.assertFalse( result )
    
    #.-------------------------------------------------------------------.  