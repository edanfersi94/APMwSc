"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Nicolas Manan.      Carnet: 06-39883
        Edward Fernandez.   Carnet: 10-11121

    DESCRIPCION: Script que contiene los metodos requeridos para trabajar con
                 el login de la aplicacion.
		
"""

#-------------------------------------------------------------------------------

# Librerias a utilizar.

import uuid
import hashlib
import re 

#-------------------------------------------------------------------------------

class clsLogin():
    def __init__(self):
        
        # Expresion regular que nos permitira saber si un string es valido.

        self.regularExp = ('(([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[@.#$+*])|'
                           '(([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*\d)|'
                           '(([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*[A-Z])|'
                           '(([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*[@.#$+*])|'
                           '(([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[A-Z])|'
                           '(([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*\d)'
                           )

    #.------------------------------------------------------------------------------------------.
     
    def encriptar(self, value):
        """
        	@brief Funcion que permite encriptar un string dado.
        	
        	@param value  : string a encriptar.
        	
        	@return codigo hash si se encripto efectivamente. De lo contrario None.
        """        
        oHash=""
        olength_password = self.longitud(value)   
        
        if (( olength_password >= 8 ) and ( olength_password <= 16 )):
            # Verificar la longitud del password
            matchObj = re.search(self.regularExp,value)
            
            # Se verifica si la cadena introducida es valida.
            if (matchObj):        
                # uuid es usado para generar numeros random
                salt = uuid.uuid4().hex
                # hash
                oHash= hashlib.sha256(salt.encode() + value.encode()).hexdigest() + ':' + salt
                return oHash 
        else:
            return(None)
    
    #.------------------------------------------------------------------------------------------.
    
    def check_password(self, oPassworkEncript, oCheckPassword):
        """
			@brief Funcion que permite verificar si dos claves son iguales.
			
			@param oPassworkEncript  : Codigo hash de la clave con la que se verificara.
			@param oCheckPassword    : String que se verificara.
			
			@return True si las claves son iguales. De lo contrario False.
		"""
        
        # Verificar la longitud del password
        olongitud = self.longitud(oCheckPassword)   
        
        if olongitud>=8 and olongitud<=16 and oPassworkEncript != None:
            matchObj = re.search(self.regularExp,oCheckPassword) 
        
            if (matchObj):
                # uuid es usado para generar numeros random
                oPassworkEncript, salt = oPassworkEncript.split(':')
                bool = oPassworkEncript == hashlib.sha256(salt.encode() + oCheckPassword.encode()).hexdigest()
                
                if (bool):
                    return(True)
                    
        return(False)
    
    
    #.------------------------------------------------------------------------------------------.
    
    def longitud(self, user_password):
        """
			@brief Funcion que indica la longitud de un string dado.
			
			@param user_password: String a utilizar.
			
			@return entero que indica la longitud de la cadena de caracteres dada.
		"""
        # uuid es usado para generar numeros random
        return len(user_password)

    #.------------------------------------------------------------------------------------------.