import os

filenames = ['service_contract.hwp', 'christmas_report.pptx',
             'business_report.docx', 'accounting_report.pptx', 'account_book.pptx']
over_5mb_filenames = []


# 이곳에 코드를 작성하세요.
def byte_to_mb(byte):
    mb = (byte / 1000) / 1000

    return mb


for i in filenames:
    print(os.path.getsize(i))
    if byte_to_mb(os.path.getsize(i)) > 5:
        over_5mb_filenames.append(i)
# 채점 코드
print("5MB가 넘는 파일 리스트:")
print(over_5mb_filenames)
