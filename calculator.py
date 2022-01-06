# importing Tkinter and math 
from tkinter import *
import math

# calc class 
class calc: 
  
   
    def getandreplace(self): 
  
        """replace x with * and ÷ with /"""
        self.expression = self.ex.get() 
        self.newtext=self.expression.replace('/','/') 
        self.newtext=self.newtext.replace('x','*') 
  
  
    def equals(self): 
        """when the equal button is pressed"""
        self.getandreplace() 
        try: 
            # evaluate the expression using the eval function 
            self.value= eval(self.newtext)  
        except SyntaxError or NameError: 
            self.ex.delete(0,END) 
            self.ex.insert(0,'Invalid Input!') 
        else: 
            self.ex.delete(0,END) 
            self.ex.insert(0,self.value) 
            
   
  
    def squareroot(self): 
        """squareroot method"""
        self.getandreplace() 
        try: 
            # evaluate the expression using the eval function 
            self.value= eval(self.newtext)  
        except SyntaxError or NameError: 
            self.ex.delete(0,END) 
            self.ex.insert(0,'Invalid Input!') 
        else: 
            self.sqrtval=math.sqrt(self.value) 
            self.ex.delete(0,END) 
            self.ex.insert(0,self.sqrtval) 
  
    def square(self): 
        """square method"""
        self.getandreplace() 
        try: 
            #evaluate the expression using the eval function 
            self.value= eval(self.newtext)  
        except SyntaxError or NameError: 
            self.ex.delete(0,END) 
            self.ex.insert(0,'Invalid Input!') 
        else: 
            self.sqval=math.pow(self.value,2) 
            self.ex.delete(0,END) 
            self.ex.insert(0,self.sqval) 
            
    def log(self):
           self.getandreplace()         
           self.logval=math.log(float(self.obj))
           self.ex.delete(0,END) 
           self.ex.insert(0,self.logval) 
  
    def clearall(self): 
            """when clear button is pressed,clears the text input area"""
            self.ex.delete(0,END) 
  
    def clear1(self): 
            self.txt=self.ex.get()[:-1] 
            self.ex.delete(0,END) 
            self.ex.insert(0,self.txt) 
  
    def action(self,argi): 
            """pressed button's value is inserted into the end of the text area"""
            self.ex.insert(END,argi) 
            
    def tanh(self):
        self.tanhval= math.tanh(math.radians(float(self.value)))
        self.ex.delete(0,END) 
        self.ex.insert(0,self.tanhval) 

    def tan(self):
        self.tanval=math.tan(math.radians(float(self.value)))
        self.ex.delete(0,END) 
        self.ex.insert(0,self.tanval) 
        
        
    def sinh(self):
       
        self.sinhval= math.sinh(math.radians(float(self.value)))
        self.ex.delete(0,END) 
        self.ex.insert(0,self.sinhval) 
        
    def sin(self):
        self.getandreplace()  
        self.sinval= math.sin(math.radians(float(self.ex)))
        self.ex.delete(0,END) 
        self.ex.insert(0,self.sinval) 
        
    def cos(self):
        self.cosval= math.cos(math.radians(float(self.value)))
        self.ex.delete(0,END) 
        self.ex.insert(0,self.cosval) 
        
    def cosh(self):
        self.coshval= math.cosh(math.radians(float(self.value)))
        self.ex.delete(0,END) 
        self.ex.insert(0,self.coshval) 
        
    
        
    def pi(self):
        self.getandreplace()        
        self.pival=math.pi
        self.ex.delete(0,END) 
        self.ex.insert(0,self.pival)
        
        
    def e(self):
        self.getandreplace()        
        self.exval=math.e
        self.ex.delete(0,END) 
        self.ex.insert(0,self.exval)
        
   
    def __init__(self,master): 
            """Constructor method"""
            master.title('Simple Calulator') 
            master.configure(background="green") 
            master.geometry("545x280") 
           
            self.ex = Entry(master) 
            self.ex.grid(row=0,column=0,columnspan=6,pady=3) 
            self.ex.focus_set() #Sets focus on the input text area 
  
            # Generating Buttons 
            Button(master,text="=",fg="blue", 
                   bg="orange", width=11, height=3,command=lambda:self.equals()).grid( 
                                     row=4, column=5,columnspan=1) 
            
            Button(master,text='AC',width=5,height=3, 
                          fg="red", bg="light green", 
             command=lambda:self.clearall()).grid(row=1, column=4) 
  
            Button(master,text='C',width=5,height=3, 
                   fg="red",bg="light green", 
                   command=lambda:self.clear1()).grid(row=1, column=5) 
  
            Button(master,text="+",width=5,height=3, 
                   fg="blue",bg="orange", 
                   command=lambda:self.action('+')).grid(row=4, column=3) 
  
            Button(master,text="x",width=5,height=3, 
                    fg="blue",bg="orange", 
                    command=lambda:self.action('x')).grid(row=2, column=3) 
  
            Button(master,text="-",width=5,height=3, 
                    fg="red",bg="light green", 
                    command=lambda:self.action('-')).grid(row=3, column=3) 
  
            Button(master,text="÷",width=5,height=3, 
                   fg="blue",bg="orange", 
                   command=lambda:self.action('/')).grid(row=1, column=3) 
  
            Button(master,text="e",width=5,height=3, 
                   fg="red",bg="light green", 
                   command=lambda:self.e()).grid(row=4, column=2) 
  
            Button(master,text="7",width=5,height=3, 
                   fg="blue",bg="orange", 
                   command=lambda:self.action('7')).grid(row=1, column=0) 
  
            Button(master,text="8",width=5,height=3, 
                   fg="red",bg="light green", 
                   command=lambda:self.action(8)).grid(row=1, column=1) 
  
            Button(master,text="9",width=5,height=3, 
                   fg="blue",bg="orange", 
                   command=lambda:self.action(9)).grid(row=1, column=2) 
  
            Button(master,text="4",width=5,height=3, 
                   fg="red",bg="light green", 
                   command=lambda:self.action(4)).grid(row=2, column=0) 
  
            Button(master,text="5",width=5,height=3, 
                   fg="blue",bg="orange", 
                   command=lambda:self.action(5)).grid(row=2, column=1) 
  
            Button(master,text="6",width=5,height=3, 
                   fg="green",bg="blue", 
                   command=lambda:self.action(6)).grid(row=2, column=2) 
  
            Button(master,text="1",width=5,height=3, 
                   fg="red",bg="light green", 
                   command=lambda:self.action(1)).grid(row=3, column=0) 
  
            Button(master,text="2",width=5,height=3, 
                   fg="blue",bg="orange", 
                   command=lambda:self.action(2)).grid(row=3, column=1) 
  
            Button(master,text="3",width=5,height=3, 
                   fg="green",bg="blue", 
                   command=lambda:self.action(3)).grid(row=3, column=2) 
  
            Button(master,text="0",width=5,height=3, 
                   fg="green",bg="blue", 
                   command=lambda:self.action(0)).grid(row=4, column=0) 
  
            Button(master,text=".",width=5,height=3, 
                   fg="red",bg="light green", 
                   command=lambda:self.action('.')).grid(row=4, column=1) 
  
            Button(master,text="(",width=5,height=3, 
                   fg="green",bg="blue", 
                   command=lambda:self.action('(')).grid(row=2, column=4) 
  
            Button(master,text=")",width=5,height=3, 
                   fg="blue",bg="orange", 
                   command=lambda:self.action(')')).grid(row=2, column=5) 
  
            Button(master,text="2root",width=5,height=3, 
                   fg="red",bg="light green", 
                   command=lambda:self.squareroot()).grid(row=3, column=4) 
  
            Button(master,text="x²",width=5,height=3, 
                   fg="green",bg="blue", 
                   command=lambda:self.square()).grid(row=3, column=5) 
            
  
            Button(master,text="pi",width=5,height=3, 
                   fg="blue",bg="light green", 
                   command=lambda:self.pi()).grid(row=4, column=4) 
    
# Driver Code 
root = Tk() 
  
obj=calc(root) # object instantiated 
  
root.mainloop()