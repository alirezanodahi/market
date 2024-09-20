#به نام خداوند یکتا
#ایمپورت ها
#---------------------------------------------------------------------------
from pymysql import *
from tkinter import *
from tkinter import messagebox
import mysql.connector
from functools import partial
#----------------------------------------------------------------------------
#برقراری ارتباط با پایگاه داده
data = mysql.connector.connect(host= "localhost",database='store',user = "alirezanodahi",password= "09010859997")
my_cursor = data.cursor()
my_cursor.execute("create database if not exists Store")#اگه نبود یدونه بساز!
my_cursor.execute("use Store")# اپشن هست میشه نباشه زساد مهم نیست
#---------------------------------------------------------------------------------------
#ساخت جدول ها در پایگاه داده
user_table ="""create table if not exists user(
    username varchar(20) PRIMARY KEY,
    password varchar(20),
    type VARCHAR(10) )
    """
stationary_table = """create table if not exists stationary(
    item_name VARCHAR(20) not null unique,
    item_price INTEGER(10), 
    item_quantity INTEGER(10),
    item_category VARCHAR(20),
    item_discount float(3),
    item_id INTEGER AUTO_INCREMENT PRIMARY KEY)"""
    
my_cart = """create table if not exists mycart(
    item_name VARCHAR(20) not null unique,
    item_quantity INTEGER(10),
    item_price float(10),
    item_pay BOOLEAN not null default 0)
"""
show_cart= """create table if not exists showcart(
    item_name VARCHAR(20) not null ,
    item_quantity INTEGER(10),
    item_price float(10),
    item_id INTEGER AUTO_INCREMENT PRIMARY KEY)
"""
my_cursor.execute(my_cart) 
my_cursor.execute(show_cart) 
my_cursor.execute(user_table)
my_cursor.execute(stationary_table)

#---------------------------------------------------------------------------------------
#لیست ها و تاپل ها
owners = ('alireza',"benyamin")
admin_list = []
all_buy = []

sql="select username from user where type = 'admin' "


my_cursor= data.cursor()
my_cursor.execute(sql)

result = my_cursor.fetchall()

for i in range(len(result)):
    admin_list.append(result[i][0])



#توابع
#تابه ورود و ثبت نام

def conect():
    data = mysql.connector.connect(host= "localhost",database='store',user = "alirezanodahi",password= "09010859997")
    my_cursor = data.cursor()
    user_table ="""create table if not exists user(
    username varchar(20) PRIMARY KEY,
    password varchar(20),
    type VARCHAR(10) )
    """
    stationary_table = """create table if not exists stationary(
        item_name VARCHAR(20) not null unique,
        item_price INTEGER(10), 
        item_quantity INTEGER(10),
        item_category VARCHAR(20),
        item_discount float(3),
        item_id INTEGER AUTO_INCREMENT PRIMARY KEY)"""
        
    
        
    my_cursor.execute(user_table)
    my_cursor.execute(stationary_table)
    
    #my_cursor.execute("create database if not exists Store")
#---------------------------------------------------------------------------------------
#ورود و ثبت نام
def sign_up():
    #ثبت نام
    def sing_in():
        sign.withdraw()
        conect()
        
        win2=Toplevel(sign)
        win2.title("Register")
        win2.geometry('500x500')
        win2.configure(bg='gray')
        

        
#---------------------------------------------------------------------------------           
        #اضافه کردن ممبر
#---------------------------------------------------------------------------------
        def insert(usn,cpsw,psw,ch,win2):
            try:
                u = usn.get()
                cp = cpsw.get()
                p = psw.get()
                c = ch.get()
                us = "user"
                wind = win2
                
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                
                l4=Label(fm4,font=('Times' ,20,'bold'),fg='green',bg='grey')
                l4.pack()
                
                mycursor= data.cursor()
                
                if(u and p and cp) :
                    
                    if (p == cp):
                        
                        if (c==True):
                            
                            sql="INSERT INTO user (username,Password,type) VALUES (%s,%s,%s)"
                            val = (u,p,us)
                            mycursor.execute(sql,val)
                            data.commit()
                            
                            l4.config(text="Register successfully!")
                            wind.destroy()
                            user()
                            return
                        
                        else:
                            messagebox.showerror('Warning','You have to agree the terms and policies')
                            return
                        
                    else:
                        messagebox.showerror(  "Warning", 'Passwords must match ')
                        return
                else:
                    messagebox.showerror('Warning','All fields are required')
                    return
            except(mysql.connector.Error,mysql.connector.Warning) as e:
                messagebox.showerror("Duplicate","username is already taken") 
                e3.delete(0, END)
            finally:
                conect()  
