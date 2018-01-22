from Tkinter import *
root = Tk()
root.title('formulario 1')
# Row1: Título
# Row2: Espacio
# Row3: Numero de Cuenta
# Row4: Nombre de Cuenta
# Row5: Espacio
# Row6: Botones Aceptar, Borrar, Cerrar
# Row7: Espacio
# Row8: Nivel 


# row 1 : the name
nombre_label = Label(root,text="Nombre :")
nombre_label.grid(row=1,column=1)
nombre_str = StringVar()
nombre_entry = Entry(root,textvariable=nombre_str)
nombre_entry.grid(row=1,column=2)
#row 2 : the last name
last_label= Label(root,text="Apellido : ")
last_label.grid(row=2,column=1)
last_str = StringVar()
last_entry = Entry(root,textvariable=last_str)
last_entry.grid(row=2,column=2)
#row 3 : the email
mail_label = Label(root,text="Email : ")
mail_label.grid(row=3,column=1)
mail_str = StringVar()
mail_entry = Entry(root,textvariable=mail_str)
mail_entry.grid(row=3,column=2)
#row 4 : end
finish = Button(root,text="finalizar",relief=FLAT)
finish.grid(row=4,column=2)
root.mainloop()