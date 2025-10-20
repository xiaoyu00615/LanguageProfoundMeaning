from file_window import child_ui

def ui_setting_click(title,parent,width,height):
    child_setting_window = child_ui.ChildWindow(title=title,parent=parent,width=width,height=height)

    child_setting_window.add_label_ordinary_text('set_label_width','窗口宽度：',20,20)
    child_setting_window.add_input('set_input_width',130,20)

    child_setting_window.add_label_ordinary_text('set_label_height', '窗口高度：', 20, 80)
    child_setting_window.add_input('set_input_height', 130, 80)

def ui_start_click():
    print('开始答题')
