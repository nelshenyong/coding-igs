from flask import Flask, render_template

app = Flask(__name__)

titleWeb= "MY FLASK"

data = [
    {
        'author' : 'Keffe',
        'content' : 'lorem',
        'date' : '01-01-2020'
    },
    {
        'author' : 'Latte',
        'content' : 'ipsum',
        'date' : '01-01-2025'
    }
]      

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", titleWeb = titleWeb, data = data, usia = 20)

@app.route("/about")
def about():
    return render_template('about.html', titleWeb = titleWeb)
@app.route('/content')
def content():
    return f"Content page..."
@app.route('/contact')
def contact():
    return render_template('contact.html', titleWeb = titleWeb)
@app.route('/blog')
def blog():
    return render_template('blog.html', titleWeb = titleWeb)

if __name__  == '__main__':
    app.run(debug=True)
