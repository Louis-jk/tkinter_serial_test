import tkinter
from tkinter.ttk import Combobox

window = tkinter.Tk()

window.minsize(400,400)
window.title('동네북')
window.geometry("1200x800+100+100")

label = tkinter.Label(window, text="동네북")
label.pack()

message = tkinter.Message(window, text="메세지테스트", width=100, relief="solid")
message.pack()

values=[str(i)+"번" for i in range(1, 101)]
baudRateValues=[110, 300, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]
combobox = Combobox(window, height=15, values=baudRateValues)
combobox.pack()

window.mainloop()