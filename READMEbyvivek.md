# Python_Hacktoberfest2021
Solution
Part 1: To create the required database and add data programmatically by using the Insert query
import sqlite3
db=sqlite3.connect("m5assignment.db")
cur=db.cursor()
cur.execute('''CREATE TABLE books (
BookID INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT (50) NOT NULL,
author TET(20),
price REAL);''')
for x in range(5):
    
    ttl=input("enter book's title: ")
    aut=input("enter name of author: ")
    pr=float(input("enter price: "))
    sql="INSERT INTO books (title, author, price) VALUES ('"+ttl+"','"+aut+"','"+str(pr)+"');"

    try:
        cur=db.cursor()
        cur.execute(sql)
        db.commit()
        print ("one record added successfully")
    except:
        print ("error in operation")
        db.rollback()
db.close()

Part 2: To enter the title and number of copies and see the total cost
import sqlite3
db=sqlite3.connect("m5assignment.db")
cur=db.cursor()

total=0
while True:
    
    ttl=input("enter book's title: ")

    sql="SELECT * FROM books WHERE title='"+ttl+"'"
    cur=db.cursor()
    cur.execute(sql)
    rec=cur.fetchone()
    if rec!=None:
        print (rec)
        pr=rec[3]
        qty=int(input("enter number of books purchased"))
        cost=pr*qty
        total=total+cost
    else:
        print ("Title Not Found")
    choice=input("add more books[Y/N]?")
    if choice=='N': break
print ("Total cost of Purchased Books",total)
db.close()

Sample data in the database:
BookID	Title	Author	Price
1	Learn Python 3 The Hard Way	Zed A.Shaw	575
2	Think Python	Allen B. Drowney	475
3	Data structures and algorithms in Python	Goodritch	470
4	Python Programming:A modular Approach	Taneja & Kumar	450
5	Python Machine Learning By Example	Liu & Yuxi	725
6	Core Python Programming 	R.Nageshwar Rao	599
