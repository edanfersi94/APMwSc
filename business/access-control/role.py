from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os
sys.path.append('../../data')
import model

DBSession = sessionmaker(bind=model.engine)
session = DBSession()

class clsRole():

	def insert_roles(self, newId, newNamerole):
		newRole = model.Role(newId, newNamerole)
		session.add(newRole)
		session.commit()
		
role1 = clsRole()
role1.insert_roles(1,'departamento1')
role1.insert_roles(2,'departamento2')
role1.insert_roles(3,'departamento3')