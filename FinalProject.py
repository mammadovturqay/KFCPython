from tkinter import *
# import datetime
# from tkinter.font import Font
import tkinter as tk
# from PIL import Image, ImageTk




allMusteri = {
        "cavid@gmail.com": {
        "name": "Cavid",
        "surname": "Atamoghlanov",
        "fathername": "Hesen",
        "birthyear": 1998,
        "email": "cavid@gmail.com",
        "password" : "1235"
    },
    "Kazim@gmail.com": {
        "name": "Kazim",
        "surname": "Agayev",
        "fathername": "Huseyn",
        "birthyear": 1991,
        "email": "Kazim@gmail.com",
        "password" : "12345"
    }

}

allAdmin = {
    "admin@gmail.com": {
        "name": "Admin",
        "password": "12345",
        "email": "admin@gmail.com"
    }
}
window = Tk()
# Total funksioyasi
# menu
# burger = 1
total = 0
widgetssay = 0
freesay = 0

chicken = 0
colasay=  0
fantasay = 0

def burgertotal():
    global total, widgetssay
    widgetssay +=1
    total +=2.5


    total_lbl.config(text=f"{total}$")
    say_lbl.config(text=f"Widgets Count {widgetssay}")

def freetotal():
    global total ,freesay
    total+=2
    freesay+=1
    total_lbl.config(text=f"{total}$")
    sayfree_lbl.config(text=f"Free Count {freesay}")

def chickenburgertotal():
    global total,chicken
    total += 3
    chicken+=1
    total_lbl.config(text=f"{total}$")
    chcken_lbl.config(text=f"Mc Chicken Burger Count{chicken}")


def colatotal():
    global total, colasay
    total +=1.5
    colasay+=1
    total_lbl.config(text=f"{total}$")
    cola_lbl.config(text=f"Coca Cola Count {colasay}")


def fantatotal():
    global total
    total += 1.50
    total_lbl.config(text=f"{total}$")

def spritetotal():
    global total
    total +=1.70
    total_lbl.config(text=f"{total}$")

def soustotal():
    global total
    total+=1
    total_lbl.config(text=f"{total}$")

def enter_login_page():
    frame_btn.forget()
    label_1.forget()
    canvas.forget()
    frame_login.pack(expand=True, fill=BOTH)





# Butun funksiyaLar
def enter_register_page():
    frame_btn.forget()
    label_1.forget()
    canvas.forget()

    frame_register.pack(expand=True, fill=BOTH)

def enter_adminpage():
    frame_btn.forget()
    label_1.forget()
    canvas.forget()

    frame_admin.pack(expand=True , fill=BOTH)
def back_login():
    frame_login.forget()
    label_1.forget()
    canvas.forget()
    frame_btn.pack(expand=True, fill=BOTH)
    canvas.pack(expand=True, fill=BOTH)

def btnreg_func():
    frame_register.forget()
    label_1.forget()
    canvas.forget()
    frame_btn.pack(expand=True, fill=BOTH)
    canvas.pack(expand=True, fill=BOTH)
isCheck=True

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
# admin
#
yoxlama = True
def show_loginAdmin():
    global yoxlama
    if yoxlama == True:
        entry_pass_admin.config(show="")
        btn_login_showadmin.config(text="hide")
        yoxlama = False
    elif yoxlama == False:
        entry_pass_admin.config(show="*")
        btn_login_showadmin.config(text="show")
        yoxlama = True
def enter_admin_page():
   eemail = entry_login.get()
   userPassword = entry_pass.get()
   frame_login.forget()
   frame_admin_page.pack(expand=True, fill=BOTH)
   frame_admin_page.pack(expand=True, fill=BOTH)

   if eemail in allMusteri.keys():


       if userPassword == allMusteri[eemail]["password"]:
           frame_login.forget()
           frame_admin_page.pack(expand=True, fill=BOTH)
           frame_admin_page.pack(expand=True, fill=BOTH)
       else:
           label_login_error.config(text="Invalid Password !", fg="red")
   else:
       label_login_error.config(text="Invalid Email !", fg="red")



