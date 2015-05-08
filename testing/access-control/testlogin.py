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
    # Test 22: Se genera un hash valido y se compara con el mismo password.   
    def test_22CPHashValidStringValidIqual(self):
        tempLogin = clsLogin()
        stringProbar = 'HolaSoyOg2@@'
        stringBueno = 'HolaSoyOg2@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertTrue(boolR)
        
    # Test 23: Se genera un hash valido y se compara con otro password invalido   
    def test_23CPHashValidStringValidDifferent(self):
        tempLogin = clsLogin()
        stringProbar = 'HolaSoyO'
        stringBueno = 'Holags@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)
        
    # Test 24: Se genera un hash valido y se compara con otro password valido de 14 caracteres 
    def test_24CPHashValidString14Valid(self):
        tempLogin = clsLogin()
        stringProbar = 'HolaSoyOggs@22'
        stringBueno =  'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)
        
    # Test 25: Se genera un hash valido y se compara con otro password valido de 9 caracteres 
    def test_25CPHashValidString9Valid(self):
        tempLogin = clsLogin()
        stringProbar = 'Proband9@'
        stringBueno = 'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)
    
    ### CASOS VALIDOS( Casos Fronteras ).
    
    # Test 26: Se genera un hash valido y se compara con otro password valido de 8 caracteres
    def test_26CPHashValidString8Valid(self):
        tempLogin = clsLogin()
        stringProbar = 'Hoyes2@@'
        stringBueno = 'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)
        
    # Test 27: Se genera un hash valido y se compara con otro password valido de 16 caracteres
    def test_27CPHashValidString16Valid(self):
        tempLogin = clsLogin()
        stringProbar = 'HolaSoyOggs@22!!'
        stringBueno = 'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)
        
    # Test 28: Se genera un hash valido y se compara con otro password invalido de 7 caracteres
    def test_28CPHashValidString7Invalid(self):
        tempLogin = clsLogin()
        stringProbar = 'Soyn7+@'
        stringBueno = 'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)
        
    # Test 29: Se genera un hash valido y se compara con otro password invalido de 17 caracteres    
    def test_29CPHashValidString17Invalid(self):
        tempLogin = clsLogin()
        stringProbar = 'heChoPor0r1&3Dw4#'
        stringBueno = 'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)
        
    # Test 30: Se genera un hash valido y se compara con otro password invalido de solos minusculas   
    def test_30CPHashValidStringOnlyLettersInvalid(self):
        tempLogin = clsLogin()
        stringProbar = 'hoyesjueves'
        stringBueno = 'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)
        
    # Test 31: Se genera un hash valido y se compara con otro password invalido de solos minusculas      
    def test_31CPHashValidStringOnlyLettersCInvalid(self):
        tempLogin = clsLogin()
        stringProbar = 'HOYESJUEVES'
        stringBueno = 'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)
        
    # Test 32: Se genera un hash valido y se compara con otro password invalido de solos numeros     
    def test_32CPHashValidStringOnlyNumbersInvalid(self):
        tempLogin = clsLogin()
        stringProbar = '1234567890'
        stringBueno = 'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)
        
    # Test 33: Se genera un hash valido y se compara con otro password invalido de solos caracteres especiales
    def test_33CPHashValidStringOnlyCharactersInvalid(self):
        tempLogin = clsLogin()
        stringProbar = '+@#$%&%&#'
        stringBueno = 'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)
    
    ### CASOS VALIDOS( Casos Esquinas ).

    # Test 34: Se genera un hash valido y se compara con otro password invalido de un string vacio 
    def test_34CPHashValidStringEmptyInvalid(self):
        tempLogin =  clsLogin()
        stringProbar = ''
        stringBueno = 'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)
        
    # Test 35: Se genera un hash valido y se compara con otro password invalido de solos numeros y caracteres especiales
    def test_35CPHashValidStringSCNumberInvalid(self):
        tempLogin = clsLogin()
        stringProbar = '@@@#&%123'
        stringBueno = 'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)
        
    # Test 36: Se genera un hash valido y se compara con otro password invalido de solos numeros y caracteres especiales    
    def test_36CPHashValidStringCLNumberInvalid(self):
        tempLogin = clsLogin()
        stringProbar = 'Aqui3st4mos'
        stringBueno = 'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)
        
    # Test 37: Se genera un hash valido y se compara con otro password invalido de solos caracteres especiales y letras   
    def test_37CPHashValidStringCLLettersInvalid(self):
        tempLogin = clsLogin() 
        stringProbar = 'CasoPrueba#&'
        stringBueno = 'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)

    # Test 38: Se genera un hash valido y se compara con otro password invalido de 8 espacios vacios
    def test_38CPHashValid8SpacesInvalid(self):
        tempLogin = clsLogin() 
        stringProbar = '        '
        stringBueno = 'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)
        
    # Test 39: Se genera un hash valido y se compara con otro password invalido con un caracter vacio en el medio    
    def test_39CPHashValidAnInterspaceInvalid(self):
        tempLogin = clsLogin() 
        stringProbar = '353t Y%%##'
        stringBueno = 'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringBueno)
        boolR = tempLogin.check_password(resultado, stringProbar)
        self.assertFalse(boolR)    
    
    
    ### CASOS INVALIDOS( Casos Maliciosos ).
    
    # Test 40: Se genera un hash y se compara con un Password invalido por tener 7 caracteres.
    def test_40CPString7Invalid(self):
        tempLogin = clsLogin()
        stringProbar = 'Soyn7+@'
        boolR = tempLogin.check_password(None, stringProbar)
        self.assertFalse(boolR)
     
     # Test 20:Se genera un hash invalido y se compara con un  Password invalido de 17 caracteres
    def test_41CPString17Invalid(self):
        tempLogin = clsLogin()
        stringProbar = 'heChoPor0r1&3Dw4#'
        boolR = tempLogin.check_password(None, stringProbar)
        self.assertFalse(boolR)
        
    # Test 21:Se genera un hash invalido y se compara con un  Password invalido por tener solo minusculas
    def test_42CPOnlyLettersInvalid(self):
        tempLogin = clsLogin()
        stringProbar = 'hoyesjueves'
        boolR = tempLogin.check_password(None, stringProbar)
        self.assertFalse(boolR)
        
    # Test 22: Se genera un hash invalido y se compara con un  Password invalido por tener solo mayusculas
    def test_43CPOnlyLettersCInvalid(self):
        tempLogin = clsLogin()
        stringProbar = 'HOYESJUEVES'
        boolR = tempLogin.check_password(None, stringProbar)
        self.assertFalse(boolR)
        
    # Test 44: Se genera un hash invalido y se compara con un  Password invalido por tener solo numeros.
    def test_44CPOnlyNumbersInvalid(self):
        tempLogin = clsLogin()
        stringProbar = '1234567890'
        boolR = tempLogin.check_password(None, stringProbar)
        self.assertFalse(boolR)
        
    # Test 45: Se genera un hash invalido y se compara con un  Password invalido por tener solo caracteres
    def test_45CPOnlyCharactersInvalid(self):
        tempLogin = clsLogin()
        stringProbar = '+@#$%&%&#'
        boolR = tempLogin.check_password(None, stringProbar)
        self.assertFalse(boolR)
        
     # Test 46: Se genera un hash invalido y se compara con un  Password invalido por tener solo caracter vacio
    def test_46CPtEmptyInvalid(self):
        tempLogin =  clsLogin()
        stringProbar = ''
        boolR = tempLogin.check_password(None, stringProbar)
        self.assertFalse(boolR)
        
    # Test 47: Se genera un hash invalido y se compara con un  Password invalido por tener solo caracteres y numeros
    def test_47CPStringSCNumberInvalid(self):
        tempLogin = clsLogin()
        stringProbar = '@@@#&%123'
        boolR = tempLogin.check_password(None, stringProbar)
        self.assertFalse(boolR)
        
    # Test 48: Se genera un hash invalido y se compara con un Password invalido por tener solo letras y numeros
    def test_48CPLettersCLNumberInvalid(self):
        tempLogin = clsLogin()
        stringProbar = 'Aqui3st4mos'
        boolR = tempLogin.check_password(None, stringProbar)
        self.assertFalse(boolR)
        
    # Test 49:Se genera un hash invalido y se compara con un  Password invalido por tener solo letras y numeros
    def test_49CPtStringCLLettersInvalid(self):
        tempLogin = clsLogin() 
        stringProbar = 'CasoPrueba#&'
        boolR = tempLogin.check_password(None, stringProbar)
        self.assertFalse(boolR)
        
    # Test 50: Se genera un hash invalido y se compara con un  Password invalido por tener solo 8 caracteres vacios    
    def test_50CP8SpacesInvalid(self):
        tempLogin = clsLogin() 
        stringProbar = '        '
        boolR = tempLogin.check_password(None, stringProbar)
        self.assertFalse(boolR)
        
    # Test 51: Se genera un hash invalido y se compara con un Password invalido por tener un caracter vacio en el medio    
    def test_52CPAnInterspaceInvalid(self):
        tempLogin = clsLogin() 
        stringProbar = '353t Y%%##'
        boolR = tempLogin.check_password(None, stringProbar)
        self.assertFalse(boolR)
        
    # Test 53: Se genera un hash invalido y se compara con un Password valido de 16 caracteres
    def test_53CPString16Valid(self):
        tempLogin = clsLogin()
        stringProbar = 'HolaSoyOggs@22!!'
        boolR = tempLogin.check_password(None, stringProbar)
        self.assertFalse(boolR)
        
    # Test 54: Se genera un hash invalido y se compara con un  Password valido de 14 caracteres    
    def test_54CPString14Valid(self):
        tempLogin = clsLogin()
        stringProbar = 'HolaSoyOggs@22@@'
        resultado = tempLogin.encript(stringProbar)
        self.assertNotEqual(resultado, None)
      
    #Test 55: Se genera un hash invalido y se compara con un  Password valido de 9 caracteres
    def test_55CPString9Valid(self):
        tempLogin = clsLogin()
        stringProbar = 'Proband9@'
        resultado = tempLogin.encript(stringProbar)
        self.assertNotEqual(resultado, None)
    
    
    # Test 56: Se genera un hash invalido y se compara con un  Password valido de 8 caracteres.
    def test_56CPString8Valid(self):
        tempLogin = clsLogin()
        stringProbar = 'Hoyes2@@'
        resultado = tempLogin.encript(stringProbar)
        self.assertNotEqual(resultado, None)
        
    #.-------------------------------------------------------------------.  