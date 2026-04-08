import tkinter as tk
from tkinter import messagebox
from modelo import validarUser
from modelo import limpiarEntry
from tkinter import ttk
from modelo import obtenerProductos
from modelo import agregarP
from modelo import modificarP
from modelo import eliminarP
from modelo import buscarP_CDF

#-----------------------------------------------------------------------------------------------------------------------------------------------#

ventana2 = None
ventana3 = None
ventana4 = None

#-----------------------------------------------------------------------------------------------------------------------------------------------#
 
ventana = tk.Tk()
ventana.title("Sistema de Control")
ventana.geometry("500x350")
ventana.config(background="#285c27")


label_T = tk.Label(ventana, text="Store the Chaparritos", font=("Impact", 30), bg="#285c27", fg="white")
label_T.pack(pady=30)

label_User = tk.Label(ventana, text="USUARIO", font=("Tahoma", 13, "bold"), bg="#285c27", fg="white")
label_User.pack()
entryUser = tk.Entry(ventana, width=20, font=("Verdana", 10, "bold"))
entryUser.pack(pady=5)

label_Pass = tk.Label(ventana, text="CONTRASEÑA", font=("Tahoma", 13, "bold"), bg="#285c27", fg="white")
label_Pass.pack()
entryPass = tk.Entry(ventana, width=20, font=("Verdana", 10, "bold"), show="*")  
entryPass.pack(pady=5)


frame_botones = tk.Frame(ventana, bg="#285c27")
frame_botones.pack(pady=20)

def Ingreso():
    user = entryUser.get()
    password = entryPass.get()
    
    if validarUser(user, password):
        
        ventana.withdraw()
        ventana2.deiconify()
        
    else:
        messagebox.showerror("", f"Usuario o Contraseña Incorrecto") 

botonA = tk.Button(frame_botones, text="ACEPTAR", command=Ingreso, width=12, font=("Arial Black", 10), bg="#fafbfd")
botonA.grid(row=0, column=0, padx=10)

botonC = tk.Button(frame_botones, text="CANCELAR", command=lambda: limpiarEntry(ventana), width=12, font=("Arial Black", 10), bg="#fafbfd")
botonC.grid(row=0, column=1, padx=10)

#-----------------------------------------------------------------------------------------------------------------------------------------------#

ventana2 = tk.Toplevel()
ventana2.title("Sistema de Control")
ventana2.geometry("500x350")
ventana2.config(background="#285c27")
ventana2.withdraw()


def avanzarV3():
    ventana2.withdraw()  #oculta la ventana sin cerrarla
    ventana3.deiconify() #mostrar la ventana oculta
    
def avanzarV4():
    ventana2.withdraw() 
    ventana4.deiconify()
    
def atrasV1():
    ventana2.withdraw() 
    ventana.deiconify()
    

label_T2 = tk.Label(ventana2, text="Store the Chaparritos", font=("Impact", 30), bg="#285c27", fg="white")
label_T2.pack(pady=30)

boton_Produc = tk.Button(ventana2, text="PRODUCTOS", command=avanzarV3, font=("Verdana", 13, "bold"), bg="#e1f6e2", width=20)
boton_Produc.pack(pady=20)

boton_Invent = tk.Button(ventana2, text="INVENTARIO DE PRODUCTOS", command=avanzarV4, font=("Verdana", 13, "bold"), bg="#e1f6e2", width=25)
boton_Invent.pack(pady=20)


boton_Atras1 = tk.Button(ventana2, text="atrás", command=atrasV1, font=("Oswald", 10, "bold"), bg="White", width=10)
boton_Atras1.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)

#-----------------------------------------------------------------------------------------------------------------------------------------------#

ventana3 = tk.Toplevel()
ventana3.title("Sistema de Control")
ventana3.geometry("650x500")
ventana3.config(background="#285c27")
ventana3.withdraw()


def atrasV2():
    ventana3.withdraw()  
    ventana2.deiconify()


label_T3 = tk.Label(ventana3, text="PRODUCTOS", font=("Impact", 30), bg="#285c27", fg="white")
label_T3.pack(pady=20)


frame_V3 = tk.Frame(ventana3, bg="#285c27")
frame_V3.pack(pady=15)


label_C = tk.Label(frame_V3, text="CÓDIGO", font=("Tahoma", 13, "bold"), bg="#285c27", fg="white")
label_C.grid(column=0, row=0, padx=10, pady=5, sticky="w")
entryC = tk.Entry(frame_V3, width=30, font=("Verdana", 10, "bold"))
entryC.grid(column=1, row=0, padx=10, pady=5)

