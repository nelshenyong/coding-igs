import sqlite3
from tabulate import tabulate
import pandas as pd

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

def init_db():
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first TEXT,
            last TEXT,
            pay INTEGER
        );
        '''
    )
    connection.commit()

def insert_emp(emp):
    try:
        with connection:
            cursor.execute("""
                INSERT INTO employees (first, last, pay)
                VALUES (?, ?, ?)
            """, (emp.first, emp.last, emp.pay))
    except Exception as e:
        raise Exception(f"Error: {e}")

def show_table(table):
    df = pd.DataFrame(table, columns=["ID", "First Name", "Last Name", "Salary"])
    print(tabulate(df, headers='keys', tablefmt='psql'))

def get_all_emps():
    cursor.execute("SELECT * FROM employees;")
    return cursor.fetchall()

def get_emp_by_last(last):
    cursor.execute("SELECT * FROM employees WHERE last = ?", (last,))
    return cursor.fetchall()

def get_emp_by_id(emp_id):
    cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,))
    return cursor.fetchone()

def update_emp_pay(emp_id, pay):
    try:
        with connection:
            cursor.execute("UPDATE employees SET pay = ? WHERE id = ?", (pay, emp_id))
    except Exception as e:
        raise Exception(f"Error: {e}")
    return get_emp_by_id(emp_id)

def delete_emp_by_id(emp_id):
    try:
        with connection:
            cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    except Exception as e:
        raise Exception(f"Error: {e}")

init_db()
