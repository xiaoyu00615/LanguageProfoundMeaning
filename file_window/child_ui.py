import tkinter as tk

from file_window import config

class ChildWindow:
    def __init__(self,
                 title='子窗口',
                 parent=tk.Tk,
                 width=config.child_setting_ui_width,
                 height=config.child_setting_ui_height,
                 resizable: tuple[bool, bool] = (True, True),
                 is_modal: bool = False):

        self.title = title,
        self.width = width,
        self.height = height
        self.size = f"{width}x{height}"
        self.resizable = resizable
        self.is_modal = is_modal
        self.parent = parent
        """
           初始化子窗口

           参数:
               parent: 父窗口实例
               title: 子窗口标题
               size: 子窗口大小，格式为"宽x高"
               resizable: 是否允许调整宽和高
               is_modal: 是否为模态窗口（打开后禁止操作父窗口）
           """


        self.window = tk.Toplevel(self.parent)

        self._setup_window()
        self.widgets = {}


    def _setup_window(self):

        self.window.title(self.title)
        self.window.geometry(self.size)
        self.window.resizable(*self.resizable)

        # 设置为父窗口的临时窗口（关闭父窗口时子窗口也关闭）
        self.window.transient(self.parent)

        if self.is_modal:
            self.window.grab_set()


    def add_label_ordinary_text(self,name,text='填写文本',x=0, y=0,font=('微软雅黑',16)):
        label_text = tk.Label(self.window, text=text,font=font)
        label_text.place(x=x, y=y)
        self.widgets[name] = label_text
        return label_text

    def add_input(self,name,x,y,width=10,font=('微软雅黑',14)):
        entry = tk.Entry(self.window,width=width,font=font)
        entry.place(x=x,y=y)
        self.widgets[name] = entry