label_D = tk.Label(frame_V3, text="DESCRIPCIÓN", font=("Tahoma", 13, "bold"), bg="#285c27", fg="white")
label_D.grid(column=0, row=1, padx=10, pady=5, sticky="w")
entryD = tk.Entry(frame_V3, width=30, font=("Verdana", 10, "bold"))
entryD.grid(column=1, row=1, padx=10, pady=5)

label_U = tk.Label(frame_V3, text="UNIDAD DE MEDIDA", font=("Tahoma", 13, "bold"), bg="#285c27", fg="white")
label_U.grid(column=0, row=2, padx=10, pady=5, sticky="w")
entryU = tk.Entry(frame_V3, width=30, font=("Verdana", 10, "bold"))
entryU.grid(column=1, row=2, padx=10, pady=5)

label_P = tk.Label(frame_V3, text="PRESENTACIÓN", font=("Tahoma", 13, "bold"), bg="#285c27", fg="white")
label_P.grid(column=0, row=3, padx=10, pady=5, sticky="w")
entryP = tk.Entry(frame_V3, width=30, font=("Verdana", 10, "bold"))
entryP.grid(column=1, row=3, padx=10, pady=5)

label_PV = tk.Label(frame_V3, text="PRECIO", font=("Tahoma", 13, "bold"), bg="#285c27", fg="white")
label_PV.grid(column=0, row=4, padx=10, pady=5, sticky="w")
entryPv = tk.Entry(frame_V3, width=30, font=("Verdana", 10, "bold"))
entryPv.grid(column=1, row=4, padx=10, pady=5)

label_E = tk.Label(frame_V3, text="ESTADO", font=("Tahoma", 13, "bold"), bg="#285c27", fg="white")
label_E.grid(column=0, row=5, padx=10, pady=5, sticky="w")
entryE = tk.Entry(frame_V3, width=30, font=("Verdana", 10, "bold"))
entryE.grid(column=1, row=5, padx=10, pady=5)

label_F = tk.Label(frame_V3, text="FECHA", font=("Tahoma", 13, "bold"), bg="#285c27", fg="white")
label_F.grid(column=0, row=6, padx=10, pady=5, sticky="w")
entryF = tk.Entry(frame_V3, width=30, font=("Verdana", 10, "bold"))
entryF.grid(column=1, row=6, padx=10, pady=5)


frame_bV3 = tk.Frame(ventana3, bg="#285c27")  
frame_bV3.pack(pady=15)


def AddP():
    codigo = entryC.get()
    codigo = entryC.get()
    descripcion = entryD.get()
    unidad = entryU.get()
    presentacion = entryP.get()
    precio = entryPv.get()
    estado = entryE.get()
    fecha = entryF.get()
    
    if not all([codigo, descripcion, precio, estado, fecha]):
        messagebox.showerror("", "Debe llenar todos los datos")
        return
    
    if agregarP(codigo, descripcion, unidad, presentacion, precio, estado, fecha):
        messagebox.showinfo("", "Se agregó el producto")
    else:
        messagebox.showerror("", "No se agregó el producto")

botonA = tk.Button(frame_bV3, text="AGREGAR", command=AddP, width=12, font=("Arial Black", 10), bg="#fafbfd")
botonA.grid(column=0, row=0, padx=10)


def ModP():
    codigo = entryC.get() 
    descripcion = entryD.get()
    unidad = entryU.get()
    presentacion = entryP.get()
    precio = entryPv.get()
    estado = entryE.get()
    fecha = entryF.get()
    
    if modificarP(codigo, descripcion, unidad, presentacion, precio, estado, fecha):
        messagebox.showinfo("", "Se modificó el producto")
    else:
        messagebox.showerror("", "No se modificó el producto")

botonM = tk.Button(frame_bV3, text="MODIFICAR", command=ModP, width=12, font=("Arial Black", 10), bg="#fafbfd")
botonM.grid(column=1, row=0, padx=10)  


def ElimP():
    codigo = entryC.get()
    
    if eliminarP(codigo):
        messagebox.showinfo("", "Producto eliminado")
    else:
        messagebox.showerror("", "No se pudo eliminar")

botonE = tk.Button(frame_bV3, text="ELIMINAR", command=ElimP, width=12, font=("Arial Black", 10), bg="#fafbfd")
botonE.grid(column=2, row=0, padx=10)  

botonL = tk.Button(frame_bV3, text="LIMPIAR", command=lambda: limpiarEntry(ventana3), width=12, font=("Arial Black", 10), bg="#fafbfd")
botonL.grid(column=3, row=0, padx=10) 


boton_Atras2 = tk.Button(ventana3, text="atrás", command=atrasV2, font=("Oswald", 10, "bold"), bg="White", width=10)
boton_Atras2.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)

