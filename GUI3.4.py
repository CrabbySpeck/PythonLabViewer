#!/user/bin/env python

import commands #Imports the commands.py file to keep the code cleaner
import tkinter as tk #Imports the tkinter graphics library as tk
import platform #Imports the Platform module to show basic system name

class Application(tk.Frame): #Defines the application class that inherits from the Tkinter Frame class
	def __init__(self, master=None): #Calls the constructor for the parent class, Frame
		
		tk.Frame.__init__(self, master) #Actually makes the program appear onscreen.

		self.ShowInfo()
		self.grid()
		self.createWidgets()

	def ShowInfo(self):
			print("Python Lab Viewer Import Modification Program running on:", platform.system(), "\n")
			print("By:  Crab8012 and Green_Cafe")
		
	def createWidgets(self):
		#DEFINE VARIABLES
		entryOneVar = tk.StringVar()
		
		#DEFINE WIDGETS
#		self.quitButton = tk.Button(self, text='Quit', activebackground='orange', background='black', fg='white',  command=self.quit) #Creates a button labeled 'Quit' {No longer necessary as there is a file menu in place.
		self.writeButton = tk.Button(self, text='APPEND', activebackground='orange', background='black', fg='white',  command=self.appendMe)
#		self.oneCheckbox = tk.Checkbutton(self, text='Hi') #A Test Checkbox, so that there is a reference for future checkboxes
		self.oneEntry = tk.Entry(self, textvariable=entryOneVar)
		self.instructionLabel = tk.Label(self, text='Please type in your python lab file,\n without the .py at the end:')

		self.fileMenuButton = tk.Menubutton(self, text='File', bg='black', fg='white', activebackground='orange')
		self.fileMenuButton.grid()


		self.fileMenuButton.fileMenu = tk.Menu(self.fileMenuButton, tearoff=0)
		self.fileMenuButton.config(menu=self.fileMenuButton.fileMenu)

		#Add Options to the Menus
		#fileMenu:
		self.fileMenuButton.fileMenu.add_command(command=self.quit, label='Quit')
		self.fileMenuButton.fileMenu.add_command(command=listImports, label='List File Imports')

		# ADD WIDGETS TO THE WINDOW
#		self.quitButton.grid() #Places the button on the application {Not required as there is a new menuButton that performs the same function
#		self.oneCheckbox.grid() #Reference code for a checkbox
		self.instructionLabel.grid()
		self.oneEntry.grid()
		self.writeButton.grid()

	def printTextBox(self):
		print(self.oneEntry.get())
		return()

	def appendMe(self):
		content = self.oneEntry.get()
		content = 'import ' + content + '.py'
		printFile('imports.py', 'w', content)
		while 0 < len(self.oneEntry.get()):
			self.oneEntry.delete(0)
		return()
		
		
def listImports():
	f = open('imports.py', 'r')
	reader = []
	reader = f.readlines()
	print(reader)

def printFile(filename, mode, newcontent):
	content = newcontent
	
	#OPENS THE FILE AND SAVE CONTENTS INTO BUFFER
	f = open(filename, 'a')
	f.write(content)
	f.write('\n')
	f.close()

	#OPEN THE FILE AND PRINT ITS CONTENTS TO THE CONSOLE
	f = open(filename, 'r')
	reader = f.readlines()
	f.close()
	print(reader)
	return()




app = Application() #The Main Program Starts Here
app.master.title('PLV Import Utility') #Sets the title of the window
app.mainloop() #Starts the app's main loop, waiting for keyboard and mouse events.