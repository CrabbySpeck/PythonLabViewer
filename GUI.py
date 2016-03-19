#!/user/bin/env python

import commands #Imports the commands.py file to keep the code cleaner
import Tkinter as tk #Imports the tkinter graphics library as tk

class Application(tk.Frame): #Defines the application class that inherits from the Tkinter Frame class
	def __init__(self, master=None): #Calls the constructor for the parent class, Frame
		
		tk.Frame.__init__(self, master) #Actually makes the program appear onscreen.

		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.quitButton = tk.Button(self, text='Quit', command=self.quit) #Creates a button labeled 'Quit'
		
		self.quitButton.grid() #Places the button on the application


app = Application() #The Main Program Starts Here

app.master.title('Sample Application') #Sets the title of the window

app.mainloop() #Starts the app's main loop, waiting for keyboard and mouse events.
