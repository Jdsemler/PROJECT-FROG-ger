from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=900,height=500, background='white')
#background panels
Grass1 = drawpad.create_rectangle (0,0,150,500, fill= 'chartreuse')
Road1 = drawpad.create_rectangle (150,0,250,500, fill= 'grey')
Grass2 = drawpad.create_rectangle (250,0,350,500, fill= 'chartreuse')
Road2 = drawpad.create_rectangle (350,0,450,500, fill= 'grey')
Grass3 = drawpad.create_rectangle (450,0,550,500, fill= 'chartreuse')
Road4 = drawpad.create_rectangle (550,0,650,500, fill= 'grey')

Road5 = drawpad.create_rectangle (550,0,750,500, fill= 'grey')
pond = drawpad.create_rectangle (750,0,900,500, fill= 'blue')

#character and enemies
oval = drawpad.create_oval(40,40,80,80, fill='green')
#truck1 = drawpad.create_rectangle(40, 40, 80, 80, fill='red')
#truck2 = drawpad.create_rectangle(20,40,20,40, fill='blue')
#truck3 = drawpad.create_rectangle
#truck4 = drawpad.create_rectangle
class MyApp:
	def __init__(self, parent):
                # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
 		self.button1.configure(text="Left", background= "green")
 		self.button1.grid(row=0,column=1)
		self.button1.bind("<Button-1>", self.button1Click)
 	        # Add a second button!
						
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="up", background= "yellow")
		self.button2.grid(row=0,column=2)		
		self.button2.bind("<Button-1>", self.button2Click)
			
		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="down", background= "red")
		self.button3.grid(row=0,column=3)	
		self.button3.bind("<Button-1>", self.button3Click)
		
		self.button4 = Button(self.myContainer1)
		self.button4.configure(text="right", background= "light blue")
		self.button4.grid(row=0,column=4)		
		self.button4.bind("<Button-1>", self.button4Click)
 						
 		  
 		# This creates the drawpad - no need to change this 
 		drawpad.pack()		

	def button1Click(self, event):   
		# Make the oval move to the left!
                # "global" makes sure that we can access our oval and our drawpad
		drawpad.move(oval,-20,0)
		global oval
		global drawpad
			
 	def button2Click(self, event):   
 		# Make the oval move up!
                 # "global" makes sure that we can access our oval and our drawpad
		drawpad.move(oval,0,-20)
 		global oval
 		global drawpad
 		
        def button3Click(self, event):   
 		# Make the oval move down!
                 # "global" makes sure that we can access our oval and our drawpad
		drawpad.move(oval,0,20)
 		global oval
 		global drawpad
 		
 	def button4Click(self, event):   
 		# Make the oval move to the right!
                 # "global" makes sure that we can access our oval and our drawpad
		drawpad.move(oval,20,0)
 		global oval
 		global drawpad
 		
        	

        
myapp = MyApp(root)
root.mainloop()