def saveFunk():
    print()

def chechk_adminpage():
   eemailadmin= entry_loginadmin.get()
   adminPassword = entry_pass_admin.get()
   frame_admin.forget()
   admn2.pack(expand=True, fill=BOTH)
   admn2.pack(expand=True, fill=BOTH)
   if eemailadmin in allAdmin.keys():


       if adminPassword == allAdmin[eemailadmin]["password"]:
           frame_admin.forget()
           admn2.pack(expand=True, fill=BOTH)
           admn2.pack(expand=True, fill=BOTH)
       else:
           label_login_erroradmin.config(text="Invalid Password !", fg="red")
   else:
       label_login_erroradmin.config(text="Invalid Email !", fg="red")

def backadmin (*args):
    global total ,freesay ,widgetssay ,chicken , colasay
    freesay = 0
    widgetssay = 0
    chicken = 0
    colasay = 0
    total = 0
    frame_admin_page.forget()
    total_lbl.config(text=total)
    sayfree_lbl.config(text=f"Free Count {freesay}")
    say_lbl.config(text=f"Widgets Count{widgetssay} ")
    chcken_lbl.config(text=f"Mc Chicken Burger Count {chicken}")
    cola_lbl.config(text=f"Coca Cola Count {colasay}")
    frame_login.pack(expand=True , fill=BOTH)

def cek(*args):
    global total , freesay , widgetssay , chicken , colasay ,window2 ,total_lbl,sayfree_lbl
    window2=Tk()
    wndw2_label = Label(window2 , text=f"KFC" , bg="black" , fg= "red" , font=("Arial",20))
    wndw2_label.place(relx=0.3, rely=0 , relwidth=0.4,relheight=0.1)
    label_wndw2 = Label(window2,text = "" , font=(5) , fg= "black")
    label_wndw2.place(relx=0.6 , rely=0.5)
    window2totali = Label(window2 , text=f"{total}$" , bg="black" , fg="white")
    window2totali.place(relx=0.1, rely=0.3)
    label_total = Label(window2 , text="TOTAL" , fg="white",bg="black",font=(10))
    label_total.place(relx=0.1 , rely=0.2)
    wndw2_lbl = Label(window2 , text="" ,fg="white",bg="black")
    wndw2_lbl.place(relx=0.5,rely=0.3)
    wndw_count = Label(window2,text=f"Coco Cola Sayi {colasay}")
    wndw_count.place(relx=0.1 , rely=0.6)


    window2.title("Hesab")
    window2.iconbitmap("C:/Users/lenovo/Desktop/FinalProject/finalinbasligi.ico")

    wndw_count2 = Label(window2, text=f"Widgets  Sayi {widgetssay}")
    wndw_count2.place(relx=0.1, rely=0.7)

    wndw_count3 = Label(window2,text=f" Free Sayi {freesay}")
    wndw_count3.place(relx=0.1 , rely=0.8)

    window2.geometry("500x500")
    window2.resizable(False ,False)



    if total >0 :

        wndw2_lbl.config(text="Odenildi" , fg="white",bg="black")


    else:
        wndw2_lbl.config(text="Menudan secim edilmemisdir.")











def resetfunk():
    global total , freesay , widgetssay , chicken , colasay
    freesay  = 0
    widgetssay = 0
    chicken = 0
    colasay =   0
    total =     0
    total_lbl.config(text=total)
    sayfree_lbl.config(text= f"Free Count {freesay}")
    say_lbl.config(text=f"Widgets Count {widgetssay}")
    cola_lbl.config(text=f"Coca Cola Count {colasay}")
    chcken_lbl.config(text=f"Mc Chicken Burger Count {chicken}")





