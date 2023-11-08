from tkinter import *
from PIL import Image, ImageTk
import sys
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

import os
from tkinter import messagebox  

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from controllers.controllerUser import ControllerUser

class View:
  def __init__(self):
    self.root = tk.Tk()
    self.controllerUser = ControllerUser(self)

    self.root.title("Sistemas Operacionais")
    self.root.geometry("1000x680")
    self.root.resizable(False,False)
    self.container =tk.Frame(self.root)
    self.container.pack()

    self.loginScreen()
    self.loginScreen.grid(row=0, column=0, sticky="nsew") 

    self.registerScreen()
    self.registerScreen.grid(row=0, column=0, sticky="nsew")

    self.mainScreen()
    self.mainScreen.grid(row=0, column=0, sticky="nsew")

    self.showMainScreen()

    self.root.mainloop()

  def showLoginScreen(self):
    self.clearAllFieldsLogin()
    self.loginScreen.tkraise()

  def showRegisterScreen(self):
    self.registerScreen.tkraise()

  def showMainScreen(self):
    self.mainScreen.tkraise()

  def loginScreen(self):
    self.loginScreen = tk.Frame(self.container)

    imgLogoIFPR = ImageTk.PhotoImage(Image.open("./images/logo-ifpr.png"))
    bannerIFPR = tk.Label(self.loginScreen, image=imgLogoIFPR)
    bannerIFPR.image = imgLogoIFPR
    bannerIFPR.grid(row=0, pady=20)

    #USERNAME LOGIN
    userFrame = tk.Frame(self.loginScreen)
    userFrame.grid(row=1, pady=20)

    imgIconUser = ImageTk.PhotoImage(Image.open("./images/icon-user.png"))
    iconUser = tk.Label(userFrame, image=imgIconUser)
    iconUser.image = imgIconUser    
    iconUser.grid(row=0, column=0)

    self.user_entry = Entry(userFrame, highlightthickness=1, background="white", width=18 ,highlightbackground="black", font=('Arial', 28))
    self.user_entry.grid(row=0, column=1) 
    # self.user_entry.insert(0, "Usuário")

    #PASSWORD LOGIN
    passwordFrame = tk.Frame(self.loginScreen)
    passwordFrame.grid(row=2)

    imgIconPassword = ImageTk.PhotoImage(Image.open("./images/icon-password.png"))
    iconPassword = tk.Label(passwordFrame, image=imgIconPassword)
    iconPassword.image = imgIconPassword
    iconPassword.grid(row=0, column=0)

    self.password_entry = Entry(passwordFrame, highlightthickness=1, background="white", width=18, highlightbackground="black", font=('Arial', 28), show="•")
    self.password_entry.grid(row=0, column=1)
    # self.password_entry.insert(0, "Senha")

    #BUTTON LOGIN
    imgButtonLogin = ImageTk.PhotoImage(Image.open("./images/btn-login.png"))
    button_login = tk.Button(self.loginScreen, image=imgButtonLogin, borderwidth=0, cursor="hand2", command=self.loginUser)
    button_login.image = imgButtonLogin
    button_login.grid(row=3, pady=20)

    labelCadastro = tk.Frame(self.loginScreen)
    labelCadastro.grid(row=4, pady=10)

    label = tk.Label(labelCadastro, text="Não possui uma conta?", font=('Arial', 16))
    label.grid(row=0)

    labelCadastro = tk.Button(labelCadastro, text="Cadastre-se", font=('Arial', 16), borderwidth=0, foreground='#047CFC', cursor="hand2", command=self.showRegisterScreen)
    labelCadastro.grid(row=0, column=1)



  def registerScreen(self):
    self.registerScreen = tk.Frame(self.container)

    imgLogoIFPR = ImageTk.PhotoImage(Image.open("./images/logo-ifpr.png"))
    bannerIFPR = tk.Label(self.registerScreen, image=imgLogoIFPR)
    bannerIFPR.image = imgLogoIFPR
    bannerIFPR.grid(row=0, pady=20)

    #USERNAME REGISTER
    userNameFrame = tk.Frame(self.registerScreen)
    userNameFrame.grid(row=1, pady=10)

    imgIconUser = ImageTk.PhotoImage(Image.open("./images/icon-user.png"))
    iconUser = tk.Label(userNameFrame, image=imgIconUser)
    iconUser.image = imgIconUser
    iconUser.grid(row=0, column=0)

    self.userName_entry = Entry(userNameFrame, highlightthickness=1, background="white", width=18, highlightbackground="black", font=('Arial', 28))
    self.userName_entry.grid(row=0, column=1)

    #PASSWORD REGISTER
    passwordFrame = tk.Frame(self.registerScreen)
    passwordFrame.grid(row=2, pady=10)

    imgIconPassword = ImageTk.PhotoImage(Image.open("./images/icon-password.png"))
    iconPassword = tk.Label(passwordFrame, image=imgIconPassword)
    iconPassword.image = imgIconPassword
    iconPassword.grid(row=0, column=0)

    self.newPassword_entry = Entry(passwordFrame, highlightthickness=1, background="white", width=18, highlightbackground="black", font=('Arial', 28), show="•")
    self.newPassword_entry.grid(row=0, column=1)

    #CONFIRM PASSWORD REGISTER
    confirmPasswordFrame = tk.Frame(self.registerScreen)
    confirmPasswordFrame.grid(row=3, pady=10)

    imgIconConfirmPassword = ImageTk.PhotoImage(Image.open("./images/icon-confirm-password.png"))
    iconConfirmPassword = tk.Label(confirmPasswordFrame, image=imgIconConfirmPassword)
    iconConfirmPassword.image = imgIconConfirmPassword
    iconConfirmPassword.grid(row=0, column=0)

    self.confirmPassword_entry = Entry(confirmPasswordFrame, highlightthickness=1, background="white", width=18, highlightbackground="black", font=('Arial', 28), show="•")
    self.confirmPassword_entry.grid(row=0, column=1)

    #CUTTONS REGISTER
    imgButtonBack = ImageTk.PhotoImage(Image.open("./images/btn-back.png"))
    button_back = tk.Button(self.registerScreen, image=imgButtonBack, borderwidth=0, cursor="hand2", command=self.showLoginScreen)
    button_back.image = imgButtonBack
    button_back.grid(row=4, pady=10)  

    imgButtonRegister = ImageTk.PhotoImage(Image.open("./images/btn-register.png"))
    button_register = tk.Button(self.registerScreen, image=imgButtonRegister, borderwidth=0, cursor="hand2", command=self.registerUser)
    button_register.image = imgButtonRegister
    button_register.grid(row=5)


  def mainScreen(self):
    self.mainScreen = tk.Frame(self.container)

    registerFrame = tk.Frame(self.mainScreen, width=300, height=680)
    registerFrame.pack(side=LEFT)

    treviewFrame = tk.Frame(self.mainScreen, width=700, height=680)
    treviewFrame.pack(side=RIGHT)

    imgLogoIfpr = ImageTk.PhotoImage(Image.open("./images/logo-ifpr-2.png"))
    bannerIfpr = tk.Label(registerFrame, image=imgLogoIfpr)
    bannerIfpr.image = imgLogoIfpr
    bannerIfpr.place(x=10, y=10)

    labelName = tk.Label(registerFrame, text="Nome:", font=('Arial', 14))
    labelName.place(x=20, y=100)
    self.entryName = Entry(registerFrame, highlightthickness=1, background="white", width=24, highlightbackground="black", font=('Arial', 14))
    self.entryName.place(x=20, y=130)

    labelRegistration = tk.Label(registerFrame, text="Matrícula:", font=('Arial', 14))
    labelRegistration.place(x=20, y=170)
    self.entryRegistration = Entry(registerFrame, highlightthickness=1, background="white", width=24, highlightbackground="black", font=('Arial', 14))
    self.entryRegistration.place(x=20, y=200)

    labelDateOfBirth = tk.Label(registerFrame, text="Data de Nascimento:", font=('Arial', 14))
    labelDateOfBirth.place(x=20, y=240)
    self.entryDateOfBirth = Entry (registerFrame, highlightthickness=1, background="white", width=24, highlightbackground="black", font=('Arial', 14))
    self.entryDateOfBirth.place(x=20, y=270)

    labelPhoto = tk.Label(registerFrame, text="Foto:", font=('Arial', 14))
    labelPhoto.place(x=20, y=310)
    self.photo = ImageTk.PhotoImage(Image.open("./images/icon-photo.png"))
    self.studentPhoto = tk.Label(registerFrame, image=self.photo, width=265)
    self.studentPhoto.image = self.photo
    self.studentPhoto.place(x=20, y=340)

    imgButtonUploadPhoto = ImageTk.PhotoImage(Image.open("./images/btn-upload.png"))
    button_uploadPhoto = tk.Button(registerFrame, image=imgButtonUploadPhoto, borderwidth=0, cursor="hand2", command=self.uploadPhoto)
    button_uploadPhoto.image = imgButtonUploadPhoto
    button_uploadPhoto.place(x=20, y=550)

    imgButtonAdd = ImageTk.PhotoImage(Image.open("./images/btn-add.png"))
    button_add = tk.Button(registerFrame, image=imgButtonAdd, borderwidth=0, cursor="hand2", command=self.registerStudent)
    button_add.image = imgButtonAdd
    button_add.place(x=20, y=600)

    imgLogoIfpr = ImageTk.PhotoImage(Image.open("./images/lista-alunos.png"))
    bannerIfpr = tk.Label(treviewFrame, image=imgLogoIfpr)
    bannerIfpr.image = imgLogoIfpr
    bannerIfpr.place(x=220, y=40)

    self.entrySearch = Entry(treviewFrame, highlightthickness=1, background="white", width=51, highlightbackground="black", font=('Arial', 14))
    self.entrySearch.place(x=20, y=105)

    imgButtonSearch = ImageTk.PhotoImage(Image.open("./images/btn-search.png"))
    button_search = tk.Button(treviewFrame, image=imgButtonSearch, borderwidth=0, cursor="hand2")
    button_search.image = imgButtonSearch
    button_search.place(x=590, y=102)

    columns = ('ID', 'Nome', 'Matrícula', 'Data de Nascimento', 'Foto')
    self.treeview = ttk.Treeview(treviewFrame, columns=columns, show='headings', height=21)
    self.treeview.column('ID', minwidth=0, width=50)
    self.treeview.column('Nome', minwidth=0, width=200)
    self.treeview.column('Matrícula', minwidth=0, width=100)
    self.treeview.column('Data de Nascimento', minwidth=0, width=200)
    self.treeview.column('Foto', minwidth=0, width=100)
    self.treeview.heading('ID', text='ID')
    self.treeview.heading('Nome', text='Nome')
    self.treeview.heading('Matrícula', text='Matrícula')
    self.treeview.heading('Data de Nascimento', text='Data de Nascimento')
    self.treeview.heading('Foto', text='Foto')
    self.treeview.place(x=20, y=140)

    imgButtonRemove = ImageTk.PhotoImage(Image.open("./images/btn-remove.png"))
    button_remove = tk.Button(treviewFrame, image=imgButtonRemove, borderwidth=0, cursor="hand2")
    button_remove.image = imgButtonRemove
    button_remove.place(x=490, y=600)

  def registerUser(self):
    userName = self.userName_entry.get().strip()
    password = self.newPassword_entry.get()
    confirmPassword = self.confirmPassword_entry.get()
    self.controllerUser.registerUser(userName, password, confirmPassword)

  def loginUser(self):
    userName = self.user_entry.get().strip()
    password = self.password_entry.get()
    self.controllerUser.loginUser(userName, password)

  def uploadPhoto(self):
    file_types = [('Jpg files', '*.jpg'), ('PNG files', '*.png')]
    filename = askopenfilename(filetypes=file_types)
    if filename:
      with open(filename, 'rb') as file:
        self.photo_data = file.read()
      self.photo = ImageTk.PhotoImage(Image.open(filename).resize((265, 200)))
      self.studentPhoto.configure(image=self.photo)
      self.studentPhoto.image = self.photo
  
  def registerStudent(self):
    name = self.entryName.get().strip()
    registration = self.entryRegistration.get().strip()
    dateOfBirth = self.entryDateOfBirth.get().strip()
    photo = self.photo_data
    self.controllerUser.registerStudent(name, registration, dateOfBirth, photo)

  def clearAllFieldsLogin(self):
    self.user_entry.delete(0, END)
    self.password_entry.delete(0, END)
    self.userName_entry.delete(0, END)
    self.newPassword_entry.delete(0, END)
    self.confirmPassword_entry.delete(0, END)

  def clearAllFieldsStudent(self):
    self.entryName.delete(0, END)
    self.entryRegistration.delete(0, END)
    self.entryDateOfBirth.delete(0, END)
    self.photo = ImageTk.PhotoImage(Image.open("./images/icon-photo.png"))
    self.studentPhoto.configure(image=self.photo)
    self.studentPhoto.image = self.photo
    

  def showWarningMessage(self, message):
    messagebox.showwarning(title="Error", message=message)

  def showSuccessMessage(self, message):
    messagebox.showinfo(title="Success", message=message)


View()
