from flask import *

app = Flask('__name__')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cendikia')
def cendikia():
    return render_template('cendikia.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        keyword = request.form['keyword']
        return redirect(f'https://scholar.google.com/scholar?hl=id&as_sdt=0%2C5&q={keyword}')
    else:
        keyword = request.args.get('keyword', '')
        return redirect(f'https://scholar.google.com/scholar?hl=id&as_sdt=0%2C5&q={keyword}')

if __name__ == '__main__':
    app.run(debug=True)