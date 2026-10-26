import customtkinter as ctk
from tkinter import colorchooser
import pyttsx3 as pe

# اكتب هنا رقم الصوت اللي عايزه (شوف الأرقام في الشاشة السودا لما تشغّل البرنامج)
# لو سبته None هيدوّر لوحده على صوت ست (زي Zira)
VOICE_INDEX = None

# بيطبع الأصوات المتاحة على جهازك مرة واحدة أول ما البرنامج يشتغل
for i, v in enumerate(pe.init().getProperty("voices")):
    print("voice", i, v.name)


def speak(text):
    engine = pe.init()
    engine.setProperty("rate", 150)
    voices = engine.getProperty("voices")

    index = VOICE_INDEX
    if index is None:
        index = 0
        for i, v in enumerate(voices):
            if "zira" in v.name.lower() or "female" in v.name.lower():
                index = i
                break

    # الصوت لازم يتحدد قبل say
    engine.setProperty("voice", voices[index].id)
    engine.say(text)
    engine.runAndWait()


root = ctk.CTk()
root.title("mobily")
root.geometry("500x350")

color = colorchooser.askcolor()[1]
if color:
    root.configure(fg_color=color)

label = ctk.CTkLabel(root, text="Welcome to mobily app", font=("Arial", 20), text_color="black")
label.pack()

checkbox = ctk.CTkCheckBox(root, text="choose", text_color="black",
                           command=lambda: speak("please press one or two"))
checkbox.pack(pady=30)

combo1 = ctk.CTkComboBox(root, values=("1", "2"), width=200, height=40,
                         command=speak)
combo1.pack(pady=10)

root.after(500, lambda: speak("Welcome to mobily app"))
root.mainloop()