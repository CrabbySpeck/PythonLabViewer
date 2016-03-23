import tkinter as tk
from tkinter import messagebox
import time
	
class Application(tk.Frame): #Defines the application class that inherits from the Tkinter Frame class
	def __init__(self, master=None): #Calls the constructor for the parent class, Frame
		
		tk.Frame.__init__(self, master) #Actually makes the program appear onscreen.

		self.grid()
		self.createWidgets(configureCode.confog)
		self.Started()
				
	def createWidgets(self, conf):
		listBoxContents = tk.StringVar()
				
		self.populateListButton = tk.Button(text='List Available Programs', activebackground=conf[0], bg=conf[1], fg=conf[2], command=self.populate)
		self.listbox = tk.Listbox(listvariable='listBoxContents', activestyle='none',bg=conf[1], highlightcolor='yellow',selectbackground=conf[0], foreground=conf[2])
		self.getSelectionButton = tk.Button(self, text='Open Selected Lab', activebackground=conf[0], bg=conf[1], fg=conf[2], command=self.actOnSelected)
		
		#Creates Menus
		#FileMenu
		self.fileMenuButton = tk.Menubutton(self, text='File', bg=conf[1], fg=conf[2], activebackground=conf[0])
		self.fileMenuButton.grid()

		self.fileMenuButton.fileMenu = tk.Menu(self.fileMenuButton, tearoff=0)
		self.fileMenuButton.config(menu=self.fileMenuButton.fileMenu)

		#Add Options to the Menus
		#fileMenu:
		self.fileMenuButton.fileMenu.add_command(command=self.quit, label='Quit')
		self.fileMenuButton.fileMenu.add_command(command=self.aboutMe, label='About')
		
		#Populate the Window
		self.populateListButton.grid()
		self.listbox.grid()
		self.getSelectionButton.grid()
		
		print(":::::::::::PLV STARTED::::::::::")


	def aboutMe(self):
		aboot = configureCode.confog[3]
		
		messagebox.showinfo(title='About PLV', message=aboot)
	def Started(self):
		messagebox.showinfo(title='Success!', message='PythonLabViewer has successfully started\n and all configuration files have been loaded.')
	def populate(self):
		f = open('listBox.txt', 'r')
		i = False
		while i != True:
			content = str(f.readline())
			if content != '':
				content = content[0:len(content)-1]
				self.listbox.insert(i, content)
			elif content == '':
				i = True
		f.close()

	def actOnSelected(self):
		index = self.listbox.curselection()
		lines = self.listbox.get(index)
		print('Running: ', lines)
		
		m = __import__ (lines) #Direct use of __import__() because we do not know the name of the file until selected from list.
		func = getattr(m,'mainMenu') #Assigns the function, mainMenu, from module m to the variable 'func'
		func() #Runs function, mainMenu, from m
class configureCode():
	f = open('config.txt', 'r')
	config = []
	
	activebackground = f.readline().rstrip() #f.readline().rstrip() #ActiveBackground, conf[0]
	bg = f.readline().rstrip() #f.readline().rstrip() #BackgroundColor, conf[1]
	fg = f.readline().rstrip() #f.readline().rstrip() #ForegroundColor, conf[2]
	about = f.readline() #AboutMessage, conf[3]
	confog = [activebackground, bg, fg, about]# Config File Order: PrimaryColor, AccentColor, AboutMsg
	print('Configurations: ', confog)
	f.close()
	
	def printListBox():
		sel = Application.listbox.curselection()
		print(x)
		return True


app = Application() #The Main Program Starts Here
app.master.title('Python Lab Viewer') #Sets the title of the window
app.mainloop() #Starts the app's main loop, waiting for keyboard and mouse events.