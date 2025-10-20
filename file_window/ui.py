import tkinter as tk
from file_window import config
from utils import public_fun


class UIManager:
    def __init__(self, title="我的窗口", width=config.ui_width, height=config.ui_height):
        # 1. 直接在UI管理器中创建主窗口
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.win_width = width
        self.win_height = height

        # 存储所有组件
        self.widgets = {}

    # 普通按钮
    def add_button_ordinary(self, name, text,command,pad_x = 0, x=0, y=0, width=10, height=1,center='',font_config=("微软雅黑",16,"bold")):
        """添加按钮"""

        btn = tk.Button(
            self.root,
            text=text,
            command=command,
            width=width,
            height=height,
            font=font_config,
            padx=pad_x,
        )

        if center == 'center':
            btn.place(relx=0.5, y=y, anchor="center")
        else:
            btn.place(x=x, y=y)

        self.widgets[name] = btn
        return btn

    # 标签文本
    def add_label_ordinary(self, name, text, x=0, y=0):
        """添加标签"""
        label = tk.Label(self.root, text=text)
        label.place(x=x, y=y)
        self.widgets[name] = label
        return label

    # 标题文本
    def add_label_title(self,name,text, x=0,y=0,font="微软雅黑",font_size=16,bold='bold',center = ''):
        pos_x = x
        label = tk.Label(self.root, text=text, font=(font, font_size, bold))


        if center == 'center':
            font_width = public_fun.get_text_width(text, (font, font_size, bold))

            # 可能动态调整
            pos_x = self.win_width / 2 - font_width / 2


        label.place(x=pos_x, y=y)
        self.widgets[name] = label


    def get(self, name):
        """获取组件"""
        return self.widgets.get(name)

    def run(self):
        """启动主窗口循环"""
        self.root.mainloop()


