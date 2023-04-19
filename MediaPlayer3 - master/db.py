# it,s not live

import psycopg2
import os

class DataBase():
    
    def __init__(self,dbHost):
        self.dbHost = dbHost

        self.ValueGet = ''

        self.conn = psycopg2.connect(dbname='database', user='db_user', password='mypassword', host=self.dbHost)
        self.cursor = self.conn.cursor()

        print('connecting')

    def add(self,MessageExecute):
        self.MessageExecute = MessageExecute
        self.cursor.execute(self.MessageExecute)


    def getString(self):
        self.ValueGet = self.cursor.fetchone()
        return
    def getAll(self):
        self.ValueGet = self.cursor.fetchall()
        return

os.system("ssh username1@remote.somewhere.com -L 5432:localhost:5432 -p 222 \n export BASH_SILENCE_DEPRECATION_WARNING=1")

DB = DataBase('localhost')
DB.add('SELECT * FROM airport LIMIT 10')

DB.getAll()
print(DB.getAll())