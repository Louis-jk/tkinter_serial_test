import tkinter
from tkinter.ttk import Combobox
from escpos.printer import Serial

# layout 
width = 35
currency = 'currency'
quantity = 'quantity'
product = 'item'
shot_name = 'DONGNAEBOOk'

# receipt
def receipt(purchases):
    total = 0

    items = [        
        shot_name.center(width),
        product.ljust(width),
        currency.rjust(width)
    ]

    for name, price, count in purchases:
        total += price*count

        all_price = str(round(price*count, 2))

        msg = f'{name}'.ljust(width-len(all_price), ' ')
        msg += all_price

        if type(count) is int and count >= 2:
            msg += f'\n     {count} kg x {price}'
        elif type(count) is float:
            msg += f'\n     {count} kg x {price}'

        items.append(msg)
    total = str(round(total, 2))
    items.append("\nTOTAL:".ljust(width-len(total)+1) + total)

    return '\n'.join(items)

ITEMS = [
    ('Bananas', 1.15, 3500),
    ('Bananas', 1.15, 3500),
    ('Bananas', 1.15, 3500),
    ('Bananas', 1.15, 3500),
    ('Bananas', 1.15, 3500),
]

text = receipt(ITEMS)
print(text)
        


# p = Serial(devfile='/dev/tty.Bluetooth-Incoming-Port',
#            baudrate=9600,
#            bytesize=8,
#            parity='N',
#            stopbits=1,
#            timeout=1.00,
#            dsrdtr=True)

# cp949
p = Serial('COM4', 9600)
p.charcode('CP932') 
p.text("동네북 테스트\n")
p.text(text)
p.qr("https://www.naver.com/")
p.cut()

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

# window.mainloop()