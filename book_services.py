import sqlite3
from domain import Books, Book_reviews

dbfile = "tf_backend_book"

def get_book_all():
    # Conectar a la base de datos
    con = sqlite3.connect(dbfile)
    cur = con.cursor()

    # Consultar las tablas existentes en la base de datos
    res = cur.execute("SELECT * from books").fetchall()


    # Si hay tablas, retornarlas como una lista de nombres
    if res:
        books_list = []
        for row in res:
            book = Books(
                row[0],        
                    row[1],        
                    row[2],         
                    row[3],         
                    row[4],      
                    row[5].split(";")   
                ).__dict__()
            books_list.append(book)
            return books_list       
    else:
        return None


def get_book_by_id(book_id):
    con = sqlite3.connect(dbfile)

    #ejecuta consulta
    cur = con.cursor()

    res = cur.execute("SELECT * FROM books WHERE id = ? ", (book_id,)).fetchone()
 
    if res:
          #elementos dentro de la respuesta y retornamos como diccionario
        return Books(res[0], res[1], res[2], res[3], res[4], res[5].split(";")).__dict__()
    else:
        return None
    
def get_book_review_by_id(book_id):
    con = sqlite3.connect(dbfile)

    #ejecuta consulta
    cur = con.cursor()

    res = cur.execute("SELECT * FROM book_reviews WHERE book_id = ? ", (book_id,)).fetchone()
 
    if res:
          #elementos dentro de la respuesta y retornamos como diccionario
        return Book_reviews(res[0], res[1], res[2], res[3]).__dict__()
    else:
        return None
    

def add_book(book):
    con = sqlite3.connect(dbfile)
    cur = con.cursor()

    try:
        cur.execute("INSERT INTO books (id, name, publisher, year, authors, edition) VALUES (?, ?, ?, ?, ?, ?)", 
        (book.id, book.name, book.publisher, book.year, book.authors, book.edition))
        con.commit()  
        return book.id
    except sqlite3.IntegrityError:
        con.rollback()  
        return None
    finally:    
        con.close()

def delete_book_by_id(book_id):
    con = sqlite3.connect(dbfile)
    cur = con.cursor()

    try:
        cur.execute("DELETE from books where id = ? ", (book_id,))
        con.commit()  
        return True
    except sqlite3.IntegrityError:
         con.rollback()  
         return None
    finally:    
        con.close()
