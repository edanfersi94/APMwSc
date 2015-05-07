import unittest
from dpt import *

class testDpt (unittest.TestCase):

	#.----------------------------------------------------.

	#Test 1: Verifica que se cree el objeto de la clase clsDpt
	def test1_objectExist(self):
		dpt = clsDpt()
		self.assertIsInstance(dpt,clsDpt)

	## Funcionees 'find'
	### Casos Validos

	#Test2: Busqueda de un id existente
	def test2_find_idDpt(self):
		dpt = clsDpt()
		result = dpt.find_idDpt(1)
		self.assertIsNotNone(result[0])

	#Test3: Busqueda de un id inexistente o en una lista vacia
	def test3_find_idDpt(self):
		dpt = clsDpt()
		result = dpt.find_idDpt(38)
		self.assertEqual(result,[])

	### CasosInvalidos
	#### Casos Malicia

	#Test4: Busqueda de un tipo de dato invalido 'String'
	def test4_find_idDpt(self):
		dpt = clsDpt()
		result = dpt.find_idDpt('4')
		self.assertEqual(result, [])

	#Test5: Busqueda de un tipo de dato inexistente 'entero negativo'
	def test5_find_idDpt(self):
		dpt = clsDpt()
		result = dpt.find_idDpt(-2)
		self.assertEqual(result, [])

    #Test6: Busqueda de un tipo de dato inexistente 'numero real'
	def test6_find_idDpt(self):
		dpt = clsDpt()
		result = dpt.find_idDpt(1.0)
		self.assertEqual(result, [])

    #Test7: Error de parametros en la funcion
	def test7_find_idDpt(self):
		dpt = clsDpt()
		result = dpt.find_idDpt(None)
		self.assertEqual(result, [])

    ### Casos Validos

    #Test8: Busqueda de un nombre existente
	def test8_find_nameDpt(self):
		dpt = clsDpt()
		result = dpt.find_nameDpt('dpt1')
		self.assertIsNotNone(result[0])

    #Test9: Busqueda de un nombre inexistente
	def test9_find_nameDpt(self):
		dpt = clsDpt()
		result = dpt.find_nameDpt('dpt9')
		self.assertEqual(result,[])

	### Casos invalidos
    #### Casos Malicia

	#Test10: Busqueda de un tipo de dato invalido 'entero'
	def test_10_find_nameDpt(self):
		dpt = clsDpt()
		result = dpt.find_nameDpt(1)
		self.assertEqual(result, [])

	#Test11: Buscar un String vacio
	def test_11_find_nameDpt(self):
		dpt = clsDpt()
		result = dpt.find_nameDpt('')
		self.assertEqual(result, [])

	#Test12: Error de parametros en la funcion
	def test_12_find_nameDpt(self):
		dpt = clsDpt()
		result = dpt.find_nameDpt(None)
		self.assertEqual(result, [])

"""
		### Casos Validos

	#Test12: PREGUNTAR POR LOS CASOS DE PRUEBAS DE TEST 12 Y 13
	def test_12_find_listIdDpt(self):
		dpt = clsDpt()
		result = dpt.find_listIdDpt()

	def test_13_find_listIdDpt(self):
		dpt = clsDpt()
		result = dpt.find_listIdDpt()

"""

	### Casos Validos

	#Test13: Insertar un id inexistente con su nombre
	def test_13_insert_dpt(self):
		dpt = clsDpt()
		result = dpt.insert_dpt(4,'dpt4')
		self.assertTrue(result)

	### Casos Invalidos
	### Casos Fronteras

	#Test14: Insertar un id y nombre existente
	def test_14_insert_dpt(self):
		dpt = clsDpt()
		result = dpt.insert_dpt(4,'dpt4')
		self.assertFalse(result)

	#Test15: Insertar un nombre existente y un id inexistente
	def test_15_insert_dpt(self):
		dpt = clsDpt()
		result = dpt.insert_dpt(5,'dpt4')
		self.assertFalse(result)

	#Test16: Insertar un nombre inexistente y un id existente
	def test_16_insert_dpt(self):
		dpt = clsDpt()
		result = dpt.insert_dpt(1,'dpt8')
		self.assertFalse(result)

	#Test17: 