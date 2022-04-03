import os
import datetime
#생성일
c_time = os.path.getctime("/Users/jyudas/PycharmProjects/pythonProject/python_office_automation/india.jpg")
c_time2 = datetime.datetime.fromtimestamp(c_time)
print(c_time2)
#수정일
m_time = os.path.getmtime("/Users/jyudas/PycharmProjects/pythonProject/python_office_automation/india.jpg")
m_time2 = datetime.datetime.fromtimestamp(m_time)
print(m_time2)
#access 
a_time = os.path.getatime("/Users/jyudas/PycharmProjects/pythonProject/python_office_automation/india.jpg")
a_time2 = datetime.datetime.fromtimestamp(a_time)
print(a_time2)