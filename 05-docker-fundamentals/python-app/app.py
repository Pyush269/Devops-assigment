from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello World from Python!</h1><p>Student: PIYUSH PAWAN KUMAR | Enrollment: 24bcs10296</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