#--------------------------------------------------------------------------------------------------------
        l1=Label(win2,text='Register',font=("bold", 30),bg='black',fg='white')
        l1.pack(fill=X,pady=20)

        fm1=Frame(win2,bg='gray')
        fm1.pack(pady=10)
        fm2=Frame(win2,bg='gray')
        fm2.pack(pady=10)
        fm3=Frame(win2,bg='gray')
        fm3.pack(pady=10)
        fm4=Frame(win2,bg='gray')
        fm4.pack(pady=10)
        fm5=Frame(win2,bg='gray')
        fm5.pack(pady=10)
        fm6=Frame(win2,bg='gray')
        fm6.pack(pady=10)
        
        
        l2=Label(fm1,text='username',font=("bold", 15),bg='grey')
        l2.pack(side=LEFT)
        
        e2=Entry(fm1,textvariable=usn,bd=5,width=50,font=('Times' ,10,'bold'))
        e2.pack(padx=20)

        l3=Label(fm2,text='password',font=("bold", 15),bg='grey')
        l3.pack(side=LEFT)
        
        e3=Entry(fm2,textvariable=psw,bd=5,width=50,font=('Times' ,10,'bold'),show="*")
        e3.pack(padx=20)
        
        
        l5=Label(fm3,text='Re-enter password',font=("bold", 15),bg='grey')
        l5.pack(side=LEFT)
        
        e4=Entry(fm3,textvariable = cpsw,bd=5,width=50,font=('Times' ,10,'bold'),show="*")
        e4.pack(padx=20)
        
        
        chk_state=BooleanVar()
        chk_state.set(False)
        
        chk=Checkbutton(fm4,text='I agree to the terms and policies',var=chk_state,bd=5,fg='navy',bg='grey')
        chk.pack(pady=10)
        
        insert=partial(insert,usn,psw,cpsw,chk_state,win2)
        
        Button(fm5, text='Submit',width=10,bg='brown',fg='white',command=insert,font=("bold", 15)).pack()
        
        
        win2.mainloop()
        
#--------------------------------------------------------------------------------------------------------    
#تابع ورود
#------------------------------------------------------------------------------------------------------
    def login(lable1,psw1,usn1):
        
        data = mysql.connector.connect(host= "localhost",database='store',user = "alirezanodahi",password= "09010859997")
        my_cursor = data.cursor()
        my_cursor.execute("create database if not exists Store")#اگه نبود یدونه بساز!
        my_cursor.execute("use Store")

        username =usn1.get()
        e1.delete(0, END)
        
        password= psw1.get()
        e2.delete(0, END)
 
        sql="select username , password from user where username = %s and Password = %s"
        val=(username,password)
        
        my_cursor= data.cursor()
        my_cursor.execute(sql,val)
        
        result = my_cursor.fetchall()
        
        if len(result) == 0:
            lable1.config(text='Invalid username or Password',fg='red')
            
        else: 
            counter = 0
            for i in result:
                counter = counter + 1
                if (counter> 0):
                    lable1.config(text="Logged In Successfully",fg='green')
                    #time.sleep(3)
                    sign.destroy()
            
            
                   
            for ad in admin_list:
                if (ad == result[0][0]):
                    admin()
                    conect()
                    
                    return

            if result[0][0] == "alireza" or result[0][0] =="benyamin":
                owner()
                conect()
               
                return
            
            user()
            conect()
               
        return
    
#---------------------------------------------------------------------------------------------------------   
    

    sign = Tk()
    sign.title("Sign-In")
    sign.configure(width = 300,height = 200,bg ="CadetBlue2")
    
    usn=StringVar()
    psw=StringVar()
    cpsw=StringVar()
    usn1=StringVar()
    psw1=StringVar()
    
    label=Label(sign,text='Sign-In',font=("Times", "30", "bold"),bg='green',fg='yellow')
    label.pack(fill=X)
    
    fm1=Frame(sign,bg="light sky blue")
    fm1.pack(pady=20)
    fm2=Frame(sign,bg="light sky blue")
    fm2.pack(pady=20)
    fm3=Frame(sign,bg='SkyBlue1')
    fm3.pack(pady=20)
    
    l1=Label(fm1,text='username',font=('Times' ,10,'bold'),bg="light sky blue",fg='white')
    l1.pack(side=LEFT,padx=20)
    
    e1=Entry(fm1,bd=5,font=('Times' ,10,'bold'),width=25,textvariable=usn1,bg = "light sky blue")
    e1.pack()

    l2=Label(fm2,text='password',font=('Times' ,10,'bold'),bg="light sky blue",fg='white')
    l2.pack(side=LEFT,padx=20)
    
    e2=Entry(fm2,bd=5,font=('Times' ,10,'bold'),width=25,textvariable=psw1,show='*',bg = "light sky blue")
    e2.pack()
    
    l3=Label(fm3,text='new user? sign_up',bg='SkyBlue1',fg='green yellow',font=("Times", "15", "bold italic"))
    l3.pack(side=LEFT)
    
    Button(fm3,text='here',bg='SkyBlue1',fg='green yellow',font=('Times' ,10,'bold'),command=sing_in ).pack()

    lable1=Label(sign,bg='CadetBlue2',fg='yellow',font=('Times' ,20,'bold'))
    lable1.pack(pady=10)

    login=partial(login,lable1,psw1,usn1)
    
    Button(sign,text='Login',bg='red',fg='white',font=('ariel' ,10,'bold'),width=10,command=login).pack()
    
    sign.mainloop()
    
    
