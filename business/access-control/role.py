from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
	 'postgresql://BMO@localhost/BMO'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class clsRole(db.Model):

	def insert_roles(self, newId, newNamerole):
		newRole = Role(id = newId, namerole = newNamerole)
		db.session.add(newRole)
		db.session.commit()