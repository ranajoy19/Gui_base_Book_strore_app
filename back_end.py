import sqlite3 as sq

class Database:

    def __init__(self,db):
        self.conn=sq.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(Id INTEGER PRIMARY KEY,Title text ,Author text,Year integer ,ISBN integer)")
        self.conn.commit()


    def insert(self,Title,Author,Year,ISBN):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(Title,Author,Year,ISBN))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM BOOK")
        rows =self.cur.fetchall()
        return rows


    def search(self,Title="",Author="",Year="",ISBN=""):
        self.cur.execute("SELECT * FROM BOOK WHERE Title=? OR Author=? OR Year=? OR ISBN=?",(Title,Author,Year,ISBN))
        rows = self.cur.fetchall()
        return rows

    def delete(self,Id):
        self.cur.execute("DELETE FROM BOOK WHERE Id=?",(Id,))
        self.conn.commit()

    def update(self,Id,Title,Author,Year,ISBN):
        self.cur.execute("UPDATE BOOK SET Title=?,Author=?,Year=?,ISBN=? WHERE Id=?",(Title,Author,Year,ISBN,Id))
        self.conn.commit()


    def __del__(self):
        self.conn.close()




    #delete(3)
    #insert("MAR GONGA JHILIK JHILIK","Chetan Bhagat",2012,6290331161)

    #print(search(Title="The Life of Pi"))


    #update(1,"The Life of PI","Irfan Khan",2012,6290331160)
    #print(view())
