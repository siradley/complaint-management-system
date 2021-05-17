
import sqlite3

class ConnectionDatabase:
    #create database
	def __init__(self):
		self._db = sqlite3.connect('complaintDB.db')
		self._db.row_factory = sqlite3.Row
		self._db.execute('create table if not exists complainTable(ID integer primary key autoincrement, FirstName varchar(255), LastName varchar(255), Address Text, Gender varchar(255), Comment text)')
		self._db.commit()
	def Add(self,firstname,lastname, address, gender,comment):
		self._db.execute('insert into complainTable (FirstName, LastName, Address, Gender, Comment) values (?,?,?,?,?)', (firstname, lastname, address, gender, comment))
		self._db.commit()
		return 'Your complaint has been submitted.'
	def ListRequest(self):
		cursor = self._db.execute('select * from complainTable')
		return cursor




