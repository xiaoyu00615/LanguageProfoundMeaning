import docx

def extract_text_from_docx(file_path):
    # 打开word 文档
    doc = docx.Document(file_path)

    # 存储所有行内容的列表
    all_lines = []

    # 遍历文档中的每个段落
    for para in doc.paragraphs:
        # 段落文本可能包含多个换行，按换行符分割
        lines = para.text.split('\n')
        # 过滤空行并添加到结果列表
        for line in lines:
            if line.strip():  # 只保留非空行
                all_lines.append(line)

    return all_lines


