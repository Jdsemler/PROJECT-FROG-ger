from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=900,height=500, background='white')
oval = drawpad.create_oval(40,40,80,80, fill='green')


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

truck = drawpad.create_rectangle(170,0,200,50, fill='blue')
truck2 = drawpad.create_rectangle(370,0,400,50, fill='red')
truck3 = drawpad.create_rectangle(570,0,600,50, fill= 'black')
truck4 = drawpad.create_rectangle(700,0,730,50, fill= 'green')

dir0 = 5


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

 		self.animate2()
 						
        #truck movement
        def animate2(self):
            global dir0
            global truck, truck2, truck3, truck4
            # Get the x and y co-ordinates of the circle
            x1, y1, x2, y2 = drawpad.coords(truck)
            if y2 > drawpad.winfo_height(): 
                dir0 = -6
            elif y1 < 0:
                dir0 = 6
            #Move our trucks by the value of direction
            drawpad.move(truck,0,dir0)
            drawpad.move(truck2,0,dir0)
            drawpad.move(truck3,0,dir0)
            drawpad.move(truck4,0,dir0)
            # Wait for 1 millisecond, then recursively call our animate function
            self.collisionDetect()
            drawpad.after(5, self.animate2)
            

 	
 	#function for reseting
 	def resetplayer(self):
            x1,y1,x2,y2 = drawpad.coords(oval)
 	    movex = 40-x1
 	    movey = 80-y1
 	    drawpad.move(oval,movex,movey)
 	    


 	def collisionDetect(self):
            #Reset if hit trucks (coords)
            x1,y1,x2,y2 = drawpad.coords(oval)
            truckx1,trucky1,truckx2,trucky2 = drawpad.coords(truck)
   	    truck2x1,truck2y1,truck2x2,truck2y2 = drawpad.coords(truck2)												
            truck3x1,truck3y1,truck3x2,truck3y2 = drawpad.coords(truck3)
   	    truck4x1,truck4y1,truck4x2,truck4y2 = drawpad.coords(truck4)
   	    pondx1,pondy1,pondx2,pondy2 = drawpad.coords(pond) 
   	     	#truck reset
            if x2>truckx1 and x2<truckx2 and y1>trucky1 and y2<trucky2:
                print "truck1"
           	self.resetplayer()
            if x2>truck2x1 and x2<truck2x2 and y1>truck2y1 and y2<truck2y2:
           	self.resetplayer()
            if x2>truck3x1 and x2<truck3x2 and y1>truck3y1 and y2<truck3y2:
           	self.resetplayer()
            if x2>truck4x1 and x2<truck4x2 and y1>truck4y1 and y2<truck4y2:
           	self.resetplayer()
            if x2>pondx1 and x2<pondx2 and y1>pondy1 and y2<pondy2:
                self.resetplayer()
   	    	     		  	  	     		  	  

	def button1Click(self, event):   
		# Make the oval move to the left!
                # "global" makes sure that we can access our oval and our drawpad
		
		global oval
		global drawpad
		x1,y1,x2,y2 = drawpad.coords(oval)
		if x1 > 0:
		    drawpad.move(oval,-20,0)
			
 	def button2Click(self, event):   
 		# Make the oval move up!
                 # "global" makes sure that we can access our oval and our drawpad
		global oval
 		global drawpad
 		x1,y1,x2,y2 = drawpad.coords(oval)
		if y1 > 0:
		    drawpad.move(oval,0,-20)
 		
        def button3Click(self, event):   
 		# Make the oval move down!
                 # "global" makes sure that we can access our oval and our drawpad
		global oval
 		global drawpad
 		x1,y1,x2,y2 = drawpad.coords(oval)
		if y2 < 500:
 		     drawpad.move(oval,0,20)
 		
 	def button4Click(self, event):   
 		# Make the oval move to the right!
                 # "global" makes sure that we can access our oval and our drawpad
		global oval
 		global drawpad
 		x1,y1,x2,y2 = drawpad.coords(oval)
		if x1 < 900:
 		     drawpad.move(oval,20,0)
 		
 		
        	

        
myapp = MyApp(root)
root.mainloop()