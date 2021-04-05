from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'This_is_NOT_a_good_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else:
        pass
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
