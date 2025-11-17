from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action

root = Tk()
root.title("AI Assistant")
root.geometry("550x750")   # Increased height so buttons do not get squeezed
root.resizable(False, False)
root.configure(bg="#356696")

# ask fun
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, 'User----->' + user_val+"\n")
    if bot_val != None:
        text.insert(END, "BOT<----"+str(bot_val)+"\n")
        if bot_val=="ok sir":
            root.destroy()

def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, 'User----->'+ send+"\n")
    if bot != None:
        text.insert(END, "BOT<----"+str(bot)+"\n")
        if bot=="ok sir":
            root.destroy()


def del_text():
    text.delete('1.0', "end")

# ---------- Frame ----------
frame = LabelFrame(root, padx=40, pady=20, borderwidth=3,
                   relief="raised", bg="#6F8FAF")
frame.grid(row=0, column=0, padx=20, pady=20)

# ---------- Title ----------
text_label = Label(frame, text="AI Assistant",
                   font=("Arial", 24, "bold"),
                   bg="#356696", fg="white")
text_label.grid(row=0, column=0, pady=10)

# ---------- Image ----------
image = Image.open("images.png")
image = image.resize((350, 300))
image = ImageTk.PhotoImage(image)

image_label = Label(frame, image=image, bg="#6F8FAF")
image_label.grid(row=1, column=0, pady=20)

# ---------- Text Box ----------
text = Text(root, font=("Arial", 12), bg="#356696", fg="white",
            width=48, height=5, borderwidth=3, relief="ridge")
text.grid(row=1, column=0, padx=20, pady=(0, 20))

# ---------- Entry Box ----------
entry = Entry(root, font=("Arial", 14),
              width=40, borderwidth=3, relief="ridge")
entry.grid(row=2, column=0, padx=20, pady=(0, 20))

# ---------- Button Frame ----------
btn_frame = Frame(root, bg="#356696")
btn_frame.grid(row=3, column=0, pady=20)

# Buttons with better visibility
Button1 = Button(btn_frame, text="ASK", bg="#4A90E2", fg="white",
                 font=("Arial", 12, "bold"),
                 padx=35, pady=15, borderwidth=3, relief=RAISED, command=ask)
Button1.grid(row=0, column=0, padx=15)

Button3 = Button(btn_frame, text="Delete", bg="#4A90E2", fg="white",
                 font=("Arial", 12, "bold"),
                 padx=35, pady=15, borderwidth=3, relief=RAISED, command=del_text)
Button3.grid(row=0, column=1, padx=15)

Button2 = Button(btn_frame, text="Send", bg="#4A90E2", fg="white",
                 font=("Arial", 12, "bold"),
                 padx=35, pady=15, borderwidth=3, relief=RAISED, command=send)
Button2.grid(row=0, column=2, padx=15)

root.mainloop()