#-------------------------------------------------------------------------------------------------------
#پنل کاربری
#-----------------------------------------------------------------------------------------------------
def user():
    
    window = Tk()
    window.title("user panel")
    window.configure(width=1500,height=600,bg="Grey")
    
    def mycart():
        
        def show_cart():
            try:
                window1 = Tk()
                window1.configure(bg="Grey")
                window1.title("Stationary Store Database")
             
                my_cursor.execute("select * from mycart")
                mytext1 = my_cursor.fetchall()
                
                mytext = Text(window1,width=90,height= 20 ,bg= "gray",fg="black", font=("Times", 12))
                mytext.insert(END," Item_Name \t\t Item_Quantity \t\t Item_Price \n")
                mytext.insert(END," ----------------------------------------------------------\n")
                
                for row in mytext1:
                    
                    mytext.insert(END,"    {0} \t\t      {1} \t\t   {2} \n".format(row[0],row[1],row[2]))
                
                mytext.pack( side = LEFT)
                
            except:
                messagebox.showerror("warning","error 404 page not found!")
            finally:
                conect()

        def add_to_cart():
            cart.destroy()
            conect()
            user()
            #------


        def del_from_cart():
            
            
            
            def del_cart():
                """delete from cart"""
             
                e6 = entry6.get()
                
                if e6 !=" "or e6 != "SEARCH ITEM NAME TO DELETE":
                    
                    e6 = entry6.get()
                    try:
                        my_cursor.execute("delete from mycart where item_name = '{0}'".format(str(e6)))
                        data.commit()
                        
                        my_cursor.execute("delete from showcart where item_name = '{0}'".format(str(e6)))
                        data.commit()
                        messagebox.showinfo("DELETE ITEM", "ITEM DELETED SUCCESSFULLY")
                        conect()
                    except:
                        messagebox.showerror("warning","item not found")
                        
                else:
                    messagebox.showerror("warning","enter item name")
            
                   
            window2 = Tk()
            window2.configure(bg="Grey")
            window2.title("delete from cart")
            entry6 = Entry(window2, font=("Times", 14),justify='left',bd=8,width=25,bg="#EEEEF1")
            entry6.insert(0,"SEARCH ITEM NAME TO DELETE")
            entry6.grid(row=2,column=3, padx=10, pady=10)
            button5 = Button(window2,activebackground="red", text="DELETE FROM CART",bd=8, bg="#49D810", fg="black", width =25, font=("Times", 12),command=del_cart)
            button5.grid(row=3,column=3, padx=10, pady=10)
            
          
            
        
#----------------------------------------------------------------------------------------------
        def pay():
            window3 = Tk()
            window3.configure(bg="Grey")
            window3.title("pay")
           
            
            def bol():
                
                my_cursor.execute("select * from mycart")
                items = my_cursor.fetchall()
                
                
                for i in range(len(items)):
                    
                    
                    j = items[i][0]
                    
                    my_cursor.execute("select item_quantity from stationary where item_name = '{0}' ".format(j))
                    main_q = my_cursor.fetchall()
                    main_quanty = int(main_q[0][0])
                    
                    
                    
                    my_cursor.execute("select item_quantity from mycart where item_name = '{0}' ".format(j))
                    need_q= my_cursor.fetchall()
                    need_quanty = int(need_q[0][0])
                    
                    tot = main_quanty - need_quanty
                    
                    
                    my_cursor.execute("update stationary set item_quantity = '{0}'  where item_name = '{1}' ".format(str(tot),j))
                    
                    data.commit()
                    
                    
                    my_cursor.execute("select * from mycart")
                    buyed = my_cursor.fetchall()
                    all_buy.append(buyed)
                   
                    my_cursor.execute("delete from mycart where item_name = '{0}'".format(j))
                    data.commit()
                messagebox.showinfo("pay", "ITEMS PAYED SUCCESSFULLY")
                conect()
                  
                    
                    
                        
            total_cast = 0
            
            com = "select item_price from mycart"
            my_cursor.execute(com)
            pr = my_cursor.fetchall()
            for i  in range(0,len(pr)):
                for j in pr[i]:
                    total_cast = total_cast + j
            
            my_cursor.execute("select * from mycart")
            mytext1 = my_cursor.fetchall()
            
            mytext = Text(window3,width=90,height= 20 ,bg= "gray",fg="black", font=("Times", 12))
            mytext.insert(END," Item_Name \t\t Item_Quantity \t\t Item_Price \n")
            mytext.insert(END," ----------------------------------------------------------\n")
            
            for row in mytext1:
                
                mytext.insert(END,"    {0} \t\t      {1} \t\t   {2} \n".format(row[0],row[1],row[2]))
            
            mytext.insert(END," ----------------------------------------------------------\n")
            mytext.insert(END,"total price = {0}\n".format(total_cast))
            mytext.pack( side = LEFT)
            
            button1 = Button(window3,activebackground="red", text="PAY",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=bol)
            button1.pack(side = LEFT)
            

        cart = Tk()
        cart.title("my cart")
        cart.configure(width=900,height=600,bg="Grey")
        buttoncolor = "#49D810"
        buttonfg = "black"

        label0 = Label(cart,text="CART MANAGEMENT SYSTEM ",bg="Black",fg="#F9FAE9",font=("Times", 27),width=39)

        button1 = Button(cart,activebackground="green", text="VIEW CART",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=show_cart)
        button3 = Button(cart,activebackground="red", text="PAY",bd=8, bg="#FF0000", fg="#EEEEF1", width=25, font=("Times", 12),command=pay)
        button4 = Button(cart,activebackground="green", text="ADD TO CART",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=add_to_cart)
        button2 = Button(cart,activebackground="green", text="DELETE FROM CART",bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 12),command=del_from_cart)

        label0.grid(columnspan=6, padx=10, pady=10)

        button1.grid(row=5,column=0, padx=10, pady=10)
        button2.grid(row=5,column=1, padx=10, pady=10)
        button3.grid(row=6,column=1, padx=10, pady=10)
        button4.grid(row=5,column=2, padx=10, pady=10)

        cart.mainloop()

    def addcart():

        try:
            e1=entry1.get()
            e2=entry2.get()
            
            com = "select item_quantity from stationary where item_name = '{0}' ".format(str(e1))
            my_cursor.execute(com)
            ch = my_cursor.fetchall()
            
            if len(ch)>0:
                
                check = int(ch[0][0])
                if check >= int(e2):
                    
                    com = "select item_price from stationary where item_name = '{0}' ".format(str(e1))
                    my_cursor.execute(com)
                    
                    pr = my_cursor.fetchall()
                    
                    price = int(pr[0][0])
                    
                    
                    com = "select item_discount from stationary where item_name = '{0}' ".format(str(e1))
                    my_cursor.execute(com)
                    dis = my_cursor.fetchall()
                    discount = float(dis[0][0])
                    
                    
                    
                    if discount == 0 or discount== 0.0:
                        
                        discount = 1
                      
                        
                    else:
                        
                        discount = discount/100
                        
                    totals = discount * price * int(e2)
                    if discount != 1:
                        
                        total = ( price * int(e2) ) - totals
                    else:
                        total = totals
                    
                    sql =""" INSERT INTO mycart (item_name, item_quantity,item_price) VALUES (%s, %s,%s)"""
                    
                    val = (str(e1),str(e2),str(total) )
                    my_cursor.execute(sql,val)
                    data.commit()
                    
                    sql =""" INSERT INTO showcart (item_name, item_quantity,item_price) VALUES (%s, %s,%s)"""
                    
                    val = (str(e1),str(e2),str(total) )
                    my_cursor.execute(sql,val)
                    data.commit()
                    
                    
                    
                else:
                    
                    messagebox.showerror("Error","Inventory is not enough")
            else :
                
                messagebox.showerror("Error","Element not exist")
                return
               
            
            entry1.delete(0, END)
            entry2.delete(0, END)
        
            messagebox.showinfo("ADD ITEM", "ITEM ADDED SUCCESSFULLY")
            
        except (mysql.connector.Error,mysql.connector.Warning) as e:
            messagebox.showerror("Duplicate","You are trying to insert a item which is already present in database")
        finally:
            conect()
            
