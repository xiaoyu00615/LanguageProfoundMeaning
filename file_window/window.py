import tkinter as tk
from tkinter import ttk



import utils.utils_public as utils

textfile = utils.reading_file('LanguageText.txt')
# print(textfile,"window.py-9")
utils.regx_json(textfile)



# 新窗口
def create_window():
    # 创建主窗口
    root = tk.Tk()

    root.title("笔日记")

    # 设置窗口大小
    root.geometry('800x600')

    root.mainloop()




