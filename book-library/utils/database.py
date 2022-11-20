import sqlite3
from .database_connection import DatabaseConnection

"""
	Concerned with storing and retrieving book from a list
"""

books = []

def create_book_table():
	connection = sqlite3.connect('data.db')
	cursor = connection.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text,read int)')
	connection.commit()
	connection.close()

def add_book(name,author):

	with DatabaseConnection('data.db') as connection:  
		cursor = connection.cursor()
		cursor.execute(f'INSERT INTO books VALUES("{name}","{author}","0")')
		# books.append({'name':name,'author':author,'read':False})

def get_all_books():
	connection = sqlite3.connect('data.db')
	cursor = connection.cursor()
	books = cursor.execute("SELECT * FROM books")
	books = books.fetchall()
	connection.commit()
	connection.close()
	
	books = [{'name': book[0],'author':book[1],'read':book[2]} for book in books]
	return books


def  mark_book_as_read(name):
	connection = sqlite3.connect('data.db')
	cursor = connection.cursor()
	cursor.execute(f'UPDATE books SET read=1 where name="{name}"')
	connection.commit()
	connection.close()


# def delete_book(name):
# 	for book in books:
# 		if(book['name'] == name):
# 			books.remove(book)
# 			break

def delete_book(name):
	connection = sqlite3.connect('data.db')
	cursor = connection.cursor()
	cursor.execute('DELETE FROM books where name=?',(name,))
	connection.commit()
	connection.close()
