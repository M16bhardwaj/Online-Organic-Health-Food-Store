from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

# preparing tkinter window

root = Tk()
root.title('Online Organic Health Food Store')

# creating images

menu = ImageTk.PhotoImage(Image.open("menu.png"))
add = ImageTk.PhotoImage(Image.open("add.png"))
remove = ImageTk.PhotoImage(Image.open("remove.png"))
products = ImageTk.PhotoImage(Image.open("products.png"))
income = ImageTk.PhotoImage(Image.open("income.png"))
logout_image = ImageTk.PhotoImage(Image.open("logout.png"))

# styling buttons

s=ttk.Style()
s.configure("login_as.TButton", font=("Ariel",15))
s.configure("login.TButton", font=("Ariel",11))

# creating lists

shopping = [{"id": 1001, "Name": "Organic Green Gram Dal 500g", "Available": 100, "Price": 125},
            {"id": 1002, "Name": "Organic Wild Honey 500g", "Available": 100, "Price": 350},
            {"id": 1003, "Name": "Organic Wheat Flour 5kg", "Available": 100, "Price": 300},
            {"id": 1004, "Name": "Organic Chick Peas 500g", "Available": 100, "Price": 129}]

current_shopping = [{"id": 1001, "Name": "Organic Green Gram Dal 500g", "Available": 100, "Price": 125},
                   {"id": 1002, "Name": "Organic Wild Honey 500g", "Available": 100, "Price": 350},
                   {"id": 1003, "Name": "Organic Wheat Flour 5kg", "Available": 100, "Price": 300},
                   {"id": 1004, "Name": "Organic Chick Peas 500g", "Available": 100, "Price": 129}]

add_to_cart_shopping = [{"id": 1001, "Name": "Organic Green Gram Dal 500g", "Available": 100, "Price": 125},
                   {"id": 1002, "Name": "Organic Wild Honey 500g", "Available": 100, "Price": 350},
                   {"id": 1003, "Name": "Organic Wheat Flour 5kg", "Available": 100, "Price": 300},
                   {"id": 1004, "Name": "Organic Chick Peas 500g", "Available": 100, "Price": 129}]

cart=[]

# landing page

def login_as():
    for widget in frame.winfo_children():
        widget.destroy()
    login = Label(frame, text=" Login As ", font=("Ariel",25), bg="#d6b3e7")
    login.pack(side=TOP,pady=50)
    login_as_admin = ttk.Button(frame, text="ADMIN", style="login_as.TButton", command=admin_login)
    login_as_admin.pack(side= LEFT, padx=100, pady=100)
    login_as_client = ttk.Button(frame, text="CLIENT", style="login_as.TButton", command=client_login)
    login_as_client.pack(side = LEFT, padx=100, pady=100)

# admin login page

def admin_login():
    for widget in frame.winfo_children():
        widget.destroy()
    admin_login = Label(frame, text="Admin Login", font=("Ariel",20), bg="#d6b3e7")
    admin_login.grid(row=0, column=1, padx=25, pady=40)
    username = Label(frame, text="Username", font=("Ariel",15), bg="#d6b3e7")
    username.grid(row=1,column=0, padx=25, pady=25, ipadx=20)
    username_entry = ttk.Entry(frame, width=30)
    username_entry.grid(row=1, column=2, padx=25, pady=25)
    password = Label(frame, text="Password", font=("Ariel", 15), bg="#d6b3e7")
    password.grid(row=2, column=0, padx= 25, pady=25, ipadx=20)
    password_entry = ttk.Entry(frame, width=30,show="*")
    password_entry.grid(row=2, column=2, padx=25, pady=25)
    login = ttk.Button(frame, text="Login", style="login.TButton", command=lambda: check_admin(username_entry.get(),password_entry.get()))
    login.grid(row=3,column=1, padx=25,pady=25)
    back = ttk.Button(frame, text="Back", command=login_as)
    back.grid(row=5, column=1,pady=15)

# checking username and password for admin

def check_admin(username,password):
    if username=="admin" and password=="admin":
        admin_choice()
    else:
        messagebox.showerror("Login Failed","Invalid Credentials")

# admin options page

