
from tkinter import *


allStudent = {
        "cavid@gmail.com": {
        "name": "Cavid",
        "surname": "Atamoghlanov",
        "fathername": "Hesen",
        "birthyear": 1998,
        "email": "cavid@gmail.com"
    },
    "Kazim@gmail.com": {
        "name": "Kazim",
        "surname": "Agayev",
        "fathername": "Huseyn",
        "birthyear": 1991,
        "email": "Kazim@gmail.com"
    }

}

allAdmin = {
    "admin@gmail.com": {
        "name": "Admin",
        "password": "12345",
        "email": "admin@gmail.com"
    }
}





#All function
def enter_login_page():
    frame_btn.forget()
    frame_login.pack(expand=True, fill=BOTH)

def enter_register_page():
    frame_btn.forget()
    frame_register.pack(expand=True, fill=BOTH)


def back_login():
    frame_login.forget()
    frame_btn.pack(expand=True, fill=BOTH)

isCheck = True
def show_login():
    global isCheck
    if isCheck == True:
        entry_pass.config(show="")
        btn_login_show.config(text="hide")
        isCheck = False
    elif isCheck == False:
        entry_pass.config(show="*")
        btn_login_show.config(text="show")
        isCheck = True

def save():
    name = entry_name.get()
    surname = entry_surname.get()
    fathername = entry_fathername.get()
    email = entry_email.get()
    birthyear = entry_brithyear.get()
    student = {"name": name,
            "surname": surname,
            "fathername": fathername,
            "email": email,
            "birthyear": birthyear}
    allStudent.update({email:student})

def add_student():
    frame_all_student.forget()
    frame_add_student.pack(expand=1, fill=BOTH)




def allstudent():
    frame_add_student.forget()
    frame_all_student.pack(expand=1, fill=BOTH)
    listbox_1.delete(0, END)
    count = 1
    for key, value in allStudent.items():
        listbox_1.insert(count, f"{value['name']} --> {value['surname']} -->{value['fathername']} --> {value['birthyear']} --> {value['email']}: {key}")
        count += 1






#login password check and login page
def enter_admin_page():
   eemail = entry_login.get()
   userPassword = entry_pass.get()
   if eemail in allAdmin.keys():
       if userPassword == allAdmin[eemail]["password"]:
           frame_login.forget()
           frame_admin_page.pack(expand=True, fill=BOTH)
           frame_admin_page.pack(expand=True, fill=BOTH)
       else:
           label_login_error.config(text="Invalid Password !", fg="red")
   else:
       label_login_error.config(text="Invalid Email !", fg="red")



def btnreg_func():
    frame_register.forget()
    frame_btn.pack(expand=True, fill=BOTH)




window = Tk()
window.title("Project")
window.geometry("1080x720+450+200")
window.resizable(False, False)

#All frames
frame_login = Frame(window)
frame_register = Frame(window, bg="yellow")
frame_btn = Frame(window)

#login parol dogrudursa acilan page
frame_admin_page = Frame(window, bg="black")
#-----admin uzerindekiler
frame_admin_left = Frame(frame_admin_page, bg="red")
frame_admin_left.place(relx=0, rely=0, relwidth=0.2, relheight=1)

frame_admin_right = Frame(frame_admin_page, bg="yellow")
frame_admin_right.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)





#sag terefin ustu
frame_add_student = Frame(frame_admin_right, bg="Black")
frame_all_student = Frame(frame_admin_right, bg="black")

#Acilan hisse
frame_btn.pack(expand=True, fill=BOTH)
btn_login = Button(frame_btn, text="Log in Page", font=("georgia", 25), command=enter_login_page)
btn_login.place(relx=0.4, rely=0.3, relwidth=0.2)


btn_register = Button(frame_btn, text="Register Page", font=("georgia", 25), command=enter_register_page)
btn_register.place(relx=0.4, rely=0.5, relwidth=0.2)


#------- Login page design
btn_login_back = Button(frame_login, text="Back", font=("georgia", 15), command=back_login)
btn_login_back.place(relx=0.03, rely=0.03, relwidth=0.05, relheight=0.03)


label_login_txt = Label(frame_login, text="Login", font=("georgia", 15))
label_login_txt.place(relx=0.3, rely=0.3)

entry_login = Entry(frame_login, font=("georgia", 15))
entry_login.place(relx=0.4, rely=0.3)


label_pass_txt = Label(frame_login, text="Password", font=("georgia", 15))
label_pass_txt.place(relx=0.3, rely=0.4)

entry_pass = Entry(frame_login, font=("georgia", 15), show="*")
entry_pass.place(relx=0.4, rely=0.4)

btn_login_show = Button(frame_login, text="show", font=("georgia", 10), command=show_login)
btn_login_show.place(relx=0.65, rely=0.4)

btn_login_in = Button(frame_login, text="Log In", font=("georgia", 15), command=enter_admin_page)
btn_login_in.place(relx=0.3, rely=0.5, relwidth=0.4)

label_login_error = Label(frame_login, text="", font=("Arial", 15))
label_login_error.place(relx=0.7, rely=0.7)


#----all student button





