from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('hello.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("login.html",result = result)

@app.route('/quiz')
def Quiz():
   return render_template('quiz.html')




if __name__ == '__main__':
   app.run(debug = True)