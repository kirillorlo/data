from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        response = make_response(redirect('/welcome'))
        response.set_cookie('user_data', f'{name},{email}')
        return response
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    user_data = request.cookies.get('user_data')
    if user_data:
        name, email = user_data.split(',')
        return render_template('welcome.html', name=name)
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('user_data', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
