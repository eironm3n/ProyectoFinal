"""Modulo que contiene la clase Views que contiene los métodos para la interfaz gráfica"""
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from models import Model


class Views:
    """Clase que contiene los métodos para la interfaz gráfica"""

    def __init__(self, main):
        self.root = main
        self.root.title("Control de Stock")
        self.root.geometry("600x350")
        self.root.configure(bg="#DBE543")

        self.tree = ttk.Treeview(height=10, columns=("#0", "#1", "#2", "#3"))
        self.model = Model(self.tree, self.root)
        self.tree.place(x=0, y=130)
        self.tree.column("#0", width=100)
        self.tree.heading("#0", text="ID", anchor=CENTER)
        self.tree.heading("#1", text="Producto", anchor=CENTER)
        self.tree.heading("#2", text="Cantidad", anchor=CENTER)
        self.tree.column("#3", width=100)
        self.tree.heading("#3", text="Precio ($)", anchor=CENTER)

        self.b1 = Button(root, text="Crear Registro",
                         command=self.model.insertar, bg="#919826", fg="#F8F8FA")
        self.b1.place(x=30, y=90)
        self.b2 = Button(root, text="Modificar Registro",
                         command=self.model.actualizar, bg="#919826", fg="#F8F8FA")
        self.b2.place(x=133, y=90)
        self.b4 = Button(root, text="Eliminar Registro",
                         command=self.model.borrar, bg="#919826", fg="#F8F8FA")
        self.b4.place(x=260, y=90)
        self.b5 = Button(root, text="Buscar", command=self.model.buscar,
                         bg="#919826", fg="#F8F8FA")
        self.b5.place(x=380, y=90)

        self.create_widgets()

    def mensaje(self,):
        """Muestra un mensaje de información"""
        acerca = """
        Aplicación CRUD
        Version 1.0
        Tecnología Python Tkinter
        """
        messagebox.showinfo(title="INFORMACIÓN", message=acerca)

    def create_widgets(self):
        """Crea los widgets de la interfaz gráfica"""
        self.create_menu()
        self.create_table()
        self.create_entries_labels()
        self.model.mostrar()

    def create_menu(self):
        """"Crear el menú de la aplicación"""
        menubar = Menu(self.root)
        menubasedat = Menu(menubar, tearoff=0)
        menubasedat.add_command(
            label="Crear/Conectar Base de Datos", command=self.model.conexion_db)
        menubasedat.add_command(
            label="Eliminar Base de Datos", command=self.model.eliminar_db)
        menubasedat.add_command(
            label="Salir", command=self.model.salir_aplicacion)
        menubar.add_cascade(label="Inicio", menu=menubasedat)

        temasmenu = Menu(menubar, tearoff=0)
        temasmenu.add_command(label="Opcion 1", command=self.color1)
        temasmenu.add_command(label="Opcion 2", command=self.color2)
        temasmenu.add_command(label="Opcion 3", command=self.color3)
        menubar.add_cascade(label="Temas", menu=temasmenu)

        ayudamenu = Menu(menubar, tearoff=0)
        ayudamenu.add_command(label="Resetear Campos",
                              command=self.model.limpiar_campos)
        ayudamenu.add_command(label="Acerca de..", command=self.mensaje)
        menubar.add_cascade(label="Ayuda", menu=ayudamenu)

        self.root.config(menu=menubar)

    def create_table(self):
        """Crea la tabla donde se muestran los registros"""

        self.tree.place(x=0, y=130)
        self.tree.column("#0", width=100)
        self.tree.heading("#0", text="ID", anchor=CENTER)
        self.tree.heading("#1", text="Producto", anchor=CENTER)
        self.tree.heading("#2", text="Cantidad", anchor=CENTER)
        self.tree.column("#3", width=100)
        self.tree.heading("#3", text="Precio ($)", anchor=CENTER)
        self.tree.bind("<Button-1>", self.model.seleccionar_usando_click)

    def create_entries_labels(self):
        """Crea los campos de entrada de datos"""
        e1 = Entry(root, textvariable=self.model.var_id)

        l2 = Label(root, text="Producto")
        l2.place(x=50, y=10)
        e2 = Entry(root, textvariable=self.model.var_producto, width=50)
        e2.place(x=110, y=10)

        l3 = Label(root, text="Cantidad")
        l3.place(x=50, y=40)
        e3 = Entry(root, textvariable=self.model.var_cantidad)
        e3.place(x=110, y=40)

        l4 = Label(root, text="Precio")
        l4.place(x=280, y=40)
        e4 = Entry(root, textvariable=self.model.var_precio, width=10)
        e4.place(x=320, y=40)

        l5 = Label(root, text="$")
        l5.place(x=380, y=40)

    def color1(self,):
        """Cambia el color de la interfaz gráfica"""
        root.configure(bg="#DBE543")
        self.b1.configure(bg="#919826", fg="#F8F8FA")
        self.b2.configure(bg="#919826", fg="#F8F8FA")

        self.b4.configure(bg="#919826", fg="#F8F8FA")
        self.b5.configure(bg="#919826", fg="#F8F8FA")

    def color2(self):
        """Tema 2 de la interfaz gráfica"""
        root.configure(bg="#46EAE3")
        self.b1.configure(bg="#176E6A", fg="#F8F8FA")
        self.b2.configure(bg="#176E6A", fg="#F8F8FA")

        self.b4.configure(bg="#176E6A", fg="#F8F8FA")
        self.b5.configure(bg="#176E6A", fg="#F8F8FA")

    def color3(self):
        """Tema 3 de la interfaz gráfica"""
        root.configure(bg="#9E89F3")
        self.b1.configure(bg="#554599", fg="#F8F8FA")
        self.b2.configure(bg="#554599", fg="#F8F8FA")

        self.b4.configure(bg="#554599", fg="#F8F8FA")
        self.b5.configure(bg="#554599", fg="#F8F8FA")


root = Tk()
app = Views(root)
root.mainloop()
