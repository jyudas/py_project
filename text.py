"""
연결옵션:

host - 서버주소. 자신의 컴퓨터를 서버로 사용한다면 ‘localhost’ 또는 127.0.0.1 을 입력.
user - username 입력
password - 서버 암호 입력
db - 데이터베이스, 스키마 이름 입력
charset - 문자세트 입력. 한글 사용을 위해 ‘utf8’ 입력

def insert(self, vo):
    self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='encore', charset='utf8')
    cur = self.conn.cursor()
    sql = "insert into members values(%s, %s, %s, %s)"
    vals = (vo.id, vo.pwd, vo.name, vo.email)
    cur.execute(sql, vals)
    self.conn.close()
    self.conn.commit()
"""
