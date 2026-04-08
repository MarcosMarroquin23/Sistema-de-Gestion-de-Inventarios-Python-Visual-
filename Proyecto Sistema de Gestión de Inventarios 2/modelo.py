from controlador import conectar
import tkinter as tk

#-----------------------------------------------------------------------------------------------------------------------------------------------#

def validarUser(usuario, contrasenia):
    db = conectar()
    if db is None: #si no hay conexion no se hace la validacion
        return False  

    try:
        resultado = db.cursor() #cursor para consultas
        resultado.execute("SELECT * FROM usuario WHERE usuario = %s AND contrasenia = %s", (usuario, contrasenia)) #% placeholder acepta valores 

        existe = resultado.fetchone() is not None #primera fila de resultados + si la validacion existe o no

        resultado.close()
        db.close()
        return existe 
        
    except Exception as e:
        print(f"Error en validación: {e}")
        db.close()
        return False
    
#-----------------------------------------------------------------------------------------------------------------------------------------------#

def limpiarEntry(widget): 
    for hijo in widget.winfo_children():
        if isinstance(hijo, tk.Entry):
            hijo.delete(0, tk.END)
        else:
            limpiarEntry(hijo)
    
#-----------------------------------------------------------------------------------------------------------------------------------------------#

def agregarP(codigo, descripcion, unidad, presentacion, precio, estado, fecha):
    db = conectar()
    if db is None:
        return False
    
    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO producto (codigo, descripcion, unidad_M, presentacion, precio, estado, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (codigo, descripcion, unidad, presentacion, precio, estado, fecha))
        
        db.commit() # confirma y guarda los cambios en la bd
        cursor.close()
        db.close()
        return True
    
    except Exception as e:
        print(f"No se agregó producto: {e}")
        db.close()
        return False
    
#-----------------------------------------------------------------------------------------------------------------------------------------------#

def modificarP(codigo, descripcion, unidad, presentacion, precio, estado, fecha):
    db = conectar()
    if db is None:
        return False
    
    try:
        cursor = db.cursor()
        cursor.execute("UPDATE producto SET descripcion=%s, unidad_M=%s, presentacion=%s, precio=%s, estado=%s, fecha=%s WHERE codigo=%s",
            (descripcion, unidad, presentacion, precio, estado, fecha, codigo))
        
        db.commit()
        cursor.close()
        db.close()
        return True
    
    except Exception as e:
        print(f"No se actualizó el producto: {e}")
        db.close()
        return False
    
#-----------------------------------------------------------------------------------------------------------------------------------------------#

def eliminarP(codigo):
    db = conectar()
    if db is None:
        return False
    
    try:
        cursor = db.cursor()
        cursor.execute("DELETE FROM producto WHERE codigo=%s", (codigo,))
        
        db.commit()
        cursor.close()
        db.close()
        return True
    
    except Exception as e:
        print(f"No se eliminó el producto: {e}")
        db.close()
        return False
    
#-----------------------------------------------------------------------------------------------------------------------------------------------#

def obtenerProductos():
    db = conectar()
    if db is None:
        return False
    
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM producto")
        
        productos = cursor.fetchall() #obtiene todos los resultados
        cursor.close()
        db.close()
        return productos
    
    except Exception as e:
        print(f"Error al obtener productos: {e}")
        db.close()
        return False
    
#-----------------------------------------------------------------------------------------------------------------------------------------------#
    
def buscarP_CDF(codigo, descripcion, fecha):
    db = conectar()
    if db is None:
        return False

    try:
        cursor = db.cursor()
        
        if codigo and fecha:
            cursor.execute("SELECT * FROM producto WHERE codigo=%s AND fecha=%s", (codigo, fecha))
        elif codigo:
            cursor.execute("SELECT * FROM producto WHERE codigo=%s", (codigo,))
        elif descripcion:
            cursor.execute("SELECT * FROM producto WHERE descripcion=%s", (descripcion,))
        elif fecha:
            cursor.execute("SELECT * FROM producto WHERE fecha=%s", (fecha,))
        else:
            return []  #retorno de lista vacio si no hay elemntos
        
        productos = cursor.fetchall() #obtiene todos los resultados                                                      
        cursor.close()
        db.close()
        return productos
    
    except Exception as e:
        print(f"No se pudo obtener la lista: {e}")
        db.close()
        return False