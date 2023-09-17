from tkinter import *
from PIL import Image, ImageTk
import sys
import tkinter as tk
import os
from tkinter import messagebox  

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from controllers.controllerUser import ControllerUser

class View:
  def __init__(self):
    self.root = tk.Tk()
    self._controllerUser = ControllerUser(self)

    self.root.title("Sistemas Operacionais")
    self.root.geometry("1000x680")
    # self.root.resizable(False,False)
    self.container =tk.Frame(self.root)
    self.container.pack()

    self.loginScreen()
    self.loginScreen.grid(row=0, column=0, sticky="nsew") 

    self.registerScreen()
    self.registerScreen.grid(row=0, column=0, sticky="nsew")

    self.showLoginScreen()

    self.root.mainloop()

  def showLoginScreen(self):
    self.loginScreen.tkraise()

  def showRegisterScreen(self):
    self.registerScreen.tkraise()

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

    self.user_entry = Entry(userFrame, highlightthickness=1, background="white", highlightbackground="black", font=('Arial', 28))
    self.user_entry.grid(row=0, column=1) 
    self.user_entry.insert(0, "Usuário")

    #PASSWORD LOGIN
    passwordFrame = tk.Frame(self.loginScreen)
    passwordFrame.grid(row=2)

    imgIconPassword = ImageTk.PhotoImage(Image.open("./images/icon-password.png"))
    iconPassword = tk.Label(passwordFrame, image=imgIconPassword)
    iconPassword.image = imgIconPassword
    iconPassword.grid(row=0, column=0)

    self.password_entry = Entry(passwordFrame, highlightthickness=1, background="white", highlightbackground="black", font=('Arial', 28))
    self.password_entry.grid(row=0, column=1)
    self.password_entry.insert(0, "Senha")

    #BUTTON LOGIN
    imgButtonLogin = ImageTk.PhotoImage(Image.open("./images/btn-login.png"))
    button_login = tk.Button(self.loginScreen, image=imgButtonLogin, borderwidth=0)
    button_login.image = imgButtonLogin
    button_login.grid(row=3, pady=20)

    labelCadastro = tk.Frame(self.loginScreen)
    labelCadastro.grid(row=4, pady=10)

    label = tk.Label(labelCadastro, text="Não possui uma conta?", font=('Arial', 16))
    label.grid(row=0)

    labelCadastro = tk.Button(labelCadastro, text="Cadastre-se", font=('Arial', 16), borderwidth=0, foreground='#047CFC', command=self.showRegisterScreen)
    labelCadastro.grid(row=0, column=1)



  def registerScreen(self):
    self.registerScreen = tk.Frame(self.container)

    imgLogoIFPR = ImageTk.PhotoImage(Image.open("./images/logo-ifpr.png"))
    bannerIFPR = tk.Label(self.registerScreen, image=imgLogoIFPR)
    bannerIFPR.image = imgLogoIFPR
    bannerIFPR.grid(row=0, pady=20, ipadx=90)

    #USERNAME REGISTER
    userNameFrame = tk.Frame(self.registerScreen)
    userNameFrame.grid(row=1, pady=10)

    imgIconUser = ImageTk.PhotoImage(Image.open("./images/icon-user.png"))
    iconUser = tk.Label(userNameFrame, image=imgIconUser)
    iconUser.image = imgIconUser
    iconUser.grid(row=0, column=0)

    self.userName_entry = Entry(userNameFrame, highlightthickness=1, background="white", highlightbackground="black", font=('Arial', 28))
    self.userName_entry.grid(row=0, column=1)

    #PASSWORD REGISTER
    passwordFrame = tk.Frame(self.registerScreen)
    passwordFrame.grid(row=2, pady=10)

    imgIconPassword = ImageTk.PhotoImage(Image.open("./images/icon-password.png"))
    iconPassword = tk.Label(passwordFrame, image=imgIconPassword)
    iconPassword.image = imgIconPassword
    iconPassword.grid(row=0, column=0)

    self.newPassword_entry = Entry(passwordFrame, highlightthickness=1, background="white", highlightbackground="black", font=('Arial', 28), show="•")
    self.newPassword_entry.grid(row=0, column=1)

    #CONFIRM PASSWORD REGISTER
    confirmPasswordFrame = tk.Frame(self.registerScreen)
    confirmPasswordFrame.grid(row=3, pady=10)

    imgIconConfirmPassword = ImageTk.PhotoImage(Image.open("./images/icon-confirm-password.png"))
    iconConfirmPassword = tk.Label(confirmPasswordFrame, image=imgIconConfirmPassword)
    iconConfirmPassword.image = imgIconConfirmPassword
    iconConfirmPassword.grid(row=0, column=0)

    self.confirmPassword_entry = Entry(confirmPasswordFrame, highlightthickness=1, background="white", highlightbackground="black", font=('Arial', 28), show="•")
    self.confirmPassword_entry.grid(row=0, column=1)

    #CUTTONS REGISTER
    imgButtonBack = ImageTk.PhotoImage(Image.open("./images/btn-back.png"))
    button_back = tk.Button(self.registerScreen, image=imgButtonBack, borderwidth=0, command=self.showLoginScreen)
    button_back.image = imgButtonBack
    button_back.grid(row=4, pady=10)  

    imgButtonRegister = ImageTk.PhotoImage(Image.open("./images/btn-register.png"))
    button_register = tk.Button(self.registerScreen, image=imgButtonRegister, borderwidth=0)
    button_register.image = imgButtonRegister
    button_register.grid(row=5)



View()