#-----------------------------------------------------------------------------------------------------------------------------------------------#

ventana4 = tk.Toplevel()
ventana4.title("Sistema de Control")
ventana4.geometry("850x550")
ventana4.config(background="#285c27")
ventana4.withdraw()


def atrasV3():
    ventana4.withdraw() 
    ventana2.deiconify()
        

label_T5 = tk.Label(ventana4, text="PRODUCTOS", font=("Impact", 30), bg="#285c27", fg="white")
label_T5.pack(pady=25)


frame_V4 = tk.Frame(ventana4, bg="#285c27")
frame_V4.pack(pady=10)


label_C2 = tk.Label(frame_V4, text="CÓDIGO", font=("Tahoma", 13, "bold"), bg="#285c27", fg="white")
label_C2.grid(column=0, row=0, padx=10, pady=5, sticky="w")
entryC2 = tk.Entry(frame_V4, width=20, font=("Verdana", 10, "bold"))
entryC2.grid(column=1, row=0, padx=10, pady=5)

label_F2 = tk.Label(frame_V4, text="FECHA", font=("Tahoma", 13, "bold"), bg="#285c27", fg="white")
label_F2.grid(column=2, row=0, padx=10, pady=5, sticky="w")
entryF2 = tk.Entry(frame_V4, width=20, font=("Verdana", 10, "bold"))
entryF2.grid(column=3, row=0, padx=10, pady=5)

label_D2 = tk.Label(frame_V4, text="DESCRIPCIÓN", font=("Tahoma", 13, "bold"), bg="#285c27", fg="white")
label_D2.grid(column=0, row=2, padx=10, pady=5, sticky="w")
entryD2 = tk.Entry(frame_V4, width=20, font=("Verdana", 10, "bold"))
entryD2.grid(column=1, row=2, padx=10, pady=5)


frame_bV4 = tk.Frame(ventana4, bg="#285c27")
frame_bV4.pack(pady=15)


def BuscarPoductos():
    codigo = entryC2.get()
    descripcion = entryD2.get() 
    fecha = entryF2.get() 
    
    productos = buscarP_CDF(codigo=codigo, descripcion=descripcion, fecha=fecha)
    
    if productos is False:
        messagebox.showerror("", "No se pudo realizar la búsqueda")
    elif productos:  
        for item in tree.get_children(): #obtiene la lista de la fila
            tree.delete(item) #elimina restos de busquedas anteriores
        
        for producto in productos:
            tree.insert("", "end", values=producto) #insertar elementos al final de la lista
    else:
        messagebox.showinfo("", "No se encontró ningun producto")
    
botonB = tk.Button(frame_bV4, text="BUSCAR", command=BuscarPoductos, width=12, font=("Arial Black", 10), bg="#fafbfd")
botonB.grid(column=0, row=0, padx=10)


botonL2 = tk.Button(frame_bV4, text="LIMPIAR", command=lambda: limpiarEntry(ventana4), width=12, font=("Arial Black", 10), bg="#fafbfd")
botonL2.grid(column=1, row=0, padx=10)


def listarP():
    productos = obtenerProductos()
    
    for item in tree.get_children():
        tree.delete(item)
        
    for producto in productos:
        tree.insert("", "end", values=producto)

botonC2 = tk.Button(frame_bV4, text="CANCELAR", command=listarP, width=12, font=("Arial Black", 10), bg="#fafbfd")
botonC2.grid(column=2, row=0, padx=10)


tree = ttk.Treeview(ventana4, columns=("Id", "Código", "Descripción", "Unidad", "Presentación", "Precio", "Estado", "Fecha"), show="headings") 

tree.heading("Id", text="ID")
tree.heading("Código", text="CÓDIGO")
tree.heading("Descripción", text="DESCRIPCIÓN")
tree.heading("Unidad", text="UNIDAD DE MEDIDA")
tree.heading("Presentación", text="PRESENTACIÓN")
tree.heading("Precio", text="PRECIO")
tree.heading("Estado", text="ESTADO")
tree.heading("Fecha", text="FECHA")

tree.column("Id", width=50)                    
tree.column("Código", width=70)               
tree.column("Descripción", width=150)         
tree.column("Unidad", width=150)              
tree.column("Presentación", width=100)        
tree.column("Precio", width=70)              
tree.column("Estado", width=70)               
tree.column("Fecha", width=70)

tree.pack()
listarP()


boton_Atras3 = tk.Button(ventana4, text="atrás", command=atrasV3, font=("Oswald", 10, "bold"), bg="White", width=10)
boton_Atras3.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)

ventana.mainloop()