import mysql.connector
from flask import current_app

class produkModel:
    def __init__(self):
        self.config = current_app.config
        
    def connect(self):
        return mysql.connector.connect(
            host=self.config['MYSQL_HOST'],
            database=self.config['MYSQL_DATABASE'],
            password=self.config['MYSQL_PASSWORD'],
            user=self.config['MYSQL_USER']
        ) 
        
    def get_all_produk(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("""
            SELECT p.id, p.nama, p.harga, pj.nama as penjual 
            FROM produk p
            JOIN penjual pj ON p.penjualid = pj.id
        """)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    def save_produk(self, nama, harga, penjualid):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("INSERT INTO produk (nama, harga, penjualid) VALUES (%s, %s, %s)", 
                      (nama, harga, penjualid))
        db.commit()
        cursor.close()
        db.close()
        return True

    def update_produk(self, id, nama, harga, penjualid):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("UPDATE produk SET nama = %s, harga = %s, penjualid = %s WHERE id = %s", 
                      (nama, harga, penjualid, id))
        db.commit()
        cursor.close()
        db.close()
        return True

    def delete_produk(self, id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("DELETE FROM produk WHERE id = %s", (id,))
        db.commit()
        cursor.close()
        db.close()
        return True

    def get_produk_by_id(self, id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("""
            SELECT p.id, p.nama, p.harga, pj.nama as penjual 
            FROM produk p
            JOIN penjual pj ON p.penjualid = pj.id
            WHERE p.id = %s
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