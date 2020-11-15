# -*- coding: utf-8 -*-
import queue
import threading
import os
from tkinter import *
from message import decode_msg_size


stream = queue.Queue()
speechQ = queue.Queue()
count = 0


IPC_FIFO_NAME = 'ipc'
fifo = os.open(IPC_FIFO_NAME, os.O_RDONLY)


def get_message():
    """Get a message from the named pipe."""
    msg_size_bytes = os.read(fifo, 4)
    while len(msg_size_bytes) < 4:
        msg_size_bytes += os.read(fifo, 4 - len(msg_size_bytes))
    msg_size = decode_msg_size(msg_size_bytes)
    msg_content = os.read(fifo, msg_size)
    while len(msg_content) < msg_size:
        msg_content += os.read(fifo, 4 - len(msg_content))
    return msg_content.decode("utf8").split('\t')


def read_thd():
    while True:
        msg = get_message()
        print(msg)


def main():
    root = Tk()
    root.geometry("1500x500")
    root.title('Result')

    lbl = Label(root, text="")
    lbl.config()
    lbl.config(width=50)
    lbl.config(font=("Courier", 44))
    lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

    ths = list()
    ths.append(threading.Thread(target=read_thd))
    for th in ths:
        th.daemon = True
        th.start()

    root.mainloop()


if __name__ == '__main__':
    main()
