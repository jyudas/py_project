import pymysql

"""
연결옵션:

host - 서버주소. 자신의 컴퓨터를 서버로 사용한다면 ‘localhost’ 또는 127.0.0.1 을 입력.
user - username 입력
password - 서버 암호 입력
db - 데이터베이스, 스키마 이름 입력
charset - 문자세트 입력. 한글 사용을 위해 ‘utf8’ 입력
"""

conn = pymysql.connect(host='jyudas.synology.me', user='test', password='########!', db='test', charset='utf8')
cur = conn.cursor()

cur.execute("select * from test_1")

print(cur.fetchall())