def freeazaltmaq():
    global total ,freesay
    if total>0:
        total-=2
    if freesay> 0:
        freesay-=1
        sayfree_lbl.config(text=f"Free Count {freesay}")
        total_lbl.config(text=f"{total}$")


def widgetsazaltmaq():
    global total,widgetssay
    if total>0:
        total-=2.5
    if widgetssay>0:
        widgetssay-=1
        say_lbl.config(text=f"Widgets Count {widgetssay}")
        total_lbl.config(text=f"{total}$")


def chickenazaltmaq():
    global total ,chicken
    if total>0:
        total-=3
    if chicken> 0:
        chicken-=1
        chcken_lbl.config(text=f"Mc Chicken Burger Count {chicken}")
        total_lbl.config(text=f"{total}$")


def colaazaltmaq():
    global total, colasay
    if total > 0:
        total -= 1.5
    if colasay > 0:
        colasay -= 1
        cola_lbl.config(text=f"Coca Cola Count {colasay}")
        total_lbl.config(text=f"{total}$")





def back_menu():
    frame_admin_left.forget()
    sekil.forget()
    burgers.forget()
    drinkss.forget()
    sekilq.forget()
    sekilq1.forget()
    # admn_labl.forget()
    sekil5.forget()
    # frame_admin_right.pack(expand=True , fill=BOTH)
    # imag01.
    contact_1.pack(expand=True, fill=BOTH)

def free():
    frame_admin_left.forget()
    sekil.forget()
    burgers.forget()
    drinkss.forget()
    sekilq.forget()
    sekilq1.forget()
    frees.place()


def burger():
    frame_admin_left.forget()
    contact_1.forget()
    # admn_labl.place()#
    sekil.place()
    sekilq.place()
    sekilq1.place()
    sekil5.place()
    burgers.pack(expand=True , fill=BOTH)

def drinks():
    frame_admin_right.forget()
    contact_1.forget()
    burgers.forget()
    sekil.forget()
    sekilq.forget()
    sekilq1.forget()
    drinkss.pack(expand=True , fill=BOTH)

def widgets():
    frame_admin_left.forget()
    drinkss.forget()
    burgers.forget()
    contact_1.forget()
    sekil.place()
    sekilq.place()
    sekilq1.place()


def back_admin():
    frame_admin.forget()

    canvas.pack(expand=True, fill=BOTH)


def admin2backi():
    admn2.forget()
    frame_admin.pack(expand=True , fill=BOTH)


def admnchechkadd():
    admn_email_check.forget()
    edit_admin_right.forget()

    admn_add_menusu.pack(expand = True , fill = BOTH)

def save():
    allMusteri[username_entry]['view'].append(username_entry)



def admn2editmenu():
    admn_add_menusu.forget()
    admin_frame_right2.forget()
    admn_email_check.forget()
    edit_admin_right.pack(expand=True , fill=BOTH)

def admnadd():
    edit_admin_right.forget()
    admn_add_menusu.forget()
    admn_email_check.pack(expand=True , fill=BOTH)
#____----------+++++++++++++SEHVLIK OLAN KOD ++++++


window.title("KFC")
window.geometry("1280x720+100+70")
# window.minsize(600 , 370)
# window.maxsize(850 , 650)
window.resizable(False , False)





# sekilller

# sekiller






img = tk.PhotoImage(file="2cilogo.png")
width, height = img.width(), img.height()
canvas = tk.Canvas(window, width=width, height=height)
canvas.pack()
canvas.create_image((0, 0), image=img, anchor="nw")
canvas.pack(expand=True , fill=BOTH)
#All frames
# LOgin
frame_login = Frame(window,bg='red')
# admin
frame_admin = Frame(window, bg='black')
# Regster
frame_register = Frame(window, bg="black" )
label_1 = Label(window, bg='red' , fg = 'blue' , text = 'Welcome' , font=('Helvetica' , 100))

