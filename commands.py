def printHello():
    print("Hello")
    
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