#---birinci sol teref
btn_admin_add_student = Button(frame_admin_left, text="Add Student", font=("georgia", 15), command=add_student)
btn_admin_add_student.place(relx=0.2, rely=0.35, relwidth=0.6)

btn_admin_all_student = Button(frame_admin_left, text="All Student", font=("georgia", 15), command=allstudent)
btn_admin_all_student.place(relx=0.2, rely=0.45, relwidth=0.6)


############

btn_back_reg = Button(frame_register, text="<---", command=btnreg_func)
btn_back_reg.place(relx=0.05, rely=0.05)

save_btn1 = Button(frame_register, text="Save", bg="grey")
save_btn1.place(relx=0.9, rely=0.9, relwidth=0.08)

username = Label(frame_register, text="Ad", bg="yellow")
username.place(relx=0.1, rely=0.15)
username_entry = Entry(frame_register)
username_entry.place(relx=0.16, rely=0.15, relwidth=0.15)


surname = Label(frame_register, text="Soyad", bg="yellow")
surname.place(relx=0.3, rely=0.15, relwidth=0.15)
surname_entry = Entry(frame_register)
surname_entry.place(relx=0.435, rely=0.15, relwidth=0.15)


fathername = Label(frame_register, text="Ata adi", bg="yellow")
fathername.place(relx=0.6, rely=0.15, relwidth=0.15)
father_name = Entry(frame_register)
father_name.place(relx=0.758, rely=0.15, relwidth=0.15)


day = Label(frame_register, text="Gun", bg="yellow")
day.place(relx=0.1, rely=0.25, relwidth=0.15)
day_entry = Entry(frame_register)
day_entry.place(relx=0.1, rely=0.3, relwidth=0.1)


month = Label(frame_register, text="Ay", bg="yellow")
month.place(relx=0.3, rely=0.25, relwidth=0.15)
month_entry = Entry(frame_register)
month_entry.place(relx=0.3, rely=0.3, relwidth=0.1)


year = Label(frame_register, text="il", bg="yellow")
year.place(relx=0.5, rely=0.25, relwidth=0.1)
year_entry = Entry(frame_register)
year_entry.place(relx=0.5, rely=0.3, relwidth=0.1)

a = IntVar()
r_btn_1 = Radiobutton(frame_register, text="Kisi", variable=a, value=1,bg="yellow")
r_btn_1.place(relx=0.7, rely=0.278, relwidth=0.1)


r_btn_2 = Radiobutton(frame_register, text="Qadin", variable=a, bg="yellow", value=2)
r_btn_2.place(relx=0.8, rely=0.278, relwidth=0.1)


email_1 = Label(frame_register, text="Email", bg="yellow")
email_1.place(relx=0.1, rely=0.4, relwidth=0.1)
email = Entry(frame_register)
email.place(relx=0.2, rely=0.4, relwidth=0.15)


#Name
name_label = Label(frame_add_student, text="Name", bg="red", font=("georgia", 15))
name_label.place(relx=0.1, rely=0.1)
entry_name = Entry(frame_add_student)
entry_name.place(relx=0.27, rely=0.1, relheight=0.05)
#Surname
surname_label = Label(frame_add_student, text="Surname", bg="red", font=("georgia", 15))
surname_label.place(relx=0.1, rely=0.17)
entry_surname = Entry(frame_add_student)
entry_surname.place(relx=0.27, rely=0.17, relheight=0.05)
# Fathername
fathername_label = Label(frame_add_student, text="Fathername", bg="red", font=("georgia", 15))
fathername_label.place(relx=0.1, rely=0.24)
entry_fathername = Entry(frame_add_student)
entry_fathername.place(relx=0.27, rely=0.24, relheight=0.05)
# EMAIL
email_label = Label(frame_add_student, text="Email", bg="red", font=("georgia", 15))
email_label.place(relx=0.1, rely=0.31)
entry_email = Entry(frame_add_student)
entry_email.place(relx=0.27, rely=0.31, relheight=0.05)
# BRITHYEAR
birthyear_label = Label(frame_add_student, text="Birthyear", bg="red", font=("georgia", 15))
birthyear_label.place(relx=0.1, rely=0.38)
entry_brithyear = Entry(frame_add_student)
entry_brithyear.place(relx=0.27, rely=0.38, relheight=0.05)

save_btn = Button(frame_add_student, text="Save", bg="green", command=save)
save_btn.place(relx=0.9, rely=0.9, relwidth=0.08)

listbox_1 = Listbox(frame_all_student)
listbox_1.place(relx= 0.05, rely= 0.05, relwidth=0.9, relheight=0.9)
window.mainloop()
#entry_name.get(), entry_surname.get(), entry_fathername.get(), entry_email.get(), entry_brithyear.get()
import tkinter as tk

root = tk.Tk()
root.resizable(width=False, height=False)

img = tk.PhotoImage(file="restoran.png")
width, height = img.width(), img.height()
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()
canvas.create_image((0, 0), image=img, anchor="nw")

entry = tk.Entry(master=canvas)

button = tk.Button(master=canvas, text="hello")

canvas.create_window((width / 2, 50), window=button, anchor="center")
canvas.create_window((width / 2, 100), window=entry, anchor="center")

root.mainloop()