def admin_choice():
    for widget in frame.winfo_children():
        widget.destroy()
    welcome_admin = Label(frame, text="Welcome Admin", font=("Ariel",20), bg="#d6b3e7")
    welcome_admin.grid(row=0,column=1,pady=40,padx=20)
    display_menu = Button(frame, text="Display Menu", image=menu, compound=LEFT, font=("Ariel",12), padx=22, pady=10, command=admin_display_menu)
    display_menu.grid(row=1,column=0,pady=30,padx=20)
    add_product = Button(frame, text="Add Product", image=add, compound=LEFT, font=("Ariel",12), padx=25, pady=10, command=admin_add_product)
    add_product.grid(row=1,column=1,pady=30,padx=20)
    remove_product = Button(frame, text="Remove Product", image=remove, compound=LEFT, font=("Ariel",12), padx=8, pady=10, command=admin_remove_product)
    remove_product.grid(row=1,column=2,pady=30,padx=20)
    products_available = Button(frame, text="Products Available", image=products, compound=LEFT, font=("Ariel",12), padx=8, pady=10, command=admin_available_products)
    products_available.grid(row=2,column=0,pady=30,padx=20)
    total_income = Button(frame, text="Total Income", image=income, compound=LEFT, font=("Ariel",12), padx=22, pady=10, command=admin_total_income)
    total_income.grid(row=2,column=1,pady=30,padx=20)
    logout = Button(frame, text="Logout", image=logout_image, compound=LEFT, font=("Ariel",12), padx=30, pady=10, command=login_as)
    logout.grid(row=2, column=2,pady=30,padx=20)
    space = Label(frame,text="   ",font=("Ariel",15), bg="#d6b3e7")
    space.grid(row=3,column=0, pady=20)

# display menu option

def admin_display_menu():
    d=0
    for widget in frame.winfo_children():
        widget.destroy()
    menu = Label(frame, text="Menu", font=("Ariel",20), bg="#d6b3e7")
    menu.grid(row=0, column=0, columnspan=3,padx=280,pady=30)
    item = Label(frame, text="ID : "+str(current_shopping[d]["id"]) + "\n"+current_shopping[d]["Name"] + "\n Price : " + str(
        current_shopping[d]["Price"]) + "\n Available : " + str(current_shopping[d]["Available"]), bg="#d6b3e7")
    item.grid(row=3, column=1, pady=10)
    back = ttk.Button(frame, text="<<", command=lambda: back_item(d, item), state=DISABLED, width=9)
    back.grid(row=4, column=0, pady=10)
    main_menu = ttk.Button(frame, text="Main Menu", style="login.TButton", command=admin_choice)
    main_menu.grid(row=4, column=1, pady=30)
    forward = ttk.Button(frame, text=">>", command=lambda: forward_item(d, item))
    forward.grid(row=4, column=2, pady=10)
    status = Label(frame, text="Product " + str(d + 1) + " of " + str(len(current_shopping)), bg="#d6b3e7",
                   relief=SUNKEN)
    status.grid(row=5, column=0, columnspan=3)

# back button

def back_item(d, item):
    d = d - 1
    item.grid_forget()
    items = Label(frame, text="ID : "+str(current_shopping[d]["id"]) + "\n"+current_shopping[d]["Name"] + "\n Price : " + str(
        current_shopping[d]["Price"]) + "\n Available : " + str(current_shopping[d]["Available"]), bg="#d6b3e7")
    items.grid(row=3, column=1, pady=10)
    back = ttk.Button(frame, text="<<", command=lambda: back_item(d, items))
    back.grid(row=4, column=0, pady=10)
    main_menu = ttk.Button(frame, text="Main Menu", style="login.TButton", command=admin_choice)
    main_menu.grid(row=4, column=1, pady=30)
    forward = ttk.Button(frame, text=">>", command=lambda: forward_item(d, items))
    forward.grid(row=4, column=2, pady=10)
    if d == 0:
        back = ttk.Button(frame, text="<<", command=lambda: back_item(d, items), state=DISABLED)
        back.grid(row=4, column=0, pady=10)
    status = Label(frame, text="Product " + str(d + 1) + " of " + str(len(current_shopping)), bg="#d6b3e7",
                   relief=SUNKEN)
    status.grid(row=5, column=0, columnspan=3)

