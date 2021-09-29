# Database 연동

# 테이블 생성
import sqlite3

def create_table():
	conn = sqlite3.connect('my_books.db')

	cur = conn.cursor()  # 커서 획득
	cur.execute('''create table my_books(
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