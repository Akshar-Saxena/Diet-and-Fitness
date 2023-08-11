from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk
import time
import tkinter.font as tkFont

window = Tk()
window.resizable(False, False)
window.geometry("720x560")
window.title("Diet and Fitness")
window.configure(bg="white")
window.wm_iconbitmap("icon.ico")

bg = ImageTk.PhotoImage(file="Bg.png")
b_login = ImageTk.PhotoImage(file="button.png")
b_signup = ImageTk.PhotoImage(file="button2.png")
sign_ = ImageTk.PhotoImage(file="button3.png")
healthy_pic = ImageTk.PhotoImage(file="healthy.png")

text = '''All information presented and written within this app are intended for informational purposes only. You should not rely on 
this information as a substitute for, nor does it replace, professional medical advice, diagnosis, or treatment. If you have 
any concerns or questions about your health, you should always consult with a physician or other health-care professional.'''

canvas = Canvas(window)
canvas.create_image(0, 0, image=bg,anchor=NW)
canvas.create_image(300, 100, image=healthy_pic, anchor=NW)
canvas.create_text(200, 225, text="Username", fill="black", font=('times', 17, 'bold'))
canvas.create_text(200, 275, text="Password", fill="black", font=('times', 17, 'bold'))
canvas.create_text(360, 490, text="** DISCLAIMER **", fill="red",font=('times', 15, 'bold'))
canvas.create_text(360, 530, text=text, fill="black", font=('times', 10, 'bold'))

def admin():
	canvas.destroy()
	u_name.destroy()
	pswd.destroy()
	log.place_forget()
	sig.place_forget()
	progress.place_forget()
	window.configure(bg="white")
	ntbook = ttk.Notebook(window)
	ntbook.pack()
	f1 = Frame(ntbook, width=720, height=580, bg="white")
	f2 = Frame(ntbook, width=720, height=580, bg="white")
	f3 = Frame(ntbook, width=720, height=580, bg="white")
	f1.pack(fill="both", expand=1)
	f2.pack(fill="both",expand=1)
	f3.pack(fill="both",expand=1)
	ntbook.add(f1, text="  Personal Info  ")
	ntbook.add(f2, text="  Diet Plan  ")
	ntbook.add(f3 ,text="  Exercise  ")
	tab1 = ImageTk.PhotoImage(file="Tab1.png")
	per_info = ImageTk.PhotoImage(file="per_info.png")
	Label(f1, image = per_info).pack()
	Label(f2, image = tab1).pack()
	Label(f3, image = tab1).pack()

	#Personal Info Tab
	with open("creds.txt", 'r') as f:
		global credits
		credits = f.read()
		credits = credits.split()
	c = credits.index(username)
	h = Entry(f1, textvariable=StringVar(value=credits[c+4]),bd=4,font="times 12" ,width=20, state=DISABLED)
	h.place(x=120, y=60)
	w = Entry(f1, textvariable=StringVar(value=credits[c+6]),bd=4,font="times 12" ,width=20, state=DISABLED)
	w.place(x=120, y=113)
	ch_food = StringVar()
	ch_food.set(credits[c+10])
	gender = StringVar()
	gender.set(credits[c+8])
	times = tkFont.Font(family='times', size=11)
	drop_menu_food = OptionMenu(f1, ch_food, "Veg","Non-Veg","Vegan","Keto")
	drop_menu_food.place(x=140, y=217)
	drop_menu_food.config(font=times, state=DISABLED)
	drop_gender = OptionMenu(f1, gender, "Male","Female")
	drop_gender.place(x=140, y=165)
	drop_gender.config(font=times, state=DISABLED)
	bmi = Entry(f1, textvariable=StringVar(), bd=4, font="times 12", width=15, state=DISABLED)
	bmi.place(x=158, y=274)
	body_type = Entry(f1, textvariable=StringVar(), bd=4, font="times 12", width=15, state=DISABLED)
	body_type.place(x=158, y=328)
	weight = float(w.get()) * 2.20462
	height = float(h.get()) * 0.393701
	BMI = (weight/(height**2))*703
	BMI = round(BMI, 1)
	str(BMI)
	bmi = Entry(f1, textvariable=StringVar(value=BMI), bd=4, font="times 12", width=15, state=DISABLED)
	bmi.place(x=158, y=274)
	b = ""
	global badge
	if int(BMI) < 18.5:
		b = "Underweight"
	elif int(BMI) >= 18.5 and int(BMI) < 25:
		b = "Normal"
	elif int(BMI) >= 25 and int(BMI) < 30:
		b = "Overweight"
	else:
		b = "Obese"
	body_type = Entry(f1, textvariable=StringVar(value = b), bd=4, font="times 12", width=15, state=DISABLED)
	body_type.place(x=158, y=328)
	bmi_change = 21.7 - int(BMI)
	weight_change = (bmi_change/703)*(height**2)
	weight_change = weight_change / 2.20462
	print(round(weight_change,1)," Kg")
	#s_but = ImageTk.PhotoImage(file="save.png")
	#Button(f1, image=s_but, bd=0, bg="black").place(x=110, y=420)
	window.mainloop()

