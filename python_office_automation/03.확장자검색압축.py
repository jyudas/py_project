import os
import zipfile

files = [
    "account_book.pptx", "accounting_report.pptx", "automation_video.mp4",
    "business_report.docx", "codeit_cloud.png", "codeit_contract.hwp",
    "codeit_cs.png", "git_final.mp4", "image_mac.svg", "KDW_report_01_2020-07-16.docx",
    "KHS_report_01_2020-07-16.docx", "money_book.xlsx", "screenshot_2000-09-05 20_28_29.jpeg",
]

with zipfile.ZipFile("images.zip", "w", compression=zipfile.ZIP_DEFLATED) as zip:
    for file in files:
        filename, extension = os.path.splitext(file)
        if extension == ".png" or extension == ".jpeg":
            print(file)
            zip.write(file)

# 채점 코드
print(os.path.getsize("images.zip"))