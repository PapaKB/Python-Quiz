from tkinter import*
import random

def pages2():
    global item
    frame_list[item].pack_forget()
    item=item-1
    frame_list[item].pack()
    
def pages1():
    global item
    total=0
    if item != len(frame_list)-1:
        frame_list[item].pack_forget()
        item=item+1
        frame_list[item].pack()
    else:
        frame_list[item].pack_forget()
        frame4=Frame(screen3)
        frame4.pack()
        Label(frame4, text="Complete", width="400", height="2", fg="purple", font=("Helvetica", 26)).pack()
        q=0
        while q!=(question.get()):
            if var[q].get()==1:
                total=total+1
            q=q+1
        statement=name.get()+", you scored: "+ str(total) +"/"+ str(question.get())
        Label(frame4, text=statement, width="400", height="2", fg="blue", font=("Calibri", 20)).pack()
        
def all_csv(csv_name, screen_name):
    global var
    global item
    global screen3
    global frame_list
    if (flag==True and question.get() in range(5,11)) or (flag==False):
        
        question_list=[]
        import csv
        csvFile=open(csv_name)
        details=(csvFile)

        for row in details:
            item=row.rstrip("\n").split(",")
            heading=["Question","Answer1","Answer2","Answer3"]
            data=zip(heading,item)
            details_data_dict=dict(data)
            question_list.append(details_data_dict)
            
    if flag==False:
        change(question_list)
        
    if (flag==True and question.get() in range(5,11)):
        screen3=Tk()
        screen3.geometry("500x300")
        screen3.title(screen_name)
            
        i=0
        var={}
        random.shuffle(question_list)
        frame_list=[]

    
        for j in question_list:
            while i in range(0, (question.get())):
                new_page=Frame(screen3)
                Label(new_page, text=j["Question"], wraplength="400", width="400", fg="navy", font=("Calibri", 16)).pack()
                var[i] = IntVar(new_page)
                first=Radiobutton(new_page, text=j["Answer1"], padx=5, variable=var[i], value=1)
                second=Radiobutton(new_page, text=j["Answer2"], padx=5, variable=var[i], value=2)
                third=Radiobutton(new_page, text=j["Answer3"], padx=5, variable=var[i], value=3)
                button_list=[first, second, third]
                random.shuffle(button_list)
                var[i].set(0)
                for k in button_list:
                    k.pack()
                if i==0:
                    Button(new_page, text="Next", width="5", height="1", command=pages1).pack(side=RIGHT)
                else:
                    Button(new_page, text="Next", width="5", height="1", command=pages1).pack(side=RIGHT)
                    Button(new_page, text="Back", width="5", height="1", command=pages2).pack(side=LEFT)
                frame_list.append(new_page)
                i=i+1
                break
        item=0
        frame_list[0].pack()

    if (flag==True and (question.get()<5 or question.get()>10)):
        question.set("Invalid Entry")

        
