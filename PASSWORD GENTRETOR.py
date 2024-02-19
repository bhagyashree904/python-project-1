import string,random
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
root=Tk()
root.title("Password Generator ")
root.geometry("1000x1000")
root["bg"]="light pink"
# root.config(bg="beige")
root.resizable(False,False)
all_no={"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"10",
         "11":"11","12":"12","13":"13","14":"14","15":"15","16":"16","17":"17","18":"18","19":"19","20":"20"}
def reset():
    password_final.config(text='')
    password_final.config(text='')
def password_generate():
    try:
        length_pass=solid.get()
        small_pass=string.ascii_lowercase
        capital_pass=string.ascii_uppercase
        digits=string.digits
        special_char=string.punctuation
        all_list=[]
        all_list.extend(list(small_pass))
        all_list.extend(list(capital_pass))
        all_list.extend(list(digits))
        all_list.extend(list(special_char))
        random.shuffle(all_list)
        password.set("".join(all_list[0:length_pass]))

    except:
       messagebox.askretrycancel("A problem has been occured")
stu_lbl = Label(root, text="PASSWORD GENERATOR  ", font="ariel  25 bold underline " ,bg="light pink")
stu_lbl.place(x=400, y=10)

stu_lbl = Label(root, text="Enter User Name : ", font=90 ,bg="light pink")
stu_value = Entry(root, fg='black', font=90, width=60)

stu_lbl.place(x=0, y=150)
stu_value.place(x=250, y=150)

stu_lbl = Label(root, text="Enter password Length : ", font=200,bg="light pink")
# stu_value = Entry(root, fg='black', font=90, width=60)

stu_lbl.place(x=0, y=200)
# stu_value.place(x=250, y=200)

solid=IntVar()
selector=Combobox(root,textvariable=solid,state="readonly")
selector['values']=[l for l in all_no.keys()]
selector.current(7)
selector.place(x=250, y=200)

stu_lbl = Label(root, text="Generated password: ", font=90,bg="light pink")
# stu_value = Entry(root, fg='black', font=90, width=60)

stu_lbl.place(x=0, y=250)
# stu_value.place(x=250, y=250)


gen_btn=Button(root,text="Generate password  ",bg='white',fg="black",font=30,command=password_generate)
gen_btn.place(x=400,y=405)


# gen_btn=Button(root,text="ACCEPT ",bg='white',fg="black",font=30)
# gen_btn.place(x=450,y=455)

password=StringVar()
password_final=Entry(root,textvariable=password,state="readonly",bg='white',fg="black",font=30)
password_final.place(x=250, y=250)

reset_btn=Button(root,text="RESET ",bg='white',fg="black",font=30 ,command=reset)
reset_btn.place(x=450,y=505)

root.mainloop()