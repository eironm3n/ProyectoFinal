"""Módulo que contiene la clase principal del modelo"""

import os
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import sqlite3
import re


class Model:
    """Clase principal del modelo"""

    def __init__(self, tree, root):
        self.var_id = StringVar()
        self.var_producto = StringVar()
        self.var_cantidad = IntVar()
        self.var_precio = IntVar()
        self.tree = tree
        self.root = root

    def conexion_db(self):
        """Crea la base de datos"""
        mi_conexion = sqlite3.connect("base.db")
        mi_cursor = mi_conexion.cursor()
        try:
            mi_cursor.execute('''CREATE TABLE planilla(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            PRODUCTO VARCHAR(80) NOT NULL,
            CANTIDAD INT(4) NOT NULL,
            PRECIO INT NOT NULL)''')
            messagebox.showinfo(
                "CONEXION", "Base de Datos Creada exitosamente")
        except sqlite3.OperationalError:
            messagebox.showinfo(
                "CONEXION", "La base de datos ya existe")

    def limpiar_campos(self):
        """Limpia los campos de entrada"""
        self.var_id.set("")
        self.var_producto.set("")
        self.var_cantidad.set("")
        self.var_precio.set("")

    def insertar(self):
        """Inserta un registro"""
        mi_conexion = sqlite3.connect("base.db")
        mi_cursor = mi_conexion.cursor()
        try:
            datos = self.var_producto.get(), self.var_cantidad.get(), self.var_precio.get()
            mi_cursor.execute("INSERT INTO planilla VALUES(NULL,?,?,?)", datos)
            mi_conexion.commit()
        except sqlite3.OperationalError:
            messagebox.showwarning(
                "AVERTENCIA", "Ocurrió un error al crear el registro")
        self.limpiar_campos()
        self.mostrar()

    def borrar(self):
        """Borra un registro"""
        mi_conexion = sqlite3.connect("base.db")
        mi_cursor = mi_conexion.cursor()
        try:
            if messagebox.askyesno(title="ADVERTENCIA",
                                   message="¿Realmente desea eliminar el registro?"):
                mi_cursor.execute(
                    "DELETE FROM planilla WHERE ID=" + self.var_id.get())
                mi_conexion.commit()

        except sqlite3.OperationalError:
            messagebox.showwarning(
                title="ADVERTENCIA", message="Ocurrió un error al eliminar el registro")
        self.limpiar_campos()
        self.mostrar()

    def actualizar(self):
        """Actualiza los datos de un registro"""
        mi_conexion = sqlite3.connect("base.db")
        mi_cursor = mi_conexion.cursor()
        try:
            datos = self.var_producto.get(), self.var_cantidad.get(), self.var_precio.get()
            mi_cursor.execute(
                'UPDATE planilla SET PRODUCTO=?, CANTIDAD=?,\
                      PRECIO=? WHERE ID=' + self.var_id.get(), (datos), )
            mi_conexion.commit()
        except sqlite3.OperationalError:
            messagebox.showwarning(
                "ADVERTENCIA", "Ocurrió un error al actualizar el registro")
        self.limpiar_campos()
        self.mostrar()

    def buscar(self):
        """Busca un registro"""
        mi_conexion = sqlite3.connect("base.db")
        mi_cursor = mi_conexion.cursor()

        # Obtener el patrón de búsqueda
        patron = simpledialog.askstring(
            "Buscar", "Introduzca el patrón de búsqueda:")

        # Buscar los registros por nombre de producto
        registros = mi_cursor.execute('SELECT * FROM planilla')
        resultados = []
        for registro in registros:
            if re.search(patron, registro[1]):
                resultados.append(registro)

        # Borrar los registros de la tabla
        for elemento in self.tree.get_children():
            self.tree.delete(elemento)

        # Insertar los registros de la lista de resultados en la tabla
        for resultado in resultados:
            self.tree.insert("", 0, text=resultado[0], values=(
                resultado[1], resultado[2], resultado[3]))

    def seleccionar_usando_click(self, event):
        """Selecciona un registro de la tabla usando el doble click del mouse"""
        self.limpiar_campos()
        item = self.tree.selection()[0]
        self.var_id.set(self.tree.item(item, "text"))
        self.var_producto.set(self.tree.item(item, "values")[0])
        self.var_cantidad.set(self.tree.item(item, "values")[1])
        self.var_precio.set(self.tree.item(item, "values")[2])

    def eliminar_db(self):
        """Elimina la base de datos"""
        mi_conexion = sqlite3.connect("base.db")
        db_file = "base.db"
        if os.path.exists(db_file):
            if messagebox.askyesno(message="Los datos se perderán definitivamente, ¿Desea continuar?",
                                   title="ADVERTENCIA"):
                mi_conexion.close()
                os.remove(db_file)
                messagebox.showinfo(
                    "Base de Datos Eliminada", "La base de datos ha sido eliminada exitosamente")
            else:
                messagebox.showinfo(
                    "Eliminación Cancelada", "La eliminación de la base de datos ha sido cancelada")
        else:
            messagebox.showinfo("Base de Datos No Encontrada",
                                "La base de datos no existe")

    def drop_table(self):
        """Elimina la tabla planilla"""
        mi_conexion = sqlite3.connect("base.db")
        mi_cursor = mi_conexion.cursor()
        if messagebox.askyesno(message="Se borrara la tabla planilla,¿Desea continuar?",
                               title="ADVERTENCIA",):
            mi_cursor.execute("DROP TABLE planilla")
        else:
            pass
        self.limpiar_campos()
        self.mostrar()

    def salir_aplicacion(self):
        """Cierra la aplicación"""
        valor = messagebox.askquestion(
            "Salir", "Esta seguro que desea salir de la aplicación")
        if valor == "yes":
            self.root.destroy()

    def mostrar(self):
        """Muestra los registros en la tabla"""
        mi_conexion = sqlite3.connect("base.db")
        mi_cursor = mi_conexion.cursor()
        registros = self.tree.get_children()
        for elemento in registros:
            self.tree.delete(elemento)
        try:
            mi_cursor.execute("SELECT * FROM planilla")
            for row in mi_cursor:
                self.tree.insert("", 0, text=row[0], values=(
                    row[1], row[2], row[3]))
        except sqlite3.OperationalError:
            pass
