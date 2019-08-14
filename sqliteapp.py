from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/createquiz')
def new_student():
    return render_template('create_quiz.html')

@app.route('/pythonquiz')
def pythonquiz():
    con = sql.connect("python_quiz.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from QA1")

    rows = cur.fetchall()
    return render_template("python_quiz.html", rows=rows)



@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            q = request.form['ques']
            O1 = request.form['O1']
            O2 = request.form['O2']
            O3 = request.form['O3']
            O4 = request.form['O4']
            ra = request.form['rans']
            with sql.connect("python_quiz.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO QA1 (Ques, O1,O2,O3,O4, Right_Answer) VALUES(?, ?,?,?,?,?)", (q,O1,O2,O3,O4,ra) )

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("results.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect("python_quiz.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from QA1")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)