from tkinter import *
from tkinter import ttk,colorchooser,messagebox
from tkinter.filedialog import asksaveasfilename
from PIL import ImageGrab


class paint(Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Paint")
        self.geometry("800x520")
        self.configure(background="white")
        self.resizable(0,0)
        
        
        #self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.eraser_col="white"
        self.penwidth = 5
        self.drawWidgets()
        self.canvas.bind('<B1-Motion>',self.paints)#drwaing the line 
        
     
    def paints(self,event):
        x1,y1 =(event.x-2),(event.y-2)
        x2,y2 =(event.x+2),(event.y+2)
        
        self.canvas.create_oval(x1,y1,x2,y2,fill=self.color_fg,outline=self.color_fg,width=self.pen_size.get())
        
        
    
    def change_fg(self):  #changing the pen color
        self.color_fg=colorchooser.askcolor(color=self.color_fg)[1]

    def change_bg(self):  #changing the background color canvas
        self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
        self.canvas['bg'] = self.color_bg
        self.eraser_col= self.color_bg
        
    
    
    
        
    def drawWidgets (self):
        menubar= Menu(self,font=("Helvetica",14),)
        filemenu = Menu(menubar,tearoff=1,font=("Helvetica",14),bd=2,activebackground="black")
        filemenu.add_command(label="new",command = self.new)
        filemenu.add_command(label="clear",command =self.clear)
        filemenu.add_separator()
        filemenu.add_command(label="Quit",command = self.destroy)
        menubar.add_cascade(label="File",font=("Helvetica",14),menu=filemenu)
        self.config(menu=menubar)
        
        container=ttk.Frame(self)
        container.grid(sticky="EW")
        
        f_options=ttk.Frame(container)
        f_options.grid(row=0,column=0,sticky="EW")

        
        
        f_canvas=ttk.Frame(container)
        f_canvas.grid(row=0,column=1,sticky="EW")

        
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=8)
        
        colour_frame=LabelFrame(f_options,text="colour",font=("arial",15,"bold"),bd=5,relief=RIDGE,bg='white')
        colour_frame.grid(row=0,column=0,sticky="EWNS")
        
        
        col_in_frame=Frame(colour_frame,bg='white')
        col_in_frame.grid(row=0,column=0,sticky="EWNS")        
        edit_button=Button(colour_frame,text="Edit Color",command=self.change_fg,width=3,bd=2,relief=RIDGE).grid(padx=2,pady=2,row=1,column=0,sticky="EWNS")
        colors=["#4285F4","#DB4437","#F4B400","#0F9D58","#1D05F7","#FF9D00","#00FF2A","#E600FF","#FFFFFF","#000000","#FF03B7","#CCCFCE"]
        i=j=0
        
        for color in colors:
            Button(col_in_frame,bg=color,command = lambda col=color:self.select_color(col),width=3,bd=2,relief=RIDGE).grid(padx=2,pady=2,row=i,column=j)
            i +=1
            if i==6:
                i=0
                j=1
        
        eraser_button=Button(f_options,text="Eraser",command=self.erase,bg="black",fg="white",width=3,bd=2,relief=RIDGE)
        eraser_button.grid(padx=2,pady=2,row=1,column=0,sticky="EWNS")
        
        bg_button=Button(f_options,text="background",command=self.change_bg,bg="black",fg="white",width=3,bd=2,relief=RIDGE)
        bg_button.grid(padx=2,pady=2,row=2,column=0,sticky="EWNS")
        
        
        self.pen_size_frame=LabelFrame(f_options,text="size",font=("arial",15,"bold"),fg="white",bd=5,relief=RIDGE,bg='black')
        self.pen_size_frame.grid(row=3,column=0,sticky="EWNS")
        
        self.pen_size = Scale(self.pen_size_frame,orient=VERTICAL,from_=5,to=50,length=170)
        self.pen_size.set(1)
        self.pen_size.grid(row=0,column=1,pady=10,padx=15,sticky="EWNS")
        
        #creating of canvas
        
        self.canvas=Canvas(f_canvas,height=500,width=700,bg=self.color_bg,)
        self.canvas.grid(sticky="EWNS")
        
    def select_color(self,col):
        self.color_fg=col
        
    def clear(self):
        self.canvas.delete(ALL)
        
    def erase(self):
        self.color_fg=self.eraser_col
    
    def new(self):
        self.clear()
        self.canvas['bg']="white"
        
        
if __name__=="__main__":
    root = paint()
    
    root.mainloop()