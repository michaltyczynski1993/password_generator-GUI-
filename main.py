from tkinter import *
import random, generator as g

class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.lbl = Label(self, text = "Wprowadź liczbę znaków które ma zawierać hasło")
		self.lbl.grid(row = 0,column = 0, columnspan = 2, sticky = W)

		self.pw_label = Label(self, text = "Liczba znaków: ")
		self.pw_label.grid(row = 1, column = 0, sticky = W)

		self.entry = Entry(self)
		self.entry.grid(row = 1, column = 1, sticky = W)

		self.submit_bttn = Button(self, text = "Generuj", command = self.reveal)
		self.submit_bttn.grid(row = 2, column = 0, sticky = W)

		self.text = Text(self, width = 35,height = 5,wrap = WORD)
		self.text.grid(row = 3, column = 0, columnspan = 2, sticky = W)

	def reveal(self):
		LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','&','*']
		new_password=''
		num_characters=int(self.entry.get())
		for i in range(num_characters):
			i = random.randrange(len(LETTERS)-1)
			new_password += LETTERS[i]
		self.text.delete(0.0, END)
		self.text.insert(0.0, new_password)

# main
root = Tk()
root.title("Długowieczność")
root.geometry("300x150")
app = Application(root)
root.mainloop()