from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "muah"

@app.route('/')
def clicker ():
    if 'count' not in session:
        session['count'] = 0
    else: session['count'] += 1
    return render_template('index.html')

@app.route('/count')
def count():
    session['count'] += 1
    print('increasing count by 1')
    return redirect('/')

@app.route('/counter', methods = ['POST'])
def counter():
    print('new visit')
    print(request.form)
    print(request.form['visits'])
    return redirect('/count')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)    # Run the app in debug mode.