#----------------------------------------------------------------------------------------------------
#نمایش کالا ها 
#-----------------------------------------------------------------------------------------------------
    def showdatabase():
        window1 = Tk()
        window1.configure(bg="Grey")
        window1.title("Stationary Store Database")
        
        my_cursor.execute("select * from stationary")
        mytext1 = my_cursor.fetchall()
        
        mytext = Text(window1,width=90,height= 20 ,bg= "gray",fg="black", font=("Times", 12))
        mytext.insert(END," Item_Name \t\tItem_Price \t\tItem_Quantity \t\tItem_Category \t\tItem_Discount \n")
        mytext.insert(END," ------------ \t\t----------- \t\t-------------- \t\t--------------- \t\t--------------- \n")
        
        for row in mytext1:
            
            mytext.insert(END,"       {0} \t\t     {1} \t\t         {2} \t\t   {3} \t\t          {4}\n".format(row[0],row[1],row[2],row[3],row[4]))
        
        mytext.pack( side = LEFT)
        conect()
#--------------------------------------------------------------------------------------------------------------
#خروج
#------------------------------------------------------------------------------------------------------------
    def qExit():
        qExit= messagebox.askyesno("Quit System","Do you want to quit?")
        
        if (qExit > 0):
            window.destroy()
            return
#--------------------------------------------------------------------------------------------------------------------

    label0 = Label(window,text="PURCHASING MANAGEMENT SYSTEM ",bg="Black",fg="#F9FAE9",font=("Times", 20),width=39)
    
    label1 = Label(window,text="ENTER ITEM NAME",bg="black",relief="ridge",fg="white",bd=8,font=("Times", 12),width=25)
    entry1 = Entry(window , font=("Times", 14),bd=8,width=25,bg="white")
    
    label2 = Label(window, text="ENTER ITEM QUANTITY",relief="ridge",height="1",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
    entry2 = Entry(window, font=("Times", 14),bd=8,width=25,bg="white")
    
    buttoncolor = "#49D810"
    buttonfg = "black"
    
    
    button1 = Button(window,activebackground="green", text="VIEW DATABASE",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=showdatabase)
    button3 = Button(window,activebackground="red", text="EXIT",bd=8, bg="#FF0000", fg="#EEEEF1", width=25, font=("Times", 12),command=qExit)
    button4 = Button(window,activebackground="green", text="ADD TO CART",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=addcart)
    button2 = Button(window,activebackground="green", text="MY CART",bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 12),command=mycart)

    entry6 = Entry(window, font=("Times", 14),justify='left',bd=8,width=25,bg="#EEEEF1")
    entry6.insert(0,"SEARCH")
    
    label0.grid(columnspan=6, padx=10, pady=10)
    label1.grid(row=1,column=0, padx=10, pady=10)
    label2.grid(row=2,column=0, padx=10, pady=10)
   
    entry1.grid(row=1,column=1, padx=10, pady=10)
    entry2.grid(row=2,column=1, padx=10, pady=10)
    
    button2.grid(row=5,column=0, padx=10, pady=10)
    button1.grid(row=5,column=1, padx=10, pady=10)
    
    button3.grid(row=6,column=1, padx=10, pady=10)
    button4.grid(row=6,column=0, padx=10, pady=10)

    window.mainloop()
    
