from flask import Flask, render_template, request, redirect, abort, session, url_for
from firebase import Firebase
import json

app = Flask(__name__)
app.secret_key = 'our_first!Blog$'
fr = Firebase()

@app.route('/')
def index():
    posts = fr.getPosts('token')
    print(len(posts))
    return render_template('index.html', posts=posts)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = fr.sign_in(email, password)
        session['id'] = user['idToken']
        if user == None:
            abort(401)
        else:
            return redirect(url_for('new_post'))
    else:
        return render_template('login.html')

@app.route('/add_new_post', methods=['GET', 'POST'])
def new_post():
    if(session.get('id') == None): 
        return redirect(url_for('login'))
    print(session['id'])
    if request.method == 'POST':
        #TITLE, BODY get values
        data = {}
        data['title'] = request.form['title']
        data['body'] = request.form['body']
        posts = fr.getPosts('token')
        postId = len(posts)
        fr.addPost(data, postId)
        return render_template('dashboard.html', status=1)
    return render_template('dashboard.html', status=0)

if __name__ == '__main__':
    app.run(debug=True)
