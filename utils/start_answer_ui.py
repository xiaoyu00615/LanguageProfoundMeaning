import tkinter as tk

from utils import public_fun
from utils.public_fun import write_json, reading_json


class StartAnswerUI:
    def __init__(self, parent,arr_json):
        self.window = parent
        self.widgets = {}
        self.index = 0
        self.arr_json = arr_json

        # 1. 创建按钮容器（Frame）
        self.button_frame = tk.Frame(self.window)
        # 2. 容器放在窗口底部，且自身居中（anchor=CENTER）
        self.button_frame.pack(side=tk.BOTTOM, pady=10, anchor=tk.CENTER)

    def add_label_ordinary_text(self, name, text='填写文本', x=0, y=0, font=('微软雅黑', 16)):
        answer = None
        if type(text) ==  dict:
            answer = text['regx_topic'][self.index]
        else:
            answer = text
        label_text = tk.Label(self.window, text=answer, font=font,wraplength=600)
        label_text.pack(padx=x, pady=y)
        self.widgets[name] = label_text
        return label_text

    def add_input(self, name, x, y, width=10, font=('微软雅黑', 14)):
        entry = tk.Entry(self.window, width=width, font=font)
        entry.pack(padx=x,pady=y)
        self.widgets[name] = entry
        return entry

    def add_text(self,name,text='文本',x=0, y=0,width=50,height=10):

        text_widget = tk.Text(
            self.window,
            width=50,  # 宽度（字符数）
            height=10,  # 高度（行数）
            wrap=tk.WORD,  # 按单词换行

        )
        text_widget.insert("1.0", text[self.index]["answer"])  # "1.0" 表示从开头插
        text_widget.pack(padx=x, pady=y)
        self.widgets[name] = text_widget
        return text_widget

    def add_button(self, name, text, command,side=tk.LEFT ,x=20, y=8, width=10, height=1,
                            font_config=("微软雅黑", 18, "bold")):


        btn = tk.Button(
            self.button_frame,
            text=text,
            command=command,
            width=width,
            height=height,
            font=font_config,
        )
        btn.pack(side=side,padx=x,pady=(10,20),fill=tk.X)


        self.widgets[name] = btn
        return btn

    def submit_text(self,demo):
        # 获取 Text 控件中的所有文本
        # 1.0 表示从第1行第0列开始，tk.END 表示到文本末尾
        content = self.widgets[demo].get("1.0", tk.END)

        # 去除末尾可能的空行（因为 Text 控件默认会在最后加一个换行符）
        content = content.strip()

        config = reading_json('./config/config_path.json')

        write_json(config["answer_json_file"],self.index,content)
        print(content)


    def next_topic(self,fun):
        self.submit_text('answer')
        self.index += 1
        print("下一题",self.index,len(self.arr_json))
        if self.index >= len(self.arr_json):
            self.index = len(self.arr_json)-1
            return

        self.widgets['topic'].destroy()
        self.widgets['answer'].destroy()
        fun()


    def up_topic(self,fun):
        self.index -= 1
        if self.index < 0:
            self.index = 0
            return

        self.widgets['topic'].destroy()
        self.widgets['answer'].destroy()
        fun()

    def back_home(self):
        public_fun.del_demo(self.widgets)
        self.button_frame.destroy()
        print("删除刷新")