frame_btn = Frame(window)
# sekilllllllllllllllllllllllllllllllllllllllllllll2222
imag11 = tk.PhotoImage(file="Giris.png")
width, height = imag11.width(), imag11.height()
canvas1 = tk.Canvas(frame_login, width=width, height=height)
canvas1.pack()
canvas1.create_image((0, 0), image=imag11, anchor="nw")
canvas.pack(expand=True , fill=BOTH)

imagAdmin = tk.PhotoImage(file="kfcsekiladmin.png")
width, height = imagAdmin.width(), imagAdmin.height()
canvasAdmin = tk.Canvas(frame_admin, width=width, height=height)
canvasAdmin.pack()
canvasAdmin.create_image((0, 0), image=imagAdmin, anchor="nw")
canvasAdmin.pack(expand=True , fill=BOTH)

#login parol dogrudursa acilan page
frame_admin_page = Frame(window, bg="black")
#-----musteri uzerindekiler


frame_admin_left = Frame(frame_admin_page, bg="#cdd1e4")#cdd1e4
frame_admin_left.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
# admin uzerindekiler
frame_admin_right = Frame(frame_admin_page, bg="#0db4b9")#1c474d
#0db4b9
frame_admin_right.place(relx=0, rely=0, relwidth=0.2, relheight=1)
#


# Admin parol yoxlanisinan sonrasinda gelen fRAME +++++++++++++


#
#


admn2 = Frame(bg="grey")

# Left

admin_frame_left2 = Frame(admn2 , bg="grey")
admin_frame_left2.place(relx=0.2 , rely= 0 , relwidth=0.8 , relheight=1)


# Right
admin_frame_right2 = Frame(admn2 , bg="red")
admin_frame_right2.place(relx=0.2 , rely= 0 , relwidth=0.8 , relheight=1)
# admin left

loginbackadmin= Button(admn2 , text= '<--Back' , font=('Georgia' , 20),command = admin2backi)
loginbackadmin.place(relx= 0.01 , rely = 0.01, relwidth=0.1)

# left uzerindekiler admn 2 + admin gore bileceyi isler

admn_btn_left1 = Button(admn2 , text= "editing menus" , bg="purple" , fg="black", command=admn2editmenu)
admn_btn_left1.place(relx=0.01 , rely=0.3 , relwidth=0.1 , relheight=0.1)



# edit menusu===============================
edit_admin_right = Frame(admin_frame_right2 , bg="black")
edit_admin_rightButon = Button(edit_admin_right , text="Menu duzelisi")
edit_admin_rightButon.place(relx= 0.01 , rely = 0.3 , relwidth=0.1 ,relheight=0.1)

# ==================
admn_btn_left2 = Button(admn2 , text= "emails of users" , bg="red" , fg="black" , command=admnadd)
admn_btn_left2.place(relx=0.01 , rely=0.45 , relwidth=0.1 , relheight=0.1)
# emaillerin yoxlaniwi
admn_email_check = Frame(admin_frame_right2,bg="red")


# add menu

admn_btn_left3 = Button(admn2 , text= "Add a user" , bg="red" , fg="black" , command=admnchechkadd)
admn_btn_left3.place(relx=0.01 , rely=0.6 , relwidth=0.1 , relheight=0.1)

admn_add_menusu = Frame(bg="black")

