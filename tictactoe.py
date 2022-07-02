from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("hello")
root.geometry()

def disable_all_buttons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)
     
    
#FOR CHECK
def checkifwon(X):
    global winner
    winner = False
    
    if btn1["text"]==X and btn2["text"]==X and btn3["text"]==X:
        btn1.config(bg="red")
        btn2.config(bg="red")
        btn3.config(bg="red")
        messagebox.showinfo(X+" you won")
        messagebox.Message("you won")
        disable_all_buttons()

    elif btn4["text"]==X and btn5["text"]==X and btn6["text"]==X:
        btn4.config(bg="red")
        btn5.config(bg="red")
        btn6.config(bg="red")
        messagebox.showinfo(X," you won")
        disable_all_buttons()
    elif btn7["text"]==X and btn8["text"]==X and btn9["text"]==X:
        btn7.config(bg="red")
        btn8.config(bg="red")
        btn9.config(bg="red")
        messagebox.showinfo(X," you won")
        disable_all_buttons()
    elif btn1["text"]==X and btn4["text"]==X and btn7["text"]==X:
        btn1.config(bg="red")
        btn4.config(bg="red")
        btn7.config(bg="red")
        messagebox.showinfo(X," you won")
        disable_all_buttons()
    elif btn2["text"]==X and btn5["text"]==X and btn8["text"]==X:
        btn2.config(bg="red")
        btn5.config(bg="red")
        btn8.config(bg="red")
        messagebox.showinfo(X," you won")
        disable_all_buttons()
    elif btn3["text"]==X and btn6["text"]==X and btn9["text"]==X:
        btn3.config(bg="red")
        btn6.config(bg="red")
        btn9.config(bg="red")
        messagebox.showinfo(X," you won")
        disable_all_buttons()
    elif btn1["text"]==X and btn5["text"]==X and btn9["text"]==X:
        btn1.config(bg="red")
        btn5.config(bg="red")
        btn9.config(bg="red")
        messagebox.showinfo(X," you won")
        disable_all_buttons() 
    elif btn3["text"]==X and btn5["text"]==X and btn7["text"]==X:
        btn3.config(bg="red")
        btn5.config(bg="red")
        btn7.config(bg="red")
        messagebox.showinfo(X," you won")
        disable_all_buttons()
    elif btn1["text"]!=" " and btn2["text"]!=" " and btn3["text"]!=" " and btn4["text"]!=" " and btn5["text"]!=" " and btn6["text"]!=" " and btn7["text"]!=" " and btn8["text"]!=" " and btn9["text"]!=" ":
        messagebox.showinfo('ERROR','nobody  WON')
#function
clicked=True
count=0
def b_click(b):
    global clicked,count
    
    if b["text"]==" "and clicked == True:
        b["text"]="X"
        clicked = False
        count+=1
        b["bg"]="blue"
        checkifwon('X')    
    elif b["text"]==" " and clicked == False:
        b["text"]="O"
        clicked = True
        count+=1
        b["bg"]="white"
        checkifwon('O')    
    else :
        messagebox.showerror("error")

n=2
i=2*n
j=3*n
btn1 = Button(root, text = ' ',font=("Helvetica",30),height=i,width=j, bd = '10',bg="green",command = lambda:b_click(btn1))      
btn2 = Button(root, text = ' ',font=("Helvetica",30),height=i,width=j ,bd = '10',bg="green",command = lambda:b_click(btn2))     
btn3 = Button(root, text = ' ',font=("Helvetica",30),height=i,width=j, bd = '10',bg="green",command = lambda:b_click(btn3))      
btn4 = Button(root, text = ' ',font=("Helvetica",30),height=i,width=j ,bd = '10',bg="green",command = lambda:b_click(btn4))     
btn5 = Button(root, text = ' ',font=("Helvetica",30),height=i,width=j, bd = '10',bg="green",command = lambda:b_click(btn5))      
btn6 = Button(root, text = ' ',font=("Helvetica",30),height=i,width=j ,bd = '10',bg="green",command = lambda:b_click(btn6))     
btn7 = Button(root, text = ' ',font=("Helvetica",30),height=i,width=j, bd = '10',bg="green",command = lambda:b_click(btn7))      
btn8 = Button(root, text = ' ',font=("Helvetica",30),height=i,width=j ,bd = '10',bg="green",command = lambda:b_click(btn8))     
btn9 = Button(root, text = ' ',font=("Helvetica",30),height=i,width=j, bd = '10',bg="green",command = lambda:b_click(btn9))
#btn10 = Button(root, text = 'restart ',height=i,width=j*3, bd = '5',command = lambda:restart())
         
    

  
           
btn1.grid(row=0,column=0)  
btn2.grid(row=0,column=1)   
btn3.grid(row=0,column=2)   
btn4.grid(row=1,column=0)   
btn5.grid(row=1,column=1)   
btn6.grid(row=1,column=2)   
btn7.grid(row=2,column=0)   
btn8.grid(row=2,column=1)   
btn9.grid(row=2,column=2) 
#btn10.grid(row=3,column=3)      
#btn10=(root, text =" hi", command =lambda )
                 

root.mainloop()