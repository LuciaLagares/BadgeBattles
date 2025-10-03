from flask import Flask, render_template; 
import datetime 

app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bienvenida')
def hello_welcome():
    year=datetime.datetime.now().year
    return render_template('index.html', year=year)

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug="True")