# forward button

def forward_item(d, item):
    d = d + 1
    item.grid_forget()
    items = Label(frame, text="ID : "+str(current_shopping[d]["id"]) + "\n"+current_shopping[d]["Name"] + "\n Price : " + str(
        current_shopping[d]["Price"]) + "\n Available : " + str(current_shopping[d]["Available"]), bg="#d6b3e7")
    items.grid(row=3, column=1, pady=10)
    back = ttk.Button(frame, text="<<", command=lambda: back_item(d, items))
    back.grid(row=4, column=0, pady=10)
    main_menu = ttk.Button(frame, text="Main Menu", style="login.TButton", command=admin_choice)
    main_menu.grid(row=4, column=1, pady=30)
    forward = ttk.Button(frame, text=">>", command=lambda: forward_item(d, items))
    forward.grid(row=4, column=2, pady=10)
    if d == (len(current_shopping) - 1):
        forward = ttk.Button(frame, text=">>", command=lambda: forward_item(d, items), state=DISABLED)
        forward.grid(row=4, column=2, pady=10)
    status = Label(frame, text="Product " + str(d + 1) + " of " + str(len(current_shopping)), bg="#d6b3e7",
                   relief=SUNKEN)
    status.grid(row=5, column=0, columnspan=3)

# add product option

def admin_add_product():
    for widget in frame.winfo_children():
        widget.destroy()
    add_product = Label(frame, text="    Add Product",font=("Ariel",20), bg="#d6b3e7")
    add_product.grid(row=0, column=1, padx=40, pady=50)
    product_id = Label(frame, text="ID : ",font=("Ariel",10), bg="#d6b3e7")
    product_id.grid(row=1, column= 0, padx=40, pady=10)
    product_id_entry= ttk.Entry(frame, width=30)
    product_id_entry.grid(row=1,column=2, padx=20, pady=10)
    product_name = Label(frame, text="Name : ",font=("Ariel",10), bg="#d6b3e7")
    product_name.grid(row=2,column= 0, padx=40, pady=10)
    product_name_entry = ttk.Entry(frame, width=30)
    product_name_entry.grid(row=2, column=2,padx =20, pady=10)
    product_available = Label(frame, text="Quantity : ",font=("Ariel",10), bg="#d6b3e7")
    product_available.grid(row=3, column= 0, padx=40, pady=10)
    product_available_entry = ttk.Entry(frame, width=30)
    product_available_entry.grid(row=3, column=2, padx =20, pady=10)
    product_price = Label(frame, text="Price : ",font=("Ariel",10), bg="#d6b3e7")
    product_price.grid(row=4, column=0, padx=40, pady=10)
    product_price_entry = ttk.Entry(frame, width=30)
    product_price_entry.grid(row=4, column=2, padx =20, pady=10)
    add = ttk.Button(frame, text="Add", command=lambda: adding(product_id_entry,product_name_entry,product_available_entry,product_price_entry))
    add.grid(row=5, column=2, pady=10)
    back = ttk.Button(frame, text="Back", command=admin_choice)
    back.grid(row=5, column=0, pady=20)

# add backend functioning

def adding(id, name, available, price):
    new = {"id": id.get(), "Name": name.get(), "Available": available.get(),"Price": price.get()}
    new1 = {"id": id.get(), "Name": name.get(), "Available": available.get(), "Price": price.get()}
    new2 = {"id": id.get(), "Name": name.get(), "Available": available.get(), "Price": price.get()}
    for d in current_shopping:
        if int(d["id"])==int(new["id"]):
            messagebox.showwarning("Warning","This product ID is already available")
            response = messagebox.askyesno("Increase Quantity","Do you want to increase the quantity of this product")
            if response==1:
                add_quantity(id,name,available,price)
            else:
                admin_add_product()
            return

    shopping.append(new)
    current_shopping.append(new1)
    add_to_cart_shopping.append(new2)
    id.delete(0,END)
    name.delete(0,END)
    available.delete(0,END)
    price.delete(0,END)
    messagebox.showinfo("Successful","Added Successfully")

