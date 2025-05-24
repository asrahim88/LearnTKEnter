from tkinter import *
window = Tk()
window.title("my apps")
window.geometry("400x500+500+250")
window.minsize(300, 300)
window.configure(bg="black")
Label(window, text="Welcome to tkinter bro!", font=("arial", 16)).pack(pady=50)
window.mainloop()