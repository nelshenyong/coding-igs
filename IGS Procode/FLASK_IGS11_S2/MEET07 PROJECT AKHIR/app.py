from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///buddhist_wisdom.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    favorites = db.relationship('Favorite', backref='user', lazy=True)

class Quote(db.Model):
    __tablename__ = 'quotes'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    source = db.Column(db.String(200))
    category = db.Column(db.String(50))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    favorites = db.relationship('Favorite', backref='quote', lazy=True)

class Paritta(db.Model):
    __tablename__ = 'parittas'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    meaning = db.Column(db.Text)
    category = db.Column(db.String(50))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    favorites = db.relationship('Favorite', backref='paritta', lazy=True)

class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quote_id = db.Column(db.Integer, db.ForeignKey('quotes.id'))
    paritta_id = db.Column(db.Integer, db.ForeignKey('parittas.id'))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

def get_current_user():
    if 'user_id' in session:
        return User.query.get(session['user_id'])
    return None

def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this page.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

def admin_required(f):
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this page.')
            return redirect(url_for('login'))
        user = User.query.get(session['user_id'])
        if not user or not user.is_admin:
            flash('You need to be an admin to access this page.')
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@app.route('/')
def home():
    quotes = Quote.query.order_by(Quote.date_added.desc()).limit(5).all()
    parittas = Paritta.query.order_by(Paritta.date_added.desc()).limit(3).all()
    return render_template('home.html', quotes=quotes, parittas=parittas)

@app.route('/quotes')
def quotes():
    quotes = Quote.query.order_by(Quote.date_added.desc()).all()
    return render_template('quotes.html', quotes=quotes)

@app.route('/parittas')
def parittas():
    parittas = Paritta.query.order_by(Paritta.date_added.desc()).all()
    return render_template('parittas.html', parittas=parittas)

@app.route('/add_quote', methods=['GET', 'POST'])
@admin_required
def add_quote():
    if request.method == 'POST':
        content = request.form.get('content')
        source = request.form.get('source')
        category = request.form.get('category')
        
        new_quote = Quote(content=content, source=source, category=category)
        db.session.add(new_quote)
        db.session.commit()
        
        flash('Quote added successfully!')
        return redirect(url_for('quotes'))
    
    return render_template('add_quote.html')

@app.route('/edit_quote/<int:quote_id>', methods=['GET', 'POST'])
@admin_required
def edit_quote(quote_id):
    quote = Quote.query.get_or_404(quote_id)
    
    if request.method == 'POST':
        quote.content = request.form.get('content')
        quote.source = request.form.get('source')
        quote.category = request.form.get('category')
        
        db.session.commit()
        flash('Quote updated successfully!')
        return redirect(url_for('quotes'))
    
    return render_template('edit_quote.html', quote=quote)

@app.route('/delete_quote/<int:quote_id>', methods=['POST'])
@admin_required
def delete_quote(quote_id):
    quote = Quote.query.get_or_404(quote_id)
    db.session.delete(quote)
    db.session.commit()
    flash('Quote deleted successfully!')
    return redirect(url_for('quotes'))

@app.route('/add_paritta', methods=['GET', 'POST'])
@admin_required
def add_paritta():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        meaning = request.form.get('meaning')
        category = request.form.get('category')
        
        new_paritta = Paritta(title=title, content=content, meaning=meaning, category=category)
        db.session.add(new_paritta)
        db.session.commit()
        
        flash('Paritta added successfully!')
        return redirect(url_for('parittas'))
    
    return render_template('add_paritta.html')

@app.route('/edit_paritta/<int:paritta_id>', methods=['GET', 'POST'])
@admin_required
def edit_paritta(paritta_id):
    paritta = Paritta.query.get_or_404(paritta_id)
    
    if request.method == 'POST':
        paritta.title = request.form.get('title')
        paritta.content = request.form.get('content')
        paritta.meaning = request.form.get('meaning')
        paritta.category = request.form.get('category')
        
        db.session.commit()
        flash('Paritta updated successfully!')
        return redirect(url_for('parittas'))
    
    return render_template('edit_paritta.html', paritta=paritta)

@app.route('/delete_paritta/<int:paritta_id>', methods=['POST'])
@admin_required
def delete_paritta(paritta_id):
    paritta = Paritta.query.get_or_404(paritta_id)
    db.session.delete(paritta)
    db.session.commit()
    flash('Paritta deleted successfully!')
    return redirect(url_for('parittas'))

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    user = get_current_user()
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        existing_user = User.query.filter(User.username == username, User.id != user.id).first()
        if existing_user:
            flash('Username already exists')
            return redirect(url_for('edit_profile'))
        
        user.username = username
        if password:
            user.password = password
        
        db.session.commit()
        flash('Profile updated successfully!')
        return redirect(url_for('home'))
    
    return render_template('edit_profile.html', user=user)

@app.route('/manage_users')
@admin_required
def manage_users():
    users = User.query.all()
    return render_template('manage_users.html', users=users)

@app.route('/add_user', methods=['POST'])
@admin_required
def add_user():
    username = request.form.get('username')
    password = request.form.get('password')
    is_admin = bool(int(request.form.get('is_admin', 0)))
    
    if User.query.filter_by(username=username).first():
        flash('Username already exists')
        return redirect(url_for('manage_users'))
    
    new_user = User(username=username, password=password, is_admin=is_admin)
    db.session.add(new_user)
    db.session.commit()
    
    flash('User added successfully!')
    return redirect(url_for('manage_users'))

@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
@admin_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        is_admin = bool(int(request.form.get('is_admin', 0)))
        
        existing_user = User.query.filter(User.username == username, User.id != user.id).first()
        if existing_user:
            flash('Username already exists')
            return redirect(url_for('edit_user', user_id=user.id))
        
        user.username = username
        if password:
            user.password = password
        user.is_admin = is_admin
        
        db.session.commit()
        flash('User updated successfully!')
        return redirect(url_for('manage_users'))
    
    return render_template('edit_profile.html', user=user)

@app.route('/delete_user/<int:user_id>', methods=['POST'])
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    
    if user.is_admin and User.query.filter_by(is_admin=True).count() <= 1:
        flash('Cannot delete the last admin user')
        return redirect(url_for('manage_users'))
    
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!')
    return redirect(url_for('manage_users'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('home'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
        
        new_user = User(username=username, password=password, is_admin=False)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

def init_db():
    if os.path.exists('buddhist_wisdom.db'):
        os.remove('buddhist_wisdom.db')
    
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        admin = User(username='admin', password='admin123', is_admin=True)
        db.session.add(admin)
        db.session.commit()
        print('Database initialized with admin user!')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