# add backend functioning continue

def add_quantity(id,name,quantity,price):
    for (d,p,i) in zip(current_shopping,shopping,add_to_cart_shopping):
        if int(d["id"]) == int(id.get()):
            d["Available"] = d["Available"] + int(quantity.get())
            p["Available"] = p["Available"] + int(quantity.get())
            i["Available"] = i["Available"] + int(quantity.get())
    id.delete(0, END)
    name.delete(0, END)
    quantity.delete(0, END)
    price.delete(0, END)
    messagebox.showinfo("Successful","Added Successfully")

# remove product option

def admin_remove_product():
    for widget in frame.winfo_children():
        widget.destroy()
    remove_product = Label(frame, text="Remove Product", font=("Ariel",20), bg="#d6b3e7")
    remove_product.grid(row=0, column=1, padx=20, pady=50)
    enter_id = Label(frame, text="Enter Product ID : ", font=("Ariel",10), bg="#d6b3e7")
    enter_id.grid(row=1,column=0, padx=20, pady=30)
    enter_id_entry = ttk.Entry(frame, width=30)
    enter_id_entry.grid(row=1, column=2, padx=20, pady=30)
    enter_quantity = Label(frame, text="Enter Quantity to be removed : ", font=("Ariel",10), bg="#d6b3e7")
    enter_quantity.grid(row=2,column=0, pady=30)
    enter_quantity_entry = ttk.Entry(frame, width=30)
    enter_quantity_entry.grid(row=2,column=2, padx=20, pady=30)
    back = ttk.Button(frame, text="Back", command=admin_choice)
    back.grid(row=3, column=0, pady=20)
    remove = ttk.Button(frame, text="Remove", command=lambda: removing(enter_id_entry,enter_quantity_entry))
    remove.grid(row=3, column=2, pady=20)

# remove backend functioning

def removing(id,quantity):
    check=0
    for (d,p,i) in zip(current_shopping,shopping,add_to_cart_shopping):
        if int(d["id"])==int(id.get()):
            check=1
            if int(d["Available"]) >= int(quantity.get()):
                d["Available"] = int(d["Available"]) - int(quantity.get())
                p["Available"] = int(p["Available"]) - int(quantity.get())
                i["Available"] = int(i["Available"]) - int(quantity.get())
                messagebox.showinfo("Successful","Product Removed Successfully")
                if int(d["Available"])==0:
                    del shopping[shopping.index(d)]
                    del current_shopping[current_shopping.index(d)]
                    del add_to_cart_shopping[add_to_cart_shopping.index(d)]
            else:
                messagebox.showerror("Error","Quantity Exceeded")
    if check==0:
        messagebox.showerror("Error","Invalid Product ID")

# products available option

def admin_available_products():
    for widget in frame.winfo_children():
        widget.destroy()
    available_products = Label(frame, text="Products Available", font=("Ariel",20), bg="#d6b3e7")
    available_products.pack(padx=200, pady=20)
    total=0
    line1 = Label(frame, text="-----------------------------------------", bg="#d6b3e7")
    line1.pack()
    for d in current_shopping:
        total=total+int(d["Available"])
        product = Label(frame, text = str(d["Name"])+" : "+str(d["Available"])+" units ", bg="#d6b3e7")
        product.pack(pady=5)
    total_products=Label(frame, text="Total Products Available : "+str(total),bg="#d6b3e7")
    total_products.pack(pady=20)
    line2 = Label(frame, text="-----------------------------------------", bg="#d6b3e7")
    line2.pack()
    back = ttk.Button(frame, text="Back", command=admin_choice)
    back.pack(pady=30)

# total income option