# USER QQEYDIYYATI
user_name_lbl = Label(admn_add_menusu , text="User Name ")
user_name_lbl.place(relx=0.1 , rely=0.1)
user_name_entry = Entry(admn_add_menusu)
user_name_entry.place(relx=0.1 ,rely=0.2)
user_surname_lbl = Label(admn_add_menusu , text="User Surname ")
user_surname_lbl.place(relx=0.1 , rely= 0.3)
user_surname_entry = Entry(admn_add_menusu)
user_surname_entry.place(relx= 0.1 , rely=0.4)
user_fathername_lbl = Label(admn_add_menusu , text= "User Fathername")
user_fathername_lbl.place(relx=0.1 , rely=0.5)
user_fathername_entry = Entry(admn_add_menusu)
user_fathername_entry.place(relx=0.1, rely=0.6)
user_day_lbl= Label(admn_add_menusu , text="User Day ")
user_day_lbl.place(relx = 0.3 , rely=0.1)
user_day_entry = Entry(admn_add_menusu)
user_day_entry.place(relx=0.3 , rely=0.2)
user_month_lbl = Label(admn_add_menusu , text="User Month ")
user_month_lbl.place(relx=0.3 ,rely=0.3)
user_month_entry = Entry(admn_add_menusu)
user_month_entry.place(relx=0.3 , rely=0.4)
user_year_lbl = Label(admn_add_menusu , text="User Year")
user_year_lbl.place(relx=0.3 , rely=0.5)
user_year_entry = Entry(admn_add_menusu)
user_year_entry.place(relx=0.3 , rely=0.6)
user_saveButon = Button(admn_add_menusu , text="Save")
user_saveButon.place(relx=0.2 , rely=0.8 , relheight=0.1 , relwidth=0.1)
#ADMINE GIRIIIIIIIIIIIIIIIIIIISSSSSSSSSSSSSSSSSS


label_login_admn= Label(frame_admin, text="Login", font=("georgia", 15) , fg="white" , bg="black")
label_login_admn.place(relx=0.2, rely=0.3)

entry_loginadmin = Entry(frame_admin, font=("georgia", 15) , bg="black" , fg="white")
entry_loginadmin.place(relx=0.3, rely=0.3)


label_pass_admin = Label(frame_admin, text="Password", font=("georgia", 15) , fg="white" , bg="black")
label_pass_admin.place(relx=0.2, rely=0.4)



entry_pass_admin = Entry(frame_admin, font=("georgia", 15), show="*" , fg="white" , bg="black")
entry_pass_admin.place(relx=0.3, rely=0.4)



btn_login_showadmin = Button(master=canvasAdmin, text="show", font=("georgia", 10),command=show_loginAdmin ,bg="black" , fg = "white")
btn_login_showadmin.place(relx=0.5, rely=0.4)



label_login_erroradmin = Label(frame_admin, text="", font=("Arial", 15))
label_login_erroradmin.place(relx=0.7, rely=0.7)



loginbackadmin= Button(master=canvasAdmin , text= 'Back' , font=('Georgia' , 20),command = back_admin, fg="white" , bg="black")
loginbackadmin.place(relx= 0.05 , rely = 0.05)



btn_login_in = Button(master=canvasAdmin, text="Log In", font=("georgia", 15) , command=chechk_adminpage, bg="red" , fg="black")
btn_login_in.place(relx=0.3, rely=0.5, relwidth=0.4)








# back kodlari
# btn_back_reg = Button(frame_register , text='Back' , font=('georgia' , 20), command = btnreg_func)
# btn_back_reg.place(relx= 0.05 , rely = 0.05)

# loginback
loginback= Button(frame_login , text= 'Back' , font=('Georgia' , 20),command=back_login)
loginback.place(relx= 0.05 , rely = 0.05)

#sag terefin ustu
frame_add_student = Frame(frame_admin_right, bg="Black")
frame_all_student = Frame(frame_admin_right, bg="black")

#Acilan hisse
frame_btn.pack(expand=True, fill=BOTH)
btn_login = Button(master=canvas, text="Sign", font=("georgia", 20),fg='black',bg='red',command=enter_login_page)
btn_login.place(relx=0.17, rely=0.7, relwidth=0.2)


btn_register = Button(master=canvas, text="Register", font=("georgia", 20),fg = 'black' , bg = 'red', command=enter_register_page)
btn_register.place(relx=0.68, rely=0.7, relwidth=0.2)



