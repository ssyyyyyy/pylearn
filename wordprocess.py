import re
from docx import Document

# 定义正则表达式，用于匹配邮箱地址
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# 定义一个函数，用于删除文本中的邮箱地址
def remove_emails(text):
    return re.sub(email_pattern, '', text)

# 定义一个函数，处理Word文档中的邮箱地址
def process_word_document(docx_file):
    doc = Document(docx_file)
    for paragraph in doc.paragraphs:
        # 删除段落中的邮箱地址
        paragraph.text = remove_emails(paragraph.text)
    # 保存修改后的文档
    doc.save(f"processed_{docx_file}")

# 批量处理多个Word文档
files = ["word.docx"]
for file in files:
    process_word_document(file)
