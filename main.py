import tkinter
from PIL import ImageTk,Image

window = tkinter.Tk()
window.title("To-Do List")
window.geometry("500x600")
window.resizable(False, False)
window.configure(bg = "#DBE7C9")


del_btn = False
checkbutton_vars = []
checkbuttons = []

def delete_selected():      
    
    for i in reversed(range(0,len(checkbutton_vars))) :
        if checkbutton_vars[i].get() == 1:       
            checkbuttons[i].destroy()  
            del checkbutton_vars[i]
            del checkbuttons[i]  
    
def show_state():
    states = [var.get() for var in checkbutton_vars]
    print("Checkbutton states:", states)


# add new task
def add_item() :    
    text = entry.get(1.0,"end")
    text = " ".join(text.split())
    if not len(text)==0:
        index = len(checkbutton_vars)
        var = tkinter.IntVar()
        checkbutton_vars.append(var)
        checkbutton = tkinter.Checkbutton(
        list_frame,
        padx = 20,   
        pady = 10,   
        font=('Comic Sans MS',14,"italic"),
        anchor = "w",
        text = text,
        variable = var        
        )
        checkbutton.pack(fill = tkinter.X, pady = 10)
        checkbuttons.append(checkbutton)
        entry.delete(1.0, "end")
    else :
        pass   
    
# task frame
frame = tkinter.Frame(window, padx = 20, pady = 10, bg = "#789461")
frame.pack(pady = 15)

list_frame = tkinter.Frame(window, padx = 20, pady = 10, width = 50, height = 400, bg = "#789461")
list_frame.pack(pady = 15, padx = 20, fill = tkinter.BOTH)

entry = tkinter.Text(
    frame, 
    width = 30, 
    height = 1,    
    font = ("Comic Sans MS", 12),
    padx = 10,
    pady = 10 
    )
entry.focus_set()
entry.pack(side = tkinter.LEFT)

# add task buttton image
img = Image.open("./images/add.png")
resized_img = img.resize((30, 30), Image.BILINEAR)
add_img = ImageTk.PhotoImage(resized_img)

# add gap between entry and button widget
tkinter.Label(frame, padx = 10, bg = "#789461").pack(side = tkinter.LEFT)

tkinter.Button(
    frame,
    image = add_img,
    bg = "#DBE7C9", 
    padx = 20, 
    pady = 2, 
    relief = tkinter.FLAT  ,
    command = add_item
    ).pack(pady = 10, side = tkinter.LEFT)


delete_button = tkinter.Button(window, text="Delete", bg = "#333333", fg = "#FFFFFF", font = ("Georgia" ,20), padx = 8, pady = 5, command=delete_selected)
delete_button.pack(pady=5 ,side = tkinter.BOTTOM)



window.mainloop()





