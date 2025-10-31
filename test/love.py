import sys
import random
import threading
import tkinter as tk
import time

def show_window_tip():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window_width = 250
    window_height = 60
    x = random.randrange(0, width - window_width)
    y = random.randrange(0, height - window_height)

    window.title('温馨提示')
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    tips = [
        '多喝热水', '注意保暖', '保持微笑', '记得吃水果', '梦想成真'
    ]
    tip = random.choice(tips)
    bg_colors = [
        'red', 'blue', 'oldlace'
    ]
    bg = random.choice(bg_colors)
    tk.Label(
        window,
        text=tip,
        bg=bg,
        font=('微软雅黑', 16),
        width=30,
        height=3
    ).pack()
    window.attributes('-topmost', True)
    
    def on_space(event):
        window.destroy()
    window.bind('<space>', on_space)
    window.mainloop()

threads = []
for i in range(30):
    t = threading.Thread(target=show_window_tip)
    threads.append(t)
    time.sleep(0.005)
    threads[i].start()