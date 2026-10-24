import tkinter as tk
from pathlib import Path
import winsound as ws
import random
import webbrowser

window = tk.Tk()
window.title("gustav.ai")
window.geometry("410x300")
window.resizable(False, False)
window.iconbitmap(str(Path(__file__).parent / "gustav_icon.ico"))

label = tk.Label(window, text="gustav.ai", font=("Arial", 16), fg="red", bg="blue", padx=30, pady=1)
label.place(relx=0.7, rely=0.1, anchor="center")

image_path = Path(__file__).parent / "gustav_char.png"
gustav_image = tk.PhotoImage(file=str(image_path))
gustav_image = gustav_image.subsample(3, 3)

gustav_label = tk.Label(window, image=gustav_image)
gustav_label.place(relx=0.2, rely=0.3, anchor="center")

gpt_label = tk.Label(window, text="ChatGPT, suck it!!!", font=("Times New Roman Bold", 9), fg="Yellow", bg="Gray", padx=25, pady=1)
gpt_label.place(relx=0.2, rely=0.6, anchor="center")

gustav_answer = tk.Label(window, text="answer here ^_^", font=("Arial", 10))
gustav_answer.place(relx=0.7, rely=0.55, anchor="center")

gustav_sound = Path(__file__).parent / "gustav_sound.wav"
is_def = 0

def ask_gustav(_):
    global is_def
    if len(entry.get()) < 1 or is_def == 1:
        return
    is_def = 1
    entry.delete(0, tk.END)
    gustav_answer.config(text="loading....")

    window.after(random.randint(1, 3) * 1000, show_answer)

def show_answer():
    ws.PlaySound(
        str(gustav_sound),
        ws.SND_FILENAME | ws.SND_ASYNC
    )

    gustav_answer.config(text="gustav")

    global is_def
    is_def = 0

entry = tk.Entry(window)
entry.place(relx=0.5, rely=0.8, anchor="center", relwidth=0.8, height=20)
entry.bind("<Return>", ask_gustav)

support_label = tk.Label(window, text="support gustav.ai", font=("Arial", 8, "underline"), fg="blue", bg="cyan", padx=30, pady=1)
support_label.place(relx=0.2, rely=0.92, anchor="center", relwidth=0.3, height=15)
support_label.bind("<Button-1>", lambda event: webbrowser.open("https://www.donationalerts.com/r/vindency"))

window.mainloop()