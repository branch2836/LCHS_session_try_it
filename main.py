from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'K>~EEAnH_x,Z{q.43;NmyQiNz1^Yr7'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_item = request.form["new_item"]
        current_list = session['list_name']
        if new_item not in current_list:
            current_list.append(new_item)
        else:
            current_list.remove(new_item)
        session['list_name'] = current_list

    else:
        if 'list_name' not in session:
            session['list-name'] =[]
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
