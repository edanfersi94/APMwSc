"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Nicolas Manan.      Carnet: 06-39883
        Edward Fernandez.   Carnet: 10-11121
		

    DESCRIPCION: Script que contiene los casos de prueba del modulo "login.py"

"""

#------------------------------------------------------------------------------------

# Librerias a utilizar.

import os
import sys

# PATH que permite utilizar al modulo "role.py"
sys.path.append('../../business/access-control')
from login import clsLogin

import unittest

class TestLogin(unittest.TestCase):
	
	#.-------------------------------------------------------------------.  
    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsRole.
    def test1ObjectExist(self):
        tempLogin = clsLogin()
        self.assertIsNotNone(tempLogin)

	#.-------------------------------------------------------------------.  
    # FUNCION LONGITUD.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 2: El string dado es la cadena vacia.
    def test2LenStringEmpty(self):
        tempLogin = clsLogin()
        stringTest = ''
        result = tempLogin.longitud( stringTest )
        tamEsp = 0
        self.assertEqual(result, tamEsp)
        
    # Test 3: El string dado es una cadena que contiene un solo caracter.
    def test3LenOneChar(self):
        tempLogin = clsLogin()
        stringTest = 'a'
        result = tempLogin.longitud( stringTest )
        tamEsp = 1
        self.assertEqual (result, tamEsp )
    
    # Test 4: El string dado es una cadena que contiene 14 caracteres.
    def test4LenString14(self):
        tempLogin = clsLogin()
        stringTest = 'abcdefg1234567'
        result = tempLogin.longitud( stringTest )
        tamEsp = 14
        self.assertEqual( result, tamEsp )
    
    # Test 5: El string dado es una cadena que contiene (2**31)-1 caracteres.
    def test5LPStringBig(self):
        tempLogin = clsLogin()
        stringTest = 'a'*((2**31)-1)
        result = tempLogin.longitud( stringTest )
        tamEsp = (2**31)-1
        self.assertEqual( result, tamEsp )
    
    #.-------------------------------------------------------------------.  
    # FUNCION ENCRIPTAR.

    ### CASOS VALIDOS( Casos Interiores ).
    # Test 6: El string a encriptar tiene 14 caracteres y al menos una letra
    #        mayuscula, un numero y un caracter especial.
    def test6encriptStringLen14(self):
        tempLogin = clsLogin()
        stringTest = 'HolaSoyOggs@22@@'
        result = tempLogin.encriptar( stringTest )
        resultInv = None
        self.assertNotEqual( result, resultInv )

    ### CASOS VALIDOS( Casos Fronteras ).
    # Test 7: El string a encriptar tiene 8 caracteres y al menos una letra
    #        mayuscula, un numero y un caracter especial.
    def test7encriptStringLen8(self):
        tempLogin = clsLogin()
        stringTest = 'Hoyes2@@'
        result = tempLogin.encriptar( stringTest )
        resultInv = None
        self.assertNotEqual( result, resultInv )
        
    # Test 8: El string a encriptar tiene 16 caracteres y al menos una letra
    #        mayuscula, un numero y un caracter especial.
    def test8encriptStringLen16(self):
        tempLogin = clsLogin()
        stringTest = 'HolaSoyOggs@22!!'
        result = tempLogin.encriptar( stringTest )
        resultInv = None
        self.assertNotEqual( result, resultInv )
    
    ### CASOS INVALIDOS( Casos Maliciosos ).
    # Test 9: El string a encriptar tiene 7 caracteres y al menos una letra
    #        mayuscula, un numero y un caracter especial.
    def test9encriptStringLen7(self):
        tempLogin = clsLogin()
        stringTest = 'Soyn7+@'
        result = tempLogin.encriptar( stringTest )
        resultEsp = None
        self.assertEqual( result, resultEsp )
        
    # Test 10: El string a encriptar tiene 17 caracteres y al menos una letra
    #         mayuscula, un numero y un caracter especial.
    def test_10encriptStringLen17(self):
        tempLogin = clsLogin()
        stringTest = 'heChoPor0r1&3Dw4#'
        result = tempLogin.encriptar( stringTest )
        resultEsp = None
        self.assertEqual( result, resultEsp )

    # Test 11: El string a encriptar solo tiene letras minusculas. La longitud 
    #          es valida.
    def test_11encriptStringLowercase(self):
        tempLogin = clsLogin()
        stringTest = 'hoyesjueves'
        result = tempLogin.encriptar( stringTest )
        resultEsp = None
        self.assertEqual( result, resultEsp )

    # Test 12: El string a encriptar solo tiene letras mayusculas. La longitud
    #          es valida.
    def test_12encriptStringUppercase(self):
        tempLogin = clsLogin()
        stringTest = 'HOYESJUEVES'
        result = tempLogin.encriptar( stringTest )
        resultEsp = None
        self.assertEqual( result, resultEsp )
        
    # Test 13: El string a encriptar solo tiene numeros. La longitud es valida.
    def test_13encriptStringOnlyNumbers(self):
        tempLogin = clsLogin()
        stringTest = '1234567890'
        result = tempLogin.encriptar( stringTest )
        resultEsp = None
        self.assertEqual( result, resultEsp )

    # Test 14: El string a encriptar solo tiene caracteres especiales. La 
    #          longitud es valida.
    def test_14encriptStringOnlySpecialChars(self):
        tempLogin = clsLogin()
        stringTest = '+@#$%&%&#'
        result = tempLogin.encriptar( stringTest )
        resultEsp = None
        self.assertEqual( result, resultEsp )

    # Test 15: El string a encriptar solo tiene numeros. La longitud es valida.
    def test_15encriptStringOnlyNumbers(self):
        tempLogin = clsLogin()
        stringTest = '1234567890'
        result = tempLogin.encriptar( stringTest )
        resultEsp = None
        self.assertEqual( result, resultEsp )

    # Test 16: El string a encriptar es la cadena vacia.
    def test_16encriptStringEmpty(self):
        tempLogin = clsLogin()
        stringTest = ''
        result = tempLogin.encriptar( stringTest )
        resultEsp = None
        self.assertEqual( result, resultEsp )

    # Test 17: El string a encriptar solo tiene caracteres especiales y numeros.
    def test_17encriptStringOnlySpecialCharsAndNumbers(self):
        tempLogin = clsLogin()
        stringTest = '@@@#&%123'
        result = tempLogin.encriptar( stringTest )
        resultEsp = None
        self.assertEqual( result, resultEsp )

    # Test 18: El string a encriptar solo tiene letras (mayusculas y minusculas)
    #          y numeros.
    def test_18encriptStringOnlyLettersAndNumbers(self):
        tempLogin = clsLogin()
        stringTest = 'Aqui3st4moS'
        result = tempLogin.encriptar( stringTest )
        resultEsp = None
        self.assertEqual( result, resultEsp )

    # Test 19: El string a encriptar solo tiene caracteres especiales y letras
    #          tanto mayusculas como minusculas.
    def test_19encriptStringOnlySpecialCharsAndLetters(self):
        tempLogin = clsLogin()
        stringTest = 'CasoPrueba#&'
        result = tempLogin.encriptar( stringTest )
        resultEsp = None
        self.assertEqual( result, resultEsp )

    # Test 20: El string solo tiene caracteres vacios. La longitud es valida.
    def test_20encriptStringOnlyEmptyChars(self):
        tempLogin = clsLogin()
        stringTest = '        '
        result = tempLogin.encriptar( stringTest )
        resultEsp = None
        self.assertEqual( result, resultEsp )

    # Test 21: El string a encriptar tiene espacios en blanco.
    def test_21encriptStringWithSpaces(self):
        tempLogin = clsLogin()
        stringTest = '353t Y%%##'
        result = tempLogin.encriptar( stringTest )
        resultEsp = None
        self.assertEqual( result, resultEsp )

    #.-------------------------------------------------------------------.  
    # FUNCION CHECK_PASSWORD. 
    
    ### CASOS VALIDOS( Casos Interiores ).
    
    ### CASOS VALIDOS( Casos Fronteras ).
    
    ### CASOS VALIDOS( Casos Esquinas ).
    
    ### CASOS INVALIDOS( Casos Maliciosos ).
    
    #.-------------------------------------------------------------------.  