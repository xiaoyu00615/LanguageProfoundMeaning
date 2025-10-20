# 这是一个示例 Python 脚本。
import utils.analysis_docx as analysis
import utils.file_path as file_path
import utils.utils_public as utils
from utils.public_fun import reading_json
from utils.start_answer_ui import StartAnswerUI
from file_window.ui import UIManager
from file_window import config

from file_window import click_fun
from utils import create_json_file, public_fun


def init_data():
    global data_json
    docx_text = analysis.extract_text_from_docx(file_path.topics_path)
    # print(docx_text)

    data_json = utils.regx_json(docx_text)



def start_page(ui):
    # 2. 添加组件
    ui.add_label_title("title", "思辨问答录", y=20, font_size=32, center='center')

    # 开始答题按钮
    ui.add_button_ordinary("start_answer", "开始答题", lambda: answer_page(ui,data_json), pad_x=10, x=0, y=150, width=10,
                           height=1, center='center', font_config=("微软雅黑", 16, ''))
    # 设置按钮
    ui.add_button_ordinary("setting", "设置", lambda: click_fun.ui_setting_click(
        config.child_setting_ui_title,
        ui.root,
        config.child_setting_ui_width,
        config.child_setting_ui_height

    ), pad_x=10, x=0, y=230, width=10, height=1, center='center', font_config=("微软雅黑", 16, ''))

def test():
    print('测试')


def answer_page(uis,data_json):
    global answer_json
    # print("答题页",ui)
    # print(ui.widgets)
    arr_json = reading_json('./save_data/answer.json')


    public_fun.del_demo(uis.widgets)
    print(uis)


    ui = StartAnswerUI(uis.root,arr_json)
    print(ui)
    ui.add_label_ordinary_text('topic',data_json,10,20)

    answer_json = public_fun.reading_json('./save_data/answer.json')
    print(answer_json,'数据')


    ui.add_text('answer',answer_json,10,20)

    def inits():
        answer_json = public_fun.reading_json('./save_data/answer.json')
        ui.add_label_ordinary_text('topic', data_json, 10, 20)
        ui.add_text('answer', answer_json, 10, 20)

    ui.add_button("submit","提交",lambda: ui.submit_text('answer'))
    ui.add_button('up_topic',"上一题",lambda: ui.up_topic(inits))
    ui.add_button('next_topic',"下一题",lambda: ui.next_topic(inits))
    ui.add_button('back_home',"返回首页",lambda: (ui.back_home(),start_page(uis)))


    # print(ui)





def run_app():
    # 1. 初始化UI管理器（自动创建主窗口）
    ui = UIManager(title=config.ui_title, width=config.ui_width, height=config.ui_height)

    start_page(ui)

    # 3. 启动窗口
    ui.run()

def init_ui():

    init_data()
    create_json_file.create_json_init(data_json)
    run_app()




if __name__ == '__main__':
    init_ui()


