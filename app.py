from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Ensure data directory exists
os.makedirs('data', exist_ok=True)

def read_json(filename):
    path = os.path.join('data', filename)
    try:
        if not os.path.exists(path):
            return []
        with open(path, 'r') as f:
            if os.path.getsize(path) == 0:
                return []
            return json.load(f)
    except json.JSONDecodeError:
        return []

def write_json(filename, data):
    path = os.path.join('data', filename)
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

# Initialize JSON files if empty
def init_json_files():
    if not read_json('books.json'):
        write_json('books.json', [])
    if not read_json('issued_books.json'):
        write_json('issued_books.json', [])

init_json_files()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        book_id = request.form.get('book_id', '').strip()
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        quantity = request.form.get('quantity', '1').strip()

        if not all([book_id, title, author, quantity]):
            flash('Please fill all fields', 'error')
            return redirect(url_for('add_book'))

        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            flash('Quantity must be a positive number', 'error')
            return redirect(url_for('add_book'))

        books = read_json('books.json')
        existing_book = next((b for b in books if b['book_id'] == book_id), None)

        if existing_book:
            existing_book['quantity'] += quantity
        else:
            books.append({
                'book_id': book_id,
                'title': title,
                'author': author,
                'quantity': quantity
            })

        write_json('books.json', books)
        flash('Book added successfully!', 'success')
        return redirect(url_for('book_list'))
    
    return render_template('add_book.html')

@app.route('/book_list')
def book_list():
    books = read_json('books.json')
    return render_template('book_list.html', books=books)

@app.route('/issue_book', methods=['GET', 'POST'])
def issue_book():
    if request.method == 'POST':
        book_id = request.form.get('book_id', '').strip()
        student_name = request.form.get('student_name', '').strip()
        student_id = request.form.get('student_id', '').strip()
        issue_date = request.form.get('issue_date', '').strip()
        return_date = request.form.get('return_date', '').strip()

        if not all([book_id, student_name, student_id, issue_date, return_date]):
            flash('Please fill all fields', 'error')
            return redirect(url_for('issue_book'))

        books = read_json('books.json')
        issued_books = read_json('issued_books.json')

        book = next((b for b in books if b['book_id'] == book_id), None)
        
        if not book:
            flash('Book not found!', 'error')
            return redirect(url_for('issue_book'))
        
        if book['quantity'] <= 0:
            flash('Book not available for issuing!', 'error')
            return redirect(url_for('issue_book'))

        # Reduce book quantity
        book['quantity'] -= 1
        write_json('books.json', books)

        # Add to issued books
        issued_books.append({
            'book_id': book_id,
            'title': book['title'],
            'author': book['author'],
            'student_name': student_name,
            'student_id': student_id,
            'issue_date': issue_date,
            'return_date': return_date,
            'returned': False
        })

        write_json('issued_books.json', issued_books)
        flash('Book issued successfully!', 'success')
        return redirect(url_for('issued_book_list'))
    
    books = read_json('books.json')
    return render_template('issue_book.html', books=books)

@app.route('/issued_book_list')
def issued_book_list():
    issued_books = read_json('issued_books.json')
    return render_template('issued_book_list.html', issued_books=issued_books)

@app.route('/return_book/<int:index>')
def return_book(index):
    issued_books = read_json('issued_books.json')
    books = read_json('books.json')
    
    if 0 <= index < len(issued_books) and not issued_books[index]['returned']:
        # Mark as returned
        issued_books[index]['returned'] = True
        
        # Increase book quantity
        book_id = issued_books[index]['book_id']
        book = next((b for b in books if b['book_id'] == book_id), None)
        if book:
            book['quantity'] += 1
        
        write_json('issued_books.json', issued_books)
        write_json('books.json', books)
        flash('Book returned successfully!', 'success')
    
    return redirect(url_for('issued_book_list'))

if __name__ == '__main__':
    app.run(debug=True)