def questions1(csv_name, screen_name):
    global frame3
    global question
    global name
    frame2.pack_forget()
    screen2.title(screen_name)
    frame3=Frame(screen2)
    frame3.pack()
    
    question=IntVar()
    name=StringVar()
    
    Label(frame3, text="How many questions would you like to answer (5-10)? ", wraplength="280", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(frame3, text="").pack()
    question_entry=Entry(frame3, textvariable=question)
    question_entry.pack()
    Label(frame3, text="").pack()
    question.set("")
    Label(frame3, text="Enter your name below ", wraplength="280", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(frame3, text="").pack()
    name_entry=Entry(frame3, textvariable=name)
    name_entry.pack()
    Button(frame3, text="Enter", width="10", height="1", command=lambda:all_csv(csv_name, screen_name ) ).pack()
    Label(frame3, text="").pack()
    Button(frame3, text="Back", height="1", width="5", command=lambda:(frame3.pack_forget(), frame2.pack(), screen2.title("Menu"))).pack()

def add( ):
    coin=0

def edit():
    coin=0
def delete():
    coin=0
    
def change(list_of_questions):
    frame2.pack_forget()
    screen2.title("")
    screen2.geometry("600x400")
    
    canvas=Canvas(screen2, borderwidth=0)
    frame6=Frame(canvas)
    scrollbar=Scrollbar(screen2, orient=VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    canvas.create_window((4,4), window=frame6, anchor=NW)
    frame6.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

    number=1
    row_number=0
    for i in list_of_questions:
        statement=(str(number)+". "+(i["Question"]))
        Label(frame6, text=statement, fg="navy", wraplength="500", font=("Calibri", 16)).grid(row=row_number, column=0, sticky=W)
        Label(frame6, text=("       "+i["Answer1"]), wraplength="500", fg="navy", font=("Calibri", 16)).grid(row=row_number+1, column=0, sticky=W)
        Label(frame6, text=("       "+i["Answer2"]), wraplength="500", fg="navy", font=("Calibri", 16)).grid(row=row_number+2, column=0, sticky=W)
        Label(frame6, text=("       "+i["Answer3"]), wraplength="500", fg="navy", font=("Calibri", 16)).grid(row=row_number+3, column=0, sticky=W)
        row_number=row_number+4
        number=number+1

    Label(frame6, text="Please select a function below:", bg="grey", height="2", font=("Calibri", 13)).grid(row=row_number+1, column=0)
    Label(frame6, text="").grid(row=row_number+2)
    Button(frame6, text="Add", height="2", width="30", command=lambda:add(csv_name, topic_name)).grid(row=row_number+3, column=0)
    Label(frame6, text="").grid(row=row_number+4)
    Button(frame6, text="Edit", height="2", width="30", command=lambda:edit(csv_name, topic_name)).grid(row=row_number+5, column=0)
    Label(frame6, text="").grid(row=row_number+6)
    Button(frame6, text="Delete", height="2", width="30", command=lambda:delete(csv_name, topic_name)).grid(row=row_number+7, column=0)
    Label(frame6, text="").grid(row=row_number+8)
    Button(frame6, text="Back", height="1", width="5", command=lambda:(frame6.unbind("<Configure>"), frame2.pack())).grid(row=row_number+9, column=0)
#canvas.delete("all")
    
def sub_menu1():
    global frame2
    frame1.pack_forget()  
    frame2=Frame(screen2)
    frame2.pack()
    if flag==False:
        Label(frame2, text="Please select a sub-topic below", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
        Label(frame2, text="").pack()
        Button(frame2, text="BIOS", height="2", width="30", command=lambda:all_csv("bios.csv", "BIOS")).pack()
        Label(frame2, text="").pack()
        Button(frame2, text="Interrupts", height="2", width="30", command=lambda:all_csv("interrupts.csv", "Interrupts")).pack()
        Label(frame2, text="").pack()
        Button(frame2, text="Scheduling", height="2", width="30", command=lambda:all_csv("scheduling.csv", "Scheduling")).pack()
        Label(frame2, text="").pack()
        Button(frame2, text="Back", height="1", width="5", command=lambda:(frame2.pack_forget(), frame1.pack())).pack()
    else:
        Label(frame2, text="Please select a sub-topic below", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
        Label(frame2, text="").pack()
        Button(frame2, text="BIOS", height="2", width="30", command=lambda:questions1("bios.csv", "BIOS")).pack()
        Label(frame2, text="").pack()
        Button(frame2, text="Interrupts", height="2", width="30", command=lambda:questions1("interrupts.csv", "Interrupts")).pack()
        Label(frame2, text="").pack()
        Button(frame2, text="Scheduling", height="2", width="30", command=lambda:questions1("scheduling.csv", "Scheduling")).pack()
        Label(frame2, text="").pack()
        Button(frame2, text="Back", height="1", width="5", command=lambda:(frame2.pack_forget(), frame1.pack())).pack()

def sub_menu2():
    global frame2
    frame1.pack_forget()
    frame2=Frame(screen2)
    frame2.pack()
    
    Label(frame2, text="Please select a sub-topic below", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(frame2, text="").pack()
    Button(frame2, text="Queues", height="2", width="30", command=lambda:questions1("queues.csv", "Queues")).pack()
    Label(frame2, text="").pack()
    Button(frame2, text="Stacks", height="2", width="30", command=lambda:questions1("stacks.csv", "Stacks")).pack()
    Label(frame2, text="").pack()
    Button(frame2, text="Graphs", height="2", width="30", command=lambda:questions1("graphs.csv", "Graphs")).pack()
    Label(frame2, text="").pack()
    Button(frame2, text="Back", height="1", width="5", command=lambda:(frame2.pack_forget(), frame1.pack())).pack()
   
def student():
    global screen2
    global frame1
     #if a teacher logged in and then wanted to see the question layout for students flag would be equal to false so it has to change here
    screen2=Toplevel(screen)
    frame1=Frame(screen2)
    frame1.pack() 
    screen2.title("Menu")
    screen2.geometry("300x280") 
    Label(frame1, text="Please select a topic below", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(frame1, text="").pack()
    Button(frame1, text="Operating Systems", height="2", width="30", command=sub_menu1).pack()
    Label(frame1, text="").pack()
    Button(frame1, text="Data Structures", height="2", width="30", command=sub_menu2).pack()

def login_user():
    global flag
    login_list=[]
    import csv
    csvFile=open("login.csv")
    details=(csvFile)

    for row in details:
        item=row.rstrip("\n").split(",")
        heading=["Username","Password"]
        data=zip(heading,item)
        details_data_dict=dict(data)
        login_list.append(details_data_dict)

    for i in login_list:
        if username.get()==i["Username"] and password.get()==i['Password']: 
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            flag=False
            student()
        else:
            password_entry.delete(0, END)
            username.set("Re-enter login details")
    
def login():
    global username
    global password
    global username_entry
    global password_entry

    frame.pack_forget()
    frame5 = Frame(screen)
    frame5.pack()
    screen.title("Login")
    screen.geometry("300x250")

    username=StringVar()
    password=StringVar()

    Label(frame5, text="Please enter details below", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(frame5, text="").pack()
    Label(frame5, text="Username*").pack()
    username_entry=Entry(frame5, textvariable=username)
    username_entry.pack()
    Label(frame5, text="Password*").pack()
    password_entry=Entry(frame5, textvariable=password)
    password_entry.pack()
    Label(frame5, text="").pack()
    Button(frame5, text="Enter", width="10", height="1", command=login_user).pack()
    Button(frame5, text="Back", width="5", height="1", command=lambda:(frame5.pack_forget(), frame.pack())).pack(side=LEFT)
    
def main_screen():
    global frame
    global screen
    global flag
    flag=True
    screen = Tk()
    frame=Frame(screen)
    frame.pack()
    screen.geometry("300x250")
    screen.title("Welcome to the quiz")
    Label(frame, text = "Quiz", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(frame, text="").pack()
    Button(frame, text="Student", height="2", width="30", command=student).pack()
    Label(frame,text="").pack()
    Button(frame, text="Login", height="2", width="30", command=login).pack()

    screen.mainloop()
main_screen()
