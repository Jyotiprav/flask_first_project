import sqlite3

conn = sqlite3.connect('python_quiz.db')
print("Opened database successfully")

conn.execute('CREATE TABLE QA1 (Ques TEXT, O1 TEXT,O2 TEXT,O3 TEXT,O4 TEXT, Right_Answer TEXT)')
print("Table created successfully")
conn.close()