import tkinter as tk
from tkinter import font

import json

def get_text_width(text,font_config=('微软雅黑',12,'')):
    """
       直接获取文字的宽度（像素）

       参数:
           text: 要计算宽度的文字
           font_config: 字体配置，格式为(字体名称, 大小, 样式)
       """
    # 创建临时字体对象
    text_font = font.Font(family=font_config[0], size=font_config[1], weight=font_config[2])
    # 直接返回文字宽度（像素）
    return text_font.measure(text)

def del_demo(demo_arr):
    for demo in demo_arr.values():
        if hasattr(demo, 'widgets'):
            del_demo(demo.widgets)
            # 销毁当前控件（核心步骤）
        if hasattr(demo, 'destroy'):
            demo.destroy()
    demo_arr.update()

def reading_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data

def write_json(path, index,text):
    json_data = reading_json(path)
    json_data[index]['answer'] = text

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False)

    print("写入成功")
