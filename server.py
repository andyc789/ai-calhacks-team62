from flask import Flask, render_template, request
from subprocess import call
import sys

app = Flask(__name__)

@app.route('/')
def webapp():
  return render_template('webapp.html')

@app.route('/submitted/', methods=['GET', 'POST'])
def submitted():
  if request.method == 'POST':
    text = request.form.get('code')
    problemname = "twosum"
    filename = problemname+".py"
    sys.stdout = open(problemname+"_output", "w")
    f = open(filename, "w")
    f.write(text)
    f.close()
    g = open(filename, "a")
    for line in open("testcases/twosum/test_twosum.py", r):
      g.write(line)
    subprocess.call(['python', filename])
  return 'test'




if __name__ == '__main__':
  app.run(debug=True)