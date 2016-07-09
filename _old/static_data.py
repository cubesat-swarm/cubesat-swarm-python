
"""
Model Class for Static Static Data
"""

import sqlite3

class StaticData:

	conn = sqlite3.connect('smember.db')
	c = conn.cursor()
	
	def __init__(self, i, v, d, u):
		self.id = i
		self.value = v
		self.description = d
		self.unit = u
		

	def save_data_db(self):
		params = (self.id, self.value, self.description,self.unit)
		self.c.execute("INSERT INTO static_data VALUES (?,?,?,?)",params)
		self.conn.commit()

	def get_data_db(self,id):
		self.c.execute("SELECT * FROM static_data WHERE id ="+str(id))
		#print(self.c.fetchone())
		d = self.c.fetchone()
		return str(d)
	def fill_table():
		StaticData(1,"4","cpu_cores","Main_CPU").save_data_db()
		StaticData(2,"A7","arch","").save_data_db()
		#... put the next attributes

#data = StaticData(1,"4","cpu_cores","Main_CPU")
#data.save_data_db()
#data.get_data_db(1)



