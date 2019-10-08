from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name='Nyamkhuu'):
    return render_template('main.html', name=name)

@app.route('/about')
def about():
    return 'Hello world!, this is my first blog'

if __name__ == '__main__':
    app.run(debug=True)
