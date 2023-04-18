from tkinter import *
import cv2
import pyzbar.pyzbar as pyzbar


def scanQR():
    i = 0
    vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while i < 2:
        _, f = vid.read()
        decoded = pyzbar.decode(f)
        for obj in decoded:
            lbl.config(text=f'{obj.data}')
            i += 1
        cv2.imshow('QRCode', f)
        cv2.waitKey(1)
        cv2.destroyAllWindows()


ws = Tk()
ws.title('PythonGuides')
ws.geometry('300x200')

Button(
    ws,
    text='Scan QRCode',
    command=scanQR
).pack(pady=10)

lbl = Label(ws, font=('times', 20))
lbl.pack()

ws.mainloop()
