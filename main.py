from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'Chemistry'

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')

if __name__ == '__main__':
    app.run()