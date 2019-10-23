from flask import Flask, render_template, request, redirect, abort, session, url_for
from firebase import Firebase

app = Flask(__name__)
app.secret_key = 'our_first!Blog$'
fr = Firebase()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = fr.sign_in(email, password)
        session['id'] = email
        if user == None:
            abort(401)
        else:
            return redirect(url_for('new_post'))
    else:
        return render_template('login.html')

@app.route('/add_new_post', methods=['GET', 'POST'])
def new_post():
    print(session['id'])
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