btn_admin = Button(master=canvas , text = "Admin" , font=("georgia" , 20 ), fg='black' , bg="red" ,command=enter_adminpage)
btn_admin.place(relx=0.42,rely=0.7,relwidth=0.2)

label_login_txt= Label(master=canvas1, text="Login", font=("georgia", 15))
label_login_txt.place(relx=0.2, rely=0.3)

entry_login = Entry(master=canvas1, font=("georgia", 15))
entry_login.place(relx=0.3, rely=0.3)


label_pass_txt = Label(frame_login, text="Password", font=("georgia", 15))
label_pass_txt.place(relx=0.2, rely=0.4)

entry_pass = Entry(frame_login, font=("georgia", 15), show="*")
entry_pass.place(relx=0.3, rely=0.4)

btn_login_show = Button(frame_login, text="show", font=("georgia", 10),command=show_login)
btn_login_show.place(relx=0.5, rely=0.4)

label_login_error = Label(frame_login, text="", font=("Arial", 15))
label_login_error.place(relx=0.7, rely=0.7)

btn_login_in = Button(frame_login, text="Log In", font=("georgia", 15), command=enter_admin_page)
btn_login_in.place(relx=0.3, rely=0.5, relwidth=0.4)
kfc_login_in1 = Label(frame_login, text='Sign Up', font=("Georgia",21),fg='black' , bg="red")
kfc_login_in1.place(relx=0.5,rely=0.1,width=100)

backlogin_2 = Button(frame_admin_page , text="Back" , bg= 'blue' ,font=("arial", 15),command=backadmin)
backlogin_2.place(relx=0.01, rely= 0.01)
# admin lABEL
# admin left
imag01 = tk.PhotoImage(file="menuda.png")
width, height = imag01.width(), imag01.height()
canvas01 = tk.Canvas(frame_admin_right, width=width, height=height)
canvas01.create_image((0, 0), image=imag01, anchor="nw")
canvas01.pack(expand=True , fill=BOTH)


# imagq = tk.PhotoImage(file="qirmizi.png")
# width, height = imagq.width(), imagq.height()
# canvasq = tk.Canvas(frame_admin_left, width=width, height=height)
# canvasq.create_image((0, 0), image=imagq, anchor="nw")
# canvasq.pack(expand=True , fill=BOTH)
# canvasq.place(relx=0 , rely=-0.4)

imaj5 = PhotoImage(file="images (1).png")
kimaj5 = imaj5.subsample(1,1)
sekil5 = Label(frame_admin_left,  image=kimaj5, compound=RIGHT,font=("george" , 15))
sekil5.place(relx= 0.31 , rely = 0 )

# imag011 = tk.PhotoImage(file="images (1).png")
# width, height = imag011.width(), imag011.height()

# canvas011 = tk.Canvas(frame_admin_left, width=width, height=height)
# canvas011.create_image((0, 0), image=imag011, anchor="nw")
# canvas011.pack(expand=True , fill=BOTH)
# canvas011.place(relx=0.34 , rely= 0)


# admn_labl= Label(master=frame_admin_left , text="Menu" , font=("George" , 30) , bg="black" , fg= "red")
# admn_labl.place(relx=0.4 , rely = 0 , relwidth= 0.3)
#################################################################
imaj = PhotoImage(file="images.png")
kimaj = imaj.subsample(2,2)
sekil = Button(frame_admin_left,text="Widgets\nBuy 2.50$" , image=kimaj, compound=RIGHT,font=("george" , 15),command=burgertotal)
sekil.place(relx= 0.01 , rely = 0.20)


total_lbl = Label(frame_admin_right,text="0$" , font=(12), bg="red")
total_lbl.place(relx= 0.025, rely=0.9 ,relheight=0.08 , relwidth=0.9)

total_yaz = Label(frame_admin_right,text="TOTAL" , font=("Arial", 20) , bg= "red")
total_yaz.place(relx=0.055, rely= 0.82 , relheight=0.05 , relwidth=0.7)

