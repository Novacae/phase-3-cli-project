"""from flask import Flask, render_template, url_for,redirect,request

app = Flask(__name__)

@app.route('/')
def base():
    with app.test_request_context():
        url = url_for('base')
       
        print(url) 
    return render_template('base.html')

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/view_categories')
def view_categories():
    return render_template('view_categories.html')

app.route('/view_categories')
def view_categories():
    # Logic to retrieve the list of categories
    categories = [
        {'name': 'Category 1'},
        {'name': 'Category 2'},
        {'name': 'Category 3'}
    ]

    return render_template('view_categories.html', categories=categories)

@app.route('/add_expense')
def add_expense():
    return render_template('add_expense.html')

       
        'title': 'Expense Title',
        'amount': 100.0,
        'date': '2023-11-05',
        'category': 'Food',
        'description': 'Expense description',
        'person': {
            'name': 'John',
            'age': 30,
            'occupation': 'Software Engineer'
        }
    }

    return render_template('view_expense.html', expense=expense)


@app.route('/view_expenses/<expense_id>')
def view_expense(expense_id):
  
    expense = {
        'id': expense_id,
        'title': 'Sample Expense',
        'amount': 100.0,
        'date': '2023-11-06',
        'category': 'Food',
        'description': 'Sample expense description',
    }

    return render_template('view_expense.html', expense=expense)

if __name__ == '__main__':
    app.run(debug=True)   """
import sqlite3 as db
import sys


def init():
   
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS EXPENSES (
    amount NUMBER,
    category STRING,
    message STRING,
    date STRING
    )'''
    cur.execute(sql)
    conn.commit()


def log(amount, category, message=''):
  
    from datetime import datetime
    date = str(datetime.now())
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = '''
    INSERT INTO EXPENSES VALUES(
    {},'{}','{}','{}')
    '''.format(amount, category, message, date)
    cur.execute(sql)
    conn.commit()


def view(category=None,sort_by=None):

    sql = "SELECT * FROM EXPENSES"

    if category:
        sql += f" WHERE category = '{category}'"

    if sort_by:
        sql += f" ORDER BY {sort_by}"
   
    conn = db.connect("spent.db")
    cur = conn.cursor()
    if (category):
        sql = '''
        SELECT * FROM EXPENSES WHERE CATEGORY='{}'
        '''.format(category)
        sql2 = '''
        SELECT SUM(amount) FROM EXPENSES WHERE CATEGORY='{}'
        '''.format(category)
    else:
        sql = 'SELECT * FROM EXPENSES'
        sql2 = 'SELECT SUM(amount) FROM EXPENSES'
    cur.execute(sql)
    results = cur.fetchall()
    print("Total rows are:  ", len(results))
    for row in results:
        print("Amount: ", row[0])
        print("Category: ", row[1])
        print("Message: ", row[2])
        print("Date: ", row[3])
        print("\n")
    cur.execute(sql2)
    total_amount = cur.fetchone()[0]
    print("Total amount spent:", total_amount)
    


def month_view(month):
    
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = '''
        SELECT amount,category,message,strftime("%Y/%m/%d", date) FROM EXPENSES
        WHERE strftime('%m', date) = '{}'
        '''.format(month)
    sql2 = '''
          SELECT MAX(amount),category FROM EXPENSES
          WHERE strftime('%m', date) = '{}'
        '''.format(month)
    cur.execute(sql)
    result = cur.fetchall()
    print("Total rows are:  ", len(result))
    for row in result:
        print("Amount: ", row[0])
        print("Category: ", row[1])
        print("Message: ", row[2])
        print("Date: ", row[3])
        print("\n")
    cur.execute(sql2)
    max_spent = cur.fetchone()[0]
    print("Maximum spent: ", max_spent)
    


def year_view(year):
  
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = '''
        SELECT amount,category,message,strftime("%Y/%m/%d", date) FROM EXPENSES
        WHERE strftime('%Y', date) = '{}'
        '''.format(year)
    cur.execute(sql)
    result = cur.fetchall()
    print("Total rows are:  ", len(result))
    for row in result:
        print("Amount: ", row[0])
        print("Category: ", row[1])
        print("Message: ", row[2])
        print("Date: ", row[3])
        print("\n")

    

def main():
    init()

    if __name__ == "__main__":
        print("****************************")
        print("EXPENSE TRACKER APPLICATION")
        print("*************************")
        choice = int(input(
            "Enter your choice: \n 1. Log into Tracker \n 2. View expense report \n 3. View monthly report \n 4. View yearly report \n 5. Exit\n\n"))
        if (choice == 1):
            amount = int(input("How much did you spend?\t"))
            category = input("What did you buy?\t")
            message = input("Any additional message? Enter '' to leave blank.\t")
            log(amount, category, message)
        elif (choice == 3):
            category = input(
                "Do you want to see expenses of particular category? Press Enter to leave blank and view complete report. \t")
            print(view(category))
        elif (choice == 2):
            month = input("For which month do you want the expense report? (Enter in numerical form) \t")
            print(month_view(month))
        elif (choice == 4):
            year = input("For which year do you want the expense report? (Enter in numerical form) \t")
            print(year_view(year))
        elif (choice == 5):
            sys.exit()
        else:
            print("Choose the correct option")
            main()
        while choice == 5:
            break
        else:
            replayMenu()


def replayMenu():
    startover = ""
    startover = input("Would you like to start from the beginning, yes or no? ")
    while startover.lower() != "yes":
        print("Thanks for using Expense Tracker! ")
        break
    else:
        main()

def display():
    print("        //\   \\\                 ")
    print("      //   \/   (@)          ")
    print("      \    //  \\\      (@)")
    print("      /    []   \\\  WELCOME TO MY EXPENSE TRACKER    ")
    print("       \  []  ][]         ")
    print("        \_/   ")

display()
main()