#------------------------------------------------------------------------------------------------------
#پنل ادمین   
#-----------------------------------------------------------------------------------------------------
def admin():
    
    root = Tk()
    root.title("admin panel")
    root.configure(width=1500,height=600,bg="Grey")
#اضافه کردن کالا
    def additem():

        try:
            e1=entry1.get()
            e2=entry2.get()
            e3=entry3.get()
            e4=entry4.get()
            e5=entry5.get()
            
            sql = "INSERT INTO stationary (item_name, item_price, item_quantity, item_category, item_discount) VALUES (%s, %s, %s, %s, %s)"
            val = (str(e1),e2,e3,str(e4),e5)
            my_cursor.execute(sql,val)
            data.commit()
            
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
    
            messagebox.showinfo("ADD ITEM", "ITEM ADDED SUCCESSFULLY")
            
        except (mysql.connector.Error,mysql.connector.Warning) as e:
            messagebox.showerror("Duplicate","You are trying to insert a item which is already present in database")
        finally:
            conect()
#----------------------------------------------------------------------------------------------------
#حذف کالا
#----------------------------------------------------------------------------------------------------
    def delete1():
        
        e6 = entry6.get()
        my_cursor.execute("delete from stationary where item_name = '{0}'".format(str(e6)))
        data.commit()
        messagebox.showinfo("DELETE ITEM", "ITEM DELETED SUCCESSFULLY")
#-------------------------------------------------------------------------------------------------------
#نمایش کالا ها 
#-----------------------------------------------------------------------------------------------------
    def showdatabase():
        root1 = Tk()
        root1.configure(bg="Grey")
        root1.title("Stationary Store Database")
        
        my_cursor.execute("select * from stationary")
        mytext1 = my_cursor.fetchall()
        
        mytext = Text(root1,width=90,height= 20 ,bg= "gray",fg="black", font=("Times", 12))
        mytext.insert(END," Item_Name \t\tItem_Price \t\tItem_Quantity \t\tItem_Category \t\tItem_Discount \n")
        mytext.insert(END," ------------ \t\t----------- \t\t-------------- \t\t--------------- \t\t--------------- \n")
        
        for row in mytext1:
            
            mytext.insert(END,"       {0} \t\t     {1} \t\t         {2} \t\t   {3} \t\t          {4}\n".format(row[0],row[1],row[2],row[3],row[4]))
        
        mytext.pack( side = LEFT)
        conect()
#--------------------------------------------------------------------------------------------------------------
#جستجو کالا
#--------------------------------------------------------------------------------------------------------    
    def searchitem():
        
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        
        e6 = entry6.get()
        if e6 == "SEARCH" or e6 == "":{
            messagebox.showwarning("Warning","Please first enter item name for search")
        }
        
        my_cursor.execute("select * from stationary where item_name = '{0}'".format(str(e6)))
        mytext1 = my_cursor.fetchone()
        
        if (mytext1 == None):
            messagebox.showinfo("Error","Element not exist")
        else:
            entry1.insert(0,mytext1[0])
            entry2.insert(0,mytext1[1])
            entry3.insert(0,mytext1[2])
            entry4.insert(0,mytext1[3])
            entry5.insert(0,mytext1[4])
            
            entry6.delete(0, END)
            entry6.insert(0,"SEARCH")
#-----------------------------------------------------------------------------------------------------
#اپدیت وضعیت کالا
#--------------------------------------------------------------------------------------------------        
    def update():
        
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        
        root2 = Tk()
        root2.title("Update Records")
        root2.configure(width=900,height=500,bg="Grey")
        conect()
#-------------------------------------------------------------------------------------------------
        def actualupdate():
            
            e1 = uentry1.get()
            e2 = uentry2.get()
            e3 = uentry3.get()
            e4 = uentry4.get()
            e5 = uentry5.get()
            e6 = uentry6.get()
            
            my_cursor.execute("select * from stationary where item_name = '{0}'".format(str(e6)))
            line = my_cursor.fetchone()
            
            iname = line[0]
            iprice = line[1]
            iquantity = line[2]
            icategory = line[3]
            idiscount = line[4]
            
            if (e1!="Update"):
                iname=e1
            if (e2!="Update"):
                iprice=e2
            if (e3!="Update"):
                iquantity=e3
            if (e4!="Update"):
                icategory=e4
            if (e5!="Update"):
                idiscount=e5
                
            sql = "update stationary set item_name = %s, item_price = %s, item_quantity = %s, item_category = %s, item_discount = %s  where item_name = %s"
            val = (str(iname),iprice,iquantity,str(icategory),idiscount,str(e6))
            my_cursor.execute(sql,val)
            data.commit()
            
            messagebox.showinfo("UPDATE ITEM", "ITEM UPDATED SUCCESSFULLY")
            
            uentry1.delete(0, END)
            uentry2.delete(0, END)
            uentry3.delete(0, END)
            uentry4.delete(0, END)
            uentry5.delete(0, END)
            uentry6.delete(0, END)
            
            entry6.insert(0,"SEARCH")
            root2.destroy()