def admin_total_income():
    for widget in frame.winfo_children():
        widget.destroy()
    income = Label(frame, text="Total Income", font=("Ariel",20), bg="#d6b3e7")
    income.pack(padx=230,pady=30)
    total=0
    products=0
    for d,p in zip(current_shopping,shopping):
        total = total + (int(p["Available"])*int(p["Price"]) - int(d["Available"])*int(d["Price"]))
        products = products + (int(p["Available"])-int(d["Available"]))
    products_sold = Label(frame, text="Number of Products Sold : " + str(products), font=("Ariel",12), bg="#d6b3e7")
    products_sold.pack(pady=20)
    line1 = Label(frame, text="-----------------------------------------", bg="#d6b3e7")
    line1.pack(pady=5)
    total_income = Label(frame, text="Income : "+str(total), font=("Ariel",12), bg="#d6b3e7")
    total_income.pack(pady=5)
    line2 = Label(frame, text="-----------------------------------------", bg="#d6b3e7")
    line2.pack(pady=5)
    back = ttk.Button(frame, text="Back", command=admin_choice)
    back.pack(pady=30)

# client login page

def client_login():
    for widget in frame.winfo_children():
        widget.destroy()
    client_login = Label(frame, text="Client Login", font=("Ariel", 20), bg="#d6b3e7")
    client_login.grid(row=0, column=1, padx=25, pady=40)
    username = Label(frame, text="Username", font=("Ariel", 15), bg="#d6b3e7")
    username.grid(row=1, column=0, padx=25, pady=25, ipadx=20)
    username_entry = ttk.Entry(frame, width=30)
    username_entry.grid(row=1, column=2, padx=25, pady=25)
    password = Label(frame, text="Password", font=("Ariel", 15), bg="#d6b3e7")
    password.grid(row=2, column=0, padx=25, pady=25, ipadx=20)
    password_entry = ttk.Entry(frame, width=30, show="*")
    password_entry.grid(row=2, column=2, padx=25, pady=25)
    login = ttk.Button(frame, text="Login", style="login.TButton",
                   command=lambda: check_client(username_entry.get(), password_entry.get()))
    login.grid(row=3, column=1, padx=25, pady=25)
    back = ttk.Button(frame, text="Back", command=login_as)
    back.grid(row=5, column=1, pady=15)

# checking username and password for client

def check_client(username,password):
    if username=="client" and password=="client":
        client_home()
    else:
        messagebox.showerror("Login Failed","Invalid Credentials")

# client home page

def client_home():
    d=0
    for widget in frame.winfo_children():
        widget.destroy()
    menu = Label(frame, text = "Menu", font=("Ariel", 20), bg="#d6b3e7")
    menu.grid(row=0,column=0,columnspan=3,padx=280,pady=20)
    logout = ttk.Button(frame,text="Logout",style="login.TButton",command=login_as)
    logout.grid(row=1,column=0,pady=30)
    show_cart = ttk.Button(frame, text="Cart", style="login.TButton", command=showing_cart)
    show_cart.grid(row=1, column=2,pady=30)
    item = Label(frame,text=add_to_cart_shopping[d]["Name"]+"\n Price : "+str(add_to_cart_shopping[d]["Price"])+"\n Available : "+str(add_to_cart_shopping[d]["Available"]),bg="#d6b3e7")
    item.grid(row=3, column=1,pady=10)
    back = ttk.Button(frame, text="<<",command=lambda:backing(d,item),state=DISABLED,width=9)
    back.grid(row=4, column=0,pady=10)
    add_to_cart = ttk.Button(frame,text="Add to Cart", style="login.TButton",command=lambda:add_cart(d))
    add_to_cart.grid(row=4, column=1,pady=10)
    forward = ttk.Button(frame, text=">>", command=lambda:forwarding(d,item))
    forward.grid(row=4, column=2,pady=10)
    status = Label(frame, text="Product "+str(d+1)+" of "+str(len(add_to_cart_shopping)), bg="#d6b3e7", relief=SUNKEN)
    status.grid(row=5, column=0, columnspan=3)

# back button

