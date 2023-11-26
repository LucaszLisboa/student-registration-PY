from tkinter import *
from PIL import Image, ImageTk
import sys
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox  
from tkcalendar import Calendar, DateEntry
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from controllers.controller import Controller

class View:
  def __init__(self):
    self.root = tk.Tk()
    self.controller = Controller(self)
    self.file_path = None

    self.root.title("Instituto Federal do Paraná - Campus Londrina")
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

    self.showLoginScreen()

    self.root.mainloop()

  def showLoginScreen(self):
    self.clearAllLoginFields()
    self.loginScreen.tkraise()

  def showRegisterScreen(self):
    self.registerScreen.tkraise()

  def showMainScreen(self):
    self.updateStudentsTable()
    self.mainScreen.tkraise()

  def loginScreen(self):
    self.loginScreen = tk.Frame(self.container)

    imgLogoIFPR = ImageTk.PhotoImage(Image.open("./images/interface/logo-ifpr.png"))
    bannerIFPR = tk.Label(self.loginScreen, image=imgLogoIFPR)
    bannerIFPR.image = imgLogoIFPR
    bannerIFPR.grid(row=0, pady=20, padx=360)

    userFrame = tk.Frame(self.loginScreen)
    userFrame.grid(row=1, pady=20)

    imgIconUser = ImageTk.PhotoImage(Image.open("./images/interface/icon-user.png"))
    iconUser = tk.Label(userFrame, image=imgIconUser)
    iconUser.image = imgIconUser    
    iconUser.grid(row=0, column=0)

    self.user_entry = Entry(userFrame, highlightthickness=1, background="white", width=18 ,highlightbackground="black", font=('Arial', 28))
    self.user_entry.grid(row=0, column=1) 

    passwordFrame = tk.Frame(self.loginScreen)
    passwordFrame.grid(row=2)

    imgIconPassword = ImageTk.PhotoImage(Image.open("./images/interface/icon-password.png"))
    iconPassword = tk.Label(passwordFrame, image=imgIconPassword)
    iconPassword.image = imgIconPassword
    iconPassword.grid(row=0, column=0)

    self.password_entry = Entry(passwordFrame, highlightthickness=1, background="white", width=18, highlightbackground="black", font=('Arial', 28), show="•")
    self.password_entry.grid(row=0, column=1)

    imgButtonLogin = ImageTk.PhotoImage(Image.open("./images/interface/btn-login.png"))
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

    imgLogoIFPR = ImageTk.PhotoImage(Image.open("./images/interface/logo-ifpr.png"))
    bannerIFPR = tk.Label(self.registerScreen, image=imgLogoIFPR)
    bannerIFPR.image = imgLogoIFPR
    bannerIFPR.grid(row=0, pady=20, padx=360)

    userNameFrame = tk.Frame(self.registerScreen)
    userNameFrame.grid(row=1, pady=10)

    imgIconUser = ImageTk.PhotoImage(Image.open("./images/interface/icon-user.png"))
    iconUser = tk.Label(userNameFrame, image=imgIconUser)
    iconUser.image = imgIconUser
    iconUser.grid(row=0, column=0)

    self.userName_entry = Entry(userNameFrame, highlightthickness=1, background="white", width=18, highlightbackground="black", font=('Arial', 28))
    self.userName_entry.grid(row=0, column=1)

    passwordFrame = tk.Frame(self.registerScreen)
    passwordFrame.grid(row=2, pady=10)

    imgIconPassword = ImageTk.PhotoImage(Image.open("./images/interface/icon-password.png"))
    iconPassword = tk.Label(passwordFrame, image=imgIconPassword)
    iconPassword.image = imgIconPassword
    iconPassword.grid(row=0, column=0)

    self.newPassword_entry = Entry(passwordFrame, highlightthickness=1, background="white", width=18, highlightbackground="black", font=('Arial', 28), show="•")
    self.newPassword_entry.grid(row=0, column=1)

    confirmPasswordFrame = tk.Frame(self.registerScreen)
    confirmPasswordFrame.grid(row=3, pady=10)

    imgIconConfirmPassword = ImageTk.PhotoImage(Image.open("./images/interface/icon-confirm-password.png"))
    iconConfirmPassword = tk.Label(confirmPasswordFrame, image=imgIconConfirmPassword)
    iconConfirmPassword.image = imgIconConfirmPassword
    iconConfirmPassword.grid(row=0, column=0)

    self.confirmPassword_entry = Entry(confirmPasswordFrame, highlightthickness=1, background="white", width=18, highlightbackground="black", font=('Arial', 28), show="•")
    self.confirmPassword_entry.grid(row=0, column=1)

    imgButtonBack = ImageTk.PhotoImage(Image.open("./images/interface/btn-back.png"))
    button_back = tk.Button(self.registerScreen, image=imgButtonBack, borderwidth=0, cursor="hand2", command=self.showLoginScreen)
    button_back.image = imgButtonBack
    button_back.grid(row=4, pady=10)  

    imgButtonRegister = ImageTk.PhotoImage(Image.open("./images/interface/btn-register.png"))
    button_register = tk.Button(self.registerScreen, image=imgButtonRegister, borderwidth=0, cursor="hand2", command=self.registerUser)
    button_register.image = imgButtonRegister
    button_register.grid(row=5)


  def mainScreen(self):
    self.mainScreen = tk.Frame(self.container)

    registerFrame = tk.Frame(self.mainScreen, width=300, height=680)
    registerFrame.pack(side=LEFT)

    treeviewFrame = tk.Frame(self.mainScreen, width=700, height=680)
    treeviewFrame.pack(side=RIGHT)

    imgLogoIfpr = ImageTk.PhotoImage(Image.open("./images/interface/logo-ifpr-2.png"))
    bannerIfpr = tk.Label(registerFrame, image=imgLogoIfpr)
    bannerIfpr.image = imgLogoIfpr
    bannerIfpr.place(x=10, y=10)

    imgButtonClean = ImageTk.PhotoImage(Image.open("./images/interface/btn-clean.png"))
    button_clean = tk.Button(registerFrame, image=imgButtonClean, borderwidth=0, cursor="hand2", command=self.clearAllStudentFields)
    button_clean.image = imgButtonClean
    button_clean.place(x=193, y=90)

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
    calendar = DateEntry(registerFrame, width=22, background="green",  foreground='black', borderwidth=8, year=2023, highlightbackground="black", font=('Arial', 14))
    calendar.place(x=20, y=270)
    self.entryDateOfBirth = calendar

    labelPhoto = tk.Label(registerFrame, text="Foto:", font=('Arial', 14))
    labelPhoto.place(x=20, y=310)
    self.photo = ImageTk.PhotoImage(Image.open("./images/interface/icon-photo.png"))
    self.photo_data = None
    self.studentPhoto = tk.Label(registerFrame, image=self.photo, width=265)
    self.studentPhoto.image = self.photo
    self.studentPhoto.place(x=20, y=340)

    imgButtonUploadPhoto = ImageTk.PhotoImage(Image.open("./images/interface/btn-upload.png"))
    button_uploadPhoto = tk.Button(registerFrame, image=imgButtonUploadPhoto, borderwidth=0, cursor="hand2", command=self.uploadPhoto)
    button_uploadPhoto.image = imgButtonUploadPhoto
    button_uploadPhoto.place(x=20, y=550)

    imgButtonAdd = ImageTk.PhotoImage(Image.open("./images/interface/btn-add.png"))
    button_add = tk.Button(registerFrame, image=imgButtonAdd, borderwidth=0, cursor="hand2", command=self.registerStudent)
    button_add.image = imgButtonAdd
    button_add.place(x=20, y=600)

    imgButtonUpdate = ImageTk.PhotoImage(Image.open("./images/interface/btn-update.png"))
    button_update = tk.Button(registerFrame, image=imgButtonUpdate, borderwidth=0, cursor="hand2", command=self.updateStudent)
    button_update.image = imgButtonUpdate
    button_update.place(x=20, y=635)     
  
    imgStudentList = ImageTk.PhotoImage(Image.open("./images/interface/student-list.png"))
    studentList = tk.Label(treeviewFrame, image=imgStudentList)
    studentList.image = imgStudentList
    studentList.place(x=220, y=40)

    imgButtonLogout = ImageTk.PhotoImage(Image.open("./images/interface/btn-logout.png"))
    button_logout = tk.Button(treeviewFrame, image=imgButtonLogout, borderwidth=0, cursor="hand2", command=self.showLoginScreen)
    button_logout.image = imgButtonLogout
    button_logout.place(x=650, y=20)

    self.entrySearch = Entry(treeviewFrame, highlightthickness=1, background="white", width=51, highlightbackground="black", font=('Arial', 14))
    self.entrySearch.place(x=20, y=105)

    imgButtonSearch = ImageTk.PhotoImage(Image.open("./images/interface/btn-search.png"))
    button_search = tk.Button(treeviewFrame, image=imgButtonSearch, borderwidth=0, cursor="hand2", command=self.searchStudents)
    button_search.image = imgButtonSearch
    button_search.place(x=590, y=102)

    columns = ('ID', 'Nome', 'Matrícula', 'Data de Nascimento', 'Foto')
    self.treeview = ttk.Treeview(treeviewFrame, columns=columns, show='headings', height=21)
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
    self.treeview.bind("<ButtonRelease-1>", self.selectStudentInTable)

    imgButtonRemove = ImageTk.PhotoImage(Image.open("./images/interface/btn-remove.png"))
    button_remove = tk.Button(treeviewFrame, image=imgButtonRemove, borderwidth=0, cursor="hand2", command=self.removeStudent)
    button_remove.image = imgButtonRemove
    button_remove.place(x=490, y=600)

  def registerUser(self):
    userName = self.userName_entry.get().strip()
    password = self.newPassword_entry.get()
    confirmPassword = self.confirmPassword_entry.get()
    self.controller.registerUser(userName, password, confirmPassword)

  def loginUser(self):
    userName = self.user_entry.get().strip()
    password = self.password_entry.get()
    self.controller.loginUser(userName, password)

  def uploadPhoto(self):
    curr_directory = os.getcwd()
    self.file_path = askopenfilename(initialdir=curr_directory, title="Select Image", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
    if self.file_path is not None:
      photo = ImageTk.PhotoImage(Image.open(self.file_path).resize((265, 200)))
      self.studentPhoto.configure(image=photo)
      self.studentPhoto.image = photo

  def registerStudent(self):
    name = self.entryName.get().strip()
    registration = self.entryRegistration.get().strip()
    dateOfBirth = self.entryDateOfBirth.get().strip()
    photo = self.file_path
    userLoggedIn = self.user_entry.get().strip()
    self.controller.registerStudent(name, registration, dateOfBirth, photo, userLoggedIn)

  def updateStudent(self):
    self.treeview.update_idletasks()
    selected_student = self.treeview.item(self.treeview.focus()).get('values')
    if selected_student:
      student_id = selected_student[0]
      name = self.entryName.get().strip()
      registration = self.entryRegistration.get().strip()
      dateOfBirth = self.entryDateOfBirth.get().strip()
      photo = self.file_path
      userLoggedIn = self.user_entry.get().strip()
      self.controller.updateStudent(student_id, name, registration, dateOfBirth, photo, userLoggedIn)
    else:
      self.showWarningMessage('Selecione um aluno para atualizar!')

  def updateStudentsTable(self, search_term=None):
    self.treeview.delete(*self.treeview.get_children())
    students = self.controller.consultStudents(search_term)
    for student in students:
      self.treeview.insert('', 'end', values=(student['_id'], student['name'], student['registration'], student['dateOfBirth'], student['photo']))

  def searchStudents(self):
    search_term = self.entrySearch.get().strip()
    self.updateStudentsTable(search_term)
  
  def selectStudentInTable(self, event):
    student = self.treeview.item(self.treeview.focus(), 'values')
    if student:
      if student[4] == "None":
        path_photo = "./images/interface/icon-photo.png"
        photo = ImageTk.PhotoImage(Image.open(path_photo))
        self.file_path = None
      else:
        path_photo = student[4]
        photo = ImageTk.PhotoImage(Image.open(path_photo).resize((265, 200)))
        self.file_path = path_photo
      self.studentPhoto.configure(image=photo)
      self.studentPhoto.image = photo
      self.entryName.delete(0, END)
      self.entryName.insert(0, student[1])
      self.entryRegistration.delete(0, END)
      self.entryRegistration.insert(0, student[2])
      self.entryDateOfBirth.delete(0, END)
      self.entryDateOfBirth.insert(0, student[3])

  def removeStudent(self):
    selected_student = self.treeview.focus()
    if selected_student:
      student_id = self.treeview.item(selected_student, 'values')[0]
      userLoggedIn = self.user_entry.get().strip()
      self.controller.removeStudent(student_id, userLoggedIn)
    else:
      self.showWarningMessage('Selecione um aluno para remover!')

  def clearAllLoginFields(self):
    self.user_entry.delete(0, END)
    self.password_entry.delete(0, END)
    self.userName_entry.delete(0, END)
    self.newPassword_entry.delete(0, END)
    self.confirmPassword_entry.delete(0, END)

  def clearAllStudentFields(self):
    self.updateStudentsTable()
    self.entrySearch.delete(0, END)
    self.entryName.delete(0, END)
    self.entryRegistration.delete(0, END)
    self.entryDateOfBirth.delete(0, END)
    self.photo = ImageTk.PhotoImage(Image.open("./images/interface/icon-photo.png"))
    self.studentPhoto.configure(image=self.photo)
    self.studentPhoto.image = self.photo

  def showWarningMessage(self, message):
    messagebox.showwarning(title="Error", message=message)

  def showSuccessMessage(self, message):
    messagebox.showinfo(title="Success", message=message)


View()
