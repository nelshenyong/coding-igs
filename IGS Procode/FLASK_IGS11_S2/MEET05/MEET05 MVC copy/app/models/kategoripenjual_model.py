import mysql.connector
from flask import current_app

class kategoripenjualModel:
    def __init__(self):
        self.config = current_app.config
        
    def connect(self):
        return mysql.connector.connect(
            host=self.config['MYSQL_HOST'],
            database=self.config['MYSQL_DATABASE'],
            password=self.config['MYSQL_PASSWORD'],
            user=self.config['MYSQL_USER']
        ) 
        
    def get_all_kategoripenjual(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("""
            SELECT kp.id, p.nama as penjual, k.nama as kategori 
            FROM kategoripenjual kp
            JOIN penjual p ON kp.penjualid = p.id
            JOIN kategori k ON kp.kategoriid = k.id
        """)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    def save_kategoripenjual(self, penjualid, kategoriid):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("INSERT INTO kategoripenjual (penjualid, kategoriid) VALUES (%s, %s)", 
                      (penjualid, kategoriid))
        db.commit()
        cursor.close()
        db.close()
        return True

    def update_kategoripenjual(self, id, penjualid, kategoriid):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("UPDATE kategoripenjual SET penjualid = %s, kategoriid = %s WHERE id = %s", 
                      (penjualid, kategoriid, id))
        db.commit()
        cursor.close()
        db.close()
        return True

    def delete_kategoripenjual(self, id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("DELETE FROM kategoripenjual WHERE id = %s", (id,))
        db.commit()
        cursor.close()
        db.close()
        return True

    def get_kategoripenjual_by_id(self, id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("""
            SELECT kp.id, p.nama as penjual, k.nama as kategori 
            FROM kategoripenjual kp
            JOIN penjual p ON kp.penjualid = p.id
            JOIN kategori k ON kp.kategoriid = k.id
            WHERE kp.id = %s
        """, (id,))
        data = cursor.fetchone()
        cursor.close()
        db.close()
        return data

    def get_all_penjual(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM penjual")
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    def get_all_kategori(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM kategori")
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data 