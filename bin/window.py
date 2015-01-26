
import Tkinter


class messengerApp(Tkinter.Tk):

	def __init__(self, *args, **kwargs):

		Tkinter.Tk.__init__(self, *args, **kwargs)
		self.title("natMessenger")
		
		container = Tkinter.Frame(self)	
		container.pack()

		self.frames = {}

		win1 = LoginWindow(container, self)
		self.frames[LoginWindow] = win1
		win1.grid(row=0, column=0, sticky="nsew")

		win2 = SecureArea(container, self)
		self.frames[SecureArea] = win2
		win2.grid(row=0, column=0, sticky="nsew")

		win1.tkraise()

	
class LoginWindow(Tkinter.Frame):

	def __init__(self, parent, controller):
		self.controller=controller
		Tkinter.Frame.__init__(self, parent)
		
		username_label = Tkinter.Label(self, text="Username")
		username_label.pack()

		username_entry = Tkinter.Entry(self)
		username_entry.pack()

		password_label = Tkinter.Label(self, text="Password")
		password_label.pack()

		password_entry = Tkinter.Entry(self)
		password_entry.pack()
		
		self.username = username_entry
		self.password = password_entry

		ok_button = Tkinter.Button(self, text="Login", command=self.login)
		ok_button.pack()		


	def login(self):

		if (self.username.get() == 'admin' and self.password.get() == '1234'):
		
			print "logged in!!!"
			self.controller.frames[SecureArea].tkraise()


class SecureArea(Tkinter.Frame):

	def __init__(self, parent, controller):

		Tkinter.Frame.__init__(self, parent)

		text = Tkinter.Label(self, text="This is a secure area")
		text.pack()

		talk_text = Tkinter.Text(self)
		talk_text.insert(Tkinter.END, "Me: This is a chat!!!")
		talk_text.configure(state='disabled')
		talk_text.pack()

		message_entry = Tkinter.Entry(self)
		message_entry.pack()




app = messengerApp()
app.mainloop()
