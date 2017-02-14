# coding: utf-8

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
import requests

# 获取文档对象
# fp = open('xx.pdf', 'rb')
print("开始下载文件...")
r = requests.get('http://static.sse.com.cn/disclosure/listedinfo/announcement/c/2016-12-16/600652_20161216_1.pdf',
                 stream=True)
with open('test.pdf', 'wb') as fd:
    for chunk in r.iter_content(8192):
        fd.write(chunk)

print("下载完成...")

fp = open('test.pdf', 'rb')

# 创建一个与文档关联的解释器
parser = PDFParser(fp)

# pdf文档对象
doc = PDFDocument()

# 链接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

# 初始化文档
doc.initialize("")

# 创建资源管理器
resource = PDFResourceManager()

# 参数分析器
laparam = LAParams()

# 创建一个聚合器
device = PDFPageAggregator(resource, laparams=laparam)

# 创建pdf页面解释器
interpreter = PDFPageInterpreter(resource, device)

# 使用文档对象得到页面的集合
for page in doc.get_pages():
    # 使用页面解释器来读取
    interpreter.process_page(page)
    # 使用聚合器来获得内容
    layout = device.get_result()

    for out in layout:
        if hasattr(out, "get_text"):
            print(out.get_text())
