import re

from utils import regx
from utils.regx import meaning_content


def regx_json(arr_lines):
    regx_data = []
    regx_meaning = []
    regx_topic = []


    for line in arr_lines:
        # print(line)

        # 获取时间日期
        if re.search(regx.problem_date,line):
            regx_data.append(line)

        # 获取含义内容
        if re.search(regx.meaning_content,line):
            regx_meaning.append(line)

        # 获取题目
        if re.search(regx.topic_data, line):
            regx_topic.append(line)

    return {
        'regx_data' :regx_data,
        'regx_meaning' :regx_meaning,
        'regx_topic' :regx_topic
    }




