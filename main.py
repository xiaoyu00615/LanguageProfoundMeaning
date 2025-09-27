# 这是一个示例 Python 脚本。
import file_window.window as win
import utils.analysis_docx as analysis
import utils.file_path as file_path
import utils.utils_public as utils

def main_program():
    win.create_window()

def init_data():
    docx_text = analysis.extract_text_from_docx(file_path.topics_path)
    # print(docx_text)
    data = utils.regx_json(docx_text)
    print(data['regx_topic'])


if __name__ == '__main__':
    init_data()
    main_program()

