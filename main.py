import pandas
import pymysql
import numpy as np
from IPython.display import display

df = pandas.read_excel('/Users/jyudas/PycharmProjects/pythonProject/book.xlsx',sheet_name='도서관목록', header=1, nrows=98)
df.fillna('', inplace=True)
# print(df.shape)
# print(df.index)
# print(df.columns)

# Use `iloc[]` to select a row
# display(df.iloc[1])
# display(df.loc[1])

# Use `loc[]` to select a column
# display(df.loc[:,'제목'])
# display(df['제목'])
# for i in range(0, 99):
#     for i in range(0, 9):
#         display(df.loc[0][0])

conn = pymysql.connect(host='jyudas.synology.me', user='test', password='Seoyh3107!', db='test', charset='utf8')
cur = conn.cursor()
sql = "insert into breathoftree_book (pk, category, title, writer, publisher) values (%s ,%s ,%s ,%s ,%s )"

for i in range(0, 98):
    for a in range(0, 5):
        print("행수{}".format(i))
        print("열수{}".format(a))
        print(df.loc[i][a])
        if a  == 0:
            str_0 = df.loc[i][a]
        elif a  == 1:
            str_1 = df.loc[i][a]
        elif a == 2:
            str_2 = df.loc[i][a]
        elif a == 3:
            str_3 = df.loc[i][a]
        elif a == 4:
            str_4 = df.loc[i][a]
    cur.execute(sql, ( str_0 ,str_1 ,str_2 ,str_3 ,str_4))

conn.commit()
cur.close()