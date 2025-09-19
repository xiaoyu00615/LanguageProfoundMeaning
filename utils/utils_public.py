import re
from pathlib import Path

import utils.regx as regx


# 读取文件内容
def reading_file(file_name):
    try:
        with open(file_name,'r',encoding='utf-8') as file:
            content = file.read()
            # print(content)
    except FileNotFoundError:
        print('错误：文件不存在')
    except Exception as e:
        print(f"发生错误：{e}")
    return content

    # content = Path(file_name).read_text(encoding='utf-8')
    # # print(content)
    # normalized_text = content.replace('\r\n', '\n').replace('\r', '\n')
    # return normalized_text




def regx_json(str_txt):

    # print(str_txt)
    content = re.search(regx.meaning_content, str_txt)
    print(content)



