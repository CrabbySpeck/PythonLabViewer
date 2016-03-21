import commands
import imports
import tkinter as tk
from tkinter import messagebox
	
class Application(tk.Frame): #Defines the application class that inherits from the Tkinter Frame class
	def __init__(self, master=None): #Calls the constructor for the parent class, Frame
		
		tk.Frame.__init__(self, master) #Actually makes the program appear onscreen.

		self.grid()
		self.createWidgets()
		
	def createWidgets(self):
		listBoxContents = tk.StringVar()
		listBoxContents.set('And The Dog')
				
		self.populateListButton = tk.Button(text='Populate Menu', activebackground='orange', bg='black', fg='white', command=self.populate)
		self.listbox = tk.Listbox(listvariable='listBoxContents', activestyle='none',background='black', highlightcolor='yellow',selectbackground='orange', foreground='white')
		self.aboutDialog = tk.Message(self, text='Hello', takefocus=True)
		self.lengthLabel = tk.Label(self, text='Length of list: []')
		
		#Creates Menus
		#FileMenu
		self.fileMenuButton = tk.Menubutton(self, text='File', bg='black', fg='white', activebackground='orange')
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
		self.lengthLabel.grid()
		
		print(":::::::::::PLV STARTED::::::::::")

	def aboutMe(self):
		f = open('config.txt', 'r')
		aboot = str(f.readline())
		messagebox.showinfo(title='About', message=aboot)
	def populate(self):
		f = open('listBox.txt', 'r')
		i = 1
		length = int(f.readline())
		labeled = 'Length of list: [', str(length), ']'
		self.lengthLabel.config(text=labeled)
		print(length)
		while i < length + 1:
			content = str(f.readline())
			content = content[0:len(content)-1]
			self.listbox.insert(i, content)
			i = i + 1
		f.close()

app = Application() #The Main Program Starts Here
app.master.title('Python Lab Viewer') #Sets the title of the window
app.mainloop() #Starts the app's main loop, waiting for keyboard and mouse events.