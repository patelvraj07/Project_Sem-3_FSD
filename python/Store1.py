from tkinter import *
from tkinter import messagebox
import random
class Owner:
    products={
        "Maggie":{'price':56,"quantity":5},
        "Coca Cola":{'price':40,"quantity":10},
        "Ferrero Rocher":{"price":494,"quantity":15},
        "Amul Dark Chocolate":{"price":300,"quantity":8},
        "Nescafe Coffe":{'price':390,"quantity":15},
        "Nutella":{'price':441,'quantity':25},
        "Tata Cashews":{'price':561,"quantity":12},
        "Wagh Bakri Tea":{'price':541,'quantity':25},
        "Oreo":{'price':340,'quantity':15},
        "Bikaneri Bhujia":{'price':242,'quantity':30},
        "Olive Oil":{'price':2350,'quantity':8},
        "Tata Salt":{'price':25,'quantity':25},
        "Red Bull":{'price':469,'quantity':12},
        "Bread":{'price':30,'quantity':13},
        "Amul Butter":{'price':56,'quantity':24}
    }
    def owner_button_click(self):
        global username_entry,password_entry,login_window
        login_window=Toplevel()
        login_window.title("Owner Login")
        login_window.geometry("1080x1080")
        login_window.config(bg=BG)
        username_label=Label(login_window,text="Username: ",font=("Comic Sans MS",22,"bold"),bg=BG,fg=FONT)
        username_label.place(y=150,x=350)
        username_entry=Entry(login_window,bd=8,relief=GROOVE,font=("Comic Sans MS",10,"bold"))
        username_entry.place(y=165,x=550)
        password_label=Label(login_window,text="Password: ",font=("Comic Sans MS",22,"bold"),bg=BG,fg=FONT)
        password_label.place(y=250,x=350)
        password_entry=Entry(login_window,show="*",bd=8,relief=GROOVE,font=("Comic Sans MS",10,"bold"))
        password_entry.place(y=265,x=550)
        login_btn=Button(login_window,text="Login In",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT,bd=8,relief=GROOVE,command=Owner().login_in)
        login_btn.place(y=350,x=550)
    def login_in(self):
        username="vraj2004"
        password=99099
        if username==username_entry.get() and password==int(password_entry.get()):
            login_window.destroy()
            self.show_owner_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    def show_owner_menu(self):
        self.owner_menu=Toplevel()
        self.owner_menu.title("Owner Menu")
        self.owner_menu.geometry("400x200")
        self.owner_menu.config(bg=BG)
        add_product_btn=Button(self.owner_menu,text="Add Product",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT,bd=8,relief=GROOVE,command=self.add_product)
        add_product_btn.place(y=150,x=610)
        remove_product_btn=Button(self.owner_menu,text="Remove Product",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT,bd=8,relief=GROOVE,command=self.remove_product)
        remove_product_btn.place(y=230,x=610)
        view_product_btn=Button(self.owner_menu,text="View Product",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT,bd=8,relief=GROOVE,command=self.view_product_list)
        view_product_btn.place(y=310,x=610)
    def view_product_list(self):
        view_product_window = Toplevel()
        view_product_window.title("View Product")
        view_product_window.geometry("1080x1080")
        Label(view_product_window, text="Product",font=("Comic Sans MS",15,"bold")).grid(row=0, column=0, padx=5)
        Label(view_product_window, text="Price",font=("Comic Sans MS",15,"bold")).grid(row=0, column=1, padx=5)
        Label(view_product_window, text="Quantity",font=("Comic Sans MS",15,"bold")).grid(row=0, column=2, padx=5)
        for idx, (product_name, product_details) in enumerate(self.products.items(), start=1):
            Label(view_product_window, text=product_name,font=("Harlow Solid",10,"bold")).grid(row=idx, column=0, padx=5)
            Label(view_product_window, text=f"{product_details['price']:.2f}",font=("Harlow Solid",10,"bold")).grid(row=idx, column=1, padx=5)
            Label(view_product_window, text=str(product_details['quantity']),font=("Harlow Solid",10,"bold")).grid(row=idx, column=2, padx=5)

    def add_product(self):
        add_product_window=Toplevel()
        add_product_window.title("Add Product")
        add_product_window.geometry("1080x1080")
        add_product_window.config(bg=BG)
        product_name=Label(add_product_window,text="Product Name: ",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT)
        product_name.place(y=150,x=350)
        self.product_name_entry=Entry(add_product_window,bd=8,relief=GROOVE,font=("Comic Sans MS",10,"bold"))
        self.product_name_entry.place(y=165,x=550)
        product_price=Label(add_product_window,text="Price: ",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT)
        product_price.place(y=250,x=350)
        self.product_price_entry=Entry(add_product_window,bd=8,relief=GROOVE,font=("Comic Sans MS",10,"bold"))
        self.product_price_entry.place(y=265,x=550)
        product_quantity=Label(add_product_window,text="Quantity: ",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT)
        product_quantity.place(y=350,x=350)
        self.product_quantity_entry=Entry(add_product_window,bd=8,relief=GROOVE,font=("Comic Sans MS",10,"bold"))
        self.product_quantity_entry.place(y=365,x=550)
        add_button=Button(add_product_window,text="Add",font=("Comic Sans MS",15,"bold"),fg=FONT,bg=BG,command=self.add_to_list)
        add_button.place(y=450,x=350)
    def add_to_list(self):
        price=self.product_price_entry.get()
        quantity=self.product_quantity_entry.get()
        if self.product_name_entry.get() not in self.products:
            self.products[self.product_name_entry.get()]={'price':int(price),'quantity':int(quantity)}
        else:
            existing_price = self.products[self.product_name_entry.get()]['price']
            existing_quantity = self.products[self.product_name_entry.get()]['quantity']
            updated_price = int(price)
            updated_quantity = existing_quantity + int(quantity)
            self.products[self.product_name_entry.get()] = {'price': updated_price, 'quantity': updated_quantity}
    def remove_product(self):
        self.remove_product_window=Toplevel()
        self.remove_product_window.title("Remove Product")
        self.remove_product_window.geometry("1080x1080")
        self.remove_product_window.config(bg=BG)

        self.product_name=Label(self.remove_product_window,text="Product Name: ",font=("Comic Sans MS",15,"bold"),fg=FONT,bg=BG)
        self.product_name.place(y=150,x=350)
        self.re_product_name_entry=Entry(self.remove_product_window,font=("Comic Sans MS",15,"bold"),fg=FONT,bd=8,relief=GROOVE)
        self.re_product_name_entry.place(y=165,x=550)
        confirm_btn=Button(self.remove_product_window,text="Confirm",font=("Comic Sans MS",10,"bold"),command=self.confirm_removal,bg=BG,fg=FONT)
        confirm_btn.place(y=220,x=550)
    def confirm_removal(self):
        product_name=self.re_product_name_entry.get()
        if product_name in self.products:
            del self.products[product_name]
            messagebox.showinfo(f"Success!! {product_name} is removed successfully")
        else:
            messagebox.showerror(f"{product_name} not found")
        self.remove_product_window.destroy()
