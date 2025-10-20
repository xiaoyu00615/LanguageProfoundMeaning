import json
from pathlib import Path

from utils.public_fun import reading_json



def create_json_init(data_json):
    configs = reading_json('./config/config_path.json')
    create_json_file_topic_answer(configs,data_json)



def json_container(data):
    print(data)
    topics = data['regx_topic']

    json_arr = []

    for index,topic in enumerate(topics):

        json_arr.append(
            {
                "id":index,
                "topic":topic,
                "answer":''
            }
        )

    return  json_arr


def create_json_file_topic_answer(configs,data_json):


    json_text = json_container(data_json)
    url = Path(configs['answer_json_file'])

    # 如果有文件就不会创建
    if url.exists():

        return

    # 创建文件
    try:
        # 确保父文件夹存在
        url.parent.mkdir(parents=True, exist_ok=True)

        # 创建并写入文件
        with url.open("w", encoding="utf-8") as f:
            json.dump(json_text, f, indent=2, ensure_ascii=False)
        print(f"文件创建成功：{url}")
    except IOError as e:
        print(f"文件创建失败：{e}")



