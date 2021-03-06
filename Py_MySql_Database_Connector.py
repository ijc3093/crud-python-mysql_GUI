# Step 1
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from unittest import result
from markupsafe import re
import pymysql

# Step 2
class ConnectorDB:
    # Step 3
    def __init__(self, roof):

        # Step 4
        # Connect to python from mysql
        sqlCon = pymysql.connect(host = "127.0.0.1", user="root", password="Merciful#100", database="employees")

        # Step 5
        self.root = root
        titlespace = " "
        self.root.title(15 * titlespace + "MySQL Connects to Python")

        # Those are for width, height, move to or from (left and top). They are for out of the square with title.
        self.root.geometry("900x670+500+0") # 900x700+1140+0
        self.root.resizable(width = False, height = False)

        # Those are for width and height with frame in the square. They are unable to move around but it is fix in the square.
        MainFrame = Frame(self.root, bd=10, width=900, height=680, relief = RIDGE, bg = "grey")
        MainFrame.grid()

        # Step 7 (See step 6 at the end of ConnectorDB)
        #==============================================Title Frame===================================================
        TitleFrame = Frame(MainFrame, bd=7, width=880, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)

        # Step 8        
        #==============================================Body Frame===================================================
        TopFrame3 = Frame(MainFrame, bd=5, width=980, height=550, relief=RIDGE, bg = "grey")
        TopFrame3.grid(row=1, column=0)


        # Step 9
        #==============================================Right Frame===================================================
        # When you want frame to in the LEFT, it will move it to the LEFT once you add new frame. That's all

        LeftFrame = Frame(TopFrame3, bd=5, width=850, height=400, padx=2, bg="grey", relief=RIDGE)
        LeftFrame.pack(side=RIGHT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=833, height=350, padx=1, pady=40, relief=RIDGE)
        LeftFrame1.pack(side=TOP)


        # Step 10
        #==============================================Left Frame===================================================
        RightFrame1 = Frame(TopFrame3, bd=5, width=220, height=400, padx=2, bg="grey", relief=RIDGE)
        RightFrame1.pack(side=LEFT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=230, height=350, padx=2, pady=2, relief=RIDGE)
        RightFrame1a.pack(side=TOP)


        # Step 11
        #==============================================Implement by StringVar and IntVar===================================================
        ID=IntVar()
        name=StringVar()
        email=StringVar()
        age=IntVar()
        designation=StringVar()
        created=StringVar()

        # Step 12
        #==============================================Exit Method===================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("MySQL Connection", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        # Step 13
        #==============================================Reset Method===================================================
        def Reset():
            self.entID.delete(0, END)
            self.entname.delete(0, END)
            self.entemail.delete(0, END)
            self.entlblage.delete(0, END)
            designation.set("")
            self.entcreated.delete(0, END)


        # Step 14
        #==============================================Add Method===================================================
        def addData():
            if ID.get() == "" or name.get() == "" or email.get() == "":
                tkinter.messagebox.showerror("Mysql Connection", "Correct Details")
            else:
                cur = sqlCon.cursor()
                cur.execute("insert into employees values(%s, %s, %s, %s, %s, %s)", (
                    ID.get(),
                    name.get(),
                    email.get(),
                    age.get(),
                    designation.get(),
                    created.get()
                ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully")

        # Step 15
        #==============================================Display All Data Method===================================================
        def displayData():
                # sqlCon = pymysql.connect(host = "127.0.0.1", user="root", password="Merciful#100", database="employees")
                cur = sqlCon.cursor()
                cur.execute("select * from employees")
                result = cur.fetchall()
                if len(result) !=0:
                    self.employer_records.delete(*self.employer_records.get_children())
                    for row in result:
                        self.employer_records.insert('', END, values = row)

                sqlCon.commit()
                sqlCon.close()
        

        # Step 16
        #==============================================Select row to display exactly data in the input Method===================================================
        def employeesInfo(ev):
            viewInfo = self.employer_records.focus()
            learnerData = self.employer_records.item(viewInfo)
            row = learnerData['values']
            ID.set(row[0])
            name.set(row[1])
            email.set(row[2])
            age.set(row[3])
            designation.set(row[4])
            created.set(row[5])
        
        # Step 17
        #==============================================Update Method===================================================
        def update():
            # sqlCon = pymysql.connect(host = "127.0.0.1", user="root", password="Merciful#100", database="employees")
            cur = sqlCon.cursor()
            cur.execute("update employees set name=%s, email=%s, age=%s, designation=%s, created=%s where id=%s",(
                name.get(),
                email.get(),
                age.get(),
                designation.get(),
                created.get(),
                ID.get()
            ))
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Updated Successfully")
            Reset()

        # Step 18
        #==============================================Delete Method===================================================
        def deleteDB():
            # sqlCon = pymysql.connect(host = "127.0.0.1", user="root", password="Merciful#100", database="employees")
            cur = sqlCon.cursor()
            cur.execute("delete from employees where id=%s", ID.get())

            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Deleted")
            Reset()


        # Step 19
        #==============================================Search Method===================================================
        def searchDB():
            try:
                sqlCon = pymysql.connect(host = "127.0.0.1", user="root", password="Merciful#100", database="employees")
                cur = sqlCon.cursor()
                cur.execute("select * from employees where id='%s'"%ID.get())

                row = cur.fetchone()

                ID.set(row[0])
                name.set(row[1])
                email.set(row[2])
                age.set(row[3])
                designation.set(row[4])
                created.set(row[5])

                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Data Entry Form", "No Such Record Found")
                Reset()
            sqlCon.close()
            
        # Step 20
        #==============================================Title Message===================================================
        self.lbltitle=Label(TitleFrame, font=('arial', 39, 'bold'), text="Employee Information System", bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        #==============================================Input===================================================
        # Student ID
        self.lblID=Label(LeftFrame1, font=('arial', 12, 'bold'), text="ID", bd=7)
        self.lblID.grid(row=0, column=0, sticky=W, padx=5)
        self.entID=Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=60, justify='left', textvariable=ID)
        self.entID.grid(row=0, column=1, sticky=W, padx=5)


        # First Name
        self.lblname=Label(LeftFrame1, font=('arial', 12, 'bold'), text="Full Name", bd=7)
        self.lblname.grid(row=1, column=0, sticky=W, padx=5)
        self.entname=Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=60, justify='left', textvariable=name)
        self.entname.grid(row=1, column=1, sticky=W, padx=5)

        # Last Name
        self.lblemail=Label(LeftFrame1, font=('arial', 12, 'bold'), text="Email Address", bd=7)
        self.lblemail.grid(row=2, column=0, sticky=W, padx=5)
        self.entemail=Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=60, justify='left', textvariable=email)
        self.entemail.grid(row=2, column=1, sticky=W, padx=5)

        # Full age
        self.lblage=Label(LeftFrame1, font=('arial', 12, 'bold'), text="Full age", bd=7)
        self.lblage.grid(row=3, column=0, sticky=W, padx=5)
        self.entlblage=Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=60, justify='left', textvariable=age)
        self.entlblage.grid(row=3, column=1)

        # designation
        self.lbldesignation=Label(LeftFrame1, font=('arial', 12, 'bold'), text="Designation", bd=7)
        self.lbldesignation.grid(row=4, column=0, sticky=W, padx=5)
        self.cbodesignation=ttk.Combobox(LeftFrame1, font=('arial', 12, 'bold'), width=60, state='readonly', textvariable=designation)
        self.cbodesignation['values']=('','Female', 'Male')
        self.cbodesignation.current(0)
        self.cbodesignation.grid(row=4, column=1)

        # created
        self.lblcreated=Label(LeftFrame1, font=('arial', 12, 'bold'), text="Date [yyyy-dd-mm]", bd=7)
        self.lblcreated.grid(row=5, column=0, sticky=W, padx=5)
        self.entcreated=Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=60, justify='left', textvariable=created)
        self.entcreated.grid(row=5, column=1, sticky=W, padx=5)


        # Step 20
        #==============================================Table Treeview===================================================
        scroll_y = Scrollbar(LeftFrame, orient = VERTICAL)
        
        self.employer_records=ttk.Treeview(LeftFrame, height = 12, columns=("id", "name", "email", "age", "designation", "created"), yscrollcommand=scroll_y.set)

        scroll_y.pack(side = RIGHT, fill=Y)

        self.employer_records.heading("id", text = "ID")
        self.employer_records.heading("name", text = "Full Name")
        self.employer_records.heading("email", text = "Email Address")
        self.employer_records.heading("age", text = "Age")
        self.employer_records.heading("designation", text = "Designation")
        self.employer_records.heading("created", text = "Date")

        self.employer_records['show']='headings'

        # Step 20
        #==============================================Column===================================================
        self.employer_records.column("id", width=5)
        self.employer_records.column("name", width=20)
        self.employer_records.column("email", width=70)
        self.employer_records.column("age", width=3)
        self.employer_records.column("designation", width=70)
        self.employer_records.column("created", width=15)
       
        
        self.employer_records.pack(fill = BOTH, expand=1)
        self.employer_records.bind("<ButtonRelease-1>",employeesInfo)
        # displayData()


        # Step 21
        #==============================================Button===================================================
        self.btnAddNew = Button(RightFrame1a, font=('arial', 17, 'bold'), text="Add New", bd=4, pady=1, padx=33, width = 10, height=3, command=addData).grid(row=0, column=0, padx=1)
        self.btnDisplay = Button(RightFrame1a, font=('arial', 17, 'bold'), text="Display", bd=4, pady=1, padx=33, width = 10, height=3, command=displayData).grid(row=1, column=0, padx=1)
        self.btnUpdate = Button(RightFrame1a, font=('arial', 17, 'bold'), text="Update", bd=4, pady=1, padx=33, width = 10, height=3, command=update).grid(row=2, column=0, padx=1)
        self.btnDelete = Button(RightFrame1a, font=('arial', 17, 'bold'), text="Delete", bd=4, pady=1, padx=33, width = 10, height=3, command=deleteDB).grid(row=3, column=0, padx=1)
        self.btnSearch = Button(RightFrame1a, font=('arial', 17, 'bold'), text="Search", bd=4, pady=1, padx=33, width = 10, height=3, command=searchDB).grid(row=4, column=0, padx=1)
        self.btnReset = Button(RightFrame1a, font=('arial', 17, 'bold'), text="Reset", bd=4, pady=1, padx=33, width = 10, height=3, command=Reset).grid(row=5, column=0, padx=1)
        self.btnExit = Button(RightFrame1a, font=('arial', 17, 'bold'), text="Exit", bd=4, pady=1, padx=33, width = 10, height=3, command=iExit).grid(row=6, column=0, padx=1)
# 6 
if __name__ =='__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()