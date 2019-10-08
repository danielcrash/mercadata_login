from tkinter import *
import os
import tkinter as tk

def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def delete5():
    screen10.destroy()

def logout():
    screen7.destroy()

def saved():
    global screen10
    screen10 = Toplevel(screen)
    screen10.title("Salvando")
    screen10.geometry("100x100")
    Label(screen10, text = "Salvo!").pack()
    Button(screen10, text = "OK", command = delete5).pack()

def save():
    filename = raw_filename.get()
    notes = raw_notes.get()

    data = open(filename, "w")
    data.write(notes)
    data.close()

    saved()

def create_notes():
    global raw_filename
    raw_filename = StringVar()
    global raw_notes
    raw_notes = StringVar()

    screen9 = Toplevel(screen)
    screen9.title("Informação")
    screen9.geometry("300x250")
    Label(screen9, text = "Entre com o nome do arquivo: ").pack()
    Entry(screen9, textvariable = raw_filename).pack()
    Label(screen9, text = "Entre com as notas do arquivo: ").pack()
    Entry(screen9, textvariable = raw_notes).pack()
    Button(screen9, text = "Salvar", command = save).pack()

def view_notes1():
    filename1 = raw_filename1.get()
    data = open(filename1, "r")
    data1 = data.read()
    screen12 = Toplevel(screen)
    screen12.title("Conteudo do arquivo")
    screen12.geometry("400x400")
    Label(screen12, text = data1).pack()
    

    
def view_notes():
    screen11 = Toplevel(screen)
    screen11.title("Informação")
    screen11.geometry("250x250")
    all_files = os.listdir()
    Label(screen11, text = "Use um dos arquivos abaixo").pack()
    Label(screen11, text = all_files).pack()
    global raw_filename1
    raw_filename1 = StringVar()
    Entry(screen11, textvariable=raw_filename1).pack()
    Button(screen11, command=view_notes1, text = "OK").pack()

def delete_note1():
    filename3 = raw_filename2.get()
    os.remove(filename3)
    screen14 = Toplevel(screen)
    screen14.title("Removendo conteudo do arquivo")
    screen14.geometry("400x400")
    Label(screen14, text = filename3+" removido").pack()
    

def delete_note():
    screen13 = Toplevel(screen)
    screen13.title("Informação")
    screen13.geometry("250x250")
    all_files = os.listdir()
    Label(screen13, text = "Remova um dos arquivos abaixo").pack()
    Label(screen13, text = all_files).pack()
    global raw_filename2
    raw_filename2 = StringVar()
    Entry(screen13, textvariable=raw_filename2).pack()
    Button(screen13, command=delete_note1, text = "OK").pack()

    
def session():
    screen8 = Toplevel(screen)
    screen8.title("dashboard")
    screen8.geometry("400x400")
    Label(screen8, text = "Bem vindo a dashboard").pack()
    Button(screen8, text = "Criar notas", command = create_notes).pack()
    Button(screen8, text = "Vizualizar notas", command = view_notes).pack()
    Button(screen8, text = "Deletar nota", command = delete_note).pack()

def login_sucess():
    #global screen3
    #screen3 = Toplevel(screen)
    #screen3.title("sucess")
    #screen3.geometry("150x100")
    #Label(screen3, text = "Login Efetuado").pack()
    #Label(screen3, text = "").pack()
    #Button(screen3, text = "OK", command = delete2).pack()
    session()

def senha_incorreta():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("sucess")
    screen4.geometry("150x100")
    Label(screen4, text = "Senha incorreta!").pack()
    Label(screen4, text = "").pack()
    Button(screen4, text = "OK", command = delete3).pack()

def usuario_n_encontrado():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("sucess")
    screen5.geometry("150x100")
    Label(screen5, text = "Usuário não encontrado!").pack()
    Label(screen5, text = "").pack()
    Button(screen5, text = "OK", command = delete4).pack()

def registro_user():
    print("working3")
    
    usuario_info = usuario.get()
    senha_info = senha.get()

    file=open(usuario_info, "w")
    file.write(usuario_info+"\n")
    file.write(senha_info)
    file.close()

    usuario_entry.delete(0, END)
    senha_entry.delete(0, END)

    Label(screen1, text = "Registrado com sucesso!", fg = "green", font = ("calibri", 11)).pack()

def login_verify():
    usuario1 = usuario_verify.get()
    senha1 = senha_verify.get()
    usuario_entry1.delete(0, END)
    senha_entry1.delete(0, END)

    list_of_files = os.listdir()
    if usuario1 in list_of_files:
        file1 = open(usuario1, "r")
        verify = file1.read().splitlines()
        if senha1 in verify:
            login_sucess()
        else:
            senha_incorreta()
    else:
        usuario_n_encontrado()



def registro():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Registrar")
    screen1.geometry("300x250")
    
    global usuario
    global senha
    global usuario_entry
    global senha_entry
    usuario = StringVar()
    senha = StringVar()

    Label(screen1, text = "Por favor, preencher abaixo").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Nome de usuário * ").pack()
    
    usuario_entry = Entry(screen1, textvariable = usuario)
    usuario_entry.pack()
    Label(screen1, text = "Senha * ").pack()
    senha_entry = Entry(screen1, textvariable = senha)
    senha_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Registro", width = 10, height = 1, command = registro_user).pack()

    
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text = "Por favor, preencher abaixo seu login").pack()
    Label(screen2, text = "").pack()

    global usuario_verify
    global senha_verify
    
    usuario_verify = StringVar()
    senha_verify = StringVar()

    global usuario_entry1
    global senha_entry1
    
    Label(screen2, text = "Usuário * ").pack()
    usuario_entry1 = Entry(screen2, textvariable = usuario_verify)
    usuario_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Senha * ").pack()
    senha_entry1 = Entry(screen2, textvariable = senha_verify)
    senha_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
    

def main_screen():
    global screen
    screen = tk.Tk()
    screen.geometry("300x250")
    screen.title("Login Mercadata")
    photo = tk.PhotoImage(file="myfile.png")
    Label = tk.Label(screen, text = "Login Mercadou", width = "251", height = "70", bg = 'white', font = ("Calibri", 13), image=photo).pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Button(text = "Registrar", height = "2", width = "30", command = registro).pack()

    screen.mainloop()
main_screen()
