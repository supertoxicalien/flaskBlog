from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index_2.html')


@app.route('/about')
def about():
    return render_template('about_2.html')


if __name__ == '__main__':
    app.run(debug=True)