def backing(d,item):
    d=d-1
    item.grid_forget()
    items = Label(frame, text=add_to_cart_shopping[d]["Name"] + "\n Price : " + str(add_to_cart_shopping[d]["Price"]) + "\n Available : " + str(add_to_cart_shopping[d]["Available"]), bg="#d6b3e7")
    items.grid(row=3, column=1,pady=10)
    back = ttk.Button(frame, text="<<", command=lambda:backing(d, items))
    back.grid(row=4, column=0,pady=10)
    add_to_cart = ttk.Button(frame, text="Add to Cart", style="login.TButton", command=lambda: add_cart(d))
    add_to_cart.grid(row=4, column=1,pady=10)
    forward = ttk.Button(frame, text=">>", command=lambda:forwarding(d, items))
    forward.grid(row=4, column=2,pady=10)
    if d==0:
        back = ttk.Button(frame, text="<<", command=lambda:backing(d, items),state=DISABLED)
        back.grid(row=4, column=0,pady=10)
    status = Label(frame, text="Product " + str(d + 1) + " of " + str(len(add_to_cart_shopping)), bg="#d6b3e7",
                   relief=SUNKEN)
    status.grid(row=5, column=0, columnspan=3)

# forward button

def forwarding(d,item):
    d=d+1
    item.grid_forget()
    items = Label(frame, text=add_to_cart_shopping[d]["Name"] + "\n Price : " + str(add_to_cart_shopping[d]["Price"]) + "\n Available : " + str(add_to_cart_shopping[d]["Available"]), bg="#d6b3e7")
    items.grid(row=3, column=1,pady=10)
    back = ttk.Button(frame, text="<<", command=lambda:backing(d, items))
    back.grid(row=4, column=0,pady=10)
    add_to_cart = ttk.Button(frame, text="Add to Cart", style="login.TButton", command=lambda: add_cart(d))
    add_to_cart.grid(row=4, column=1,pady=10)
    forward = ttk.Button(frame, text=">>", command=lambda:forwarding(d, items))
    forward.grid(row=4, column=2,pady=10)
    if d==(len(add_to_cart_shopping)-1):
        forward = ttk.Button(frame, text=">>", command=lambda:forwarding(d, items),state=DISABLED)
        forward.grid(row=4, column=2,pady=10)
    status = Label(frame, text="Product " + str(d + 1) + " of " + str(len(add_to_cart_shopping)), bg="#d6b3e7",
                   relief=SUNKEN)
    status.grid(row=5, column=0, columnspan=3)

# add to cart button

def add_cart(d):
    cart.append(add_to_cart_shopping[d])
    messagebox.showinfo("Added to Cart",shopping[d]["Name"]+" successfully added to cart!")
    add_to_cart_shopping[d]["Available"]=int(add_to_cart_shopping[d]["Available"])-1

# displaying shopping cart

def showing_cart():
    for widget in frame.winfo_children():
        widget.destroy()
    i=0
    show_cart = Label(frame,text="Cart",font=("Ariel",20),bg="#d6b3e7")
    show_cart.grid(row=0,column=0,columnspan=3,padx=280,pady=30)
    for d in cart:
        i=i+1
        item = Label(frame, text=str(d["Name"])+" : "+str(d["Price"])+"Rs.",bg="#d6b3e7")
        item.grid(row=i, column=1,pady=10)
    back = ttk.Button(frame, text="Back", command=client_home)
    back.grid(row=i+1, column=0, pady=20)
    buy = ttk.Button(frame, text="Buy", command=buy_selected)
    buy.grid(row=i+1, column=1, pady=20)
    clear = ttk.Button(frame, text="Clear All", command=clear_all)
    clear.grid(row=i+1, column=2, pady=20)

# buy button

def buy_selected():
    total=0
    for d in cart:
            total=total+int(d["Price"])
    response = messagebox.askyesno("Are you sure", "Total Price : "+str(total)+"\n"+"Do you want to continue to buy")
    if response == 1:
        messagebox.showinfo("Thank You", "Products successfully ordered\nThank You and have a nice day")
        for d in cart:
            for p in current_shopping:
                if d["Name"]==p["Name"]:
                    p["Available"]=int(p["Available"])-1
    cart.clear()
    showing_cart()

# clear all button

def clear_all():
    for d in cart:
        for p in add_to_cart_shopping:
            if d["Name"]==p["Name"]:
                p["Available"]=int(p["Available"])+1
    cart.clear()
    showing_cart()

# creating frame

frame = Frame(root, bg="#d6b3e7", height =350, width=800)
frame.pack()

# running landing page

login_as()

# looping tkinter window

root.mainloop()