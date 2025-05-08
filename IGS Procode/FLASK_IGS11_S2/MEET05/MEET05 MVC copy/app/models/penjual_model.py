import mysql.connector
from flask import current_app

class penjualModel:
    def __init__(self):
        self.config = current_app.config
        
    def connect(self):
        return mysql.connector.connect(
            host=self.config['MYSQL_HOST'],
            database=self.config['MYSQL_DATABASE'],
            password=self.config['MYSQL_PASSWORD'],
            user=self.config['MYSQL_USER']
        ) 
        
    def get_all_penjual(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("""
            SELECT p.id, p.nama, p.alamat, k.nama as kota 
            FROM penjual p
            JOIN kota k ON p.kotaid = k.id
        """)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    def save_penjual(self, nama, alamat, kotaid):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("INSERT INTO penjual (nama, alamat, kotaid) VALUES (%s, %s, %s)", 
                      (nama, alamat, kotaid))
        db.commit()
        cursor.close()
        db.close()
        return True

    def update_penjual(self, id, nama, alamat, kotaid):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("UPDATE penjual SET nama = %s, alamat = %s, kotaid = %s WHERE id = %s", 
                      (nama, alamat, kotaid, id))
        db.commit()
        cursor.close()
        db.close()
        return True

    def delete_penjual(self, id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("DELETE FROM penjual WHERE id = %s", (id,))
        db.commit()
        cursor.close()
        db.close()
        return True

    def get_penjual_by_id(self, id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("""
            SELECT p.id, p.nama, p.alamat, k.nama as kota 
            FROM penjual p
            JOIN kota k ON p.kotaid = k.id
            WHERE p.id = %s
        """, (id,))
        data = cursor.fetchone()
        cursor.close()
        db.close()
        return data

    def get_all_kota(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM kota")
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data 