import os
import datetime

filenames = ['service_contract.hwp', 'christmas_report.pptx', 'business_report.docx', 'accounting_report.pptx', 'account_book.pptx']

for filename in filenames:
# 이곳에 코드를 작성해주세요.
    mtimestamp = os.path.getmtime(filename)
    mtime = datetime.datetime.fromtimestamp(mtimestamp)
    size = os.path.getsize(filename)
    file_info = {}
    file_info["filename"] = filename
    file_info["mtime"] = str(mtime)
    file_info["size"] = size

    print(file_info)

'''
{'filename': 'service_contract.hwp', 'mtime': '2021-04-12 06:50:57', 'size': 64000}
{'filename': 'christmas_report.pptx', 'mtime': '2021-04-12 06:50:57', 'size': 7976285}
{'filename': 'business_report.docx', 'mtime': '2021-04-12 06:49:26', 'size': 36656}
{'filename': 'accounting_report.pptx', 'mtime': '2021-04-12 06:49:26', 'size': 236437}
{'filename': 'account_book.pptx', 'mtime': '2021-04-12 06:49:25', 'size': 7724941}
'''