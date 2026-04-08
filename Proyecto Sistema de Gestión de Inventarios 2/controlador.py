import mysql.connector 
from tkinter import messagebox

def conectar():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="232006",
            database="Sistema_Control"
        )
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {err}")
        return None


