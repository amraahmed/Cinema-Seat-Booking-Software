import tkinter as tk
import tkinter.ttk
import database 
screens = ["Screen 1",'Screen 2',"Screen 3",'Screen 4',"Screen 5",'Screen 6']
times = ['10:00',"13:00","16:00","19:00","21:00","00:00"]
seatList = []
seatSelected = []
class Application(tk.Tk):
    
    def __init__(self):
        super().__init__()
        global db
        db = database.Database()
        self.generes = db.get_generes()
        global movies
        movies = db.get_movies()
        self.title('Movie Booking')
        self.createWidgets()

    def update_movies(self,event=None):
        self.comboxlaue = self.genreCombo.get()
        if self.comboxlaue != '':
           movies = db.get_movie(self.comboxlaue)
           self.movieCombo.config(values=movies)
        else:
            movies = db.get_movie(self.comboxlaue) 

        
    
    def createWidgets(self):
        heading_Label = tk.Label(self,text='Cinema Seat Booking',font='Aries 12 bold')
        heading_Label.grid(row=0,column=0,columnspan=5,padx=10,pady=10,sticky='w')
        tkinter.ttk.Separator(self,orient='horizontal').grid(row=1,column=0,columnspan=5,sticky='w')
        day = tk.Frame(self)
        tk.Label(day,text='______________').pack()
        tk.Label(day,text='Today',font='Aries 10 underline').pack()
        tk.Label(day,text='',font='Aries 10 underline').pack()
        day.grid(row=2,column=0,padx=10)
        tk.Label(self,text='Genre: ').grid(row=2,column=1,padx=10)
        self.genreCombo = tkinter.ttk.Combobox(self,width=15,values=self.generes,state='readonly')
        self.genreCombo.set("Select Genre")
        self.genreCombo.bind('<<ComboboxSelected>>',self.update_movies)
        self.genreCombo.grid(row=2,column=2)
        tk.Label(self,text='Movies: ').grid(row=2,column=3,padx=(10,0))
        self.movieCombo = tkinter.ttk.Combobox(self,width=15,values=movies,state='readonly')
        self.movieCombo.set("Select Movie")
        self.movieCombo.bind('<<ComboboxSelected>>',self.createTimeButtons)
        self.movieCombo.grid(row=2,column=4)
        
    def createTimeButtons(self,ev=None):
        tk.Label(self,text='Select a time',font='Aries 11 bold').grid(
            row=5,column=0,columnspan=2,pady=5)
        Time = tk.Frame(self).grid(row=5,column=0,columnspan=5)
        for i in range(len(times)):
            tk.Button(Time,text=times[i],command=self.select_seat).grid(row=4+i//7,column=i%7)
    def select_seat(self):
        seatswindow = tk.Toplevel()
        seatswindow.title("Select Seats")
        checkoutHeading = tk.Label(seatswindow,text='Seat Selection',font='Aries 12')
        checkoutHeading.grid(row=0,column=0,columnspan=5,padx=10,pady=(10,0),sticky="w")
        infer = tk.Frame(seatswindow)
        infer.grid(row=1,column=0)
        tk.Label(infer,text='Blue = Seclected',fg='blue').grid(row=0,column=0,padx=10)
        tk.Label(infer,text='Red = Booked',fg='red').grid(row=0,column=1,padx=10)
        tk.Label(infer,text='Green = Avilable',fg='green').grid(row=0,column=2,padx=10)
        tkinter.ttk.Separator(seatswindow,orient='horizontal') .grid(row=3,column=0,columnspan=5,pady=(0,5),sticky='ew')
        w = tk.Canvas(seatswindow,width=500,height=15)
        w.create_rectangle(10,0,490,10,fill='black')
        w.grid(row=3,column=0)
        seats = tk.Frame(seatswindow).grid(row=5,column=0)
        seatList.clear()
        seatSelected.clear()
        for i in range(4):
            temp = []
            for j in range(15):
                button = tk.Button(seatswindow,bd=2,bg='Green',activebackground='forestGreen',
                                command=lambda x=i, y=j: self.selected(x,y))
                temp.append(button)
                button.grid(row=i+1,column=j+1,padx=5,pady=5)
            seatList.append(temp)
        tk.Button(seatswindow,text='Book Seats',bg='black',fg='white',command=self.bookseat).grid(row=6,column=0,padx=10)

                
    def selected(self,i,j):
        if seatList[i][j]['bg'] == 'blue':
            seatList[i][j]['bg'] == 'green'
            seatList[i][j]['activebackground'] = 'forestgreen'
            seatSelected.remove((i,j))
            return 
        seatList[i][j]['bg'] = 'blue'
        seatList[i][j]['activebackground'] = 'blue'
        seatSelected.append((i,j))
        
    def bookseat(self):
        for i in seatSelected:
            seatSelected[i[0]][i[1]]['bg'] = 'brown'
            seatSelected[i[0]][i[1]]['activebackground'] = 'brown'
            seatSelected[i[0]][i[1]]['relief'] = 'sunken'
            
            
    
app = Application()
app.mainloop()