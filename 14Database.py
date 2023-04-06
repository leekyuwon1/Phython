#INSERT

import mysql.connector

#mysql 연결정보
# config = {
#     'user' : 'root',
#     'password' : '1234',
#     'host' : 'localhost',
#     'database' : 'testdb'
# }
# #Connection 객체 생성
# conn = mysql.connector.connect(**config) # ** : key value
#
# #커서 생성
# cursor = conn.cursor()
# #SQL 쿼리 작성
# sql = "insert into tbl_member values (null, %s, %s, %s)"
# val = ('이태수','55', '울산')
#
#
# #실행
# cursor.execute(sql,val)
# conn.commit()
#
# #연결종료
# cursor.close()
# conn.close()


#SELECT
#
# #mysql 연결정보
# config = {
#     'user' : 'root',
#     'password' : '1234',
#     'host' : 'localhost',
#     'database' : 'testdb'
# }
# #Connection 객체 생성
# conn = mysql.connector.connect(**config) # ** : key value
#
# #커서 생성
# cursor = conn.cursor()
# #SQL 쿼리 작성
# sql = "SELECT * FROM tbl_member "
#
# #실행
# cursor.execute(sql)
#
# #결과 출력
# for row in cursor.fetchall():
#     print(row)
#
# #연결종료
# cursor.close()
# conn.close()

#UPDATE

# #mysql 연결정보
# config = {
#     'user' : 'root',
#     'password' : '1234',
#     'host' : 'localhost',
#     'database' : 'testdb'
# }
# #Connection 객체 생성
# conn = mysql.connector.connect(**config) # ** : key value
#
# #커서 생성
# cursor = conn.cursor()
#
# #SQL 쿼리 작성
# sql = "UPDATE tbl_member set addr=%s WHERE addr=%s LIMIT 1"
# val = ("울산", "서울")
#
# #실행
# cursor.execute(sql,val)
# conn.commit()
#
# #연결종료
# cursor.close()
# conn.close()
#

# DELITE
#mysql 연결정보
config = {
    'user' : 'root',
    'password' : '1234',
    'host' : 'localhost',
    'database' : 'testdb'
}
#Connection 객체 생성
conn = mysql.connector.connect(**config) # ** : key value

#커서 생성
cursor = conn.cursor()

#SQL 쿼리 작성
sql = "DELETE FROM tbl_member WHERE addr='울산' LIMIT 1"

#실행
cursor.execute(sql)
conn.commit()

#연결종료
cursor.close()
conn.close()
