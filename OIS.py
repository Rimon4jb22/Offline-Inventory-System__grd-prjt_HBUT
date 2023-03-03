from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3

import tkinter as tk
from tkinter import Button, StringVar, ttk

root = Tk()
root.title("Offline Inventory System")

width = 1024
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="mediumslateblue")

# ========================================VARIABLES========================================

USERNAME = StringVar()
PASSWORD = StringVar()


# ========================================METHODS==========================================

def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()


def Exit():
    result = tkMessageBox.askquestion('Offline Inventory System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


'''def Exit2():
    result = tkMessageBox.askquestion('Offline Inventory System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
       # Home.destroy()
        exit()
'''

def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Offline Inventory System/Account Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()


def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Administrator Login", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)

'''
def Logout():
    result = tkMessageBox.askquestion('Offline Inventory System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        admin_id = ""
        root.deiconify()
        ShowHome.destroy()
'''



def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            #smain()
            #hm()
            ShowHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()




# ========================================From s main ===================================


def ShowHome():
    root.withdraw()
    smain()
    #loginform.withdraw()
    #loginform.destroy()


def smain():

    loginform.destroy()

    win = tk.Tk()
    win.geometry("1350x700+0+0")
    win.title("OIS")

    # ---------Background Color
    win.config(bg="#7285CC")

    #--------- Adding some style
    style = ttk.Style()

    # --------Pick a theme
    style.theme_use("default")

    style.configure("Treeview",
                    background="white",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="white"
                    )

    #--------- Change selected color
    style.map(
        "Treeview",
        background=[("selected", "darkred")]
    )

    #-------- Top Menu

    title_label = tk.Label(
        win,
        text="Offline Inventory System",
        font=("Arial", 20, "bold"),
        padx=15,
        pady=15,
        border=0,
        relief=tk.GROOVE,
        bg="mediumslateblue",
        foreground="white"
    )
    title_label.pack(side=tk.TOP, fill=tk.X)

    #------ Left Menu

    detail_frame = tk.LabelFrame(
        win, text="Records",
        font=("Arial", 14),
        bg="#7285CC",
        foreground="black",
        relief=tk.GROOVE
    )
    detail_frame.place(x=40, y=90, width=420, height=565)

    #--------- Data Frame

    data_frame = tk.Frame(
        win,
        bg="#495582",
        relief=tk.GROOVE
    )
    data_frame.place(x=490, y=98, width=830, height=565)

    #--------- Label with Entry

    id_lab = tk.Label(
        detail_frame,
        text="ID:",
        font=("Arial", 16),
        bg="#7285CC",
        foreground="black"
    )
    id_lab.place(x=20, y=15)

    id_ent = tk.Entry(
        detail_frame,
        bd=1,
        font=("arial", 16),
        bg="white",
        foreground="black",
    )
    id_ent.place(x=110, y=17, width=250, height=30)

    # 2
    Productname_lab = tk.Label(
        detail_frame,
        text="Product:",
        font=("Arial", 16),
        bg="#7285CC",
        foreground="black"
    )
    Productname_lab.place(x=20, y=65)

    Productname_ent = tk.Entry(
        detail_frame,
        bd=1,
        font=("arial", 16),
        bg="white",
        foreground="black",
    )
    Productname_ent.place(x=110, y=65, width=250, height=30)


    # 4
    price_lab = tk.Label(
        detail_frame,
        text="price:",
        font=("Arial", 16),
        bg="#7285CC",
        foreground="black"
    )
    price_lab.place(x=20, y=113)

    price_ent = tk.Entry(
        detail_frame,
        bd=1,
        font=("arial", 16),
        bg="white",
        foreground="black",
    )
    price_ent.place(x=110, y=113, width=250, height=30)

    # 5
    quantity_lab = tk.Label(
        detail_frame,
        text="Quantity:",
        font=("Arial", 16),
        bg="#7285CC",
        foreground="black"
    )
    quantity_lab.place(x=20, y=161)

    quantity_ent = tk.Entry(
        detail_frame,
        bd=1,
        font=("arial", 16),
        bg="white",
        foreground="black",
    )
    quantity_ent.place(x=110, y=161, width=250, height=30)



    # 7
    Total_lab = tk.Label(
        detail_frame,
        text="Total:",
        font=("Arial", 16),
        bg="#7285CC",
        foreground="black"
    )
    Total_lab.place(x=20, y=209)

    Total_ent = tk.Entry(
        detail_frame,
        bd=1,
        font=("arial", 16),
        bg="white",
        foreground="black",
    )
    Total_ent.place(x=110, y=209, width=250, height=30)



    # Database frame

    main_frame = tk.Frame(
        data_frame,
        bg="#495582",
        bd=2,
        relief=tk.GROOVE
    )
    main_frame.pack(fill=tk.BOTH, expand=True)

    y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

    # Treeview database

    inventory_table = ttk.Treeview(main_frame, columns=(
        "ID", "Product Name", "price", "Quantity", "Total",
    ), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    y_scroll.config(command=inventory_table.yview)
    x_scroll.config(command=inventory_table.xview)

    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    inventory_table.heading("ID", text="ID")
    inventory_table.heading("Product Name", text="Product Name")
    inventory_table.heading("price", text="price")
    inventory_table.heading("Quantity", text="Quantity")
    inventory_table.heading("Total", text="Total")


    inventory_table["show"] = "headings"

    inventory_table.column("ID", width=100)
    inventory_table.column("Product Name", width=100)
    inventory_table.column("price", width=100)
    inventory_table.column("Quantity", width=100)
    inventory_table.column("Total", width=100)
    inventory_table.pack(fill=tk.BOTH, expand=True)

    # Default data

    data = [

    ]

    # Create stripped row tags
    inventory_table.tag_configure("oddrow", background="white")
    inventory_table.tag_configure("evenrow", background="#A5ABC1")

    global count
    count = 0
    for record in data:
        if count % 2 == 0:
            inventory_table.insert(parent="", index="end", iid=count, text="", values=(
            record[0], record[1], record[2], record[3], record[4],record[5], record[6], record[7]), tags=("evenrow"))
        else:
            inventory_table.insert(parent="", index="end", iid=count, text="", values=(
            record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=("oddrow"))

        count += 1




    # Functions

    # Add Function
    def add_record():
        inventory_table.tag_configure("oddrow", background="white")
        inventory_table.tag_configure("evenrow", background="#A5ABC1")

        global count
        if count % 2 == 0:
            inventory_table.insert(parent="", index="end", iid=count, text="", values=(
                id_ent.get(),
                Productname_ent.get(),
                price_ent.get(),
                quantity_ent.get(),
                Total_ent.get(),


            ),
                                 tags=("evenrow")
                                 )
        else:
            inventory_table.insert(parent="", index="end", iid=count, text="", values=(
                id_ent.get(),
                Productname_ent.get(),
                price_ent.get(),
                quantity_ent.get(),
                Total_ent.get(),


            ),
                                 tags=("oddrow")
                                 )
        count += 1


    # Delete All Function
    def delete_all():
        for record in inventory_table.get_children():
            inventory_table.delete(record)


    # Delete One Function
    def delete_one():
        x = inventory_table.selection()[0]
        inventory_table.delete(x)


    # Select Record
    def select_record():
        id_ent.delete(0, END)
        Productname_ent.delete(0, END)
        price_ent.delete(0, END)
        quantity_ent.delete(0, END)
        Total_ent.delete(0, END)
        selected = inventory_table.focus()

        values = inventory_table.item(selected, "values")
        id_ent.insert(0, values[0])
        Productname_ent.insert(0, values[1])
        price_ent.insert(0, values[2])
        quantity_ent.insert(0, values[3])
        Total_ent.insert(0, values[4])



    # Update Button
    def update_record():
        selected = inventory_table.focus()
        inventory_table.item(selected, text="", values=(
        id_ent.get(), Productname_ent.get(), price_ent.get(), quantity_ent.get(), Total_ent.get(), ))

        id_ent.delete(0, END)
        Productname_ent.delete(0, END)
        price_ent.delete(0, END)

        quantity_ent.delete(0, END)

        Total_ent.delete(0, END)


        # Clear boxes
        id_ent.delete(0, END),
        Productname_ent.delete(0, END),
        price_ent.delete(0, END),

        quantity_ent.delete(0, END),

        Total_ent.delete(0, END),



    #----------------------- Buttons -------

    btn_frame = tk.Frame(
        detail_frame,
        bg="#7285CC",
        bd=0,
        relief=tk.GROOVE
    )
    btn_frame.place(x=40, y=309, width=310, height=130)

    #-------- Add Button
    add_btn = tk.Button(
        btn_frame,
        bg="#495582",
        foreground="white",
        text="Add",
        bd=2,
        font=("Arial", 13), width=15,
        command=add_record
    )
    add_btn.grid(row=0, column=0, padx=2, pady=2)

    #--------- Update Button
    update_btn = tk.Button(
        btn_frame,
        bg="#495582",
        foreground="white",
        text="Update",
        bd=2,
        font=("Arial", 13), width=15,
        command=select_record
    )
    update_btn.grid(row=0, column=1, padx=2, pady=2)

    # --------- LogOut Button
    LogOut_btn = tk.Button(
        btn_frame,
        bg="#495582",
        foreground="white",
        text="LogOut",
        bd=2,
        font=("Arial", 13), width=15,
        #command=Logout

    )
    LogOut_btn.grid(row=1, column=0, padx=2, pady=2)

    #-------- Save Button
    cal_btn = tk.Button(
        btn_frame,
        bg="#495582",
        foreground="white",
        text="Save",
        bd=2,
        font=("Arial", 13), width=15,
        command=update_record
    )
    cal_btn.grid(row=1, column=1, padx=2, pady=2)

    #-------- Save Button
    save_btn = tk.Button(
        btn_frame,
        bg="#495582",
        foreground="white",
        text="Clear",
        bd=2,
        font=("Arial", 13), width=15,
        command=delete_all
    )
    save_btn.grid(row=2, column=0, padx=2, pady=2)

    #------ Delete Button
    delete_btn = tk.Button(
        btn_frame,
        bg="#495582",
        foreground="white",
        text="Delete",
        bd=2,
        font=("Arial", 13), width=15,
        command=delete_one
    )
    delete_btn.grid(row=2, column=1, padx=2, pady=2)

    win.mainloop()



# ========================================MENUBAR WIDGETS==================================

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)


# ========================================FRAME============================================

Title = Frame(root, bd=0, relief=SOLID)
Title.pack(pady=10)

# ========================================LABEL WIDGET=====================================


lbl_display = Label(Title, text="Offline Inventory System", font=('arial', 45),
                      bg="mediumslateblue",
                      foreground="white")
lbl_display.pack( )

login_button = Button(root, text="login", font=("arial, 28"), command=ShowLoginForm)
login_button.pack()

Exit_button = Button(root, text="Exit", font=("arial, 28"), command=Exit)
Exit_button.pack()


# ========================================INITIALIZATION===================================

if __name__ == '__main__':
    root.mainloop()