def signup():
	Sign_up_window = Toplevel(window)
	s_window = ImageTk.PhotoImage(file="s_window.png")
	Sign_up_window.geometry("400x400")
	Sign_up_window.title("Sign up window")
	Sign_up_window.resizable(False, False)
	Sign_up_window.configure(bg="green")
	Sign_up_window.wm_iconbitmap("icon.ico")
	next_but = ImageTk.PhotoImage(file="next.png")

	s_canvas = Canvas(Sign_up_window)
	s_canvas.create_image(0, 0, image=s_window, anchor=NW)
	s_canvas.create_text(80, 130, text="Username", fill="black", font=("times", 12, "bold"), tag="u")
	s_canvas.create_text(80, 160, text="Password", fill="black", font=("times", 12, "bold"), tag="p")
	s_canvas.create_text(80, 190, text="Confirm Password", fill="black", font=("times", 12, "bold"), tag="pc")
	s_canvas.pack(fill="both", expand=True)

	uname = Entry(Sign_up_window, textvariable=StringVar(),width=30,bd=2)
	uname.place(x=160, y=120)
	pwd = Entry(Sign_up_window, textvariable=StringVar(),show = "*",width=30,bd=2)
	pwd.place(x=160, y=150)
	pwd_c = Entry(Sign_up_window, textvariable=StringVar(),show = "*",width=30,bd=2)
	pwd_c.place(x=160, y=180)

	def Next():
		s_canvas.delete("u")
		s_canvas.delete("p")
		s_canvas.delete("pc")
		uname.place_forget()
		pwd.place_forget()
		pwd_c.place_forget()
		next_button.place_forget()
		sign.place(x=160, y=260)
		s_canvas.create_text(80, 110, text="Height", fill="Black", font=("times", 12, "bold"))
		s_canvas.create_text(80, 145, text="Weight", fill="Black", font=("times", 12, "bold"))
		s_canvas.create_text(80, 180, text="Gender", fill="Black", font=("times", 12, "bold"))
		s_canvas.create_text(80, 215, text="Food Type", fill="Black", font=("times", 12, "bold"))
		global hei, wei, ch_food_, gender_
		hei = Entry(s_canvas, textvariable=StringVar(value="Write in 'cm'"),bd=2,font="times 12" ,width=20)
		hei.place(x=120, y=95)
		wei = Entry(s_canvas, textvariable=StringVar(value="Write in Kg"),bd=2,font="times 12" ,width=20)
		wei.place(x=120, y=133)
		ch_food_ = StringVar()
		ch_food_.set("Veg")
		gender_ = StringVar()
		gender_.set("Male")
		times = tkFont.Font(family='times', size=11)
		drop_menu_food_ = OptionMenu(s_canvas, ch_food_, "Veg","Non-Veg","Vegan","Keto")
		drop_menu_food_.place(x=140, y=165)
		drop_menu_food_.config(font=times)
		drop_gender_ = OptionMenu(s_canvas, gender_, "Male","Female")
		drop_gender_.place(x=140, y=200)
		drop_gender_.config(font=times)

	def Push():
		def d():
			Sign_up_window.destroy()
		if pwd.get() == pwd_c.get():
			with open("creds.txt", "a+") as f:
				f.write(f"{uname.get()} : {pwd.get()} : {hei.get()} : {wei.get()} : {gender_.get()} : {ch_food_.get()}" + "\n")
			def step():
				for x in range(10):
					myprogress['value'] += 10
					Sign_up_window.update_idletasks()
					time.sleep(0.1)
				d()
			myprogress = ttk.Progressbar(Sign_up_window, orient=HORIZONTAL ,length=200, mode='determinate')
			myprogress.place(x=102,y=330)
			step()
		else:
			messagebox.showinfo("Error", "Password do not match with each other!")

	sign = Button(Sign_up_window, image = b_signup, bg="black",bd=0, command=Push)
	next_button = Button(Sign_up_window, image = next_but, bg="black",bd=0, command=Next)
	next_button.place(x=160, y=260)
	Sign_up_window.mainloop()


def login():
	with open("creds.txt", "r") as f:
		data = f.read()
	lis = data.split()
	try:
		global username
		username = u_name.get()
		i = lis.index(username)
		password = lis[i+2]
		if u_name.get() == username and pswd.get() == password:
			def step():
				for x in range(10):
					progress['value'] += 10
					window.update_idletasks()
					time.sleep(0.07)
				admin()
			global progress
			progress = ttk.Progressbar(window, orient=HORIZONTAL ,length=300, mode='determinate')
			progress.place(x=210,y=420)
			step()
		elif u_name.get() == username and pswd.get() != password:
			messagebox.showinfo("Invalid Password","Wrong Password! Please enter correct password")
		elif u_name.get() != username and pswd.get() == password:
			messagebox.showinfo("Invalid Username","Invalid Username! Please enter a valid username")
		else:
			messagebox.showinfo("Invalid Username and Password","Both username and password are incorrect!")
	except:
		messagebox.showinfo("Error", "Username not found")

u_name = Entry(window, textvariable = StringVar(),font = 'times 14 bold' ,width = 25)
u_name.place(x=320, y=215)

pswd = Entry(window, textvariable = StringVar(),font = 'times 14 bold',show="*" ,width = 25)
pswd.place(x=320, y=263)

log = Button(window,image = b_login,bg="black",bd=0, command = login)
log.place(x=220, y=350)
sig = Button(window,image= sign_,bg="black",bd=0, command = signup)
sig.place(x=380, y=350)

canvas.pack(fill="both", expand=True)

window.mainloop()

