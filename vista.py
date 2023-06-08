from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from modelo import Modelo

class Ventana():
    def __init__(self, windows, color1, color2, color3):
        self.obj_de_modelo= Modelo()
        self.master=windows
        self.master.title("Stock All")
        self.master.geometry("600x350")
        self.master.configure(bg="#DBE543")

        # Se movieron hacia modelo, pero no entiendo por que no las reconoce
        #var_id = StringVar()
        #var_producto = StringVar()
        #var_cantidad = IntVar()
        #var_precio = IntVar()
        
        # columnas  
        self.tree["columns"] = ("ID","PRODUCTO","CANTIDAD","PRECIO",)
        self.tree = ttk.Treeview(self.master)


        self.tree = ttk.Treeview(height=10, columns=("#0", "#1", "#2", "#3"))
        self.tree.place(x=0, y=130)
        self.tree.column("#0", width=100)
        self.tree.heading("#0", text="ID", anchor=CENTER)
        self.tree.heading("#1", text="Producto", anchor=CENTER)
        self.tree.heading("#2", text="Cantidad", anchor=CENTER)
        self.tree.column("#3", width=100)
        self.tree.heading("#3", text="Precio ($)", anchor=CENTER)
        self.tree.bind("<Button-1>", self.obj_de_modelo.seleccionarUsandoClick)
        menubar = Menu(self.master)
        menubasedat = Menu(menubar, tearoff=0)
        menubasedat.add_command(label="Crear/Conectar Base de Datos", command=self.obj_de_modelo.conexionBD(messagebox))
        menubasedat.add_command(label="Eliminar Base de Datos", command=self.obj_de_modelo.eliminarBD)
        menubasedat.add_command(label="Salir", command=self.obj_de_modelo.salirAplicacion)
        menubar.add_cascade(label="Inicio", menu=menubasedat)
        temasmenu = Menu(menubar, tearoff=0)
        temasmenu.add_command(label="Opcion 1", command=color1)
        temasmenu.add_command(label="Opcion 2", command=color2)
        temasmenu.add_command(label="Opcion 3", command=color3)
        menubar.add_cascade(label="Temas", menu=temasmenu)
        ayudamenu = Menu(menubar, tearoff=0)
        ayudamenu.add_command(label="Resetear Campos", command=self.obj_de_modelo.limpiarCampos)
        ayudamenu.add_command(label="Acerca de..", command=mensaje)
        menubar.add_cascade(label="Ayuda", menu=ayudamenu)
        e1 = Entry(self.master, textvariable=var_id)
        l2 = Label(self.master, text="Producto")
        l2.place(x=50, y=10)
        e2 = Entry(self.master, textvariable=var_producto, width=50)
        e2.place(x=110, y=10)
        l3 = Label(self.master, text="Cantidad")
        l3.place(x=50, y=40)
        e3 = Entry(self.master, textvariable=var_cantidad)
        e3.place(x=110, y=40)
        l4 = Label(self.master, text="Precio")
        l4.place(x=280, y=40)
        e4 = Entry(self.master, textvariable=var_precio, width=10)
        e4.place(x=320, y=40)
        l5 = Label(self.master, text="$")
        l5.place(x=380, y=40)
        b1 = Button(self.master, text="Crear Registro", command=self.obj_de_modelo.crear, bg="#919826", fg="#F8F8FA")
        b1.place(x=30, y=90)
        b2 = Button(self.master, text="Modificar Registro", command=self.obj_de_modelo.actualizar, bg="#919826", fg="#F8F8FA")
        b2.place(x=130, y=90)
        b3 = Button(self.master, text="Mostrar Lista", command=self.obj_de_modelo.mostrar, bg="#919826", fg="#F8F8FA")
        b3.place(x=250, y=90)
        b4 = Button(self.master, text="Eliminar Registro", command=self.obj_de_modelo.borrar, bg="#919826", fg="#F8F8FA")
        b4.place(x=340, y=90)
        b5 = Button(self.master, text="Buscar", command=self.obj_de_modelo.buscar, bg="#919826", fg="#F8F8FA")
        b5.place(x=450, y=90)
        self.master.config(menu=menubar)

  #     ####################
  #     # Temas de colores #
  #     ####################

        #color1 - amarillo
    def color1(self, b1, b2, b3, b4, b5):
        self.configure(bg="#DBE543")
        b1.configure(bg="#919826", fg="#F8F8FA")
        b2.configure(bg="#919826", fg="#F8F8FA")
        b3.configure(bg="#919826", fg="#F8F8FA")
        b4.configure(bg="#919826", fg="#F8F8FA")
        b5.configure(bg="#919826", fg="#F8F8FA")


        #color2 - celeste
    def color2(self, b1, b2, b3, b4, b5):
        self.configure(bg="#46EAE3")
        b1.configure(bg="#176E6A", fg="#F8F8FA")
        b2.configure(bg="#176E6A", fg="#F8F8FA")
        b3.configure(bg="#176E6A", fg="#F8F8FA")
        b4.configure(bg="#176E6A", fg="#F8F8FA")
        b5.configure(bg="#176E6A", fg="#F8F8FA")

        #color3 - lila
    def color3(self, b1, b2, b3, b4, b5):
        self.configure(bg="#9E89F3")
        b1.configure(bg="#554599", fg="#F8F8FA")
        b2.configure(bg="#554599", fg="#F8F8FA")
        b3.configure(bg="#554599", fg="#F8F8FA")
        b4.configure(bg="#554599", fg="#F8F8FA")
        b5.configure(bg="#554599", fg="#F8F8FA")