# Importing all packages
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import Tk, Label, Entry, Button
import os
import mysql.connector
from tkinter.filedialog import askopenfilename, asksaveasfilename
import mysql.connector as sk
from model import *
from send_sms import *
print('GUI SYSTEM STARTED...')
#---------------------------------------------------------------------------------

def LogIn():
    username = box1.get()

    u = 1

    if len(username) == 0:
        u = 0
        messagebox.showinfo("Error", "You must enter something Sir")

    if u:
            password = box2.get()

            if len(password):
                query = "SELECT * FROM THEGREAT"

                sql.execute(query)

                data = sql.fetchall()

                g = 0
                b = 0

                for i in data:
                    if i[0] == username:
                        g = 1
                    if i[1] == password:
                        b = 1


                if g and b:
                    messagebox.showinfo('Hello!!', 'Welcome to the Diabetes Retinopathy Detection System')
                else:
                    messagebox.showinfo('Sorry', 'Wrong Username or Password')

                global y
                y = True
            else:
                messagebox.showinfo("Error", "You must enter a password!!")

def OpenFile():
    username = box1.get()
    if y:
        try:
            a = askopenfilename()
            print(a)
            value, classes = main(a)
            messagebox.showinfo("Your report", f"Predicted Label is {value}\nPredicted Class is {classes}")

            query = 'UPDATE THEGREAT SET PREDICT = "%s" WHERE USERNAME = "%s"'%(value, username)

            sql.execute(query)
            #print(query)
            connection.commit()

            #------********************Only use when required to send message
            send(value, classes)
            #------*********************************************************
            image = Image.open(a)
            # plotting image
            file = image.convert('RGB')
            plt.imshow(np.array(file))
            plt.title(f'Your report is Label : {value} Class : {classes}')
            plt.show()
            #print(image)
            print('Thanks for using the system !')
            #fn, text = os.path.splitext(a) #fn stands for filename
        except Exception as error:
            print("File not selected ! Exiting..., Please try again")


    else:
        messagebox.showinfo("Hello", "You need to Login first")


x = 0
y = False


def Signup():
    username = box1.get()
    password = box2.get()

    u = 1

    if len(username) == 0 or len(password) == 0:
        u = 0
        messagebox.showinfo("Error", "You must enter something")

    if u:
        query1 = "SELECT * FROM THEGREAT"
        sql.execute(query1)

        data = sql.fetchall()

        z = 1

        for i in data:
            if i[0] == username:
                messagebox.showinfo("Sorry", "This  username is already registered, try a new one")
                z = 0

        if z:
            query = "INSERT INTO THEGREAT (USERNAME, PASSWORD) VALUES('%s', '%s')" % (username, password)
            messagebox.showinfo("signed up", ("Hi ",username ,"\n Now you can login with your credentials !"))
            sql.execute(query)
            connection.commit()


#-----------------------------------------------------------------------------------------


connection = sk.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="batch_db_new"
)

sql = connection.cursor()

def resize_background(event=None):
    if 'background_image' in globals():
        image = Image.open("bg.jpg")
        image = image.resize((root.winfo_width(), root.winfo_height()), Image.LANCZOS)
        bg_image = ImageTk.PhotoImage(image)
        background_label.config(image=bg_image)
        background_label.image = bg_image

# Initialize the main window
root = Tk()
root.title("Diabetes Retinopathy Detection")
root.geometry("700x400")

background_label = Label(root)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_image = Image.open("bg.jpg")
background_image = background_image.resize((root.winfo_width(), root.winfo_height()),Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
background_label.config(image=background_photo)
background_label.image = background_photo

root.bind("<Configure>", resize_background)

# Widgets - Keep your existing widgets
label2 = Label(root, text="Enter your username: ", font=('Arial', 15))
label2.grid(padx=20, pady=20, row=5, column=0)

label3 = Label(root, text="Enter your password: ", font=('Arial', 15))
label3.grid(padx=20, pady=30, row=6, column=0)

box1 = Entry(root)
box1.grid(row=5, column=1)

box2 = Entry(root, show='*')
box2.grid(row=6, column=1)

button3 = Button(root, text="Signup", command=Signup)
button3.grid(padx=20, pady=30, row=8, column=1)

button1 = Button(root, text="Login", command=LogIn)
button1.grid(padx=20, pady=30, row=8, column=2)

button2 = Button(root, text="Upload Image", command=OpenFile)
button2.grid(padx=20, pady=30, row=6, column=3)

root.mainloop()