#-------------------------------------------------------------------------------------------------------------------
#پاک کردن ایتم            
#--------------------------------------------------------------------------------------------------------------------
        def clearuitem():
            
            uentry1.delete(0, END)
            uentry2.delete(0, END)
            uentry3.delete(0, END)
            uentry4.delete(0, END)
            uentry5.delete(0, END)
#--------------------------------------------------------------------------------------------------------------------------------------

        button8 = Button(root2,activebackground="green", text="UPDATE ITEM",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=actualupdate)
        button8.grid(row=7,column=1, padx=10, pady=10)
        
        button9 = Button(root2,activebackground="green", text="CLEAR",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=clearuitem)
        button9.grid(row=7,column=0,padx=10,pady=10)
        
        ulabel0 = Label(root2,text="UPDATE RECORD",bg="Black",fg="#F9FAE9",font=("Times", 30),width=23)
        ulabel0.grid(columnspan=6, padx=10, pady=10)
        
        ulabel1 = Label(root2,text="ENTER ITEM NAME",bg="black",relief="ridge",fg="white",bd=8,font=("Times", 12),width=25)
        ulabel1.grid(row=2,column=0, padx=10, pady=10)
        
        uentry1 = Entry(root2, font=("Times", 14),bd=8,width=25,bg="white")
        uentry1.grid(row=2,column=1, padx=10, pady=10)
        
        ulabel2 = Label(root2, text="ENTER ITEM PRICE",relief="ridge",height="1",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
        ulabel2.grid(row=3,column=0, padx=10, pady=10)
        
        uentry2 = Entry(root2, font=("Times", 14),bd=8,width=25,bg="white")
        uentry2.grid(row=3,column=1, padx=10, pady=10)
        
        ulabel3 = Label(root2, text="ENTER ITEM QUANTITY",relief="ridge",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
        ulabel3.grid(row=4,column=0, padx=10, pady=10)
        
        uentry3 = Entry(root2, font=("Times", 14),bd=8,width=25,bg="white")
        uentry3.grid(row=4,column=1, padx=10, pady=10)
        
        ulabel4 = Label(root2, text="ENTER ITEM CATEGORY",relief="ridge",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
        ulabel4.grid(row=5,column=0, padx=10, pady=10)
        
        uentry4 = Entry(root2, font=("Times", 14),bd=8,width=25,bg="white")
        uentry4.grid(row=5,column=1, padx=10, pady=10)
        
        ulabel5 = Label(root2, text="ENTER ITEM DISCOUNT",bg="black",relief="ridge",fg="white",bd=8, font=("Times", 12),width=25)
        ulabel5.grid(row=6,column=0, padx=10, pady=10)
        
        uentry5 = Entry(root2, font=("Times", 14),bd=8,width=25,bg="white")
        uentry5.grid(row=6,column=1, padx=10, pady=10)
        
        ulabel6 = Label(root2,text="ITEM NAME TO BE UPDATED",bg="black",relief="ridge",fg="white",bd=8,font=("Times", 12),width=25)
        ulabel6.grid(row=1,column=0, padx=10, pady=10)
        
        uentry6 = Entry(root2, font=("Times", 14),bd=8,width=25,bg="white")
        uentry6.grid(row=1,column=1, padx=10, pady=10)
        
        
        uentry1.insert(0,"Update")
        uentry2.insert(0,"Update")
        uentry3.insert(0,"Update")
        uentry4.insert(0,"Update")
        uentry5.insert(0,"Update")
        uentry6.insert(0,"Item Name")
        entry6.insert(0,"SEARCH")
#-------------------------------------------------------------------------------------------------------------
#پاک کردن جاهای خالی        
#-------------------------------------------------------------------------------------------------------------     
    def clearitem():
        
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
#-------------------------------------------------------------------------------------------------------------
#خروج
#------------------------------------------------------------------------------------------------------------
    def qExit():
        qExit= messagebox.askyesno("Quit System","Do you want to quit?")
        
        if (qExit > 0):
            root.destroy()
            return
#--------------------------------------------------------------------------------------------------------------------

    label0 = Label(root,text="PURCHASING MANAGEMENT SYSTEM ",bg="Black",fg="#F9FAE9",font=("Times", 27),width=39)
    label1 = Label(root,text="ENTER ITEM NAME",bg="black",relief="ridge",fg="white",bd=8,font=("Times", 12),width=25)
    entry1 = Entry(root , font=("Times", 14),bd=8,width=25,bg="white")
    label2 = Label(root, text="ENTER ITEM PRICE",relief="ridge",height="1",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
    entry2 = Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
    label3 = Label(root, text="ENTER ITEM QUANTITY",relief="ridge",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
    entry3 = Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
    label4 = Label(root, text="ENTER ITEM CATEGORY",relief="ridge",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
    entry4 = Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
    label5 = Label(root, text="ENTER ITEM DISCOUNT",bg="black",relief="ridge",fg="white",bd=8, font=("Times", 12),width=25)
    entry5 = Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
    buttoncolor = "#49D810"
    buttonfg = "black"
    button1 = Button(root,activebackground="green", text="ADD ITEM",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=additem)
    button2 = Button(root,activebackground="green", text="DELETE ITEM",bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 12),command=delete1)
    button3 = Button(root,activebackground="green", text="VIEW DATABASE",bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 12),command=showdatabase)
    button4 = Button(root,activebackground="green", text="SEARCH ITEM",bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 12),command=searchitem)
    button5 = Button(root,activebackground="green", text="CLEAR SCREEN",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=clearitem)
    button6 = Button(root,activebackground="red", text="EXIT",bd=8, bg="#FF0000", fg="#EEEEF1", width=25, font=("Times", 12),command=qExit)
    entry6 = Entry(root, font=("Times", 14),justify='left',bd=8,width=25,bg="#EEEEF1")
    entry6.insert(0,"SEARCH")
    button7 = Button(root,activebackground="green", text="UPDATE ITEM",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=update)
    
    label0.grid(columnspan=6, padx=10, pady=10)
    label1.grid(row=1,column=0, padx=10, pady=10)
    label2.grid(row=2,column=0, padx=10, pady=10)
    label3.grid(row=3,column=0, padx=10, pady=10)
    label4.grid(row=4,column=0, padx=10, pady=10)
    label5.grid(row=5,column=0, padx=10, pady=10)
    entry1.grid(row=1,column=1, padx=10, pady=10)
    entry2.grid(row=2,column=1, padx=10, pady=10)
    entry3.grid(row=3,column=1, padx=10, pady=10)
    entry4.grid(row=4,column=1, padx=10, pady=10)
    entry5.grid(row=5,column=1, padx=10, pady=10)
    entry6.grid(row=1,column=2, padx=10, pady=10)
    button1.grid(row=6,column=0, padx=10, pady=10)
    button2.grid(row=6,column=1, padx=10, pady=10)
    button3.grid(row=3,column=2, padx=10, pady=10)
    button4.grid(row=2,column=2, padx=10, pady=10)
    button5.grid(row=4,column=2, padx=10, pady=10)
    button6.grid(row=6,column=2, padx=10, pady=10)
    button7.grid(row=5,column=2, padx=10, pady=10)

    root.mainloop()
    
def owner():
    
    owner_win = Tk()
    owner_win.title("user panel")
    owner_win.configure(width=600,height=600,bg="gray")
    conect()
    
    def show_admin():  
        window1 = Tk()
        window1.configure(bg="Grey")
        window1.title("admin list")  
        my_cursor.execute("select username from user where type = 'admin' ")
        mytext1 = my_cursor.fetchall()
        mytext = Text(window1,width=50,height= 20 ,bg= "gray",fg="black", font=("Times", 12))
        mytext.insert(END," item name \n")
        mytext.insert(END,"------------- \n")
        for row in range( len(mytext1)):
            
            mytext.insert(END,"    {0}\n".format(mytext1[row][0]))

        mytext.pack( side = LEFT)
        conect()
            
            
    def uesr_show():
        window2 = Tk()
        window2.configure(bg="Grey")
        window2.title("user list")  
        my_cursor.execute("select username from user where type = 'user' ")
       
        mytext1 = my_cursor.fetchall()
        mytext = Text(window2,width=50,height= 20 ,bg= "gray",fg="black", font=("Times", 12))
        mytext.insert(END," username \n")
        mytext.insert(END,"------------- \n")
        for row in range( len(mytext1)):
            
            mytext.insert(END,"    {0}\n".format(mytext1[row][0]))

        mytext.pack( side = LEFT)
        
        
    
    
    def show_paid_cart():
        window3 = Tk()
        window3.configure(bg="Grey")
        window3.title("payed cart ")  
        mytext = Text(window3,width=50,height= 20 ,bg= "gray",fg="black", font=("Times", 12))
        
        my_cursor.execute("select * from showcart")
        all_buy = my_cursor.fetchall()
        print(all_buy)
        
        if len(all_buy) == 0:
            messagebox.showerror("empty","cart list is empty")
        else:
            mytext.insert(END,"  Item_Name \t\tItem_Quantity   \t\tItem_Price\n")
            mytext.insert(END," ------------ \t\t----------- \t\t--------------\n")

           
            for i in range(len(all_buy)):
               
                
                    
                      
                Item_Name = str(all_buy[i][0])
                Item_Quantity = str(all_buy[i][1])
                Item_Price = str(all_buy[i][2])
            
                mytext.insert(END,"       {0} \t\t     {1} \t\t      {2}\n".format(Item_Name,Item_Quantity,Item_Price ))
                
            mytext.insert(END," ------------ \t\t----------- \t\t--------------\n")
            mytext.pack( side = LEFT)
        conect()   
            
    def update_admin():
        root = Tk()
        root.title("admin panel")
        root.configure(width=600,height=600,bg="Grey")

        def clearuitem():
            
            uentry1.delete(0, END)
            uentry2.delete(0, END)
            
            
        def actualupdate():
            
            e1 = uentry1.get()
            e2 = uentry2.get()
          
            try:
                
                my_cursor.execute("select username from user where username = '{0}'".format(str(e1)))
                line = my_cursor.fetchone()
             
                iname = line[0]
                itype = e2
                
                my_cursor.execute("update user set type = '{0}' where  username = '{1}' ".format(itype,iname))
                data.commit()
                
                messagebox.showinfo("UPDATE ITEM", "ITEM UPDATED SUCCESSFULLY")
            
                uentry1.delete(0, END)
                uentry2.delete(0, END)
                if e2 == "user":
                    
                    
                    admin_list.remove(iname)
                    
            except:
                messagebox.showerror("not found","user not found")
            finally:
                conect()
                
                
        button1 = Button(root,activebackground="green", text="UPDATE ADMIN",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=actualupdate)
        button1.grid(row=7,column=1, padx=10, pady=10)

        button2 = Button(root,activebackground="red", text="CLEAR",bd=8, bg='red', fg=buttonfg, width=25, font=("Times", 12),command=clearuitem)
        button2.grid(row=7,column=0,padx=10,pady=10)

        ulabel0 = Label(root,text="UPDATE ADMIN PANEL",bg="Black",fg="#F9FAE9",font=("Times", 30),width=23)
        ulabel0.grid(columnspan=6, padx=10, pady=10)

        ulabel1 = Label(root,text="ENTER ADMIN NAME",bg="black",relief="ridge",fg="white",bd=8,font=("Times", 12),width=25)
        ulabel1.grid(row=2,column=0, padx=10, pady=10)

        uentry1 = Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
        uentry1.grid(row=2,column=1, padx=10, pady=10)

        ulabel2 = Label(root, text="ENTER TYPE",relief="ridge",height="1",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
        ulabel2.grid(row=3,column=0, padx=10, pady=10)

        uentry2 = Entry(root, font=("Times", 14),bd=8,width=25,bg="white")
        uentry2.grid(row=3,column=1, padx=10, pady=10)
        
    
    def update_user():
        root1 = Tk()
        root1.title("user panel")
        root1.configure(width=600,height=600,bg="Grey")

        def clearuitem():
            
            uentry1.delete(0, END)
            uentry2.delete(0, END)
            
            
        def actualupdate():
            
            e1 = uentry1.get()
            e2 = uentry2.get()
           
            try:
                
                my_cursor.execute("select username from user where username = '{0}'".format(str(e1)))
                line = my_cursor.fetchone()
                
                iname = line[0]
                itype = e2
                
                my_cursor.execute("update user set type = '{0}' where  username = '{1}' ".format(itype,iname))
                data.commit()
                
                messagebox.showinfo("UPDATE ITEM", "ITEM UPDATED SUCCESSFULLY")
            
                uentry1.delete(0, END)
                uentry2.delete(0, END)
                if e2 == "admin":
                    admin_list.append(iname)
                    
                    
            except:
                messagebox.showerror("not found","user not found")
            finally:
                conect()
                
                
        button1 = Button(root1,activebackground="green", text="UPDATE ADMIN",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=actualupdate)
        button1.grid(row=7,column=1, padx=10, pady=10)

        button2 = Button(root1,activebackground="red", text="CLEAR",bd=8, bg='red', fg=buttonfg, width=25, font=("Times", 12),command=clearuitem)
        button2.grid(row=7,column=0,padx=10,pady=10)

        ulabel0 = Label(root1,text="UPDATE ADMIN PANEL",bg="Black",fg="#F9FAE9",font=("Times", 30),width=23)
        ulabel0.grid(columnspan=6, padx=10, pady=10)

        ulabel1 = Label(root1,text="ENTER ADMIN NAME",bg="black",relief="ridge",fg="white",bd=8,font=("Times", 12),width=25)
        ulabel1.grid(row=2,column=0, padx=10, pady=10)

        uentry1 = Entry(root1, font=("Times", 14),bd=8,width=25,bg="white")
        uentry1.grid(row=2,column=1, padx=10, pady=10)

        ulabel2 = Label(root1, text="ENTER TYPE",relief="ridge",height="1",bg="black",bd=8,fg="white", font=("Times", 12),width=25)
        ulabel2.grid(row=3,column=0, padx=10, pady=10)

        uentry2 = Entry(root1, font=("Times", 14),bd=8,width=25,bg="white")
        uentry2.grid(row=3,column=1, padx=10, pady=10)
        
    
    
    def exit():
        qExit= messagebox.askyesno("Quit System","Do you want to quit?")
        if (qExit > 0):
            return
    
    
    
    label0 = Label(owner_win,text="OWNER MANAGEMENT SYSTEM ",bg="Black",fg="#F9FAE9",font=("Times", 20),width=39)
    
    buttoncolor = "#49D810"
    buttonfg = "black"
    
    
    button1 = Button(owner_win,activebackground="green", text="SHOW ADMIN",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=show_admin)
    button3 = Button(owner_win,activebackground="red", text="EXIT",bd=8, bg="#FF0000", fg="#EEEEF1", width=25, font=("Times", 12),command=exit)
    button4 = Button(owner_win,activebackground="green", text="SHOW PAYED CART",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=show_paid_cart )
    button2 = Button(owner_win,activebackground="green", text="UPDATE ADMIN",bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 12),command=update_admin)
    button5 = Button(owner_win,activebackground="green", text="UPDATE USER",bd=8, bg=buttoncolor, fg=buttonfg, width=25, font=("Times", 12),command=update_user)
    button6 = Button(owner_win,activebackground="green", text="SHOW USER",bd=8, bg=buttoncolor, fg=buttonfg, width =25, font=("Times", 12),command=uesr_show)
    
    
    label0.grid(columnspan=6, padx=10, pady=10)
 
    
    button2.grid(row=5,column=0, padx=10, pady=10)
    button4.grid(row=5,column=1, padx=10, pady=10)
    button5.grid(row=5,column=2, padx=10, pady=10)
    
    button3.grid(row=6,column=1, padx=10, pady=10)
    button1.grid(row=6,column=0, padx=10, pady=10)
    button6.grid(row=6,column=2, padx=10, pady=10)

    owner_win.mainloop()

#main برنامه اصلی
sign_up()
