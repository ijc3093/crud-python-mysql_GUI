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
        sqlCon = pymysql.connect(host = "127.0.0.1", user="root", password="Merciful#100", database="employees")

        # Step 5
        self.root = root
        titlespace = " "
        self.root.title(15 * titlespace + "Employee Information System")
        self.root.geometry("745x600+300+0")
        self.root.resizable(width = False, height = False)

        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief = RIDGE, bg = "grey")
        MainFrame.grid()

        # Step 7 (See step 6 at the end of ConnectorDB)
        #==============================================Title===================================================
        TitleFrame = Frame(MainFrame, bd=7, width=700, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        # Step 8
        #==============================================Left===================================================
        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2, bg="grey", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=12, pady=9, relief=RIDGE)
        LeftFrame1.pack(side=TOP)

        # Step 9
        #==============================================Right===================================================
        RightFrame1 = Frame(TopFrame3, bd=5, width=100, height=400, padx=2, bg="grey", relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        RightFrame1a.pack(side=TOP)

        # Step 10
        #==============================================Implement by StringVar===================================================
        ID=IntVar()
        name=StringVar()
        email=StringVar()
        age=IntVar()
        designation=StringVar()
        created=StringVar()

        # Step 11
        #==============================================Exit===================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("MySQL Connection", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        # Step 12
        #==============================================Reset===================================================
        def Reset():
            self.entID.delete(0, END)
            self.entname.delete(0, END)
            self.entemail.delete(0, END)
            self.entlblage.delete(0, END)
            designation.set("")
            self.entcreated.delete(0, END)

        # Step 13
        #==============================================Add Item===================================================
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

        # Step 14
        #==============================================Display All Data===================================================
        def displayData():
                # sqlCon = pymysql.connect(host = "127.0.0.1", user="root", password="Merciful#100", database="employees")
                cur = sqlCon.cursor()
                cur.execute("select * from employees")
                result = cur.fetchall()
                if len(result) !=0:
                    self.student_records.delete(*self.student_records.get_children())
                    for row in result:
                        self.student_records.insert('', END, values = row)

                sqlCon.commit()
                sqlCon.close()
        

        # Step 15
        #==============================================Select row to display exactly data in the input===================================================
        def employeesInfo(ev):
            viewInfo = self.student_records.focus()
            learnerData = self.student_records.item(viewInfo)
            row = learnerData['values']
            ID.set(row[0])
            name.set(row[1])
            email.set(row[2])
            age.set(row[3])
            designation.set(row[4])
            created.set(row[5])
        
        # Step 16
        #==============================================Update===================================================
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

        # Step 17
        #==============================================Delete===================================================
        def deleteDB():
            # sqlCon = pymysql.connect(host = "127.0.0.1", user="root", password="Merciful#100", database="employees")
            cur = sqlCon.cursor()
            cur.execute("delete from employees where id=%s", ID.get())

            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Deleted")
            Reset()


        # Step 18
        #==============================================Search===================================================
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
            

        # Step 19
        #==============================================Input===================================================
        self.lbltitle=Label(TitleFrame, font=('arial', 40, 'bold'), text="MySQL Connection", bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        # Student ID
        self.lblID=Label(LeftFrame1, font=('arial', 12, 'bold'), text="ID", bd=7)
        self.lblID.grid(row=0, column=0, sticky=W, padx=5)
        self.entID=Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=ID)
        self.entID.grid(row=0, column=1, sticky=W, padx=5)

        # First Name
        self.lblname=Label(LeftFrame1, font=('arial', 12, 'bold'), text="Full Name", bd=7)
        self.lblname.grid(row=1, column=0, sticky=W, padx=5)
        self.entname=Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=name)
        self.entname.grid(row=1, column=1, sticky=W, padx=5)

        # Last Name
        self.lblemail=Label(LeftFrame1, font=('arial', 12, 'bold'), text="Email Address", bd=7)
        self.lblemail.grid(row=2, column=0, sticky=W, padx=5)
        self.entemail=Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=email)
        self.entemail.grid(row=2, column=1, sticky=W, padx=5)

        # Full age
        self.lblage=Label(LeftFrame1, font=('arial', 12, 'bold'), text="Full age", bd=7)
        self.lblage.grid(row=3, column=0, sticky=W, padx=5)
        self.entlblage=Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=age)
        self.entlblage.grid(row=3, column=1)

        # designation
        self.lbldesignation=Label(LeftFrame1, font=('arial', 12, 'bold'), text="Designation", bd=7)
        self.lbldesignation.grid(row=4, column=0, sticky=W, padx=5)
        self.cbodesignation=ttk.Combobox(LeftFrame1, font=('arial', 12, 'bold'), width=43, state='readonly', textvariable=designation)
        self.cbodesignation['values']=('','Female', 'Male')
        self.cbodesignation.current(0)
        self.cbodesignation.grid(row=4, column=1)

        # created
        self.lblcreated=Label(LeftFrame1, font=('arial', 12, 'bold'), text="Date [yyyy-dd-mm]", bd=7)
        self.lblcreated.grid(row=5, column=0, sticky=W, padx=5)
        self.entcreated=Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=created)
        self.entcreated.grid(row=5, column=1, sticky=W, padx=5)


        # Step 20
        #==============================================Table Treeview===================================================
        scroll_y = Scrollbar(LeftFrame, orient = VERTICAL)
        
        self.student_records=ttk.Treeview(LeftFrame, height = 12, columns=("id", "name", "email", "age", "designation", "created"), yscrollcommand=scroll_y.set)

        scroll_y.pack(side = RIGHT, fill=Y)

        self.student_records.heading("id", text = "ID")
        self.student_records.heading("name", text = "Full Name")
        self.student_records.heading("email", text = "Email Address")
        self.student_records.heading("age", text = "Age")
        self.student_records.heading("designation", text = "Designation")
        self.student_records.heading("created", text = "Date")

        self.student_records['show']='headings'
        

        self.student_records.column("id", width=70)
        self.student_records.column("name", width=70)
        self.student_records.column("email", width=70)
        self.student_records.column("age", width=70)
        self.student_records.column("designation", width=70)
        self.student_records.column("created", width=70)

        
        self.student_records.pack(fill = BOTH, expand=1)
        self.student_records.bind("<ButtonRelease-1>",employeesInfo)
        # displayData()

        # Step 21
        #==============================================Button===================================================
        self.btnAddNew = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Add New", bd=4, pady=1, padx=24, width = 8, height=2, command=addData).grid(row=0, column=0, padx=1)
        self.btnDisplay = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24, width = 8, height=2, command=displayData).grid(row=1, column=0, padx=1)
        self.btnUpdate = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24, width = 8, height=2, command=update).grid(row=2, column=0, padx=1)
        self.btnDelete = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24, width = 8, height=2, command=deleteDB).grid(row=3, column=0, padx=1)
        self.btnSearch = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24, width = 8, height=2, command=searchDB).grid(row=4, column=0, padx=1)
        self.btnReset = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24, width = 8, height=2, command=Reset).grid(row=5, column=0, padx=1)
        self.btnExit = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=24, width = 8, height=2, command=iExit).grid(row=6, column=0, padx=1)

        #==============================================Add Item===================================================

# 6 
if __name__ =='__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()