silmek_buton = Button(frame_admin_right , text="Reset" , font=("Arial",10), bg="red" ,command=resetfunk)
silmek_buton.place(relx=0.065 , rely=0.52 , relheight=0.05 , relwidth=0.4)

cekcixartmaq = Button(frame_admin_right , text="Pay" , font=("Arial " , 10) , bg="red",command=cek)
cekcixartmaq.place(relx=0.065 ,rely=0.62 , relheight=0.05,relwidth=0.4)

say_lbl = Label(frame_admin_left,text=f"Widgets count   {widgetssay}" , font=("Arial",10) , bg="black" , fg="red" )
say_lbl.place(relx=0.8,rely=0.20, relheight=0.05 , relwidth=0.2)

sayfree_lbl =Label(frame_admin_left , text=f'Free Count {freesay}', font=("Arial",10),bg='black',fg="red")
sayfree_lbl.place(relx=0.8,rely=0.30, relheight=0.05, relwidth=0.2)

chcken_lbl = Label(frame_admin_left , text=f'McChicken Burger Count  {chicken}' , font=("Arial",10),bg="black",fg="red")
chcken_lbl.place(relx=0.8 , rely=0.40 , relheight=0.05 , relwidth=0.2)

count_yazi = Label(frame_admin_left,text="Count" , font=("George",20) , fg="black" , bg="red")
count_yazi.place(relx=0.8 , rely=0.1 , relheight=0.05 , relwidth=0.2)

cola_lbl = Label(frame_admin_left,text=f"Coca Cola Count {colasay}" , font=("Arial",10),fg="red",bg="black" )
cola_lbl.place(relx=0.8 , rely=0.50 , relheight=0.05,relwidth=0.2)

# 2 QANAD
imajq = PhotoImage(file="freesekil.png")
kimajq = imajq.subsample(7,7)
sekilq = Button(frame_admin_left,text="Free\nBuy 2$" , image=kimajq, compound=RIGHT,font=("george" , 15),command=freetotal)
sekilq.place(relx= 0.01 , rely = 0.35)
# 3Burger
# imajq1 = PhotoImage(file="chickenburger2.png")
# kimajq1 = imaj.subsample(2,2)
# sekilq1 = Button(frame_admin_left,text="Mc Chicken Burger \n Buy 3$" , image=kimaj, compound=RIGHT,font=("george" , 15), command=chickenburgertotal)
# sekilq1.place(relx= 0.01 , rely = 0.55)

imajq1 = PhotoImage(file="chickenburger2.png")
kimajq1 = imajq1.subsample(7,7)
sekilq1 = Button(frame_admin_left,text="Mc Chicken Burger \n Buy 3$" , image=kimajq1, compound=RIGHT,font=("george" , 15), command=chickenburgertotal)
sekilq1.place(relx= 0.01 , rely = 0.55)





imajcola = PhotoImage(file="cola.png")
kimajcola = imajcola.subsample(2,2)
sekilcola = Button(frame_admin_left,text="Coca Cola \n Buy 1.50 $" , image=kimajcola, compound=RIGHT,font=("george" , 15), command=colatotal)
sekilcola.place(relx= 0.01 , rely = 0.75)


fre_azalt = Button(frame_admin_left , text="--" , font=(20) , bg="red" , fg="black", command=freeazaltmaq)
fre_azalt.place(relx=0.75, rely=0.30)\


chcken_azalt = Button(frame_admin_left , text="--" , font=(20),bg="red",fg="black",command=chickenazaltmaq)
chcken_azalt.place(relx= 0.75, rely=0.40)

widgets_azalt=Button(frame_admin_left , text="--" , font=(20) , bg="red" , fg="black" , command=widgetsazaltmaq)
widgets_azalt.place(relx= 0.75 , rely = 0.20)

