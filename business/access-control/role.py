from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
 
from data import model

class clsRole(db.Model):

	def insert_roles(self, newId, newNamerole):
		newRole = Role(id = newId, namerole = newNamerole)
		db.session.add(newRole)
		db.session.commit()