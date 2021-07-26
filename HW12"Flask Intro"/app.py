from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcom to calculator app!'


@app.route('/calc')
def calculator():
    return render_template('calc.html')


@app.route('/calc/<int:x>/<int:y>')
def calc(x,y):
    return render_template('calc.html', x=x, y=y, div=x/y)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

