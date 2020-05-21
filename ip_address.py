import socket
from tkinter import *

root = Tk()
root.title("Ip адрес компьютера")
root.geometry("300x100")

ipaddress=socket.gethostbyname(socket.gethostname())
print(ipaddress)


label1 = Label(text=ipaddress,font="Arial 18")
label1.pack()

root.mainloop()