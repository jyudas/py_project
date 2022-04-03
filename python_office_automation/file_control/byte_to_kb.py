import os

print(os.path.getsize("/Users/jyudas/PycharmProjects/pythonProject/python_office_automation/india.jpg"))




def byte_to_kb(byte):
    kb = byte /1000
    return kb

print(byte_to_kb(os.path.getsize("/Users/jyudas/PycharmProjects/pythonProject/python_office_automation/india.jpg")))