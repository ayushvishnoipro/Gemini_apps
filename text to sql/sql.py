# Import module 
import sqlite3 
  
# Connecting to sqlite 
conn = sqlite3.connect('student.db') 
  
# Creating a cursor object using the  
# cursor() method 
cursor = conn.cursor() 
  
# Creating table 
table ="""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(25), 
SECTION VARCHAR(25),MARKS INT);"""
cursor.execute(table) 
  
# Queries to INSERT records. 
cursor.execute('''INSERT INTO STUDENT VALUES ('Raju', '7th', 'A', 90)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Shyam', '8th', 'B', 100)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Baburao', '9th', 'C', 86)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Baburao', '9th', 'D', 50)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Baburao', '9th', 'C', 35)''') 

  
# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
conn.commit() 
  
# Closing the connection 
conn.close()