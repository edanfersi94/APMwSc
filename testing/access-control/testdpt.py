import unittest
from dpt import *

class testdpt (unittest.TestCase):


	#.----------------------------------------------------.
	# Verificacion de la clase

	#Test 1: Verifica que se cree el objeto de la clase clsDpt
	def test1_objectExist(self):
		dpt = clsDpt()
		self.assertIsInstance(dpt,clsDpt)


	#.----------------------------------------------------.
	## Funcion find_idDpt
	### Casos Validos (Casos Interiores)

	#Test2: Busqueda de un id existente
	def test2_find_idDptExist(self):
		dpt = clsDpt()
		result = dpt.find_idDpt(2)
		self.assertIsNotNone(result[0])

	#Test3: Busqueda de un id inexistente o en una lista vacia
	def test3_find_idDptNotExist(self):
		dpt = clsDpt()
		result = dpt.find_idDpt(38)
		self.assertEqual(result,[])


	### CasosInvalidos (Casos Malicia)

	#Test4: Busqueda de un tipo de dato invalido 'String'
	def test4_find_idDptString(self):
		dpt = clsDpt()
		result = dpt.find_idDpt('4')
		self.assertEqual(result, [])

    #Test5: Busqueda de un tipo de dato inexistente 'numero real'
	def test5_find_idDptFloat(self):
		dpt = clsDpt()
		result = dpt.find_idDpt(1.0)
		self.assertEqual(result, [])

    #Test6: Error de parametros en la funcion
	def test6_find_idDptNone(self):
		dpt = clsDpt()
		result = dpt.find_idDpt(None)
		self.assertEqual(result, [])


 	#.............................................................
	## Funcion: find_nameDpt
    ### Casos Validos (Casos Interiores)

    #Test7: Busqueda de un nombre existente
	def test7_find_nameDptExist(self):
		dpt = clsDpt()
		result = dpt.find_nameDpt('dpt1')
		self.assertIsNotNone(result[0])

    #Test8: Busqueda de un nombre inexistente
	def test8_find_nameDptNotExist(self):
		dpt = clsDpt()
		result = dpt.find_nameDpt('dpt9')
		self.assertEqual(result,[])


	### Casos invalidos (Casos Malicia)

	#Test9: Busqueda de un tipo de dato invalido 'entero'
	def test9_find_nameDptInteger(self):
		dpt = clsDpt()
		result = dpt.find_nameDpt(1)
		self.assertEqual(result, [])

	#Test10: Buscar un String vacio
	def test_10find_nameDptEmptyString(self):
		dpt = clsDpt()
		result = dpt.find_nameDpt('')
		self.assertEqual(result, [])

	#Test11: Error de parametros en la funcion
	def test_11find_nameDptNone(self):
		dpt = clsDpt()
		result = dpt.find_nameDpt(None)
		self.assertEqual(result, [])



	## Funcion: find_listIdDpt
	### Casos validos(Casos interiores)

    # Test 12: Se buscan los id que se encuentran en la
    #          base de datos y dicha base se encuentra vacia.
    def test_12find_listIdDptEmptyBase(self):
    	#Se limpia la base de datos
        session.query(model.Dpt).delete() 
        dpt = clsDpt()
        result = dpt.find_listIdDpt()
        self.assertEqual(result,[])  

    # Test 13: Se buscan los id que se encuentran en la
    #          base de datos y dicha base tiene una sola tupla.
    def test_13find_listIdDptOneTuple(self):
        # Se inserta un elemento valido en la base
        newIdDpt = 50
        newNameDpt = 'dpt50'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()      
                                
        dpt = clsDpt()
        result = dpt.find_listIdDpt()
        self.assertTrue( result[0].id == 50 )  
    
    # Test 14: Se buscan los id que se encuentran en la
    #          base de datos y dicha base tiene al menos dos tuplas.
    def test_14find_listIdDptAlmost2Tuples(self):
        # Se inserta un elemento valido en la base.
        newIdDpt = 51
        newNameDpt = 'dpt51.0'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()      
                                
        dpt = clsDpt()
        result = dpt.find_listIdDpt()
        resultEsp = [(50,),(51,)]
        self.assertTrue( result[:-1] == resultEsp[:-1] )      


    #.............................................................
    ## Funcion find_listNamedDpt
    ### Casos validos( Casos Interiores ).
    
    # Test 15: Se buscan los nombres de dpt que se encuentran en la
    #          base de datos y dicha base se encuentra vacia.
    def test_15find_listNameDptEmptyBase(self):
    	# Se limpia la base de datos
        session.query(model.Dpt).delete()  
        dpt = clsDpt()
        result = dpt.find_listNameDpt()
        self.assertEqual(result,[])  
    
    # Test 16: Se buscan los nombres de dpt que se encuentran en la
    #          base de datos y dicha base tiene una sola tupla.
    def test_16find_listNameDptOneTuple(self):
        # Se inserta un elemento valido en la base.
        newIdDpt = 50
        newNameDpt = 'dpt50'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()      
                                
        dpt = clsDpt()
        result = dpt.find_listNameDpt()
        self.assertTrue( result[0].name == 'dpt50' )  
    
    # Test 17: Se buscan los nombres de dpt que se encuentran en la
    #          base de datos y dicha base tiene al menos dos tuplas.
    def test_17find_listNameDptAlmost2Tuples(self):
        # Se inserta un elemento valido en la base. 
        newIdDpt = 51
        newNameDpt = 'dpt51'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()      
                                
        dpt = clsDpt()
        result = dpt.find_listNameDpt()
        resultEsp = [('dpt50',),('dpt51',)]
        self.assertTrue( result[:-1] == resultEsp[:-1] )  


    #.-------------------------------------------------------------------.  
    
    # Funcion Insertar
    
    ### Casos Validos( Casos Interiores ).
    
    # Test 18: Insertar un Id que no existe con su nombre.
	def test_18insert_dptNoExist(self):
		#Se limpia la base de datos
		session.query(model.Dpt)delete()
		dpt = clsDpt()
		newIdDpt = 4
		newNameDpt = 'dpt4'
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertTrue(result)


	#Test19: Insertar un id y nombre existente
	def test_19insert_dptExist(self):
		dpt = clsDpt()
		newIdDpt = 4
		newNameDpt = 'dpt4'
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertTrue(result)

	#Test20: Insertar un nombre existente y un id inexistente
	def test_20insert_dptNoExistsNameExist(self):
		dpt = clsDpt()
		newIdDpt = 8
		newNameDpt = 'dpt4'
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertFalse(result)

	#Test21: Insertar un nombre inexistente y un id existente
	def test_21insert_dptIdExistNameNoExist(self):
		dpt = clsDpt()
		newIdDpt = 4
		newNameDpt = 'dpt8'
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertFalse(result)


	### Casos Frontera
	
	#Test22: Se inserta un id nuevo en la base de datos
	#		 y el tamaño del nombreDpt es de longitud 1
	def test_22insert_dptIdNoExistNameLen1(self):
		dpt = clsDpt()
		newIdDpt = 5
		newNameDpt = 'a'
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertTrue(result)

	#Test23: Se inserta un id nuevo en la base de datos 
	#        y el tamaño del nombreDpt es de longitud igual a 50
	def test_23insert_dptIdNoExistNameLen50(self): 
		dpt = clsDpt()
		newIdDpt = 5
		newNameDpt = 'lebasiocin'*5
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertTrue(result)

	#Test24: Se inserta un id con el menor valor posible
	def test_24insert_dptIdNoExistEqualOne(self):
		dpt = clsDpt()
		newIdDpt = 1
		newNameDpt = 'dpt1'
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertTrue(result)

	#Test25: Se inserta un id con el mayor valor posible
	def test_25insert_dptIdNoExistBigNumber(self):
		dpt = clsDpt()
		newIdDpt = (2**31)-1
		newNameDpt = 'dpt1'
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertTrue(result)


	### CasosEsquinas

	#Test26: Se inserta un id con el menor valor posible y 
	# 		 nombre de dpto con longitud igual a 1
	def test_26insert_dptIdNoExistEqual1NameLen1(self):
		#Se limpia la base de datos
		session.query(model.Dpto).delete()
		dpt = clsDpt()
		newIdDpt = 1
		newNameDpt = 'a'
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertTrue(result)

	#Test27: Se inserta un id con el menor valor posible y 
	#	 	 nombre de dpto de longitud maxima
	def test_27insert_dptIdNoExistEqual1NameLen50(self):
		#Se limpia la base de datos
		session.query(model.Dpto).delete()
		dpt = clsDpt()
		newIdDpt = 1
		newNameDpt = 'lebasiocin'*5
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertTrue(result)

	#Test28: Se inserta un id nuevo con mayor valor posible
	#	     y nombreDpt de longitud minima
	def test_28insert_dptIdNoExistBigNumberNameLen1(self):
		#Se limpia la base de datos
		session.query(model.Dpto).delete()
		dpt = clsDpt()
		newIdDpt = (2**31)-1
		newNameDpt = 'a'
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertTrue(result)

	#Test29: Se inserta un id nuevo con mayor valor posible
	#		 y nombreDpt de longitud maxima
	def test_29insert_dptIdNoExistBigNumberNameLen50(self):
		#Se limpia la base de datos
		session.query(model.Dpto).delete()
		dpt = clsDpt()
		newIdDpt = (2**31)-1
		newNameDpt = 'lebasiocin'*5
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertTrue(result)


	
	## Casos invalidos (Casos Malicia)

	#Test30: El id a insertar es valido pero el nombreDpt es vacio
	def test_30insert_dptIdNoExistNameLen0(self):
		dpt = clsDpt()
		newIdDpt = 25
		newNameDpt = ''
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertFalse(result)

	#Test31: El id a insertar es valido pero el nombreDpt es una cadena
	#	 	 de 51 caracteres
	def test_31insert_dptIdNoExistsNameLen51(self):
		dpt = clsDpt()
		newIdDpt = 25
		newNameDpt = 'n'*51
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertFalse(result)		

	#Test32: El id a insertar es valido y el nombreDpt es un entero
	def test_32insert_dptIdNoExistNameNumber(self):
		dpt = clsDpt()
		newIdDpt = 25
		newNameDpt = 1
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertFalse(result)

	#Test33: El id a insertar es un numero negativo
	def test_33insert_dptIdNegative(self):
		dpt = clsDpt()
		newIdDpt = -2
		newNameDpt = 'dptPrueba'
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertFalse(result)

	#Test34: El id a insertar es un string y el nombreDpt es valido
	def test_34insert_dptIdString(self):
		dpt = clsDpt()
		newIdDpt = '25'
		newNameDpt = 'dpt9'
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertFalse(result)

	#Test35: El id a insertar es un numero real
	def test_35insert_dptIdFloat(self):
		dpt = clsDpt()
		newIdDpt = 25.6
		newNameDpt = 'dpt4'
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertFalse(result)

	#Test30: El id a insertar es None
	def test_36insert_dptIdNone(self):
		dpt = clsDpt()
		newIdDpt = None
		newNameDpt = 'dpto5'
		result = dpt.insert_dpt(newIdDpt,newNameDpt)
		self.assertFalse(result)


	#.----------------------------------------------------.

	# Funcion modificar.

    ### Casos Validos( Casos Interiores ).
    # Test 37: El id del dpt a modificar existe en la base de datos
    #          y el nuevo id se encuentra disponible.
    def test_37modify_idDptOldIdExistNewIdAvailable(self):
        # Se inserta un elemento valido en la base
        newIdDpt = 51
        newNameDpt = 'dpt51'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit()      
        
        dpt = clsDpt()
        oldIdDpt = 51
        newIdDpt = 15
        result = dpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertTrue( result )

    # Test 38: El id del dpt a modificar existe en la base de datos 
    #          y el nuevo id no se encuentra disponible.
    def test_38modify_idDptOldIdExistNewIdNotAvailable(self):
        dpt = clsDpt()
        oldIdDpt = 15
        newIdDpt = (2**31)-1
        result = dpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertFalse( result )

    # Test 39: El id del dpt a modificar no existe en la base de datos 
    #          pero el nuevo id se encuentra disponible.
    def test_39modify_idDptOldIdNotExistNewIdAvailable(self):
        dpt = clsDpt()
        oldIdDpt = 111
        newIdDpt = 9
        result = dpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertFalse( result )        
        
    # Test 40: El id del dpt a modificar no existe en la base de datos 
    #          y el nuevo id no se encuentra disponible.
    def test_40modify_idDptOldIdNotExistNewIdNotAvailable(self):
        dpt = clsDpt()
        oldIdDpt = 111
        newIdDpt = 15
        result = dpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertFalse( result )        


    ### Casos Validos( Casos Fronteras )  

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
        
        dpt = clsDpt()
        oldIdDpt = 1
        newIdDpt = 150
        result = dpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertTrue( result )     
    
    # Test 42: El id del dpt a modificar existe en la base de datos y su
    #          valor es muy grande. El nuevo id se encuentra disponible.
    def test_42modify_idDptOldIdExistIqualBigNumberNewIdAvailable(self):
        dpt = clsDpt()
        oldIdDpt = (2**31)-1
        newIdDpt = 200
        result = dpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertTrue( result )     
    
    # Test 43: El id del dpt a modificar existe en la base de datos. El
    #          nuevo id se encuentra disponible y es igual a 1.
    def test_43modify_idDptOldIdExistNewIdAvailableIqual1(self):
        dpt = clsDpt()
        oldIdDpt = 150
        newIdDpt = 1
        result = dpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertTrue( result )      
    
    # Test 44: El id del dpt a modificar existe en la base de datos. El
    #          nuevo id se encuentra disponible y su valor es muy grande.    
    def test_44modify_idDptOldIdExistNewIdAvailableIqualBigNumber(self):
        dpt = clsDpt()
        oldIdDpt = 200
        newIdDpt = (2**31)-1
        result = dpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertTrue( result )  


    ### Casos Validos ( Casos Esquinas )

    # Test 45: El id del dpt a modificar existe en la base de datos y su
    #          valor es muy grande. El nuevo id se encuentra disponible y
    #          su valor es igual a 1.
    def test_45modify_idDptOldIdExistIqualBigNumberNewIdAvailableIqual1(self):
        session.query(model.Dpt).delete()  
        # Se limpia la base de datos.
        # Se inserta un elemento valido en la base
        newIdDpt = (2**31)-1
        newNameDpt = 'dptDePrueba1'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit() 
        
        dpt = clsDpt()
        oldIdDpt = (2**31)-1
        newIdDpt = 1
        result = dpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertTrue( result )  
    
    
    # Test 46: El id del dpt a modificar existe en la base de datos y su
    #          valor es igual a 1. El nuevo id se encuentra disponible
    #          y su valor es muy grande.
    def test_46modify_idDptOldIdExistIqual1NewIdAvailable(self):        
        dpt = clsDpt()
        oldIdDpt = 1
        newIdDpt = (2**31)-1
        result = dpt.modify_idDpt( oldIdDpt, newIdDpt )
        self.assertTrue( result )  

    ## Casos invalidos (Casos Malicia):

    # Test 47: El id del dpt a modificar es un String
    def test_47modify_idDptOldIdExistNewIdString(self):
    	dpt = clsDpt();
    	oldIdDpt = '1'
    	newIdDpt = 156
    	result = dpt.modify_idDpt(oldIdDpt, newIdDpt)
    	self.assertFalse(result)

    # Test 48: El id del dpt a modificar es un numero negativo
    def test_48modify_idDptOldIdExistNumberNegative(self):
    	dpt = clsDpt();
    	oldIdDpt = -1
    	newIdDpt = 156
    	result = dpt.modify_idDpt(oldIdDpt, newIdDpt)
    	self.assertFalse(result)

    # Test 49: El id del dpt a modificar es uun numero real
    def test_49modify_idDptOldExistFloat(self):
     	dpt = clsDpt();
    	oldIdDpt = 1.8
    	newIdDpt = 156
    	result = dpt.modify_idDpt(oldIdDpt, newIdDpt)
    	self.assertFalse(result)

    # Test 50: Error en el id dpt, parametro None
    def test_50modify_idDptOldIdExistIdNone(self):
    	dpt = clsDpt();
    	oldIdDpt = None
    	newIdDpt = 156
    	result = dpt.modify_idDpt(oldIdDpt, newIdDpt)
    	self.assertFalse(result)

    # Test 51 : El nuevo id para el dpt a modificar es un String
    def test_51modify_idDptOldIdExistNewIdString(self):
    	dpt = clsDpt();
    	oldIdDpt = 1
    	newIdDpt = 'BadId'
    	result = dpt.modify_idDpt(oldIdDpt, newIdDpt)
    	self.assertFalse(result)


    # Test 52 : El nuevo id para el dpt a modificar es un numero negativo
    def test_52modify_idDptOldIdexistNewIdNegative(self):
    	dpt = clsDpt();
    	oldIdDpt = 1
    	newIdDpt = -3
    	result = dpt.modify_idDpt(oldIdDpt, newIdDpt)
    	self.assertFalse(result)

    # Test 53 : El nuevo id para el dpt a modificar es un numero real
    def test_53modify_idDptOldIdExistNewIdFloat(self):
    	dpt = clsDpt();
    	oldIdDpt = 1
    	newIdDpt = 2.9
    	result = dpt.modify_idDpt(oldIdDpt, newIdDpt)
    	self.assertFalse(result)

    # Test 54 : Error en el nuevo id dpt, parametro None
    def test_54modify_idDptOldIdExistNewIdNone(self):
    	dpt = clsDpt();
    	oldIdDpt = 1
    	newIdDpt = None
    	result = dpt.modify_idDpt(oldIdDpt, newIdDpt)
    	self.assertFalse(result)



    # Funcion: modify_name

    ## Casos Invalidos (Casos Interiores)

    # Test 55 : EL id del dpt a modificar existe en la base de datos
    #		   y el nuevo nombre esta disponile.
    def test_55modify_nameDptIdExistNewNameAvailable(self):
    	# Se limpia la base de datos
    	session.query(model.Dpt).delete()
    	#Se inserta un elemento valido en la base
    	newIdDpt = 3
    	newNameDpt = 'dptDePrueba1'
    	newDpt = model.Dpt(newIdDpt, newNameDpt)
    	session.add(newDpt)
    	session.commit()

    	dpt = clsDpt()
    	idDpt = 3
    	newNameDpt = 'DptDePruebax'
    	result = dpt.modify_nameDpt(idDpt, newNameDpt)
    	self.assertTrue(result)

    # Test 56 : El id del dpto a modificar existe en la base de datos
    #		   y el nuevo nombre no se encuentra disponible
    def test_56modify_nameDptIdExistNewNameNoAvailable(self):
        dpt = clsDpt()
        idDpt = 3
        newNameDpt = 'DptDePruebax'
        result = dpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertFalse( result )

    # Test 57 : El id del dpt a modificar no existe en la base de datos
    #  		   pero el nuevo nombre se encuentra disponible
    def test_57modify_nameDptIdNoExistNewNameAvailable(self):
        dpt = clsDpt()
        idDpt = 20
        newNameDpt = 'DptDePruebax'
        result = dpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertFalse( result )

    # Test 58 : El id del dpt a modificar no existe en la base de datos
    #		   y el nuevo nombre se encuentra disponible
    def test_58modify_nameDptIdNoExistNewNameNoAvailable(self):
        dpt = clsDpt()
        idDpt = 20
        newNameDpt = 'dptDePruebaX'
        result = dpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertFalse( result ) 


    ## Casos Validos (Casos Frontera)
	
	# Test 59: El id del dpt a modificar existe en la base de datos
	#		 y el valor es igual a 1. El nuevo nombre se encuentra disponible
	def test_59modify_nameDptIdExistIqual1NewNameAvailable(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida. 
        newIdDpt = 1
        newNameDpt = 'dptDePruebaCaso1'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit() 
        
        dpt = clsDpt()
        idDpt = 1
        newNameDpt = 'dptDePruebaX3'
        result = dpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result ) 

	# Test 60: El id del dpt a modificar existe en la base de datos
	#		 y el valor es un numero muy grande.
	def test_60modify_nameDptIdExisrEqualBigNumberNewNameAvailable(self):
		# Se inserta un elemento valido en la base.
		newIdDpt = (2**31)-1
        newNameDpt = 'dptDePruebaCasoBig'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit() 

        dpt = clsDpt()
        idDpt = (2**31)-1
        newNameDpt = 'dptDePruebaXBig'
        result = dpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result ) 

	# Test 61: El id del dpt a modificar existe en la base de datos
	#		 y el nomre disponible es de longitud 1.
	def test_61modify_nameDptIdExistNewNameAvailableLen1(self):
        dpt = clsDpt()
        idDpt = 3
        newNameDpt = '1'
        result = dpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result )

	# Test 62: El id del dpt a modificar existe en la base de datos
	#		 y el nombre disponible es de longitud 50
	def test_62modify_nameDptIdExistNewNameAvailableLen50(self):
        dpt = clsDpt()
        idDpt = 3
        newNameDpt = 'x'*50
        result = dpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result ) 



	### Casos Validos (Casos Esquina)
	
	# Test 63: El id del dpt a modificar existe en la base de datos
	#		   y su valor es igual a 1 y el nuevo nombre es de longitud 1
	def test_63modify_nameDptIdExistIqual1NewNameAvailableLen1(self):
        dpt = clsDpt()
        idDpt = 1
        newNameDpt = 'z'
        result = dpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result ) 

	# Test 64: El id del dpt a modificar existe en la base de datos
	#		   y su valor es igual a 1 y el nuevo nombre es de longitud 50
	def test_64modify_nameDptIdExistIqual1NewNameAvailableLen50(self):
        dpt = clsDpt()
        idDpt = 1
        newNameDpt = 'z'*50
        result = dpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result ) 

	# Test 65: El id del dpt a modificar existe en la base de datos, su 
	#		   su valor es un numero muy grande y el nuevo nombre es de longitud 1
	def test_65modify_nameDptIdExistIqualBigNumberNewNameAvailableLen1(self):
        dpt = clsDpt()
        idDpt = (2**31)-1
        newNameDpt = 'y'
        result = dpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result ) 

	# Test 66: El id del dpt a modificar existe en la base de dato, su valor es
	#		   un numero muy grande y el nuevo nombre es de longitud 50
	def test_66modify_nameDptIdExistIqualBigNumberNewNameAvailableLen50(self):
        dpt = clsDpt()
        idDpt = (2**31)-1
        newNameDpt = 'y'*50
        result = dpt.modify_nameDpt( idDpt, newNameDpt )
        self.assertTrue( result ) 


	### Casos invalidos (Casos Malicias)
	# Test 67 : El id dado del dpt a modificar es un String
    def test_67modify_nameDptIdString(self):
    	dpt = clsDpt();
    	IdDpt = '1'
    	newNameIdDpt = 'BadDpt'
    	result = dpt.modify_nameDpt(IdDpt, newNameDpt)
    	self.assertFalse(result)


	# Test 68 : El id dado del dpt a modificar es un entero negativo
    def test_68modify_nameDptNegative(self):
    	dpt = clsDpt();
    	IdDpt = -1
    	newNameIdDpt = 'BadDpt'
    	result = dpt.modify_nameDpt(IdDpt, newNameDpt)
    	self.assertFalse(result)


	# Test 69 : El id dado del dpt a modificar es un numero real
    def test_69modify_nameDptFloat(self):
    	dpt = clsDpt();
    	IdDpt = 1.0
    	newNameIdDpt = 'BadDpt'
    	result = dpt.modify_nameDpt(IdDpt, newNameDpt)
    	self.assertFalse(result)


	# Test 70 : El id dado del dpt a modificar es None
    def test_70modify_nameDptNone(self):
    	dpt = clsDpt();
    	IdDpt = None
    	newNameIdDpt = 'BadDpt'
    	result = dpt.modify_nameDpt(IdDpt, newNameDpt)
    	self.assertFalse(result)


	# Test 71 : El nuevo nombre para el dpt a modificar es un string vacio
    def test_71modify_nameDptNewNameEmpty(self):
    	dpt = clsDpt();
    	IdDpt = 1
    	newNameIdDpt = ''
    	result = dpt.modify_nameDpt(IdDpt, newNameDpt)
    	self.assertFalse(result)


	# Test 72 : El nuevo nombre para el dpt a modificar es de longitud 51
    def test_72modify_nameDptNewNameLong51(self):
    	dpt = clsDpt();
    	IdDpt = 1
    	newNameIdDpt = 'a'*51
    	result = dpt.modify_nameDpt(IdDpt, newNameDpt)
    	self.assertFalse(result)


	# Test 73 : El nuevo nombre para el dpt a modificar es un entero
    def test_73modify_nameDptNewNameInteger(self):
    	dpt = clsDpt();
    	IdDpt = 1
    	newNameIdDpt = 2
    	result = dpt.modify_nameDpt(IdDpt, newNameDpt)
    	self.assertFalse(result)


	# Test 74 : El nuevo nombre para el dpt a modificar es None
    def test_74modify_nameDptnewNameNone(self):
    	dpt = clsDpt();
    	IdDpt = 1
    	newNameIdDpt = None
    	result = dpt.modify_nameDpt(IdDpt, newNameDpt)
    	self.assertFalse(result)


    #.............................................................

        # Funcion Eliminar

        ### Casos Validos (Casos Interiores)

    # Test 75: El dpt a eliminar existe en la base de datos.
    def test_75Delete_dptExist(self):
        dpt = clsDpt()
        idDptDelete = (2**31)-1
        result = dpt.delete_dpt( idDptDelete )
        self.assertTrue(result)

    # Test 76: El  dpt a eliminar no existe en la base de datos.
    def test_76Delete_dptExist(self):
        dpt = clsDpt()
        idDptDelete = (2**31)-1
        result = dpt.delete_dpt( idDptDelete )
        self.assertFalse(result)
        
    ### Casos invalidos( Casos Malicia )

    # Test 77: El id del dpt a eliminar es un string.
    def test_77Delete_dptIdString(self):
        dpt = clsDpt()
        idDptDelete = '1'
        result = dpt.delete_dpt( idDptDelete )
        self.assertFalse(result)
    
    # Test 78: El id a buscar es un float.
    def test_78Delete_dptIdFloat(self):
        dpt = clsDpt()
        idDptDelete = 1.01
        result = dpt.delete_dpt( idDptDelete )
        self.assertFalse(result) 

    # Test 79: El id a buscar es nulo.
    def test_79Delete_dptIdNone(self):
        dpt = clsDpt()
        idDptDelete = None
        result = dpt.delete_dpt( idDptDelete )
        self.assertFalse(result)