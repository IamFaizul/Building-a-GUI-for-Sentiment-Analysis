from tkinter import *  # importing all classes from tkinter library
from mydb import Database
from tkinter import messagebox



class EmotionEcho:
    def __init__(self):

        # create db object
        self.dbo = Database()

        # Load the Login GUI while starting
        self.root = Tk()  # Create an object of Tk class (tkinter have many other classes)
        self.root.title('EmotionEcho')
        #self.root.iconbitmap('resources/rocket.ico')
        self.root.geometry('350x600')  # Sets the size of GUI
        self.root.configure(bg='#34495E')

        self.login_gui()

        self.root.mainloop()  # So that it stays and won't disappear instantly

    # We are going to build a login GUI!!!
    def login_gui(self):  # login has two sections - Email,Password
        self.clear()
        # We use Label class for showing text
        # Label(main GUI object,what we wanna show on the screen)
        heading = Label(self.root, text='EmotionEcho', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))
        # Although we used Label but it won't show anything on GUI. For that we have to use
        # geometry manager which will help us to show things on GUI.There are two geometry manager- pack & grid

        # Email section
        label1 = Label(self.root, text='Enter your Email', bg='#34495E', fg='white')
        label1.pack(pady=(10, 10))
        label1.configure(font=('verdana', 9, 'bold'))
        self.email_input = Entry(self.root, width=45)
        self.email_input.pack(pady=(5, 10), ipady=4)  # ipady- it gives the height

        # Password section
        label2 = Label(self.root, text='Enter Password', bg='#34495E', fg='white')
        label2.pack(pady=(10, 10))
        label2.configure(font=('verdana', 9, 'bold'))
        self.password_input = Entry(self.root, width=45, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        # Creating a login button
        login_button = Button(self.root, text='Login', width=12, height=2, bg='black', fg='white',command=self.perform_login)
        login_button.pack(pady=(10, 10))
        login_button.configure(font=('verdana', 9, 'bold'))

        label3 = Label(self.root, text='Not a member?', bg='#34495E', fg='white')
        label3.pack(pady=(30, 5))
        label3.configure(font=('verdana', 9, 'bold'))

        # If he's not a member,you will be redirected to register window
        redirect_button = Button(self.root, text='Register Now!', width=15, height=2, bg='black', fg='white',
                                 command=self.register_gui)
        redirect_button.pack(pady=(15, 10))
        redirect_button.configure(font=('verdana', 9, 'bold'))

    def register_gui(self):  # Register has 3 sections - name,email and password
        self.clear()

        heading = Label(self.root, text='EmotionEcho', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))
        # Although we used Label but it won't show anything on GUI. For that we have to use
        # geometry manager which will help us to show things on GUI.There are two geometry manager- pack & grid

        label0 = Label(self.root, text='Enter your Name', bg='#34495E', fg='white')
        label0.pack(pady=(10, 10))
        label0.configure(font=('verdana', 9, 'bold'))
        self.name_input = Entry(self.root, width=45)
        self.name_input.pack(pady=(5, 10), ipady=4)  # ipady- it gives the height

        # Email section
        label1 = Label(self.root, text='Enter your Email', bg='#34495E', fg='white')
        label1.pack(pady=(10, 10))
        label1.configure(font=('verdana', 9, 'bold'))
        self.email_input = Entry(self.root, width=45)
        self.email_input.pack(pady=(5, 10), ipady=4)  # ipady- it gives the height

        # Password section
        label2 = Label(self.root, text='Enter Password', bg='#34495E', fg='white')
        label2.pack(pady=(10, 10))
        label2.configure(font=('verdana', 9, 'bold'))
        self.password_input = Entry(self.root, width=45, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        # Creating a login button
        register_button = Button(self.root, text='Register', width=12, height=2, bg='black', fg='white',
                                 command=self.perform_registration)
        register_button.pack(pady=(10, 10))
        register_button.configure(font=('verdana', 9, 'bold'))

        label3 = Label(self.root, text='Already a member?', bg='#34495E', fg='white')
        label3.pack(pady=(30, 5))
        label3.configure(font=('verdana', 9, 'bold'))

        # If he's not a member,you will be redirected to register window
        redirect_button = Button(self.root, text='Login Now!', width=15, height=2, bg='black', fg='white',
                                 command=self.login_gui)
        redirect_button.pack(pady=(15, 10))
        redirect_button.configure(font=('verdana', 9, 'bold'))

    def clear(self):
        # clear the existing gui
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        # fetch data from GUI
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)
        if response:
            messagebox.showinfo('Success!','Registration successful.You can login now')
        else:
            messagebox.showinfo('Error','Email already exists')


    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email,password)
        if response:
            messagebox.showinfo('Success!','Login Successful')
            self.home_gui()
        else:
            messagebox.showinfo('Incorrect','Incorrect Email/Password')

    def home_gui(self):
        self.clear()

        heading = Label(self.root, text='EmotionEcho', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_button = Button(self.root, text='Sentiment Analysis', width=18, height=3, bg='black', fg='white',
                                 command=self.sentiment_gui)
        sentiment_button.pack(pady=(10, 10))
        sentiment_button.configure(font=('verdana', 9, 'bold'))

        logout_button = Button(self.root, text='Logout', width=15, height=2, bg='black', fg='white',
                                 command=self.login_gui)
        logout_button.pack(pady=(15, 10))
        logout_button.configure(font=('verdana', 9, 'bold'))


    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text='EmotionEcho', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root,text='Enter the text',bg='black', fg='white')
        label1.pack(pady=(10,10))

        self.sentiment_input = Entry(self.root, width=45, show='*')
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_button = Button(self.root, text='Analyze Sentiment', width=15, height=2, bg='black', fg='white',
                               command=self.login_gui)
        sentiment_button.pack(pady=(10, 10))
        sentiment_button.configure(font=('verdana', 9, 'bold'))

        self.sentiment_result = Label(self.root,text='',bg='#34495E', fg='white')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('verdana', 16))


        goback_button = Button(self.root,text='Go back',command=self.home_gui)
        goback_button.pack(pady=(60,10))



Eecho = EmotionEcho()