cola_azalt= Button(frame_admin_left , text='--' , font=(20),bg = "red" , fg="black", command=colaazaltmaq)
cola_azalt.place(relx = 0.75 , rely=0.50)


#  widgets butonu #############33
rightbtn_1 = Button(frame_admin_right , text= "All Menu",bg= "red", command= widgets)
rightbtn_1.place(relx=0.1, rely= 0.10  ,relwidth= 0.5 , relheight=0.10 )# ALL MENU

r_btn_2 =  Button(frame_admin_right , text= "Contact" , bg= "red" , command=back_menu)
r_btn_2.place(relx= 0.1 , rely=0.25, relwidth=0.5 , relheight=0.10)

# left isledil+
contact_1 = Label(frame_admin_left , text= "Contact Turqay Mammadov" , font=(30))


drinkss = Frame(frame_admin_left )
burgers = Frame(frame_admin_left)
frees = Frame(frame_admin_left)
# Regster sekli


imagr = tk.PhotoImage(file="rgster.png")
width, height = imagr.width(), imagr.height()
canvasr = tk.Canvas(frame_register, width=width, height=height)
canvasr.pack()
canvasr.create_image((0, 0), image=imagr, anchor="nw")
canvasr.pack(expand=True , fill=BOTH)


def saveLabel():

    admine_label.config(text="Qeyd Tamamlanmiwdir!")





# Regster sehifesi
save_btn1 = Button(master=canvasr, text="Save", bg="grey" ,command=saveLabel)
save_btn1.place(relx=0.9, rely=0.9,relwidth=0.09 , relheight=0.05)

username = Label(frame_register, text="Ad", bg="grey")
username.place(relx=0.11, rely=0.15)
username_entry = Entry(frame_register)
username_entry.place(relx=0.14, rely=0.15, relwidth=0.15)


surname = Label(frame_register, text="Soyad", bg="grey")
surname.place(relx=0.35, rely=0.15)
surname_entry = Entry(frame_register)
surname_entry.place(relx=0.39, rely=0.15, relwidth=0.15)


fathername = Label(frame_register, text="Ata adi", bg="grey")
fathername.place(relx=0.65, rely=0.15)
father_name = Entry(frame_register )
father_name.place(relx=0.69, rely=0.15, relwidth=0.15)


day = Label(frame_register, text="Gun", bg="grey")
day.place(relx=0.1, rely=0.25)
day_entry = Entry(frame_register )
day_entry.place(relx=0.1, rely=0.3, relwidth=0.1)


month = Label(frame_register, text="Ay", bg="grey")
month.place(relx=0.3, rely=0.25)
month_entry = Entry(frame_register)
month_entry.place(relx=0.3, rely=0.3, relwidth=0.1)


year = Label(frame_register, text="il", bg="grey")
year.place(relx=0.5, rely=0.25)
year_entry = Entry(frame_register)
year_entry.place(relx=0.5, rely=0.3, relwidth=0.1)

admine_label = Label(frame_register , text="" ,bg="red")
admine_label.place(relx= 0.8, rely=0.6)

a = IntVar()
r_btn_1 = Radiobutton(frame_register, text="Kisi", variable=a, value=1,bg="grey",fg='black')
r_btn_1.place(relx=0.7, rely=0.278, relwidth=0.1)


r_btn_2 = Radiobutton(frame_register, text="Qadin", variable=a, bg="Purple", value=2)
r_btn_2.place(relx=0.8, rely=0.278, relwidth=0.1)


email_1 = Label(frame_register, text="Email", bg="grey")
email_1.place(relx=0.1, rely=0.4)
email = Entry(frame_register)
email.place(relx=0.2, rely=0.4, relwidth=0.15)

btn_back_reg = Button(master=canvasr, text='Back' , font=('georgia' , 20), command = btnreg_func)
btn_back_reg.place(relx= 0.05 , rely = 0.05)



window.mainloop()
