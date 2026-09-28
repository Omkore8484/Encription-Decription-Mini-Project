
from tkinter import *

import base64

root = Tk()

root.geometry("1400x6000")

root.title("Message Encryption and Decryption")

Tops = Frame(root, width=1980, relief=RAISED)
Tops.pack(side=TOP)

f1 = Frame(root, width=1080, relief=RAISED)
f1.pack(side=LEFT)



lblInfo = Label(Tops, font=('helvetica', 50, 'bold'),
                text="Encrypt Decrypt \n Message",
                fg="Black", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)



Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()


lblMsg = Label(f1, font=('arial', 18, 'bold'),
               text="\t\t\tType Message or Paste Code\n", bd=18, anchor="w")

lblMsg.grid(row=1, column=0)

txtMsg = Entry(f1, font=('arial', 18, 'bold'),
               textvariable=Msg, bd=10, insertwidth=4,
               bg="powder blue", justify='right')


txtMsg.grid(row=1, column=1)

lblkey = Label(f1, font=('arial', 18, 'bold'),
               text="\t\t\tEnter Secret Key", bd=18, anchor="w")

lblkey.grid(row=2, column=0)



txtkey = Entry(f1, font=('arial', 18, 'bold'),
               textvariable=key, bd=10, insertwidth=4,
               bg="powder blue", justify='right')

txtkey.grid(row=2, column=1)


lblmode = Label(f1, font=('arial', 18, 'bold'),
                text="\t\t\tMode\n\t\t\t(E to Encrypt, D to Decrypt)",
                bd=16, anchor="w")

lblmode.grid(row=3, column=0)

txtmode = Entry(f1, font=('arial', 18, 'bold'),
                textvariable=mode, bd=10, insertwidth=4,
                bg="powder blue", justify='right')

txtmode.grid(row=3, column=1)


lblResult = Label(f1, font=('arial', 18, 'bold'),
                  text="\tCode or Message", bd=16, anchor="w")

lblResult.grid(row=2, column=2)


txtResult = Entry(f1, font=('arial', 18, 'bold'),
                  textvariable=Result, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')

txtResult.grid(row=2, column=3)




def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
        print("enc:", enc) 
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()



def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
        print("dec:", dec)
    return "".join(dec)


def Results():
   

    msg = Msg.get()
    k = key.get()
    m = mode.get()

    if(m == 'E'):
        Result.set(encode(k, msg))
    elif(m == 'D'):
        Result.set(decode(k, msg))
    else:
        Result.set('Invalid Mode')



def qClose():
    root.destroy()



def Reset():

    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")



btnShow = Button(f1, padx=16, pady=8, bd=16, fg="black",
                  font=('arial', 16, 'bold'), width=10,
                  text="Show", bg="light green",
                  command=Results).grid(row=7, column=1)


btnReset = Button(f1, padx=16, pady=8, bd=16,
                  fg="black", font=('arial', 16, 'bold'),
                  width=10, text="Reset", bg="powder blue",
                  command=Reset).grid(row=7, column=2)


btnClose = Button(f1, padx=16, pady=8, bd=16,
                 fg="black", font=('arial', 16, 'bold'),
                 width=10, text="Close", bg="red",
                 command=qClose).grid(row=7, column=3)

root.mainloop()   