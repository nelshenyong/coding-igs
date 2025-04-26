import mysql.connector
from flask import current_app

class kotaModel:
    def __init__(self):
        self.config = current_app.config
        
    def connect(self):
        return mysql.connector.connect(
            host=self.config['MYSQL_HOST'],
            user=self.config['MYSQL_USER'],
            password=self.config['MYSQL_PASSWORD'],
            database=self.config['MYSQL_DATABASE']
        ) 
        
    def get_all_kota(self):
        db = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM kota")
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data