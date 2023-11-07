"""from flask import Blueprint,render_template,redirect,url_for,request

bp = Blueprint('expense_tracker', __name__)

@bp.route('/')
def index():
    return 'Hello, Expense Tracker!'

# Add your other views and routes here
categories = []

@bp.route('/')
def home():
    return redirect(url_for('view_categories'))

@bp.route('/view_categories')
def view_categories():
    return render_template('view_categories.html', categories=categories)

@bp.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        category_name = request.form['category_name']
        categories.append(category_name)
        return redirect(url_for('view_categories'))
    return render_template('add_category.html')"""