import tkinter.messagebox
from tkinter import *
from NLPKey import NLPRequest
import json

class NL:

    def __init__(self):
        self.root = Tk()
        self.root.title('NLPApp')
        # self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#34495E')

        self.login_Page()

        self.root.mainloop()

    def login_Page(self):

        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold','italic'))

        loginID = Label(self.root, text='Enter Email Id', bg='#34495E', fg='white')
        loginID.pack(pady=(10,10))
        loginID.configure(font=('Ariel',10,'italic'))

        self.emailId = Entry(self.root, width=40)
        self.emailId.pack(pady=(10,10), ipady=5)

        password = Label(self.root, text='Enter Password', bg='#34495E', fg='white')
        password.pack(pady=(10, 10))
        password.configure(font=('Ariel', 10, 'italic'))

        self.password = Entry(self.root, width=40, show='*')
        self.password.pack(pady=(10, 10), ipady = 5)

        loginButton = Button(self.root, text='Login', width=30, height=2, command=self.loginCheck)
        loginButton.pack(pady = (10,10))

        registration = Label(self.root, text='Not A Member ??', font=('Ariel',20,'italic'), fg='white', bg='#34495E')
        registration.pack(pady=(10,0))
        registration.configure(font=('Ariel', 10, 'italic'))

        registerButton = Button(self.root, text='register', width=30, height=2, command=self.registrationPage)
        registerButton.pack(pady=(5, 10))


    def loginCheck(self):
        with open('database.json', 'r') as f:
            data = json.load(f)

        if self.emailId.get() in data:
            # tkinter.messagebox.showinfo('Success', 'Registration successful. You can login now')
            if data[self.emailId.get()][1] == self.password.get():
                self.mainPage()
            else :
                self.login_Page()
        else:
            tkinter.messagebox.showerror('Error', 'invlid Email ')
            self.login_Page()
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    # def pr(self):
    #     print(self.emailId.get(), self.password.get())

    def registrationPage(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold', 'italic'))

        heading = Label(self.root, text='Register Here', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 14, 'bold', 'italic'))

        name = Label(self.root, text='Enter Name', bg='#34495E', fg='white')
        name.pack(pady=(10, 10))
        name.configure(font=('Ariel', 10, 'italic'))

        self.name = Entry(self.root, width=40)
        self.name.pack(pady=(10, 10), ipady=5)

        loginID = Label(self.root, text='Enter Email Id', bg='#34495E', fg='white')
        loginID.pack(pady=(10, 10))
        loginID.configure(font=('Ariel', 10, 'italic'))

        self.emailId = Entry(self.root, width=40)
        self.emailId.pack(pady=(10, 10), ipady=5)

        password = Label(self.root, text='Enter Password', bg='#34495E', fg='white')
        password.pack(pady=(10, 10))
        password.configure(font=('Ariel', 10, 'italic'))

        self.password = Entry(self.root, width=40, show='*')
        self.password.pack(pady=(10, 10), ipady=5)

        registerButton = Button(self.root, text='Register', width=30, height=2, command=self.registerationCheck)
        registerButton.pack(pady=(5, 10))

        LoginButton = Button(self.root, text='Login', width=30, height=2, command=self.login_Page)
        LoginButton.pack(pady=(5, 10))

    def registerationCheck(self):
        name = self.name.get()
        email = self.emailId.get()
        password = self.password.get()
        with open('database.json', 'r') as f:
            data = json.load(f)
        # print(data)

        if email in data:
            # tkinter.messagebox.showinfo('Success', 'Registration successful. You can login now')
            self.login_Page()
        else:
            data[str(email)] = [str(name), str(password)]
            with open('database.json', 'w') as f:
                json.dump(data, f)
            # tkinter.messagebox.showerror('Error', 'Email already exists')
            self.registrationPage()



    def mainPage(self):

        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold', 'italic'))

        heading = Label(self.root, text='Sentimental Analysis', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 14, 'bold', 'italic'))

        text = Label(self.root, text='enter txt here', bg='#34495E', fg='white')
        text.pack(pady=(30,30))
        text.configure(font=('Ariel', 9, 'italic'))

        # self.password.pack(pady=(10, 10), ipady=5)
        # self.password = Entry(self.root, width=40, show='*')

        self.texts = Entry(self.root, width=30)
        self.texts.pack(pady=(30,30), ipady=5)

        analysisButton = Button(self.root, text='Analyze', width=30, height=2, command=self.analysisSegmentation)
        analysisButton.pack(pady=(5, 10))

        self.back = Button(self.root, text='Home', command=self.login_Page)
        self.back.pack(pady=(20, 0))


    def analysisSegmentation(self):

        # with open('sample.json', 'r') as f:
        #     data = json.load(f)
        #
        # data1 = ''
        # for i in data:
        #     data1 +=  str(i) + ' -> ' + str(data[i]) + ' \n '
        #
        # text = Label(self.root, text=data1, bg='#34495E', fg='white')
        #
        # text.pack(pady=(30, 0))
        # text.configure(font=('Ariel', 14, 'italic'))

        nn = NLPRequest(self.texts)
        nn.re()





n = NL()