class Customer:

    products=Owner().products
    shopping_cart={}
    def customer_button_click(self):
        customer_window = Toplevel()
        customer_window.title("Customer")
        customer_window.geometry("1080x1080")
        customer_window.config(bg="grey20")
        add_to_cart=Button(customer_window,text="Add to Cart",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT,bd=8,relief=GROOVE,command=self.add_to_cart_btn)
        add_to_cart.place(y=150,x=610)
        remove_from_cart=Button(customer_window,text="Remove From Cart",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT,bd=8,relief=GROOVE,command=self.remove_from_cart_btn)
        remove_from_cart.place(y=220,x=610)
        view_cart=Button(customer_window,text="View Cart",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT,bd=8,relief=GROOVE,command=self.view_cart)
        view_cart.place(y=290,x=610)
        bill_generate=Button(customer_window,text="Generate Bill",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT,bd=8,relief=GROOVE,command=self.bill_generate)
        bill_generate.place(y=360,x=610)
    def add_to_cart_btn(self):
        add_to_cart=Toplevel()
        add_to_cart.title("Add to Cart")
        add_to_cart.geometry("1080x1080")
        add_to_cart.config(bg=BG)
        Label(add_to_cart, text="Product",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT).grid(row=0, column=0, padx=5)
        Label(add_to_cart, text="Price",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT).grid(row=0, column=1, padx=5)
        Label(add_to_cart, text="Quantity",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT).grid(row=0, column=2, padx=5)
        Label(add_to_cart, text="Enter Quantity",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT).grid(row=0, column=3, padx=5)
        Label(add_to_cart, text="Add",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT).grid(row=0, column=4, padx=5)

        for idx, (product_name, product_details) in enumerate(self.products.items(), start=1):
            Label(add_to_cart, text=product_name,font=("Harlow Solid",10,"bold"),bg=BG,fg=FONT).grid(row=idx, column=0, padx=5)
            Label(add_to_cart, text=f"{product_details['price']:.2f}",font=("Harlow Solid",10,"bold"),bg=BG,fg=FONT).grid(row=idx, column=1, padx=5)
            Label(add_to_cart, text=str(product_details['quantity']),font=("Harlow Solid",10,"bold"),bg=BG,fg=FONT).grid(row=idx, column=2, padx=5)

            add_entry = Entry(add_to_cart, width=5)
            add_entry.grid(row=idx, column=3, padx=5)

            add_btn = Button(add_to_cart, text="Add",bg=BG,fg=FONT,bd=2,relief=GROOVE, command=lambda name=product_name, entry=add_entry: self.add_to_cart(name, entry.get()))
            add_btn.grid(row=idx, column=4, padx=5)

    def add_to_cart(self, product_name, quantity):
        if not quantity.isdigit() or int(quantity) <= 0:
            print(f"Invalid quantity for {product_name}. Please enter a positive integer.")
            return
        quantity = int(quantity)
        if product_name in self.products and self.products[product_name]['quantity'] >= quantity:
            if product_name in self.shopping_cart:
                no_of_quantity=self.shopping_cart[product_name]['quantity']+quantity
                self.shopping_cart[product_name]={'price':self.products[product_name]['price'],'quantity':no_of_quantity}
                self.products[product_name]['quantity']-=quantity
            else:
                self.shopping_cart[product_name] = {'price':self.products[product_name]['price'],'quantity':quantity}
                self.products[product_name]['quantity']-=quantity
            print(f"{quantity} {product_name}(s) added to the cart.")
            print(self.shopping_cart)
        else:
            print(f"Not enough quantity available for {product_name}.")
    def remove_from_cart_btn(self):
        remove_from_cart=Toplevel()
        remove_from_cart.title("Remove From Cart")
        remove_from_cart.geometry("1080x1080")
        remove_from_cart.config(bg=BG)
        Label(remove_from_cart, text="Product",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT).grid(row=0, column=0, padx=5)
        Label(remove_from_cart, text="Price",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT).grid(row=0, column=1, padx=5)
        Label(remove_from_cart, text="Quantity",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT).grid(row=0, column=2, padx=5)
        Label(remove_from_cart, text="Remove Quantity",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT).grid(row=0, column=3, padx=5)
        Label(remove_from_cart, text="Remove Product",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT).grid(row=0, column=5, padx=5)
        Label(remove_from_cart,text="Enter Quantity",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT).grid(row=0,column=4,padx=5)
        if len(self.shopping_cart)==0:
            messagebox.showerror(remove_from_cart,"Cart is empty You cannot remove product")
        else:
            for idx, (product_name, product_details) in enumerate(self.shopping_cart.items(), start=1):
                Label(remove_from_cart, text=product_name,font=("Harlow Solid",10,"bold"),bg=BG,fg=FONT).grid(row=idx, column=0, padx=5)
                Label(remove_from_cart, text=f"{product_details['price']:.2f}",font=("Harlow Solid",10,"bold"),bg=BG,fg=FONT).grid(row=idx, column=1, padx=5)
                Label(remove_from_cart, text=str(product_details['quantity']),font=("Harlow Solid",10,"bold"),bg=BG,fg=FONT).grid(row=idx, column=2, padx=5)
                remove_entry=Entry(remove_from_cart)
                remove_entry.grid(row=idx,column=4,padx=5)
                remove_quantity_btn = Button(remove_from_cart, text="Remove Quantity",bg=BG,fg=FONT,bd=4,relief=GROOVE,command=lambda name=product_name,entry=remove_entry:self.remove_quantity(name,entry.get()))
                remove_quantity_btn.grid(row=idx, column=3, padx=5)
                remove_product_btn=Button(remove_from_cart,text="Remove",bg=BG,fg=FONT,bd=4,relief=GROOVE,command=lambda name=product_name:self.remove_product(name))
                remove_product_btn.grid(row=idx,column=5,padx=5)
    def remove_quantity(self,product_name,quantity):
        if not quantity.isdigit() or int(quantity) <= 0:
            print(f"Invalid quantity for {product_name}. Please enter a positive integer.")
            return
        quantity = int(quantity)
        if self.shopping_cart[product_name]['quantity']>=quantity:
            self.shopping_cart[product_name]['quantity']-=quantity
            print(self.shopping_cart)
        else:
            messagebox.showinfo(f"Not enough quantity available for {product_name}.")
    def remove_product(self,product_name):
        del self.shopping_cart[product_name]
        print(self.shopping_cart)
    def view_cart(self):
        if len(self.shopping_cart)<=0:
            messagebox.showinfo(f"Cart is empty")
        else:
            view_cart=Toplevel()
            view_cart.title("View Cart")
            view_cart.geometry("1080x1080")
            view_cart.config(bg=BG)
            Label(view_cart, text="Product",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT).grid(row=0, column=0, padx=5)
            Label(view_cart, text="Price",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT).grid(row=0, column=1, padx=5)
            Label(view_cart, text="Quantity",font=("Comic Sans MS",15,"bold"),bg=BG,fg=FONT).grid(row=0, column=2, padx=5)
            total=0
            count=0
            for idx, (product_name, product_details) in enumerate(self.shopping_cart.items(), start=1):
                count=idx
                Label(view_cart, text=product_name,font=("Harlow Solid",10,"bold"),bg=BG,fg=FONT).grid(row=idx, column=0, padx=5)
                price=product_details["price"]*product_details['quantity']
                Label(view_cart, text=f"{price:.2f}",font=("Harlow Solid",10,"bold"),bg=BG,fg=FONT).grid(row=idx, column=1, padx=5)
                Label(view_cart, text=str(product_details['quantity']),font=("Harlow Solid",10,"bold"),bg=BG,fg=FONT).grid(row=idx, column=2, padx=5)
    def bill_generate(self):
        if len(self.shopping_cart)<=0:
            messagebox.showerror("Error","No products are selected")
        else:
            bill_window = Toplevel()
            bill_window.title("Bill Area")
            bill_window.geometry("1080x1080")

            label = Label(bill_window, text="Billing Section", font=("Comic Sans MS", 15, "bold"), bg="grey20", fg="gold", bd=12, relief=GROOVE)
            label.pack(fill=X)

            left_frame = Frame(bill_window, width=540, height=400, bg="grey20")
            left_frame.pack(side=LEFT, fill="both")

            customer_name = Label(left_frame, text="Name", font=("Comic Sans MS", 15, "bold"), bg="grey20", fg="gold")
            customer_name.grid(row=0, column=0, padx=20, pady=8)
            self.customer_entry = Entry(left_frame, font=("Comic Sans MS", 12, "bold"), bd=7, width=18)
            self.customer_entry.grid(row=0, column=1, padx=8, pady=8)
            customer_phone = Label(left_frame, text="Phone", font=("Comic Sans MS", 15, "bold"), bg="grey20", fg="gold")
            customer_phone.grid(row=1, column=0, padx=20, pady=8)
            self.customer_phone_entry = Entry(left_frame, font=("Comic Sans MS", 12, "bold"), bd=7, width=18)
            self.customer_phone_entry.grid(row=1, column=1, padx=8, pady=8)
            right_frame = Frame(bill_window, width=540, height=400, bg="grey20")
            right_frame.pack(side=RIGHT, fill="both")

            right_label = Label(right_frame, text="Bill Area", font=("Comic Sans MS", 15, "bold"), bg="grey20", fg="gold", bd=12, relief=GROOVE)
            right_label.pack(fill=X)
            global textarea
            textarea = Text(right_frame, height=18, width=80)
            textarea.pack(side=LEFT, fill=BOTH, expand=True)

            scrollbar = Scrollbar(right_frame, orient=VERTICAL)
            scrollbar.pack(side=RIGHT, fill=Y)
            textarea.config(yscrollcommand=scrollbar.set)

            total_btn=Button(left_frame,text="Total",font=("Comic Sans MS", 15, "bold"),fg="gold",bd=8,relief=GROOVE,bg="grey20",command=self.total)
            total_btn.grid(row=2,column=0)

            print_btn=Button(left_frame,text="Print",font=("Comic Sans MS", 15, "bold"),fg="gold",bd=8,relief=GROOVE,bg="grey20",command=self.print_bill)
            print_btn.grid(row=2,column=1)

            payment_btn=Button(left_frame,text="Pay",font=("Comic Sans MS", 15, "bold"),fg="gold",bd=8,relief=GROOVE,bg="grey20")
            payment_btn.grid(row=3,column=0)
    def total(self):
        total=0
        self.billnumber=random.randint(500,1000)
        name=self.customer_entry.get()
        phone=self.customer_phone_entry.get()
        if name=="" or phone=="":
            messagebox.showerror("Error","Customer Details are required!!")
        else:
            textarea.insert(END,"\t\t\t\t**Welcome Customer**\n")
            textarea.insert(END,f"Bill Number: {self.billnumber}\n")
            textarea.insert(END,f"Customer Name: {name}\n")
            textarea.insert(END,f"Phone No: {phone}\n")
            textarea.insert(END,"================================================================================\n")
            textarea.insert(END,"Product\t\t\tQuantity\t\t\tPrice\n")
            textarea.insert(END,"================================================================================\n")
            for product_name,product_detail in self.shopping_cart.items():
                textarea.insert(END,f"{product_name}\t\t\t{product_detail['quantity']}\t\t\t{product_detail['price']*product_detail['quantity']}\n")
                total+=product_detail['price']*product_detail['quantity']
            textarea.insert(END,
            "--------------------------------------------------------------------------------\n")
            tax=(total*10)/100
            textarea.insert(END,f"Tax:\t\t\t{tax}\t")
            totalPrice=total+tax
            textarea.insert(END,f"Total Price:\t\t\t{totalPrice}")
    def print_bill(self):
        result=messagebox.askyesno("Confirm","Do you want to save the bill")
        if result:
            bill_content=textarea.get(1.0,END)
            file=open(f"{self.billnumber}.txt",'w')
            file.write(bill_content)
            file.close()
            messagebox.showinfo("Success",f"{self.billnumber} is saved successfully")
BG="grey20"
FONT="gold"
window=Tk()
window.title("Store Management System")
window.geometry("1080x1080")
window.config(bg=BG)
store_name=Label(text="Welcome to my Store",font=("Comic Sans MS",24,"bold"),bg=BG,fg=FONT,bd=8,relief=GROOVE)
store_name.place(y=150,x=350)
customer_btn=Button(text="Customer",font=("Comic Sans MS",12,"bold"),command=Customer().customer_button_click,bg=BG,fg=FONT,bd=8,relief=GROOVE)
customer_btn.place(y=350,x=350)
owner_btn=Button(text="Owner",font=("Comic Sans MS",12,"bold"),command=Owner().owner_button_click,bg=BG,fg=FONT,bd=8,relief=GROOVE)
owner_btn.place(y=350,x=650)
window.mainloop()