# Database 연동

# 테이블 생성
import sqlite3

def create_table():
	conn = sqlite3.connect('my_book.db')

	cur = conn.cursor()  # 커서 획득
	cur.execute('''create table my_booksb(
					title text,
					published_date text,
					publisher text,
					pages integer,
					recommendation integer
				)'''
	)

	conn.commit()
	conn.close()

if __name__ == "__main__":
	create_table()

# 데이터 입력
import sqlite3

def insert_books():
	conn = sqlite3.connect('my_book.db')
	cur = conn.cursor()
	cur.execute("insert into my_books values('개발자의코드', '2013.02.28', 'A', 200, 0)")
	# insert_sql = 'insert into my_books values(?, ?, ?, ?, ?)'
	# cur.execute(insert_sql, ('클린코드', '2010.03.04', 'B', 584, 1)")
	
	books = [
        ('빅데이터 마케팅', '2014.07.02','A', 296, 1),
        ('구글드', '2010.02.10','B', 526, 0),
        ('강의력', '2013.12.12','A', 248, 1)
    ]

# 여러 데이터 입력
    cur.executemany(insert_sql, books)

    conn.commit()       # 데이터베이스 반영

    conn.close()        # 커넥션 닫기


if __name__ == "__main__":		# 외부에서 호출 시
    insert_books() 


# my_books_in_db.py -- DB 연결, 테이블 생성
# insert.py -- 데이터 삽입
# select.py -- 데이터 조회
# update.py -- 데이터 수정
# delete.py -- 데이터 삭제

###################################################################

# Oracle 연동

# cx_Oracle 라이브러리 설치
# Anaconda prompt 열기
# python -m pip install cx_Oracle --upgrade
# oracle instant client 다운로드 : http://www.oracle.com/database/technologies/instant-client/downloads.html
# PATH 설정
import cx_Oracle
import os
import pandas as pd

# LOCATION = r"C:\instantclient_19_8"
# os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]  #환경변수 등록

# Oracle DB 정보 확인 및 연결 : SQL Developer

connect = cx_Oracle.connect("사용자이름", "비밀번호", "호스트이름:포트/서비스이름")
connect = cx_Oracle.connect('hr/hr@localhost:1521/xe')
cursor = connection.cursor()

# SQL 실행
cursor.execute("select * from employees")

for i in cursor:
print(i)


# DataFrame으로 불러오기
df = pd.real_sql(""" select * from employees """ , con = connection)

