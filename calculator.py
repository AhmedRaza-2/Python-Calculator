from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(scvalue.get())
        except Exception as e:
            value = "error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("350x550")
root.title("AR Calculator")
root.configure(bg="black")


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="ROBOTO 30 bold", bd=10, relief=FLAT, bg="black", fg="white", justify='right')
screen.pack(fill=X, ipadx=8, ipady=10, padx=10, pady=20)

button_specs = [
    ['C', '±', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=']
]

def create_button(f, text, bg, fg):
    b = Button(f, text=text, padx=20, pady=10, font="Montserrat 18 bold", bg=bg, fg=fg, relief=FLAT)
    b.pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
    b.bind("<Button-1>", click)
    return b

colors = {
    'bg': 'black',
    'fg': 'white',
    'button_bg': '#333333',
    'button_fg': 'white',
    'operator_bg': '#FF9500',
    'operator_fg': 'white',
    'special_bg': '#A6A6A6',
    'special_fg': 'black'
}

for row in button_specs:
    f = Frame(root, bg=colors['bg'])
    for btn_text in row:
        if btn_text in ['C', '±', '%']:
            create_button(f, btn_text, colors['special_bg'], colors['special_fg'])
        elif btn_text in ['/', '*', '-', '+', '=']:
            create_button(f, btn_text, colors['operator_bg'], colors['operator_fg'])
        else:
            create_button(f, btn_text, colors['button_bg'], colors['button_fg'])
    f.pack(expand=True, fill=BOTH)

root.mainloop()
